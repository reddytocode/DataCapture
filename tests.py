import unittest
from unittest import TestCase

from data_capture import DataCapture, Number, Stats


class TestDataCapture(TestCase):
    def setUp(self):
        self.capture = DataCapture()
        self.numbers = [3, 9, 3, 4, 6]
        for value in self.numbers:
            self.capture.add(value)

    def test_add(self):
        new_value = 3
        capture = DataCapture()
        count = capture.count
        capture.add(new_value)

        self.assertEqual(capture.count, count + 1)
        self.assertIn(new_value, capture.numbers)

        # invalid values
        with self.assertRaises(ValueError):
            capture.add("invalid")
            capture.add(1001)
            capture.add(-1)

    def test_build_stats(self):
        stats = self.capture.build_stats()
        self.assertIsInstance(stats, Stats)
        self.assertEqual(sorted(stats.data.keys()), sorted(set(self.numbers)))

        expected_data = {
            3: Number(3, 2, 0, 3),
            4: Number(4, 1, 2, 2),
            6: Number(6, 1, 3, 1),
            9: Number(9, 1, 4, 0),
        }
        self.assertEqual(expected_data, stats.data)

    def test_less(self):
        stats = self.capture.build_stats()
        result = stats.less(4)
        self.assertEqual(result, 2)

    def test_between(self):
        stats = self.capture.build_stats()

        result = stats.between(3, 6)
        self.assertEqual(result, 4)

        result = stats.between(6, 3)
        self.assertEqual(result, 4)

        result = stats.between(4, 9)
        self.assertEqual(result, 3)

        result = stats.between(4, 6)
        self.assertEqual(result, 2)

    def test_greater(self):
        stats = self.capture.build_stats()
        result = stats.greater(4)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
