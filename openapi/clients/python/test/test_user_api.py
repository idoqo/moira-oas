# coding: utf-8

"""
    Moira Alert

    This is an API description for [Moira Alert project](https://moira.readthedocs.io/en/latest/overview.html). Please check <https://github.com/moira-alert/>  # noqa: E501

    The version of the OpenAPI document: 2.5.1.48
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.user_api import UserApi  # noqa: E501
from openapi_client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_user(self):
        """Test case for get_user

        Gets the username of the authenticated user if it is available.  # noqa: E501
        """
        pass

    def test_get_user_settings(self):
        """Test case for get_user_settings

        Get the user's contacts and subscriptions.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()