"""Plant, sensor, estimator, dan alarm dipisahkan untuk mencegah leakage."""

from __future__ import annotations

from dataclasses import dataclass
import math
import random

from .anomaly import RunningZScoreDetector
from .estimation import ScalarKalmanFilter


@dataclass(frozen=True)
class TankParameters:
    area_m2: float = 10.0
    outlet_coefficient: float = 0.55
    dt_seconds: float = 1.0
    minimum_level_m: float = 0.0
    maximum_level_m: float = 10.0

    def __post_init__(self) -> None:
        if self.area_m2 <= 0 or self.dt_seconds <= 0:
            raise ValueError("area dan dt harus positif")


class TankPlant:
    def __init__(self, level_m: float, parameters: TankParameters) -> None:
        self.level_m = level_m
        self.parameters = parameters

    def step(self, inflow_m3_s: float, *, outlet_coefficient: float | None = None) -> float:
        coefficient = (
            self.parameters.outlet_coefficient
            if outlet_coefficient is None
            else outlet_coefficient
        )
        outflow = coefficient * math.sqrt(max(self.level_m, 0.0))
        delta = (
            self.parameters.dt_seconds
            / self.parameters.area_m2
            * (inflow_m3_s - outflow)
        )
        self.level_m = min(
            self.parameters.maximum_level_m,
            max(self.parameters.minimum_level_m, self.level_m + delta),
        )
        return self.level_m


def _model_delta(level: float, inflow: float, parameters: TankParameters) -> float:
    outflow = parameters.outlet_coefficient * math.sqrt(max(level, 0.0))
    return parameters.dt_seconds / parameters.area_m2 * (inflow - outflow)


def run_tank_experiment(
    *,
    steps: int = 500,
    seed: int = 42,
    fault_step: int = 300,
    dropout_probability: float = 0.05,
    sensor_std_m: float = 0.05,
) -> list[dict[str, float | int | bool | None]]:
    """Jalankan clog fault; hasil dapat dipakai untuk plot dan metrik temporal."""

    if steps <= 0:
        raise ValueError("steps harus positif")
    if fault_step < 0:
        raise ValueError("fault_step harus non-negatif")
    if not 0 <= dropout_probability <= 1:
        raise ValueError("dropout_probability harus di rentang [0, 1]")
    if sensor_std_m <= 0:
        raise ValueError("sensor_std_m harus positif")
    parameters = TankParameters()
    plant = TankPlant(2.0, parameters)
    estimator = ScalarKalmanFilter(estimate=2.0, variance=0.2, process_variance=0.0025)
    detector = RunningZScoreDetector(threshold=3.0, warmup=30)
    rng = random.Random(seed)
    rows: list[dict[str, float | int | bool | None]] = []

    for step in range(steps):
        inflow = 1.2 + 0.3 * math.sin(step / 30.0)
        actual_coefficient = 0.40 if step >= fault_step else parameters.outlet_coefficient
        true_level = plant.step(inflow, outlet_coefficient=actual_coefficient)
        control_effect = _model_delta(estimator.estimate, inflow, parameters)
        predicted, predicted_variance = estimator.predict(control_effect)

        measurement = None
        if rng.random() >= dropout_probability:
            measurement = true_level + rng.gauss(0.0, sensor_std_m)

        residual = None if measurement is None else measurement - predicted
        alarm, score = (False, None)
        if residual is not None:
            alarm, score = detector.observe(residual)
            estimator.update(measurement, sensor_std_m**2)

        rows.append(
            {
                "step": step,
                "true_level_m": true_level,
                "measurement_m": measurement,
                "predicted_m": predicted,
                "estimate_m": estimator.estimate,
                "variance_m2": estimator.variance,
                "predicted_variance_m2": predicted_variance,
                "residual_m": residual,
                "z_score": score,
                "alarm": alarm,
                "fault_active": step >= fault_step,
            }
        )
    return rows
