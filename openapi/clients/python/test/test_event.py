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
from openapi_client.models.event import Event  # noqa: E501
from openapi_client.rest import ApiException

class TestEvent(unittest.TestCase):
    """Event unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Event
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.event.Event()  # noqa: E501
        if include_optional :
            return Event(
                trigger_event = True, 
                timestamp = 1590741878, 
                metric = 'carbon.agents.*.metricsReceived', 
                value = 70, 
                state = 'OK', 
                trigger_id = '5ff37996-8927-4cab-8987-970e80d8e0a8', 
                sub_id = '0', 
                contact_id = '0', 
                old_state = 'ERROR', 
                msg = '0', 
                event_message = openapi_client.models.event_event_message.Event_event_message(
                    maintenance = openapi_client.models.event_event_message_maintenance.Event_event_message_maintenance(
                        setup_user = '0', 
                        setup_time = 56, 
                        remove_user = '0', 
                        remove_time = 56, ), 
                    interval = 56, )
            )
        else :
            return Event(
        )

    def testEvent(self):
        """Test Event"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
