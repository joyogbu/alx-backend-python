#!/usr/bin/env python3
'''testing module for acess_map function'''


import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''defining a test access_nested_map class'''
    @parameterized.expand
    def test_access_nested_map(self):
        '''defining the function test'''
        nested_map = {"a": 1}
        self.assertEqual(access_nested_map(nested_map, ("a")), 1)

    def test_access_nested_map(self):
        '''defining the function for test2'''
        nested_map = {"a": {"b": 2}}
        self.assertEqual(access_nested_map(nested_map, ("a",)), {'b': 2})

    def test_access_nested_map(self):
        '''defining the functiin for test3'''
        nested_map = {"a": {"b": 2}}
        self.assertEqual(access_nested_map(nested_map, ("a", "b")), 2)
