"""Boundary rekomendasi-ke-command dengan hard constraint dan approval."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum


class CommandDecision(str, Enum):
    REJECTED = "rejected"
    PENDING_APPROVAL = "pending_approval"
    APPROVED = "approved"


@dataclass(frozen=True)
class Recommendation:
    asset_id: str
    target: float
    reason: str
    created_at: datetime
    model_version: str


@dataclass(frozen=True)
class GuardPolicy:
    minimum: float
    maximum: float
    maximum_delta: float
    maximum_uncertainty: float
    maximum_age: timedelta
    require_human_approval: bool = True


@dataclass(frozen=True)
class GuardResult:
    decision: CommandDecision
    reasons: tuple[str, ...]
    audit_record: dict[str, str | float]


class CommandGuard:
    def __init__(self, policy: GuardPolicy) -> None:
        self.policy = policy

    def evaluate(
        self,
        recommendation: Recommendation,
        *,
        current_value: float,
        state_uncertainty: float,
        now: datetime,
        operator_approved: bool = False,
        emergency: bool = False,
    ) -> GuardResult:
        reasons: list[str] = []
        if emergency:
            reasons.append("sistem berada pada emergency state")
        if not self.policy.minimum <= recommendation.target <= self.policy.maximum:
            reasons.append("target di luar safety envelope")
        if abs(recommendation.target - current_value) > self.policy.maximum_delta:
            reasons.append("perubahan melampaui rate/delta limit")
        if state_uncertainty > self.policy.maximum_uncertainty:
            reasons.append("uncertainty state terlalu tinggi")
        timestamps_are_aware = all(
            value.tzinfo is not None and value.utcoffset() is not None
            for value in (recommendation.created_at, now)
        )
        if not timestamps_are_aware:
            reasons.append("timestamp rekomendasi dan evaluasi harus timezone-aware")
        elif now - recommendation.created_at > self.policy.maximum_age:
            reasons.append("rekomendasi stale")

        if reasons:
            decision = CommandDecision.REJECTED
        elif self.policy.require_human_approval and not operator_approved:
            decision = CommandDecision.PENDING_APPROVAL
            reasons.append("menunggu persetujuan operator")
        else:
            decision = CommandDecision.APPROVED

        audit = {
            "asset_id": recommendation.asset_id,
            "target": recommendation.target,
            "model_version": recommendation.model_version,
            "decision": decision.value,
            "evaluated_at": now.isoformat(),
        }
        return GuardResult(decision, tuple(reasons), audit)
