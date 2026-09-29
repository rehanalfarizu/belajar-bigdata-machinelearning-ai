"""Small ML mechanics with no estimator library, intended for inspection."""

from __future__ import annotations

import math


def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def fit_simple_linear(xs: list[float], ys: list[float]) -> tuple[float, float]:
    if len(xs) != len(ys) or len(xs) < 2:
        raise ValueError("paired data needs equal length >= 2")
    x_bar, y_bar = mean(xs), mean(ys)
    denominator = sum((x - x_bar) ** 2 for x in xs)
    if denominator == 0:
        raise ValueError("feature needs variation")
    slope = sum((x - x_bar) * (y - y_bar) for x, y in zip(xs, ys)) / denominator
    return y_bar - slope * x_bar, slope


def sigmoid(score: float) -> float:
    if score >= 0:
        return 1.0 / (1.0 + math.exp(-score))
    exp_score = math.exp(score)
    return exp_score / (1.0 + exp_score)


def euclidean(left: list[float], right: list[float]) -> float:
    if len(left) != len(right):
        raise ValueError("feature vectors need equal shape")
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(left, right)))


def confusion_counts(actual: list[int], predicted: list[int]) -> dict[str, int]:
    if len(actual) != len(predicted):
        raise ValueError("actual and predicted lengths differ")
    counts = {"tp": 0, "fp": 0, "tn": 0, "fn": 0}
    mapping = {(1, 1): "tp", (0, 1): "fp", (0, 0): "tn", (1, 0): "fn"}
    for pair in zip(actual, predicted):
        if pair not in mapping:
            raise ValueError("labels must be binary")
        counts[mapping[pair]] += 1
    return counts


def classification_metrics(counts: dict[str, int]) -> dict[str, float]:
    tp, fp, fn = counts["tp"], counts["fp"], counts["fn"]
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"precision": precision, "recall": recall, "f1": f1}
