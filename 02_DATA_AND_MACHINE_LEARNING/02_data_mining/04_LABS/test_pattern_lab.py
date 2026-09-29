from __future__ import annotations

import unittest

from pattern_lab import (
    frequent_itemsets,
    normalize_transactions,
    rule_metrics,
    transition_counts,
)


class PatternLabTest(unittest.TestCase):
    def setUp(self) -> None:
        self.transactions = normalize_transactions(
            [["A", "B"], ["A"], ["A", "B"], ["A", "C"], ["B"]]
        )

    def test_manual_rule_metrics(self) -> None:
        metrics = rule_metrics(self.transactions, frozenset("A"), frozenset("B"))
        self.assertAlmostEqual(metrics["support"], 0.4)
        self.assertAlmostEqual(metrics["confidence"], 0.5)
        self.assertAlmostEqual(metrics["lift"], 5 / 6)

    def test_duplicate_item_does_not_inflate_basket(self) -> None:
        normalized = normalize_transactions([["A", "A", "B"]])
        self.assertEqual(normalized, [frozenset({"A", "B"})])

    def test_support_threshold_controls_candidates(self) -> None:
        low = frequent_itemsets(self.transactions, 0.4)
        high = frequent_itemsets(self.transactions, 0.8)
        self.assertGreater(len(low), len(high))

    def test_transition_preserves_order(self) -> None:
        counts = transition_counts([["start", "warn", "stop"], ["start", "stop"]])
        self.assertEqual(counts[("start", "stop")], 1)
