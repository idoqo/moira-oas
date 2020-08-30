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


class Trigger(object):
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
        'id': 'str',
        'name': 'str',
        'desc': 'str',
        'targets': 'list[str]',
        'warn_value': 'int',
        'error_value': 'int',
        'trigger_type': 'str',
        'tags': 'list[str]',
        'ttl_state': 'str',
        'ttl': 'int',
        'sched': 'SubscriptionSched',
        'expression': 'str',
        'patterns': 'list[str]',
        'is_remote': 'bool',
        'mute_new_metrics': 'bool',
        'throttling': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'desc': 'desc',
        'targets': 'targets',
        'warn_value': 'warn_value',
        'error_value': 'error_value',
        'trigger_type': 'trigger_type',
        'tags': 'tags',
        'ttl_state': 'ttl_state',
        'ttl': 'ttl',
        'sched': 'sched',
        'expression': 'expression',
        'patterns': 'patterns',
        'is_remote': 'is_remote',
        'mute_new_metrics': 'mute_new_metrics',
        'throttling': 'throttling'
    }

    def __init__(self, id=None, name=None, desc=None, targets=None, warn_value=None, error_value=None, trigger_type=None, tags=None, ttl_state=None, ttl=None, sched=None, expression=None, patterns=None, is_remote=None, mute_new_metrics=None, throttling=None, local_vars_configuration=None):  # noqa: E501
        """Trigger - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._desc = None
        self._targets = None
        self._warn_value = None
        self._error_value = None
        self._trigger_type = None
        self._tags = None
        self._ttl_state = None
        self._ttl = None
        self._sched = None
        self._expression = None
        self._patterns = None
        self._is_remote = None
        self._mute_new_metrics = None
        self._throttling = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.desc = desc
        if targets is not None:
            self.targets = targets
        if warn_value is not None:
            self.warn_value = warn_value
        self.error_value = error_value
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if tags is not None:
            self.tags = tags
        self.ttl_state = ttl_state
        self.ttl = ttl
        if sched is not None:
            self.sched = sched
        if expression is not None:
            self.expression = expression
        if patterns is not None:
            self.patterns = patterns
        if is_remote is not None:
            self.is_remote = is_remote
        self.mute_new_metrics = mute_new_metrics
        if throttling is not None:
            self.throttling = throttling

    @property
    def id(self):
        """Gets the id of this Trigger.  # noqa: E501

        ID of the trigger  # noqa: E501

        :return: The id of this Trigger.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Trigger.

        ID of the trigger  # noqa: E501

        :param id: The id of this Trigger.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Trigger.  # noqa: E501

        name of the trigger  # noqa: E501

        :return: The name of this Trigger.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Trigger.

        name of the trigger  # noqa: E501

        :param name: The name of this Trigger.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def desc(self):
        """Gets the desc of this Trigger.  # noqa: E501

        informative description of the trigger  # noqa: E501

        :return: The desc of this Trigger.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this Trigger.

        informative description of the trigger  # noqa: E501

        :param desc: The desc of this Trigger.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and desc is None:  # noqa: E501
            raise ValueError("Invalid value for `desc`, must not be `None`")  # noqa: E501

        self._desc = desc

    @property
    def targets(self):
        """Gets the targets of this Trigger.  # noqa: E501

        graphite metric to cause this trigger  # noqa: E501

        :return: The targets of this Trigger.  # noqa: E501
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this Trigger.

        graphite metric to cause this trigger  # noqa: E501

        :param targets: The targets of this Trigger.  # noqa: E501
        :type: list[str]
        """

        self._targets = targets

    @property
    def warn_value(self):
        """Gets the warn_value of this Trigger.  # noqa: E501

        value at which Moira should send a WARNING alert  # noqa: E501

        :return: The warn_value of this Trigger.  # noqa: E501
        :rtype: int
        """
        return self._warn_value

    @warn_value.setter
    def warn_value(self, warn_value):
        """Sets the warn_value of this Trigger.

        value at which Moira should send a WARNING alert  # noqa: E501

        :param warn_value: The warn_value of this Trigger.  # noqa: E501
        :type: int
        """

        self._warn_value = warn_value

    @property
    def error_value(self):
        """Gets the error_value of this Trigger.  # noqa: E501

        value at which Moira should send an ERROR alert  # noqa: E501

        :return: The error_value of this Trigger.  # noqa: E501
        :rtype: int
        """
        return self._error_value

    @error_value.setter
    def error_value(self, error_value):
        """Sets the error_value of this Trigger.

        value at which Moira should send an ERROR alert  # noqa: E501

        :param error_value: The error_value of this Trigger.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and error_value is None:  # noqa: E501
            raise ValueError("Invalid value for `error_value`, must not be `None`")  # noqa: E501

        self._error_value = error_value

    @property
    def trigger_type(self):
        """Gets the trigger_type of this Trigger.  # noqa: E501

        Value is either 'rising' or 'falling'. Dictates when alerts are sent for `warn_value` and `error_value`  # noqa: E501

        :return: The trigger_type of this Trigger.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this Trigger.

        Value is either 'rising' or 'falling'. Dictates when alerts are sent for `warn_value` and `error_value`  # noqa: E501

        :param trigger_type: The trigger_type of this Trigger.  # noqa: E501
        :type: str
        """
        allowed_values = ["rising", "falling"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and trigger_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `trigger_type` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger_type, allowed_values)
            )

        self._trigger_type = trigger_type

    @property
    def tags(self):
        """Gets the tags of this Trigger.  # noqa: E501

        the tags associated with this trigger. New tags are automatically created  # noqa: E501

        :return: The tags of this Trigger.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Trigger.

        the tags associated with this trigger. New tags are automatically created  # noqa: E501

        :param tags: The tags of this Trigger.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def ttl_state(self):
        """Gets the ttl_state of this Trigger.  # noqa: E501

        state to put the metric in if Moira doesn't receive new data for it from graphite. See <https://moira.readthedocs.io/en/latest/development/architecture.html?highlight=ttl#state/>  # noqa: E501

        :return: The ttl_state of this Trigger.  # noqa: E501
        :rtype: str
        """
        return self._ttl_state

    @ttl_state.setter
    def ttl_state(self, ttl_state):
        """Sets the ttl_state of this Trigger.

        state to put the metric in if Moira doesn't receive new data for it from graphite. See <https://moira.readthedocs.io/en/latest/development/architecture.html?highlight=ttl#state/>  # noqa: E501

        :param ttl_state: The ttl_state of this Trigger.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ttl_state is None:  # noqa: E501
            raise ValueError("Invalid value for `ttl_state`, must not be `None`")  # noqa: E501
        allowed_values = ["OK", "WARN", "ERROR", "NODATA", "EXCEPTION"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and ttl_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `ttl_state` ({0}), must be one of {1}"  # noqa: E501
                .format(ttl_state, allowed_values)
            )

        self._ttl_state = ttl_state

    @property
    def ttl(self):
        """Gets the ttl of this Trigger.  # noqa: E501

        number of seconds to wait for metric update from Graphite before changing the metric state  # noqa: E501

        :return: The ttl of this Trigger.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this Trigger.

        number of seconds to wait for metric update from Graphite before changing the metric state  # noqa: E501

        :param ttl: The ttl of this Trigger.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and ttl is None:  # noqa: E501
            raise ValueError("Invalid value for `ttl`, must not be `None`")  # noqa: E501

        self._ttl = ttl

    @property
    def sched(self):
        """Gets the sched of this Trigger.  # noqa: E501


        :return: The sched of this Trigger.  # noqa: E501
        :rtype: SubscriptionSched
        """
        return self._sched

    @sched.setter
    def sched(self, sched):
        """Sets the sched of this Trigger.


        :param sched: The sched of this Trigger.  # noqa: E501
        :type: SubscriptionSched
        """

        self._sched = sched

    @property
    def expression(self):
        """Gets the expression of this Trigger.  # noqa: E501


        :return: The expression of this Trigger.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this Trigger.


        :param expression: The expression of this Trigger.  # noqa: E501
        :type: str
        """

        self._expression = expression

    @property
    def patterns(self):
        """Gets the patterns of this Trigger.  # noqa: E501

        optional Graphite pattern is a single dot-separated metric name, possibly containing one or more wildcards  # noqa: E501

        :return: The patterns of this Trigger.  # noqa: E501
        :rtype: list[str]
        """
        return self._patterns

    @patterns.setter
    def patterns(self, patterns):
        """Sets the patterns of this Trigger.

        optional Graphite pattern is a single dot-separated metric name, possibly containing one or more wildcards  # noqa: E501

        :param patterns: The patterns of this Trigger.  # noqa: E501
        :type: list[str]
        """

        self._patterns = patterns

    @property
    def is_remote(self):
        """Gets the is_remote of this Trigger.  # noqa: E501

        dictates if trigger should be added to Graphite instead of Redis. See <https://moira.readthedocs.io/en/latest/installation/configuration.html#remote-triggers-checker/>  # noqa: E501

        :return: The is_remote of this Trigger.  # noqa: E501
        :rtype: bool
        """
        return self._is_remote

    @is_remote.setter
    def is_remote(self, is_remote):
        """Sets the is_remote of this Trigger.

        dictates if trigger should be added to Graphite instead of Redis. See <https://moira.readthedocs.io/en/latest/installation/configuration.html#remote-triggers-checker/>  # noqa: E501

        :param is_remote: The is_remote of this Trigger.  # noqa: E501
        :type: bool
        """

        self._is_remote = is_remote

    @property
    def mute_new_metrics(self):
        """Gets the mute_new_metrics of this Trigger.  # noqa: E501

        if true, Moira will notify you each time the metric state changes, e.g NODATA -> OK  # noqa: E501

        :return: The mute_new_metrics of this Trigger.  # noqa: E501
        :rtype: bool
        """
        return self._mute_new_metrics

    @mute_new_metrics.setter
    def mute_new_metrics(self, mute_new_metrics):
        """Sets the mute_new_metrics of this Trigger.

        if true, Moira will notify you each time the metric state changes, e.g NODATA -> OK  # noqa: E501

        :param mute_new_metrics: The mute_new_metrics of this Trigger.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and mute_new_metrics is None:  # noqa: E501
            raise ValueError("Invalid value for `mute_new_metrics`, must not be `None`")  # noqa: E501

        self._mute_new_metrics = mute_new_metrics

    @property
    def throttling(self):
        """Gets the throttling of this Trigger.  # noqa: E501

        See <https://moira.readthedocs.io/en/latest/user_guide/throttling.html/>  # noqa: E501

        :return: The throttling of this Trigger.  # noqa: E501
        :rtype: int
        """
        return self._throttling

    @throttling.setter
    def throttling(self, throttling):
        """Sets the throttling of this Trigger.

        See <https://moira.readthedocs.io/en/latest/user_guide/throttling.html/>  # noqa: E501

        :param throttling: The throttling of this Trigger.  # noqa: E501
        :type: int
        """

        self._throttling = throttling

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
        if not isinstance(other, Trigger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Trigger):
            return True

        return self.to_dict() != other.to_dict()
