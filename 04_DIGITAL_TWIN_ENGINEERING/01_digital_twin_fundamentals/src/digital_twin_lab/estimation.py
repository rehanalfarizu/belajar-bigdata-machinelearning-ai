"""Estimator linear satu-dimensi untuk memahami Kalman Filter dari nol."""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass
class ScalarKalmanFilter:
    """Kalman Filter skalar: prediction lalu correction.

    `variance` adalah uncertainty state P, `process_variance` adalah Q, dan
    `measurement_variance` adalah R. Model state: x_k = x_(k-1) + u_k + w_k.
    """

    estimate: float
    variance: float
    process_variance: float

    def __post_init__(self) -> None:
        if self.variance <= 0 or self.process_variance < 0:
            raise ValueError("variance harus > 0 dan process_variance harus >= 0")

    def predict(self, control_effect: float = 0.0) -> tuple[float, float]:
        self.estimate += control_effect
        self.variance += self.process_variance
        return self.estimate, self.variance

    def update(self, measurement: float, measurement_variance: float) -> tuple[float, float]:
        if measurement_variance <= 0:
            raise ValueError("measurement_variance harus > 0")
        if not math.isfinite(measurement):
            raise ValueError("measurement harus finite")

        innovation = measurement - self.estimate
        innovation_variance = self.variance + measurement_variance
        gain = self.variance / innovation_variance
        self.estimate += gain * innovation
        self.variance *= 1.0 - gain
        return self.estimate, self.variance

    def step(
        self,
        *,
        control_effect: float = 0.0,
        measurement: float | None = None,
        measurement_variance: float | None = None,
    ) -> tuple[float, float]:
        self.predict(control_effect)
        if measurement is not None:
            if measurement_variance is None:
                raise ValueError("measurement_variance wajib saat ada measurement")
            self.update(measurement, measurement_variance)
        return self.estimate, self.variance


def fuse_measurements(
    prior_estimate: float,
    prior_variance: float,
    measurements: list[tuple[float, float]],
) -> tuple[float, float]:
    """Fusi sensor independen secara sekuensial berdasarkan variance-nya."""

    filter_ = ScalarKalmanFilter(prior_estimate, prior_variance, 0.0)
    for value, variance in measurements:
        filter_.update(value, variance)
    return filter_.estimate, filter_.variance
