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


class DnssecKeyParameters(object):
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

        'key_parameters': 'KeyParameters',

        'nsec_parameters': 'NsecParameters',

        'validity': 'int',
    }

    attribute_map = {

        'key_parameters': 'keyParameters',

        'nsec_parameters': 'nsecParameters',

        'validity': 'validity',
    }

    def __init__(self, key_parameters=None, nsec_parameters=None, validity=None, local_vars_configuration=None):  # noqa: E501
        """DnssecKeyParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key_parameters = None
        self._nsec_parameters = None
        self._validity = None
        self.discriminator = None

        self.key_parameters = key_parameters
        self.nsec_parameters = nsec_parameters
        self.validity = validity


    @property
    def key_parameters(self):
        """Gets the key_parameters of this DnssecKeyParameters.  # noqa: E501


        :return: The key_parameters of this DnssecKeyParameters.  # noqa: E501
        :rtype: KeyParameters
        """
        return self._key_parameters

    @key_parameters.setter
    def key_parameters(self, key_parameters):
        """Sets the key_parameters of this DnssecKeyParameters.


        :param key_parameters: The key_parameters of this DnssecKeyParameters.  # noqa: E501
        :type key_parameters: KeyParameters
        """
        if self.local_vars_configuration.client_side_validation and key_parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `key_parameters`, must not be `None`")  # noqa: E501

        self._key_parameters = key_parameters

    @property
    def nsec_parameters(self):
        """Gets the nsec_parameters of this DnssecKeyParameters.  # noqa: E501


        :return: The nsec_parameters of this DnssecKeyParameters.  # noqa: E501
        :rtype: NsecParameters
        """
        return self._nsec_parameters

    @nsec_parameters.setter
    def nsec_parameters(self, nsec_parameters):
        """Sets the nsec_parameters of this DnssecKeyParameters.


        :param nsec_parameters: The nsec_parameters of this DnssecKeyParameters.  # noqa: E501
        :type nsec_parameters: NsecParameters
        """
        if self.local_vars_configuration.client_side_validation and nsec_parameters is None:  # noqa: E501
            raise ValueError("Invalid value for `nsec_parameters`, must not be `None`")  # noqa: E501

        self._nsec_parameters = nsec_parameters

    @property
    def validity(self):
        """Gets the validity of this DnssecKeyParameters.  # noqa: E501

        Signature validity in days   # noqa: E501

        :return: The validity of this DnssecKeyParameters.  # noqa: E501
        :rtype: int
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this DnssecKeyParameters.

        Signature validity in days   # noqa: E501

        :param validity: The validity of this DnssecKeyParameters.  # noqa: E501
        :type validity: int
        """
        if self.local_vars_configuration.client_side_validation and validity is None:  # noqa: E501
            raise ValueError("Invalid value for `validity`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                validity is not None and validity > 365):  # noqa: E501
            raise ValueError("Invalid value for `validity`, must be a value less than or equal to `365`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                validity is not None and validity < 90):  # noqa: E501
            raise ValueError("Invalid value for `validity`, must be a value greater than or equal to `90`")  # noqa: E501

        self._validity = validity
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
        if not isinstance(other, DnssecKeyParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DnssecKeyParameters):
            return True

        return self.to_dict() != other.to_dict()
