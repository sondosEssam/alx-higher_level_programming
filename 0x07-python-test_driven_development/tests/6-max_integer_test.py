#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self, list=[]):
        self.assertEqual(max_integer([1,2,3,4,5]), 5)
    def test_max_integer_None(self, list=[]):
        self.assertEqual(max_integer([]), None)
    def test_max_integer_positive_and_negative(self, list=[]):
        self.assertEqual(max_integer([1,2,3,4,-5]), 4)
    def test_max_integer_negative(self, list=[]):
        self.assertEqual(max_integer([-1,-2,-3,-4,-5]), -1)
    def test_max_integer_no_arg(self, list=[]):
        self.assertEqual(max_integer(), None)
    def test_max_integer(self, list=[]):
        self.assertEqual(max_integer([1,2,3,4,5]), 5)
    def test_mixed_list(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "foo"])
def test_nan(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('nan'), 100]), 100)
if __name__ == '__main__':
    unittest.main()
