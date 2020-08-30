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
from openapi_client.api.contact_api import ContactApi  # noqa: E501
from openapi_client.rest import ApiException


class TestContactApi(unittest.TestCase):
    """ContactApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.contact_api.ContactApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_new_contact(self):
        """Test case for create_new_contact

        Creates a new contact notification for the current user.  # noqa: E501
        """
        pass

    def test_delete_contact(self):
        """Test case for delete_contact

        Deletes notification contact for the current user and remove the contact ID from all subscriptions.  # noqa: E501
        """
        pass

    def test_get_contacts(self):
        """Test case for get_contacts

        Gets all Moira contacts.  # noqa: E501
        """
        pass

    def test_test_contact_notification(self):
        """Test case for test_contact_notification

        Push a test notification to verify that the contact is properly set up.  # noqa: E501
        """
        pass

    def test_update_contact(self):
        """Test case for update_contact

        Updates an existing notification contact to the values passed in the request body.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()