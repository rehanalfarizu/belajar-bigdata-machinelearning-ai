"""Small, standard-library data-quality pipeline for the Phase 2 local dataset."""

from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

VALID_STATUS = {"ok", "warning", "alarm"}


def fahrenheit_to_celsius(value: float) -> float:
    return (value - 32.0) * 5.0 / 9.0


def normalize_status(raw: str) -> str:
    status = raw.strip().lower()
    aliases = {"okay": "ok"}
    return aliases.get(status, status)


def parse_instant(raw: str) -> str:
    parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamp must include timezone")
    return parsed.astimezone(timezone.utc).isoformat()


def curate_rows(
    rows: Iterable[dict[str, str]], known_assets: set[str]
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    accepted: list[dict[str, str]] = []
    rejected: list[dict[str, str]] = []
    seen: set[str] = set()

    for source in rows:
        row = dict(source)
        reasons: list[str] = []
        event_id = row.get("event_id", "").strip()
        if not event_id or event_id in seen:
            reasons.append("duplicate_or_missing_event_id")
        seen.add(event_id)
        if row.get("asset_id") not in known_assets:
            reasons.append("unknown_asset")

        try:
            value = float(row.get("temp_value", ""))
            unit = row.get("temp_unit", "").strip().upper()
            if unit == "F":
                value = fahrenheit_to_celsius(value)
            elif unit != "C":
                raise ValueError("unknown unit")
            if not -40.0 <= value <= 100.0:
                reasons.append("temperature_out_of_range")
            row["temp_c"] = f"{value:.2f}"
        except ValueError:
            reasons.append("invalid_temperature")

        status = normalize_status(row.get("status", ""))
        if status not in VALID_STATUS:
            reasons.append("invalid_status")
        row["status"] = status

        try:
            row["event_time_utc"] = parse_instant(row.get("event_time", ""))
        except ValueError:
            reasons.append("invalid_or_naive_timestamp")

        if reasons:
            row["rejection_reasons"] = "|".join(reasons)
            rejected.append(row)
        else:
            accepted.append(row)
    return accepted, rejected


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as stream:
        return list(csv.DictReader(stream))


def main() -> None:
    raw = Path(__file__).parent / "data" / "raw"
    assets = {row["asset_id"] for row in read_csv(raw / "assets.csv")}
    readings = read_csv(raw / "readings.csv")
    accepted, rejected = curate_rows(readings, assets)
    print(f"input={len(readings)} accepted={len(accepted)} rejected={len(rejected)}")
    for row in rejected:
        print(row["event_id"], row["rejection_reasons"])


if __name__ == "__main__":
    main()
