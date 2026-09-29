from __future__ import annotations

import unittest

from foundation_math_lab import (
    bayes_positive,
    bootstrap_mean_interval,
    coin_two_sided_p_value,
    confidence_interval_mean,
    correlation,
    dot,
    gradient_descent,
    l2_norm,
    matrix_vector,
    numeric_derivative,
)


class FoundationMathLabTest(unittest.TestCase):
    def test_dot_rejects_shape_mismatch(self) -> None:
        with self.assertRaises(ValueError):
            dot([1.0], [1.0, 2.0])

    def test_three_four_five_norm(self) -> None:
        self.assertAlmostEqual(l2_norm([3.0, 4.0]), 5.0)

    def test_matrix_transforms_vector(self) -> None:
        self.assertEqual(matrix_vector([[2.0, 0.0], [0.0, 3.0]], [2.0, 1.0]), [4.0, 3.0])

    def test_numeric_derivative_matches_quadratic(self) -> None:
        self.assertAlmostEqual(numeric_derivative(lambda x: x**2, 3.0), 6.0, places=5)

    def test_reasonable_rate_reduces_loss(self) -> None:
        losses = gradient_descent(0.25)
        self.assertLess(losses[-1], losses[0])

    def test_bayes_update_uses_base_rate(self) -> None:
        self.assertAlmostEqual(bayes_positive(0.01, 0.9, 0.05), 0.1538461538)

    def test_confidence_interval_contains_sample_mean(self) -> None:
        low, high = confidence_interval_mean([9, 11, 10, 12, 8, 10, 9, 11])
        self.assertLess(low, 10.0)
        self.assertGreater(high, 10.0)

    def test_exact_coin_p_value(self) -> None:
        self.assertAlmostEqual(coin_two_sided_p_value(8, 10), 0.109375)

    def test_bootstrap_interval_is_ordered(self) -> None:
        low, high = bootstrap_mean_interval([2, 3, 3, 5, 8], repeats=500, seed=7)
        self.assertLessEqual(low, high)
        self.assertLessEqual(low, 4.2)
        self.assertGreaterEqual(high, 4.2)

    def test_u_shape_has_zero_linear_correlation(self) -> None:
        xs = [-2.0, -1.0, 0.0, 1.0, 2.0]
        self.assertAlmostEqual(correlation(xs, [x * x for x in xs]), 0.0)


if __name__ == "__main__":
    unittest.main()
