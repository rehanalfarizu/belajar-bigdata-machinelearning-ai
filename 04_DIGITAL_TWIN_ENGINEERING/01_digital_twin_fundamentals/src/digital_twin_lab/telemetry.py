"""Kontrak telemetry dan quality gate sebelum event mengubah twin state."""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime, timedelta, timezone
import math
from typing import Callable


@dataclass(frozen=True)
class TelemetryEvent:
    """Observasi immutable; event time tidak boleh diganti dengan ingest time."""

    event_id: str
    asset_id: str
    metric: str
    value: float
    unit: str
    event_time: datetime
    ingest_time: datetime
    sequence_number: int
    schema_version: int = 1
    quality: str = "good"
    source: str = "simulator"


@dataclass(frozen=True)
class MetricRule:
    canonical_unit: str
    minimum: float
    maximum: float
    max_age: timedelta = timedelta(minutes=5)


@dataclass(frozen=True)
class ValidationResult:
    accepted: bool
    event: TelemetryEvent | None
    reasons: tuple[str, ...] = ()
    late: bool = False


def _identity(value: float) -> float:
    return value


UNIT_CONVERTERS: dict[tuple[str, str], Callable[[float], float]] = {
    ("m", "m"): _identity,
    ("cm", "m"): lambda value: value / 100.0,
    ("C", "C"): _identity,
    ("F", "C"): lambda value: (value - 32.0) * 5.0 / 9.0,
    ("L/s", "m3/s"): lambda value: value / 1000.0,
    ("m3/s", "m3/s"): _identity,
}


class TelemetryValidator:
    """Validasi schema, waktu, unit, kualitas, dan batas fisik."""

    def __init__(
        self,
        rules: dict[str, MetricRule],
        *,
        future_tolerance: timedelta = timedelta(seconds=5),
        allowed_schema_versions: frozenset[int] = frozenset({1}),
    ) -> None:
        self.rules = rules
        self.future_tolerance = future_tolerance
        self.allowed_schema_versions = allowed_schema_versions

    def validate(
        self,
        event: TelemetryEvent,
        *,
        now: datetime | None = None,
        watermark: datetime | None = None,
    ) -> ValidationResult:
        now = now or datetime.now(timezone.utc)
        reasons: list[str] = []

        for field_name, timestamp in (
            ("event_time", event.event_time),
            ("ingest_time", event.ingest_time),
            ("now", now),
        ):
            if timestamp.tzinfo is None or timestamp.utcoffset() is None:
                reasons.append(f"{field_name} harus timezone-aware")

        if not event.event_id.strip():
            reasons.append("event_id kosong")
        if not event.asset_id.strip():
            reasons.append("asset_id kosong")
        if event.sequence_number < 0:
            reasons.append("sequence_number harus non-negatif")
        if event.schema_version not in self.allowed_schema_versions:
            reasons.append("schema_version tidak didukung")
        if event.quality not in {"good", "uncertain", "bad"}:
            reasons.append("quality tidak dikenal")
        elif event.quality == "bad":
            reasons.append("quality bad tidak boleh memperbarui twin state")
        if not math.isfinite(event.value):
            reasons.append("value harus finite")

        rule = self.rules.get(event.metric)
        normalized = event
        if rule is None:
            reasons.append("metric tidak dikenal")
        else:
            converter = UNIT_CONVERTERS.get((event.unit, rule.canonical_unit))
            if converter is None:
                reasons.append(
                    f"unit {event.unit!r} tidak dapat dikonversi ke {rule.canonical_unit!r}"
                )
            elif math.isfinite(event.value):
                normalized = replace(
                    event,
                    value=converter(event.value),
                    unit=rule.canonical_unit,
                )
                if not rule.minimum <= normalized.value <= rule.maximum:
                    reasons.append("value di luar batas fisik")

        if not reasons or all("timezone-aware" not in reason for reason in reasons):
            if event.event_time > now + self.future_tolerance:
                reasons.append("event_time terlalu jauh di masa depan")
            if rule is not None and now - event.event_time > rule.max_age:
                reasons.append("event stale")
            if event.ingest_time < event.event_time - self.future_tolerance:
                reasons.append("ingest_time mendahului event_time di luar toleransi")

        late = watermark is not None and event.event_time < watermark
        return ValidationResult(not reasons, normalized if not reasons else None, tuple(reasons), late)


class EventLedger:
    """Ledger in-memory untuk demo deduplikasi dan urutan per stream.

    Produksi perlu persistence/transaction. Di sini raw, accepted, dan quarantine
    tetap terpisah agar event gagal tidak hilang dari audit trail.
    """

    def __init__(self, validator: TelemetryValidator) -> None:
        self.validator = validator
        self.raw: list[TelemetryEvent] = []
        self.accepted: list[TelemetryEvent] = []
        self.quarantine: list[tuple[TelemetryEvent, tuple[str, ...]]] = []
        self._seen_ids: set[str] = set()
        self._last_sequence: dict[tuple[str, str], int] = {}

    def ingest(self, event: TelemetryEvent, *, now: datetime) -> ValidationResult:
        self.raw.append(event)
        if event.event_id in self._seen_ids:
            result = ValidationResult(False, None, ("duplicate event_id",))
            self.quarantine.append((event, result.reasons))
            return result

        stream = (event.asset_id, event.metric)
        previous = self._last_sequence.get(stream)
        result = self.validator.validate(event, now=now)
        reasons = list(result.reasons)
        if previous is not None and event.sequence_number <= previous:
            reasons.append("sequence_number tidak meningkat")

        if reasons:
            rejected = ValidationResult(False, None, tuple(reasons), result.late)
            self.quarantine.append((event, rejected.reasons))
            return rejected

        assert result.event is not None
        self._seen_ids.add(event.event_id)
        self._last_sequence[stream] = event.sequence_number
        self.accepted.append(result.event)
        return result
