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


class SubscriptionSched(object):
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
        'days': 'list[SubscriptionSchedDays]',
        'tz_offset': 'int',
        'start_offset': 'int',
        'end_offset': 'int'
    }

    attribute_map = {
        'days': 'days',
        'tz_offset': 'tzOffset',
        'start_offset': 'startOffset',
        'end_offset': 'endOffset'
    }

    def __init__(self, days=None, tz_offset=None, start_offset=None, end_offset=None, local_vars_configuration=None):  # noqa: E501
        """SubscriptionSched - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._days = None
        self._tz_offset = None
        self._start_offset = None
        self._end_offset = None
        self.discriminator = None

        if days is not None:
            self.days = days
        if tz_offset is not None:
            self.tz_offset = tz_offset
        if start_offset is not None:
            self.start_offset = start_offset
        if end_offset is not None:
            self.end_offset = end_offset

    @property
    def days(self):
        """Gets the days of this SubscriptionSched.  # noqa: E501


        :return: The days of this SubscriptionSched.  # noqa: E501
        :rtype: list[SubscriptionSchedDays]
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this SubscriptionSched.


        :param days: The days of this SubscriptionSched.  # noqa: E501
        :type: list[SubscriptionSchedDays]
        """

        self._days = days

    @property
    def tz_offset(self):
        """Gets the tz_offset of this SubscriptionSched.  # noqa: E501

        Timezone offset in seconds (wrt GMT)  # noqa: E501

        :return: The tz_offset of this SubscriptionSched.  # noqa: E501
        :rtype: int
        """
        return self._tz_offset

    @tz_offset.setter
    def tz_offset(self, tz_offset):
        """Sets the tz_offset of this SubscriptionSched.

        Timezone offset in seconds (wrt GMT)  # noqa: E501

        :param tz_offset: The tz_offset of this SubscriptionSched.  # noqa: E501
        :type: int
        """

        self._tz_offset = tz_offset

    @property
    def start_offset(self):
        """Gets the start_offset of this SubscriptionSched.  # noqa: E501


        :return: The start_offset of this SubscriptionSched.  # noqa: E501
        :rtype: int
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        """Sets the start_offset of this SubscriptionSched.


        :param start_offset: The start_offset of this SubscriptionSched.  # noqa: E501
        :type: int
        """

        self._start_offset = start_offset

    @property
    def end_offset(self):
        """Gets the end_offset of this SubscriptionSched.  # noqa: E501


        :return: The end_offset of this SubscriptionSched.  # noqa: E501
        :rtype: int
        """
        return self._end_offset

    @end_offset.setter
    def end_offset(self, end_offset):
        """Sets the end_offset of this SubscriptionSched.


        :param end_offset: The end_offset of this SubscriptionSched.  # noqa: E501
        :type: int
        """

        self._end_offset = end_offset

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
        if not isinstance(other, SubscriptionSched):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionSched):
            return True

        return self.to_dict() != other.to_dict()