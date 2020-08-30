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


class InlineResponse20010(object):
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
        'page': 'float',
        'size': 'float',
        'total': 'float',
        'list': 'list[Trigger]'
    }

    attribute_map = {
        'page': 'page',
        'size': 'size',
        'total': 'total',
        'list': 'list'
    }

    def __init__(self, page=None, size=None, total=None, list=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse20010 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._page = None
        self._size = None
        self._total = None
        self._list = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if size is not None:
            self.size = size
        if total is not None:
            self.total = total
        if list is not None:
            self.list = list

    @property
    def page(self):
        """Gets the page of this InlineResponse20010.  # noqa: E501

        current item page  # noqa: E501

        :return: The page of this InlineResponse20010.  # noqa: E501
        :rtype: float
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this InlineResponse20010.

        current item page  # noqa: E501

        :param page: The page of this InlineResponse20010.  # noqa: E501
        :type: float
        """

        self._page = page

    @property
    def size(self):
        """Gets the size of this InlineResponse20010.  # noqa: E501

        number of triggers shown per page  # noqa: E501

        :return: The size of this InlineResponse20010.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this InlineResponse20010.

        number of triggers shown per page  # noqa: E501

        :param size: The size of this InlineResponse20010.  # noqa: E501
        :type: float
        """

        self._size = size

    @property
    def total(self):
        """Gets the total of this InlineResponse20010.  # noqa: E501

        total number of matching results  # noqa: E501

        :return: The total of this InlineResponse20010.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InlineResponse20010.

        total number of matching results  # noqa: E501

        :param total: The total of this InlineResponse20010.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def list(self):
        """Gets the list of this InlineResponse20010.  # noqa: E501

        list of matching triggers  # noqa: E501

        :return: The list of this InlineResponse20010.  # noqa: E501
        :rtype: list[Trigger]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this InlineResponse20010.

        list of matching triggers  # noqa: E501

        :param list: The list of this InlineResponse20010.  # noqa: E501
        :type: list[Trigger]
        """

        self._list = list

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
        if not isinstance(other, InlineResponse20010):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20010):
            return True

        return self.to_dict() != other.to_dict()
