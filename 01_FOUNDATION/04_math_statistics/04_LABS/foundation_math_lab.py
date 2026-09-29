"""Eksperimen numerik kecil untuk Phase 1; hanya standard library."""

from __future__ import annotations

import math
import random
import statistics


def dot(left: list[float], right: list[float]) -> float:
    if len(left) != len(right):
        raise ValueError("vectors must have equal length")
    return sum(a * b for a, b in zip(left, right))


def l2_norm(vector: list[float]) -> float:
    return math.sqrt(dot(vector, vector))


def matrix_vector(matrix: list[list[float]], vector: list[float]) -> list[float]:
    if not matrix or any(len(row) != len(vector) for row in matrix):
        raise ValueError("each matrix row must match vector length")
    return [dot(row, vector) for row in matrix]


def numeric_derivative(function, x: float, step: float = 1e-5) -> float:
    if step <= 0:
        raise ValueError("step must be positive")
    return (function(x + step) - function(x - step)) / (2.0 * step)


def gradient_descent(rate: float, steps: int = 8) -> list[float]:
    value = 0.0
    losses: list[float] = []
    for _ in range(steps):
        losses.append((value - 3.0) ** 2)
        gradient = 2.0 * (value - 3.0)
        value -= rate * gradient
    return losses


def bernoulli_rate(probability: float, trials: int, seed: int) -> float:
    if not 0.0 <= probability <= 1.0 or trials <= 0:
        raise ValueError("probability must be in [0, 1] and trials positive")
    rng = random.Random(seed)
    return sum(rng.random() < probability for _ in range(trials)) / trials


def bayes_positive(
    prior: float, sensitivity: float, false_positive_rate: float
) -> float:
    if not all(0.0 <= value <= 1.0 for value in (prior, sensitivity, false_positive_rate)):
        raise ValueError("probabilities must be in [0, 1]")
    positive = sensitivity * prior + false_positive_rate * (1.0 - prior)
    if positive == 0:
        raise ValueError("positive evidence has zero probability")
    return sensitivity * prior / positive


def repeated_sample_means(sample_size: int, repeats: int, seed: int) -> list[float]:
    if sample_size <= 0 or repeats <= 0:
        raise ValueError("sample_size and repeats must be positive")
    rng = random.Random(seed)
    return [
        statistics.mean(rng.gauss(10.0, 2.0) for _ in range(sample_size))
        for _ in range(repeats)
    ]


def confidence_interval_mean(
    values: list[float], z_score: float = 1.96
) -> tuple[float, float]:
    if len(values) < 2 or z_score <= 0:
        raise ValueError("need at least two values and positive z-score")
    center = statistics.mean(values)
    margin = z_score * statistics.stdev(values) / math.sqrt(len(values))
    return center - margin, center + margin


def coin_two_sided_p_value(
    successes: int, trials: int, probability: float = 0.5
) -> float:
    if trials <= 0 or not 0 <= successes <= trials or not 0.0 < probability < 1.0:
        raise ValueError("invalid binomial parameters")

    def mass(count: int) -> float:
        return (
            math.comb(trials, count)
            * probability**count
            * (1.0 - probability) ** (trials - count)
        )

    observed = mass(successes)
    return min(1.0, sum(mass(k) for k in range(trials + 1) if mass(k) <= observed + 1e-15))


def bootstrap_mean_interval(
    values: list[float],
    repeats: int = 2_000,
    confidence: float = 0.95,
    seed: int = 42,
) -> tuple[float, float]:
    if not values or repeats <= 0 or not 0.0 < confidence < 1.0:
        raise ValueError("need values, positive repeats, and confidence in (0, 1)")
    rng = random.Random(seed)
    means = sorted(
        statistics.mean(rng.choice(values) for _ in values) for _ in range(repeats)
    )
    tail = (1.0 - confidence) / 2.0
    lower_index = max(0, math.floor(tail * repeats))
    upper_index = min(repeats - 1, math.ceil((1.0 - tail) * repeats) - 1)
    return means[lower_index], means[upper_index]


def correlation(xs: list[float], ys: list[float]) -> float:
    if len(xs) != len(ys) or len(xs) < 2:
        raise ValueError("paired vectors need equal length >= 2")
    mean_x = statistics.mean(xs)
    mean_y = statistics.mean(ys)
    centered_x = [value - mean_x for value in xs]
    centered_y = [value - mean_y for value in ys]
    denominator = l2_norm(centered_x) * l2_norm(centered_y)
    if denominator == 0:
        raise ValueError("correlation undefined for zero variance")
    return dot(centered_x, centered_y) / denominator


def ascii_bar(label: str, value: float, scale: int = 20) -> str:
    width = max(0, round(value * scale))
    return f"{label:>12}: {'#' * width} {value:.3f}"


def main() -> None:
    print("VECTOR")
    print("dot", dot([1.0, 2.0], [3.0, 4.0]))
    print("norm", l2_norm([3.0, 4.0]))

    print("\nGRADIENT DESCENT")
    for rate in (0.05, 0.25, 1.1):
        losses = gradient_descent(rate)
        print(f"rate={rate:<4}", [round(value, 3) for value in losses])

    print("\nSAMPLING DISTRIBUTION")
    for size in (5, 100):
        means = repeated_sample_means(size, repeats=500, seed=42)
        print(ascii_bar(f"SE n={size}", statistics.stdev(means)))

    print("\nCORRELATION")
    xs = [-2.0, -1.0, 0.0, 1.0, 2.0]
    print("linear", correlation(xs, [2 * x for x in xs]))
    print("u-shape", correlation(xs, [x * x for x in xs]))


if __name__ == "__main__":
    main()
