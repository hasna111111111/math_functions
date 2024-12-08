# test_utils.py
import unittest
from math_functions.utils import max_val, min_val

class TestUtils(unittest.TestCase):
    def test_max_val(self):
        self.assertEqual(max_val(1, 3, 5, 7), 7)

    def test_min_val(self):
        self.assertEqual(min_val(1, 3, 5, 7), 1)

if __name__ == "__main__":
    unittest.main()
