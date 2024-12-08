# test_advanced.py
import unittest
from math_functions.advanced import factoriel, power, sqrt

class TestAdvanced(unittest.TestCase):
    def test_factoriel(self):
        self.assertEqual(factoriel(5), 120)
        self.assertEqual(factoriel(0), 1)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2)

if __name__ == "__main__":
    unittest.main()
