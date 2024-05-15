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


class KeyParameters(object):
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

        'algorithm': 'Algorithm',

        'ksk_bits': 'KskBits',

        'zsk_bits': 'ZskBits',
    }

    attribute_map = {

        'algorithm': 'algorithm',

        'ksk_bits': 'kskBits',

        'zsk_bits': 'zskBits',
    }

    def __init__(self, algorithm=None, ksk_bits=None, zsk_bits=None, local_vars_configuration=None):  # noqa: E501
        """KeyParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._algorithm = None
        self._ksk_bits = None
        self._zsk_bits = None
        self.discriminator = None

        self.algorithm = algorithm
        self.ksk_bits = ksk_bits
        self.zsk_bits = zsk_bits


    @property
    def algorithm(self):
        """Gets the algorithm of this KeyParameters.  # noqa: E501


        :return: The algorithm of this KeyParameters.  # noqa: E501
        :rtype: Algorithm
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this KeyParameters.


        :param algorithm: The algorithm of this KeyParameters.  # noqa: E501
        :type algorithm: Algorithm
        """
        if self.local_vars_configuration.client_side_validation and algorithm is None:  # noqa: E501
            raise ValueError("Invalid value for `algorithm`, must not be `None`")  # noqa: E501

        self._algorithm = algorithm

    @property
    def ksk_bits(self):
        """Gets the ksk_bits of this KeyParameters.  # noqa: E501


        :return: The ksk_bits of this KeyParameters.  # noqa: E501
        :rtype: KskBits
        """
        return self._ksk_bits

    @ksk_bits.setter
    def ksk_bits(self, ksk_bits):
        """Sets the ksk_bits of this KeyParameters.


        :param ksk_bits: The ksk_bits of this KeyParameters.  # noqa: E501
        :type ksk_bits: KskBits
        """
        if self.local_vars_configuration.client_side_validation and ksk_bits is None:  # noqa: E501
            raise ValueError("Invalid value for `ksk_bits`, must not be `None`")  # noqa: E501

        self._ksk_bits = ksk_bits

    @property
    def zsk_bits(self):
        """Gets the zsk_bits of this KeyParameters.  # noqa: E501


        :return: The zsk_bits of this KeyParameters.  # noqa: E501
        :rtype: ZskBits
        """
        return self._zsk_bits

    @zsk_bits.setter
    def zsk_bits(self, zsk_bits):
        """Sets the zsk_bits of this KeyParameters.


        :param zsk_bits: The zsk_bits of this KeyParameters.  # noqa: E501
        :type zsk_bits: ZskBits
        """
        if self.local_vars_configuration.client_side_validation and zsk_bits is None:  # noqa: E501
            raise ValueError("Invalid value for `zsk_bits`, must not be `None`")  # noqa: E501

        self._zsk_bits = zsk_bits
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
        if not isinstance(other, KeyParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KeyParameters):
            return True

        return self.to_dict() != other.to_dict()
