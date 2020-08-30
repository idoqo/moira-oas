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


class TagStatistics(object):
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
        'name': 'str',
        'triggers': 'list[str]',
        'subscriptions': 'list[Subscription]'
    }

    attribute_map = {
        'name': 'name',
        'triggers': 'triggers',
        'subscriptions': 'subscriptions'
    }

    def __init__(self, name=None, triggers=None, subscriptions=None, local_vars_configuration=None):  # noqa: E501
        """TagStatistics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._triggers = None
        self._subscriptions = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if triggers is not None:
            self.triggers = triggers
        if subscriptions is not None:
            self.subscriptions = subscriptions

    @property
    def name(self):
        """Gets the name of this TagStatistics.  # noqa: E501

        name of the tag  # noqa: E501

        :return: The name of this TagStatistics.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TagStatistics.

        name of the tag  # noqa: E501

        :param name: The name of this TagStatistics.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def triggers(self):
        """Gets the triggers of this TagStatistics.  # noqa: E501

        array of trigger IDs that have this tag  # noqa: E501

        :return: The triggers of this TagStatistics.  # noqa: E501
        :rtype: list[str]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this TagStatistics.

        array of trigger IDs that have this tag  # noqa: E501

        :param triggers: The triggers of this TagStatistics.  # noqa: E501
        :type: list[str]
        """

        self._triggers = triggers

    @property
    def subscriptions(self):
        """Gets the subscriptions of this TagStatistics.  # noqa: E501

        subscriptions for this tag  # noqa: E501

        :return: The subscriptions of this TagStatistics.  # noqa: E501
        :rtype: list[Subscription]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this TagStatistics.

        subscriptions for this tag  # noqa: E501

        :param subscriptions: The subscriptions of this TagStatistics.  # noqa: E501
        :type: list[Subscription]
        """

        self._subscriptions = subscriptions

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
        if not isinstance(other, TagStatistics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TagStatistics):
            return True

        return self.to_dict() != other.to_dict()
