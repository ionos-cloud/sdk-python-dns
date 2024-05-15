# coding: utf-8

"""
    IONOS Cloud - DNS API

    Cloud DNS service helps IONOS Cloud customers to automate DNS Zone and Record management.   # noqa: E501

    The version of the OpenAPI document: 1.15.4
    Contact: support@cloud.ionos.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_dns.configuration import Configuration


class MetadataForSecondaryZoneRecords(object):
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

        'fqdn': 'str',

        'zone_id': 'str',

        'root_name': 'str',
    }

    attribute_map = {

        'fqdn': 'fqdn',

        'zone_id': 'zoneId',

        'root_name': 'rootName',
    }

    def __init__(self, fqdn=None, zone_id=None, root_name=None, local_vars_configuration=None):  # noqa: E501
        """MetadataForSecondaryZoneRecords - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fqdn = None
        self._zone_id = None
        self._root_name = None
        self.discriminator = None

        self.fqdn = fqdn
        self.zone_id = zone_id
        self.root_name = root_name


    @property
    def fqdn(self):
        """Gets the fqdn of this MetadataForSecondaryZoneRecords.  # noqa: E501

        A fully qualified domain name. FQDN consists of two parts - the hostname and the domain name.  # noqa: E501

        :return: The fqdn of this MetadataForSecondaryZoneRecords.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this MetadataForSecondaryZoneRecords.

        A fully qualified domain name. FQDN consists of two parts - the hostname and the domain name.  # noqa: E501

        :param fqdn: The fqdn of this MetadataForSecondaryZoneRecords.  # noqa: E501
        :type fqdn: str
        """
        if self.local_vars_configuration.client_side_validation and fqdn is None:  # noqa: E501
            raise ValueError("Invalid value for `fqdn`, must not be `None`")  # noqa: E501

        self._fqdn = fqdn

    @property
    def zone_id(self):
        """Gets the zone_id of this MetadataForSecondaryZoneRecords.  # noqa: E501

        The ID (UUID) of the DNS zone of which record belongs to.  # noqa: E501

        :return: The zone_id of this MetadataForSecondaryZoneRecords.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this MetadataForSecondaryZoneRecords.

        The ID (UUID) of the DNS zone of which record belongs to.  # noqa: E501

        :param zone_id: The zone_id of this MetadataForSecondaryZoneRecords.  # noqa: E501
        :type zone_id: str
        """
        if self.local_vars_configuration.client_side_validation and zone_id is None:  # noqa: E501
            raise ValueError("Invalid value for `zone_id`, must not be `None`")  # noqa: E501

        self._zone_id = zone_id

    @property
    def root_name(self):
        """Gets the root_name of this MetadataForSecondaryZoneRecords.  # noqa: E501

        Indicates the root name (from the primary zone) for the record  # noqa: E501

        :return: The root_name of this MetadataForSecondaryZoneRecords.  # noqa: E501
        :rtype: str
        """
        return self._root_name

    @root_name.setter
    def root_name(self, root_name):
        """Sets the root_name of this MetadataForSecondaryZoneRecords.

        Indicates the root name (from the primary zone) for the record  # noqa: E501

        :param root_name: The root_name of this MetadataForSecondaryZoneRecords.  # noqa: E501
        :type root_name: str
        """
        if self.local_vars_configuration.client_side_validation and root_name is None:  # noqa: E501
            raise ValueError("Invalid value for `root_name`, must not be `None`")  # noqa: E501

        self._root_name = root_name
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
        if not isinstance(other, MetadataForSecondaryZoneRecords):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetadataForSecondaryZoneRecords):
            return True

        return self.to_dict() != other.to_dict()
