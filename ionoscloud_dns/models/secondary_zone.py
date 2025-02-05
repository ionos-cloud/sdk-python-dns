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


class SecondaryZone(object):
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

        'zone_name': 'str',

        'description': 'str',

        'primary_ips': 'list[str]',
    }

    attribute_map = {

        'zone_name': 'zoneName',

        'description': 'description',

        'primary_ips': 'primaryIps',
    }

    def __init__(self, zone_name=None, description=None, primary_ips=None, local_vars_configuration=None):  # noqa: E501
        """SecondaryZone - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._zone_name = None
        self._description = None
        self._primary_ips = None
        self.discriminator = None

        self.zone_name = zone_name
        if description is not None:
            self.description = description
        self.primary_ips = primary_ips


    @property
    def zone_name(self):
        """Gets the zone_name of this SecondaryZone.  # noqa: E501

        The zone name  # noqa: E501

        :return: The zone_name of this SecondaryZone.  # noqa: E501
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this SecondaryZone.

        The zone name  # noqa: E501

        :param zone_name: The zone_name of this SecondaryZone.  # noqa: E501
        :type zone_name: str
        """
        if self.local_vars_configuration.client_side_validation and zone_name is None:  # noqa: E501
            raise ValueError("Invalid value for `zone_name`, must not be `None`")  # noqa: E501

        self._zone_name = zone_name

    @property
    def description(self):
        """Gets the description of this SecondaryZone.  # noqa: E501

        The hosted zone is used for...  # noqa: E501

        :return: The description of this SecondaryZone.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecondaryZone.

        The hosted zone is used for...  # noqa: E501

        :param description: The description of this SecondaryZone.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def primary_ips(self):
        """Gets the primary_ips of this SecondaryZone.  # noqa: E501

        Indicates IP addresses of primary nameservers for a secondary zone. Accepts IPv4 and IPv6 addresses  # noqa: E501

        :return: The primary_ips of this SecondaryZone.  # noqa: E501
        :rtype: list[str]
        """
        return self._primary_ips

    @primary_ips.setter
    def primary_ips(self, primary_ips):
        """Sets the primary_ips of this SecondaryZone.

        Indicates IP addresses of primary nameservers for a secondary zone. Accepts IPv4 and IPv6 addresses  # noqa: E501

        :param primary_ips: The primary_ips of this SecondaryZone.  # noqa: E501
        :type primary_ips: list[str]
        """
        if self.local_vars_configuration.client_side_validation and primary_ips is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_ips`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                primary_ips is not None and len(primary_ips) < 1):
            raise ValueError("Invalid value for `primary_ips`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._primary_ips = primary_ips
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
        if not isinstance(other, SecondaryZone):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecondaryZone):
            return True

        return self.to_dict() != other.to_dict()
