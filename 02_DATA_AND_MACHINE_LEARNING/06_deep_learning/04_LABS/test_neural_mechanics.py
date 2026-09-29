from __future__ import annotations

import unittest

from neural_mechanics import (
    binary_cross_entropy,
    finite_difference_gradient,
    neuron,
    train_linear_weight,
)


class NeuralMechanicsTest(unittest.TestCase):
    def test_neuron_rejects_shape_mismatch(self) -> None:
        with self.assertRaises(ValueError):
            neuron([1], [1, 2], 0)

    def test_correct_confident_prediction_has_low_loss(self) -> None:
        self.assertLess(binary_cross_entropy(1, 0.99), 0.02)

    def test_finite_difference_matches_quadratic(self) -> None:
        self.assertAlmostEqual(finite_difference_gradient(lambda x: x**2, 3), 6, places=5)

    def test_training_reduces_loss(self) -> None:
        weight, losses = train_linear_weight([1, 2, 3], [2, 4, 6], 0.05, 20)
        self.assertLess(losses[-1], losses[0])
        self.assertAlmostEqual(weight, 2, places=1)
