#!/usr/bin/env python3
'''testing module for acess_map function'''


import unittest
from parameterized import parameterized
from unittest import mock
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''defining a test access_nested_map class'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''defining the function test'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''defining function for test exception'''
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''defining the class for the function get_json'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @mock.patch('requests.get')
    def test_get_json(self, test_url, test_payload):
        '''defining the function for testing mock url'''
        mock.assert_call_once_with(test_url)
        self.assertEqual(get_json(test_url, test_payload))
