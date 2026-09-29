"""Transparent association-rule calculations for small transaction datasets."""

from __future__ import annotations

from collections import Counter
from itertools import combinations


def normalize_transactions(rows: list[list[str]]) -> list[frozenset[str]]:
    return [frozenset(item.strip() for item in row if item.strip()) for row in rows]


def itemset_support(
    transactions: list[frozenset[str]], itemset: frozenset[str]
) -> float:
    if not transactions:
        raise ValueError("transactions must not be empty")
    return sum(itemset <= transaction for transaction in transactions) / len(transactions)


def rule_metrics(
    transactions: list[frozenset[str]],
    antecedent: frozenset[str],
    consequent: frozenset[str],
) -> dict[str, float]:
    if not antecedent or not consequent or antecedent & consequent:
        raise ValueError("rule sides must be nonempty and disjoint")
    joint = itemset_support(transactions, antecedent | consequent)
    left = itemset_support(transactions, antecedent)
    right = itemset_support(transactions, consequent)
    return {
        "support": joint,
        "confidence": joint / left,
        "lift": joint / (left * right),
    }


def frequent_itemsets(
    transactions: list[frozenset[str]], minimum_support: float, max_size: int = 3
) -> dict[frozenset[str], float]:
    if not 0 < minimum_support <= 1 or max_size <= 0:
        raise ValueError("invalid mining parameters")
    items = sorted(set().union(*transactions))
    result: dict[frozenset[str], float] = {}
    for size in range(1, max_size + 1):
        for candidate in combinations(items, size):
            itemset = frozenset(candidate)
            support = itemset_support(transactions, itemset)
            if support >= minimum_support:
                result[itemset] = support
    return result


def transition_counts(sequences: list[list[str]]) -> Counter[tuple[str, str]]:
    return Counter(
        (left, right)
        for sequence in sequences
        for left, right in zip(sequence, sequence[1:])
    )
