"""Decision-focused helpers for threshold and calibration experiments."""

from __future__ import annotations


def threshold_labels(probabilities: list[float], threshold: float) -> list[int]:
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("threshold must be in [0, 1]")
    return [int(value >= threshold) for value in probabilities]


def classification_cost(
    actual: list[int],
    predicted: list[int],
    false_positive_cost: float,
    false_negative_cost: float,
) -> float:
    if len(actual) != len(predicted):
        raise ValueError("actual and predicted lengths differ")
    return sum(
        false_positive_cost if truth == 0 and guess == 1
        else false_negative_cost if truth == 1 and guess == 0
        else 0.0
        for truth, guess in zip(actual, predicted)
    )


def choose_threshold(
    actual: list[int],
    probabilities: list[float],
    candidates: list[float],
    false_positive_cost: float,
    false_negative_cost: float,
) -> tuple[float, float]:
    if len(actual) != len(probabilities) or not candidates:
        raise ValueError("need paired observations and candidate thresholds")
    scored = [
        (
            classification_cost(
                actual,
                threshold_labels(probabilities, threshold),
                false_positive_cost,
                false_negative_cost,
            ),
            threshold,
        )
        for threshold in candidates
    ]
    cost, threshold = min(scored)
    return threshold, cost


def brier_score(actual: list[int], probabilities: list[float]) -> float:
    if len(actual) != len(probabilities) or not actual:
        raise ValueError("need paired observations")
    return sum((probability - truth) ** 2 for truth, probability in zip(actual, probabilities)) / len(actual)
