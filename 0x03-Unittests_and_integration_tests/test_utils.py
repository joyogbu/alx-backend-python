#!/usr/bin/env python3
'''testing module for acess_map function'''


import unittest
from parameterized import parameterized
from unittest import mock
from unittest.mock import patch, Mock
from utils import access_nested_map
from utils import get_json
from utils import memoize


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
    # @mock.patch('requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    # @mock.patch('requests.get')
    def test_get_json(self, test_url, test_payload):
        '''defining the function for testing mock url'''
        # test_url="http://example.com", test_payload={"payload": True}
        # self.assert_call_once_with(test_url)
        with patch('requests.get'):
            mock_response = Mock()
            mock_response.get_json.return_value = test_payload
            # mock_get.return_value = mock_response
            mock_response.get.side_effect = test_payload.get
            self.assertEqual(mock_response.get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    '''defining the class for memoixation'''
    def test_memoize(self):
        '''defing the test function'''
        class TestClass:
            '''defining the class'''
            def a_method(self):
                '''defining the function'''
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
            with patch('utils.memoize'):
                mock_response = Mock()
                mock_response.a_method.return_value = 42
                if mock_response.call_count == 2:
                    self.assertEqual(a_method(), 42)
