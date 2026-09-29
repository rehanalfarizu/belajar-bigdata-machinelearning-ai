from datetime import datetime, timedelta, timezone
import unittest

from digital_twin_lab.telemetry import (
    EventLedger,
    MetricRule,
    TelemetryEvent,
    TelemetryValidator,
)


NOW = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)


def event(**overrides: object) -> TelemetryEvent:
    values: dict[str, object] = {
        "event_id": "evt-1",
        "asset_id": "tank-01",
        "metric": "level",
        "value": 250.0,
        "unit": "cm",
        "event_time": NOW - timedelta(seconds=1),
        "ingest_time": NOW,
        "sequence_number": 1,
    }
    values.update(overrides)
    return TelemetryEvent(**values)  # type: ignore[arg-type]


class TelemetryValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = TelemetryValidator(
            {"level": MetricRule("m", 0.0, 10.0, timedelta(minutes=1))}
        )

    def test_converts_to_canonical_unit(self) -> None:
        result = self.validator.validate(event(), now=NOW)
        self.assertTrue(result.accepted)
        self.assertIsNotNone(result.event)
        assert result.event is not None
        self.assertAlmostEqual(result.event.value, 2.5)
        self.assertEqual(result.event.unit, "m")

    def test_rejects_naive_timestamp_and_stale_event(self) -> None:
        naive = event(event_time=datetime(2026, 1, 1, 11, 0))
        result = self.validator.validate(naive, now=NOW)
        self.assertFalse(result.accepted)
        self.assertTrue(any("timezone-aware" in reason for reason in result.reasons))

        stale = event(event_time=NOW - timedelta(minutes=2))
        result = self.validator.validate(stale, now=NOW)
        self.assertIn("event stale", result.reasons)

    def test_bad_quality_does_not_update_state(self) -> None:
        result = self.validator.validate(event(quality="bad"), now=NOW)
        self.assertFalse(result.accepted)
        self.assertIn("quality bad tidak boleh memperbarui twin state", result.reasons)

    def test_ledger_deduplicates_and_enforces_order(self) -> None:
        ledger = EventLedger(self.validator)
        self.assertTrue(ledger.ingest(event(), now=NOW).accepted)
        self.assertFalse(ledger.ingest(event(), now=NOW).accepted)
        out_of_order = event(event_id="evt-2", sequence_number=0)
        result = ledger.ingest(out_of_order, now=NOW)
        self.assertFalse(result.accepted)
        self.assertIn("sequence_number tidak meningkat", result.reasons)
        self.assertEqual(len(ledger.raw), 3)
        self.assertEqual(len(ledger.accepted), 1)
        self.assertEqual(len(ledger.quarantine), 2)


if __name__ == "__main__":
    unittest.main()
