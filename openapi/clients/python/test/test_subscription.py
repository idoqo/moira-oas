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
from openapi_client.models.subscription import Subscription  # noqa: E501
from openapi_client.rest import ApiException

class TestSubscription(unittest.TestCase):
    """Subscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Subscription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.subscription.Subscription()  # noqa: E501
        if include_optional :
            return Subscription(
                contacts = ["acd2db98-1659-4a2f-b227-52d71f6e3ba1"], 
                tags = ["server","cpu"], 
                sched = openapi_client.models.subscription_sched.Subscription_sched(
                    days = [
                        openapi_client.models.subscription_sched_days.Subscription_sched_days(
                            enabled = True, 
                            name = 'Mon', )
                        ], 
                    tz_offset = -60, 
                    start_offset = 0, 
                    end_offset = 1439, ), 
                plotting = openapi_client.models.subscription_plotting.Subscription_plotting(
                    enabled = True, 
                    theme = 'dark', ), 
                id = '292516ed-4924-4154-a62c-ebe312431fce', 
                enabled = True, 
                any_tags = False, 
                ignore_warnings = False, 
                ignore_recoverings = False, 
                throttling = False, 
                user = '0'
            )
        else :
            return Subscription(
        )

    def testSubscription(self):
        """Test Subscription"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
