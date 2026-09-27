from datetime import datetime, timedelta, timezone
import unittest

from digital_twin_lab.demo import summarize
from digital_twin_lab.safety import (
    CommandDecision,
    CommandGuard,
    GuardPolicy,
    Recommendation,
)
from digital_twin_lab.simulation import TankParameters, TankPlant, run_tank_experiment


class SimulationTest(unittest.TestCase):
    def test_tank_respects_physical_bounds(self) -> None:
        plant = TankPlant(9.9, TankParameters(maximum_level_m=10.0))
        for _ in range(100):
            plant.step(100.0)
        self.assertEqual(plant.level_m, 10.0)

    def test_experiment_is_reproducible_and_detects_fault(self) -> None:
        first = run_tank_experiment(steps=240, fault_step=120, seed=7)
        second = run_tank_experiment(steps=240, fault_step=120, seed=7)
        self.assertEqual(first, second)
        metrics = summarize(first)
        self.assertIsNotNone(metrics["detection_delay_steps"])
        self.assertLess(float(metrics["mae_m"]), 0.1)

    def test_invalid_experiment_parameters_fail_fast(self) -> None:
        with self.assertRaises(ValueError):
            run_tank_experiment(steps=0)
        with self.assertRaises(ValueError):
            run_tank_experiment(sensor_std_m=0.0)


class SafetyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.now = datetime(2026, 1, 1, tzinfo=timezone.utc)
        self.guard = CommandGuard(
            GuardPolicy(
                minimum=0.0,
                maximum=10.0,
                maximum_delta=1.0,
                maximum_uncertainty=0.2,
                maximum_age=timedelta(seconds=30),
            )
        )

    def recommendation(self, target: float = 5.5) -> Recommendation:
        return Recommendation("tank-01", target, "stabilkan level", self.now, "rule-v1")

    def test_requires_operator_approval(self) -> None:
        pending = self.guard.evaluate(
            self.recommendation(), current_value=5.0, state_uncertainty=0.1, now=self.now
        )
        self.assertEqual(pending.decision, CommandDecision.PENDING_APPROVAL)
        approved = self.guard.evaluate(
            self.recommendation(),
            current_value=5.0,
            state_uncertainty=0.1,
            now=self.now,
            operator_approved=True,
        )
        self.assertEqual(approved.decision, CommandDecision.APPROVED)

    def test_hard_constraint_cannot_be_overridden(self) -> None:
        result = self.guard.evaluate(
            self.recommendation(target=12.0),
            current_value=5.0,
            state_uncertainty=0.1,
            now=self.now,
            operator_approved=True,
        )
        self.assertEqual(result.decision, CommandDecision.REJECTED)
        self.assertIn("target di luar safety envelope", result.reasons)

    def test_naive_timestamp_is_rejected(self) -> None:
        naive = Recommendation(
            "tank-01", 5.5, "stabilkan level", datetime(2026, 1, 1), "rule-v1"
        )
        result = self.guard.evaluate(
            naive,
            current_value=5.0,
            state_uncertainty=0.1,
            now=self.now,
            operator_approved=True,
        )
        self.assertEqual(result.decision, CommandDecision.REJECTED)
        self.assertTrue(any("timezone-aware" in reason for reason in result.reasons))


if __name__ == "__main__":
    unittest.main()
