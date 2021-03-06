# coding: utf-8

"""
    Moira Alert

    This is an API description for [Moira Alert project](https://moira.readthedocs.io/en/latest/overview.html). Please check <https://github.com/moira-alert/>  # noqa: E501

    The version of the OpenAPI document: 2.5.1.48
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.contact import Contact  # noqa: E501
from openapi_client.rest import ApiException

class TestContact(unittest.TestCase):
    """Contact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Contact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.contact.Contact()  # noqa: E501
        if include_optional :
            return Contact(
                id = '1dd38765-c5be-418d-81fa-7a5f879c2315', 
                user = '0', 
                type = 'mail', 
                value = 'devops@example.com'
            )
        else :
            return Contact(
        )

    def testContact(self):
        """Test Contact"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
