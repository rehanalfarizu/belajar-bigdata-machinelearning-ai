"""Inspectable neuron mechanics before TensorFlow/Keras."""

from __future__ import annotations

import math


def sigmoid(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def neuron(inputs: list[float], weights: list[float], bias: float) -> float:
    if len(inputs) != len(weights):
        raise ValueError("inputs and weights need equal shape")
    return sigmoid(sum(x * weight for x, weight in zip(inputs, weights)) + bias)


def binary_cross_entropy(target: int, probability: float) -> float:
    if target not in (0, 1) or not 0.0 < probability < 1.0:
        raise ValueError("invalid target or probability")
    return -(target * math.log(probability) + (1 - target) * math.log(1 - probability))


def finite_difference_gradient(function, value: float, step: float = 1e-5) -> float:
    if step <= 0:
        raise ValueError("step must be positive")
    return (function(value + step) - function(value - step)) / (2 * step)


def train_linear_weight(
    xs: list[float], ys: list[float], rate: float, epochs: int
) -> tuple[float, list[float]]:
    if len(xs) != len(ys) or not xs or rate <= 0 or epochs <= 0:
        raise ValueError("invalid training inputs")
    weight = 0.0
    losses: list[float] = []
    for _ in range(epochs):
        errors = [weight * x - y for x, y in zip(xs, ys)]
        losses.append(sum(error**2 for error in errors) / len(errors))
        gradient = 2 * sum(error * x for error, x in zip(errors, xs)) / len(xs)
        weight -= rate * gradient
    return weight, losses
