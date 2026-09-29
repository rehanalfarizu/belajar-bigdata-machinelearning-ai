from __future__ import annotations

import unittest

from quality_pipeline import curate_rows, fahrenheit_to_celsius, parse_instant


class QualityPipelineTest(unittest.TestCase):
    def test_unit_conversion(self) -> None:
        self.assertAlmostEqual(fahrenheit_to_celsius(75.0), 23.8888889)

    def test_naive_timestamp_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "timezone"):
            parse_instant("2026-01-01 08:00:00")

    def test_duplicate_and_unknown_asset_are_explained(self) -> None:
        row = {
            "event_id": "e1",
            "asset_id": "unknown",
            "event_time": "2026-01-01T00:00:00Z",
            "temp_value": "20",
            "temp_unit": "C",
            "status": "ok",
        }
        accepted, rejected = curate_rows([row, row], {"A-1"})
        self.assertEqual(accepted, [])
        self.assertIn("unknown_asset", rejected[0]["rejection_reasons"])
        self.assertIn("duplicate_or_missing_event_id", rejected[1]["rejection_reasons"])

    def test_accounting_reconciles(self) -> None:
        valid = {
            "event_id": "e1",
            "asset_id": "A-1",
            "event_time": "2026-01-01T00:00:00Z",
            "temp_value": "68",
            "temp_unit": "F",
            "status": " OK ",
        }
        accepted, rejected = curate_rows([valid], {"A-1"})
        self.assertEqual(len(accepted) + len(rejected), 1)
        self.assertEqual(accepted[0]["temp_c"], "20.00")
