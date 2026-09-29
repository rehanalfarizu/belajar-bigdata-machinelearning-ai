from __future__ import annotations

import unittest

from decision_lab import brier_score, choose_threshold, threshold_labels


class DecisionLabTest(unittest.TestCase):
    def test_threshold_is_explicit(self) -> None:
        self.assertEqual(threshold_labels([0.2, 0.5, 0.8], 0.5), [0, 1, 1])

    def test_cost_changes_threshold_decision(self) -> None:
        actual = [0, 0, 1, 1]
        probabilities = [0.1, 0.4, 0.45, 0.8]
        thresholds = [0.3, 0.5, 0.7]
        low, _ = choose_threshold(actual, probabilities, thresholds, 1, 10)
        high, _ = choose_threshold(actual, probabilities, thresholds, 10, 1)
        self.assertLess(low, high)

    def test_perfect_probabilities_have_zero_brier(self) -> None:
        self.assertEqual(brier_score([0, 1], [0.0, 1.0]), 0.0)
