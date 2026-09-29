"""Time-series split, lag, naive forecast, and rolling evaluation mechanics."""

from __future__ import annotations

from collections.abc import Callable


def lag_pairs(values: list[float], lag: int = 1) -> list[tuple[list[float], float]]:
    if lag <= 0 or len(values) <= lag:
        raise ValueError("lag must be positive and smaller than series")
    return [(values[index - lag:index], values[index]) for index in range(lag, len(values))]


def temporal_split(values: list[float], train_size: int) -> tuple[list[float], list[float]]:
    if not 0 < train_size < len(values):
        raise ValueError("train_size must leave nonempty train and test")
    return values[:train_size], values[train_size:]


def naive_forecast(history: list[float], horizon: int) -> list[float]:
    if not history or horizon <= 0:
        raise ValueError("need history and positive horizon")
    return [history[-1]] * horizon


def mae(actual: list[float], predicted: list[float]) -> float:
    if len(actual) != len(predicted) or not actual:
        raise ValueError("need paired nonempty values")
    return sum(abs(a - p) for a, p in zip(actual, predicted)) / len(actual)


def rolling_origin_mae(
    values: list[float],
    initial_train_size: int,
    forecaster: Callable[[list[float], int], list[float]] = naive_forecast,
) -> float:
    errors: list[float] = []
    for index in range(initial_train_size, len(values)):
        prediction = forecaster(values[:index], 1)[0]
        errors.append(abs(values[index] - prediction))
    if not errors:
        raise ValueError("initial_train_size must leave evaluation observations")
    return sum(errors) / len(errors)
