# Importing modules from another directory (Non-root directory)
# https://youtu.be/CqvZ3vGoGs0

import unittest
import calc


class TestCalc(unittest.TestCase):
    # Create new class called TestCalc and inherit from unittest.TestCase
    def test_add(self):
        # Take self as the 1st argument
        self.assertEqual(calc.add(5, 10), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -2), -3)

    def test_subtract(self):
        # Take self as the 1st argument
        self.assertEqual(calc.subtract(5, 10), -5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -2), 1)

    def test_multiply(self):
        # Take self as the 1st argument
        self.assertEqual(calc.multiply(5, 10), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -2), 2)

    def test_divide(self):
        # Take self as the 1st argument
        self.assertEqual(calc.divide(5, 10), 0.5)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -2), 0.5)

        # 👎 self.assertRaises(ValueError, calc.divide, 10, 0)

        # 👍 Preferred - Apply the context manager
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


"""
If we run the this module directly, run the code withnin the conditional
"""

if __name__ == "__main__":
    unittest.main()
