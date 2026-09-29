from __future__ import annotations

import unittest

from ml_from_scratch import (
    classification_metrics,
    confusion_counts,
    euclidean,
    fit_simple_linear,
    sigmoid,
)


class MLFromScratchTest(unittest.TestCase):
    def test_linear_fit_recovers_line(self) -> None:
        intercept, slope = fit_simple_linear([0, 1, 2], [1, 3, 5])
        self.assertAlmostEqual(intercept, 1)
        self.assertAlmostEqual(slope, 2)

    def test_sigmoid_is_bounded(self) -> None:
        self.assertLess(sigmoid(-10), 0.001)
        self.assertGreater(sigmoid(10), 0.999)

    def test_distance_rejects_shape_mismatch(self) -> None:
        with self.assertRaises(ValueError):
            euclidean([1], [1, 2])

    def test_metrics_follow_confusion_counts(self) -> None:
        counts = confusion_counts([1, 1, 0, 0], [1, 0, 1, 0])
        self.assertEqual(counts, {"tp": 1, "fp": 1, "tn": 1, "fn": 1})
        self.assertEqual(classification_metrics(counts)["f1"], 0.5)
