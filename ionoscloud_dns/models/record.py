# coding: utf-8

"""
    IONOS Cloud - DNS API

    Cloud DNS service helps IONOS Cloud customers to automate DNS Zone and Record management.   # noqa: E501

    The version of the OpenAPI document: 1.17.0
    Contact: support@cloud.ionos.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_dns.configuration import Configuration


class Record(object):
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

        'type': 'RecordType',

        'content': 'str',

        'ttl': 'int',

        'priority': 'int',

        'enabled': 'bool',
    }

    attribute_map = {

        'name': 'name',

        'type': 'type',

        'content': 'content',

        'ttl': 'ttl',

        'priority': 'priority',

        'enabled': 'enabled',
    }

    def __init__(self, name=None, type=None, content=None, ttl=3600, priority=None, enabled=True, local_vars_configuration=None):  # noqa: E501
        """Record - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._type = None
        self._content = None
        self._ttl = None
        self._priority = None
        self._enabled = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.content = content
        if ttl is not None:
            self.ttl = ttl
        if priority is not None:
            self.priority = priority
        if enabled is not None:
            self.enabled = enabled


    @property
    def name(self):
        """Gets the name of this Record.  # noqa: E501


        :return: The name of this Record.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Record.


        :param name: The name of this Record.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this Record.  # noqa: E501


        :return: The type of this Record.  # noqa: E501
        :rtype: RecordType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Record.


        :param type: The type of this Record.  # noqa: E501
        :type type: RecordType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def content(self):
        """Gets the content of this Record.  # noqa: E501


        :return: The content of this Record.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Record.


        :param content: The content of this Record.  # noqa: E501
        :type content: str
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def ttl(self):
        """Gets the ttl of this Record.  # noqa: E501

        Time to live for the record, recommended 3600.  # noqa: E501

        :return: The ttl of this Record.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this Record.

        Time to live for the record, recommended 3600.  # noqa: E501

        :param ttl: The ttl of this Record.  # noqa: E501
        :type ttl: int
        """

        self._ttl = ttl

    @property
    def priority(self):
        """Gets the priority of this Record.  # noqa: E501

        Priority value is between 0 and 65535. Priority is mandatory for MX, SRV and URI record types and ignored for all other types.  # noqa: E501

        :return: The priority of this Record.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Record.

        Priority value is between 0 and 65535. Priority is mandatory for MX, SRV and URI record types and ignored for all other types.  # noqa: E501

        :param priority: The priority of this Record.  # noqa: E501
        :type priority: int
        """

        self._priority = priority

    @property
    def enabled(self):
        """Gets the enabled of this Record.  # noqa: E501

        When true - the record is visible for lookup.  # noqa: E501

        :return: The enabled of this Record.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Record.

        When true - the record is visible for lookup.  # noqa: E501

        :param enabled: The enabled of this Record.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled
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
        if not isinstance(other, Record):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Record):
            return True

        return self.to_dict() != other.to_dict()
