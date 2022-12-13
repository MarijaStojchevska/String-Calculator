from string_calculator import Calculator
import unittest

class TestCalculator(unittest.TestCase):
    c = Calculator()

    def test_empty_input(self):
        result = self.c.add_numbers("", ",")
        self.assertEqual(result, 0)

    def test_null_input(self):
        result = self.c.add_numbers("null", ",")
        self.assertEqual(result, 0)

    def test_valid_nums(self):
        result = self.c.add_numbers("2,5,2", ",")
        self.assertEqual(result, 9)

    def test_delimiter(self):
        result = self.c.add_numbers("2/5/2", "/")
        self.assertEqual(result, 9)

    def test_negative_nums(self):
        with self.assertRaises(Exception):
            self.c.add_numbers("9,8,-1,8", ",")

    def test_nums_greater_than_100(self):
        result = self.c.add_numbers("2,101,5", ",")
        self.assertEqual(result, 7)

    def test_chars(self):
        with self.assertRaises(ValueError):
            self.c.add_numbers("aa 1 8", " ")

    def test_empty_space_character(self):
        with self.assertRaises(ValueError):
            self.c.add_numbers("4, ,5,6", ",")