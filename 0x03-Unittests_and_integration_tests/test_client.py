#!/usr/bin/env python3
'''test module for testing client'''


import unittest
from unittest import mock
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    '''defining the test class for client'''
    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    # @mock.patch('utils.get_json')
    def test_org(self, expected):
        '''defining the test org function'''
        with patch('client.GithubOrgClient.org')as p:
            mock_response = Mock()
            mock_response.org.return_value = expected
            self.assertEqual(mock_response.org(), expected)
