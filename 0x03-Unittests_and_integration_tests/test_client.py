#!/usr/bin/env python3
'''test module for testing client'''


import unittest
from unittest import mock
from unittest.mock import patch, Mock, PropertyMock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from client import GithubOrgClient
# from client import has_license


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

    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    def test_public_repos_url(self, expected):
        '''defining the test method'''
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) \
                as p:
            # mock_response = PropertyMock()
            # p._public_repos_uel.return_value = expected
            p._public_repos_url.return_value = expected
            this_p = GithubOrgClient(expected)
            self.assertEqual(p._public_repos_url(), expected)

    @patch('utils.get_json')
    def test_public_repos(self, expected):
        '''defining the function'''
        # @mock.patch('utils.get_json')
        # mock_response = Mock()
        # mock_response.get_json.return_value = '{payload: True'}
        with patch('client.GithubOrgClient._public_repos_url') as p:
            # @patch('utils.get_json')
            mock_response = Mock()
            mock_response.get_json.return_value = '{payload: True}'
            p._public_repos_url.return_value = 'test_url'
            self.assertEqual(p._public_repos_url(), 'test_url')

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, res, license_key, expected):
        '''defining the function'''
        self.assertEqual(GithubOrgClient.has_license(
            res, license_key), expected)
