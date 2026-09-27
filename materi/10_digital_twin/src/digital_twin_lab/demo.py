"""CLI demo: python -m digital_twin_lab.demo --steps 500."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from .simulation import run_tank_experiment


def summarize(rows: list[dict[str, object]]) -> dict[str, float | int | None]:
    errors = [
        abs(float(row["estimate_m"]) - float(row["true_level_m"]))
        for row in rows
    ]
    fault_steps = [int(row["step"]) for row in rows if row["fault_active"]]
    first_fault = min(fault_steps) if fault_steps else None
    alarm_steps = [int(row["step"]) for row in rows if row["alarm"]]
    post_fault = [step for step in alarm_steps if first_fault is not None and step >= first_fault]
    false_alarms = sum(first_fault is None or step < first_fault for step in alarm_steps)
    return {
        "mae_m": sum(errors) / len(errors),
        "first_alarm_step": min(post_fault) if post_fault else None,
        "detection_delay_steps": min(post_fault) - first_fault if post_fault and first_fault is not None else None,
        "false_alarms": false_alarms,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Eksperimen tank digital twin")
    parser.add_argument("--steps", type=int, default=500)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--fault-step", type=int, default=300)
    parser.add_argument("--csv", type=Path, help="Simpan histori eksperimen")
    args = parser.parse_args()

    rows = run_tank_experiment(steps=args.steps, seed=args.seed, fault_step=args.fault_step)
    print(summarize(rows))
    if args.csv:
        args.csv.parent.mkdir(parents=True, exist_ok=True)
        with args.csv.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


if __name__ == "__main__":
    main()
