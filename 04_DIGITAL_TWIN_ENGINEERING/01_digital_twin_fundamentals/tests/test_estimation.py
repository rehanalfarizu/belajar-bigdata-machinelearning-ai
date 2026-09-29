import unittest

from digital_twin_lab.estimation import ScalarKalmanFilter, fuse_measurements


class ScalarKalmanFilterTest(unittest.TestCase):
    def test_uncertainty_grows_without_sensor(self) -> None:
        filter_ = ScalarKalmanFilter(estimate=0.0, variance=1.0, process_variance=0.2)
        _, variance = filter_.step(control_effect=1.0)
        self.assertAlmostEqual(filter_.estimate, 1.0)
        self.assertAlmostEqual(variance, 1.2)

    def test_measurement_reduces_uncertainty(self) -> None:
        filter_ = ScalarKalmanFilter(estimate=0.0, variance=1.0, process_variance=0.1)
        _, predicted_variance = filter_.predict()
        estimate, corrected_variance = filter_.update(10.0, measurement_variance=1.0)
        self.assertGreater(estimate, 0.0)
        self.assertLess(estimate, 10.0)
        self.assertLess(corrected_variance, predicted_variance)

    def test_lower_variance_sensor_has_more_influence(self) -> None:
        estimate, variance = fuse_measurements(0.0, 100.0, [(2.0, 0.01), (8.0, 4.0)])
        self.assertLess(abs(estimate - 2.0), abs(estimate - 8.0))
        self.assertLess(variance, 0.01)


if __name__ == "__main__":
    unittest.main()
