# coding: utf-8

"""
    Moira Alert

    This is an API description for [Moira Alert project](https://moira.readthedocs.io/en/latest/overview.html). Please check <https://github.com/moira-alert/>  # noqa: E501

    The version of the OpenAPI document: 2.5.1.48
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class NotificationsListList(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'event': 'Event',
        'trigger': 'Trigger',
        'contact': 'Contact',
        'plotting': 'NotificationsListPlotting',
        'throttled': 'bool',
        'send_fail': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'event': 'event',
        'trigger': 'trigger',
        'contact': 'contact',
        'plotting': 'plotting',
        'throttled': 'throttled',
        'send_fail': 'send_fail',
        'timestamp': 'timestamp'
    }

    def __init__(self, event=None, trigger=None, contact=None, plotting=None, throttled=None, send_fail=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """NotificationsListList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._event = None
        self._trigger = None
        self._contact = None
        self._plotting = None
        self._throttled = None
        self._send_fail = None
        self._timestamp = None
        self.discriminator = None

        if event is not None:
            self.event = event
        if trigger is not None:
            self.trigger = trigger
        if contact is not None:
            self.contact = contact
        if plotting is not None:
            self.plotting = plotting
        if throttled is not None:
            self.throttled = throttled
        if send_fail is not None:
            self.send_fail = send_fail
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def event(self):
        """Gets the event of this NotificationsListList.  # noqa: E501


        :return: The event of this NotificationsListList.  # noqa: E501
        :rtype: Event
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this NotificationsListList.


        :param event: The event of this NotificationsListList.  # noqa: E501
        :type: Event
        """

        self._event = event

    @property
    def trigger(self):
        """Gets the trigger of this NotificationsListList.  # noqa: E501


        :return: The trigger of this NotificationsListList.  # noqa: E501
        :rtype: Trigger
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this NotificationsListList.


        :param trigger: The trigger of this NotificationsListList.  # noqa: E501
        :type: Trigger
        """

        self._trigger = trigger

    @property
    def contact(self):
        """Gets the contact of this NotificationsListList.  # noqa: E501


        :return: The contact of this NotificationsListList.  # noqa: E501
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this NotificationsListList.


        :param contact: The contact of this NotificationsListList.  # noqa: E501
        :type: Contact
        """

        self._contact = contact

    @property
    def plotting(self):
        """Gets the plotting of this NotificationsListList.  # noqa: E501


        :return: The plotting of this NotificationsListList.  # noqa: E501
        :rtype: NotificationsListPlotting
        """
        return self._plotting

    @plotting.setter
    def plotting(self, plotting):
        """Sets the plotting of this NotificationsListList.


        :param plotting: The plotting of this NotificationsListList.  # noqa: E501
        :type: NotificationsListPlotting
        """

        self._plotting = plotting

    @property
    def throttled(self):
        """Gets the throttled of this NotificationsListList.  # noqa: E501

        boolean flag to check if a notification is throttled or not  # noqa: E501

        :return: The throttled of this NotificationsListList.  # noqa: E501
        :rtype: bool
        """
        return self._throttled

    @throttled.setter
    def throttled(self, throttled):
        """Sets the throttled of this NotificationsListList.

        boolean flag to check if a notification is throttled or not  # noqa: E501

        :param throttled: The throttled of this NotificationsListList.  # noqa: E501
        :type: bool
        """

        self._throttled = throttled

    @property
    def send_fail(self):
        """Gets the send_fail of this NotificationsListList.  # noqa: E501

        count of failed attempts to send the notification  # noqa: E501

        :return: The send_fail of this NotificationsListList.  # noqa: E501
        :rtype: int
        """
        return self._send_fail

    @send_fail.setter
    def send_fail(self, send_fail):
        """Sets the send_fail of this NotificationsListList.

        count of failed attempts to send the notification  # noqa: E501

        :param send_fail: The send_fail of this NotificationsListList.  # noqa: E501
        :type: int
        """

        self._send_fail = send_fail

    @property
    def timestamp(self):
        """Gets the timestamp of this NotificationsListList.  # noqa: E501

        unix timestamp of the time the notification was created  # noqa: E501

        :return: The timestamp of this NotificationsListList.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this NotificationsListList.

        unix timestamp of the time the notification was created  # noqa: E501

        :param timestamp: The timestamp of this NotificationsListList.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NotificationsListList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationsListList):
            return True

        return self.to_dict() != other.to_dict()
