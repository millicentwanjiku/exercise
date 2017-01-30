import unittest
from fibonacci import fibonacci
class FibonacciTests(unittest.TestCase):
    def test_if_lists_are_allowed(self):
    	"""Tests if list inputs are allowed"""
    	self.assertEqual(fibonacci([]), 'Only integers are allowed')

    def test_if_dictionary_is_allowed(self):
    	"""Tests if dictionary inputs are allowed"""
    	self.assertEqual(fibonacci({}), 'Only integers are allowed')

    def test_if_a_string_is_allowed(self):
    	"""Tests if dictionary inputs are allowed"""
    	self.assertEqual(fibonacci(""), 'Only integers are allowed')

    def test_if_float_nuumbers_are_allowed(self):
    	"""Tests if dictionary inputs are allowed"""
    	self.assertEqual(fibonacci(52.28), 'Only integers are allowed')

    def test_if_it_accepts_negative_numbers(self):
    	"""Tests if the function accepts negative numbers"""
    	self.assertEqual(fibonacci(-2), 'Only positive numbers are accepted')

    def test_if_the_return_value_of_zero_is_zero(self):
    	"""Tests if dictionary inputs are allowed"""
    	self.assertEqual(fibonacci(0), 0)

    def test_if_the_return_value_of_one_is_one(self):
    	"""Tests if dictionary inputs are allowed"""
    	self.assertEqual(fibonacci(1), 1)

    def test_if_the_return_value_of_two_is_one(self):
    	"""Tests if dictionary inputs are allowed"""
    	self.assertEqual(fibonacci(2), 1)

    def test_if_the_function_returns_correct_value(self):
    	"""Tests if the function returns the correct value of a number"""
    	self.assertEqual(fibonacci(6), 8)

    def test_if_the_function_returns_result_of_type_integer(self):
    	"""Tests if the function returns a value of type integer"""
    	self.assertIsInstance(fibonacci(7), int)

    
