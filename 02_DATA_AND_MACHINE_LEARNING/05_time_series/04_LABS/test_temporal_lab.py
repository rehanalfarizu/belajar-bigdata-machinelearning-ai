from __future__ import annotations

import unittest

from temporal_lab import lag_pairs, naive_forecast, rolling_origin_mae, temporal_split


class TemporalLabTest(unittest.TestCase):
    def test_temporal_split_preserves_order(self) -> None:
        train, test = temporal_split([1, 2, 3, 4], 3)
        self.assertEqual(train, [1, 2, 3])
        self.assertEqual(test, [4])

    def test_lag_uses_only_past_values(self) -> None:
        self.assertEqual(lag_pairs([10, 20, 30], 2), [([10, 20], 30)])

    def test_naive_forecast_repeats_latest_observation(self) -> None:
        self.assertEqual(naive_forecast([1, 4], 2), [4, 4])

    def test_rolling_origin_has_expected_error(self) -> None:
        self.assertEqual(rolling_origin_mae([1, 2, 4], 1), 1.5)
