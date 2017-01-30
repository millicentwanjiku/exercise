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