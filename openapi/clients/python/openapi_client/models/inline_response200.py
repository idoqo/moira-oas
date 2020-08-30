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


class InlineResponse200(object):
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
        'remote_allowed': 'bool',
        'contacts': 'list[InlineResponse200Contacts]'
    }

    attribute_map = {
        'remote_allowed': 'remoteAllowed',
        'contacts': 'contacts'
    }

    def __init__(self, remote_allowed=None, contacts=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._remote_allowed = None
        self._contacts = None
        self.discriminator = None

        if remote_allowed is not None:
            self.remote_allowed = remote_allowed
        if contacts is not None:
            self.contacts = contacts

    @property
    def remote_allowed(self):
        """Gets the remote_allowed of this InlineResponse200.  # noqa: E501

        Flag for determining if Moira is accessible remotely.  # noqa: E501

        :return: The remote_allowed of this InlineResponse200.  # noqa: E501
        :rtype: bool
        """
        return self._remote_allowed

    @remote_allowed.setter
    def remote_allowed(self, remote_allowed):
        """Sets the remote_allowed of this InlineResponse200.

        Flag for determining if Moira is accessible remotely.  # noqa: E501

        :param remote_allowed: The remote_allowed of this InlineResponse200.  # noqa: E501
        :type: bool
        """

        self._remote_allowed = remote_allowed

    @property
    def contacts(self):
        """Gets the contacts of this InlineResponse200.  # noqa: E501

        List of enabled contact types  # noqa: E501

        :return: The contacts of this InlineResponse200.  # noqa: E501
        :rtype: list[InlineResponse200Contacts]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this InlineResponse200.

        List of enabled contact types  # noqa: E501

        :param contacts: The contacts of this InlineResponse200.  # noqa: E501
        :type: list[InlineResponse200Contacts]
        """

        self._contacts = contacts

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
        if not isinstance(other, InlineResponse200):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse200):
            return True

        return self.to_dict() != other.to_dict()
