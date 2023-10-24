# coding: utf-8

"""
    IONOS Cloud - DNS API

    Cloud DNS service helps IONOS Cloud customers to automate DNS Zone and Record management.   # noqa: E501

    The version of the OpenAPI document: 1.12.0
    Contact: support@cloud.ionos.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_dns.configuration import Configuration


class SecondaryZoneRecordRead(object):
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

        'type': 'str',

        'metadata': 'MetadataForSecondaryZoneRecords',

        'properties': 'Record',
    }

    attribute_map = {

        'type': 'type',

        'metadata': 'metadata',

        'properties': 'properties',
    }

    def __init__(self, type=None, metadata=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """SecondaryZoneRecordRead - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._metadata = None
        self._properties = None
        self.discriminator = None

        self.type = type
        self.metadata = metadata
        self.properties = properties


    @property
    def type(self):
        """Gets the type of this SecondaryZoneRecordRead.  # noqa: E501


        :return: The type of this SecondaryZoneRecordRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SecondaryZoneRecordRead.


        :param type: The type of this SecondaryZoneRecordRead.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["record"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def metadata(self):
        """Gets the metadata of this SecondaryZoneRecordRead.  # noqa: E501


        :return: The metadata of this SecondaryZoneRecordRead.  # noqa: E501
        :rtype: MetadataForSecondaryZoneRecords
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this SecondaryZoneRecordRead.


        :param metadata: The metadata of this SecondaryZoneRecordRead.  # noqa: E501
        :type metadata: MetadataForSecondaryZoneRecords
        """
        if self.local_vars_configuration.client_side_validation and metadata is None:  # noqa: E501
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def properties(self):
        """Gets the properties of this SecondaryZoneRecordRead.  # noqa: E501


        :return: The properties of this SecondaryZoneRecordRead.  # noqa: E501
        :rtype: Record
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SecondaryZoneRecordRead.


        :param properties: The properties of this SecondaryZoneRecordRead.  # noqa: E501
        :type properties: Record
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties
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
        if not isinstance(other, SecondaryZoneRecordRead):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecondaryZoneRecordRead):
            return True

        return self.to_dict() != other.to_dict()
