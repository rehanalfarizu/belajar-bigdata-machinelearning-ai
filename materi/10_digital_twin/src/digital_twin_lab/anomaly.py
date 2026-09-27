"""Detector residual streaming tanpa melihat data masa depan."""

from __future__ import annotations

from dataclasses import dataclass, field
import math


@dataclass
class RunningZScoreDetector:
    """Baseline Welford online; warm-up mencegah alarm prematur.

    Residual yang sudah menjadi alarm tidak dimasukkan ke baseline agar fault
    panjang tidak segera dianggap normal. Kebijakan ini juga punya trade-off:
    concept drift sehat perlu mekanisme recalibration terpisah.
    """

    threshold: float = 3.0
    warmup: int = 30
    count: int = 0
    mean: float = 0.0
    m2: float = 0.0
    alarm_history: list[bool] = field(default_factory=list)

    @property
    def std(self) -> float:
        return math.sqrt(self.m2 / (self.count - 1)) if self.count > 1 else 0.0

    def observe(self, residual: float) -> tuple[bool, float | None]:
        if not math.isfinite(residual):
            raise ValueError("residual harus finite")

        score = None
        alarm = False
        if self.count >= self.warmup and self.std > 0:
            score = abs(residual - self.mean) / self.std
            alarm = score > self.threshold

        if not alarm:
            self.count += 1
            delta = residual - self.mean
            self.mean += delta / self.count
            self.m2 += delta * (residual - self.mean)

        self.alarm_history.append(alarm)
        return alarm, score
