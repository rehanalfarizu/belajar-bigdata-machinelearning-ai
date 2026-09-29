from __future__ import annotations

import asyncio
import unittest

from patterns_lab import Reading, async_demo, valid_numbers


class PatternsLabTest(unittest.TestCase):
    def test_reading_rejects_empty_id(self) -> None:
        with self.assertRaises(ValueError):
            Reading(sensor_id="", value=1.0)

    def test_generator_skips_empty_lines(self) -> None:
        self.assertEqual(list(valid_numbers(["1", "", " 2.5 "])), [1.0, 2.5])

    def test_generator_exposes_invalid_input(self) -> None:
        with self.assertRaises(ValueError):
            list(valid_numbers(["invalid"]))

    def test_async_gather_preserves_input_order(self) -> None:
        self.assertEqual(asyncio.run(async_demo()), ["first", "second"])


if __name__ == "__main__":
    unittest.main()
