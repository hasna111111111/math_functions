# test_arithmetic.py
import unittest
from math_functions.arithmetic import add, subtract

class TestArithmetic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

if __name__ == "__main__":
    unittest.main()
