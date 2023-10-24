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


class NsecParameters(object):
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

        'nsec_mode': 'str',

        'nsec3_iterations': 'int',

        'nsec3_salt_bits': 'int',
    }

    attribute_map = {

        'nsec_mode': 'nsecMode',

        'nsec3_iterations': 'nsec3Iterations',

        'nsec3_salt_bits': 'nsec3SaltBits',
    }

    def __init__(self, nsec_mode='NSEC3', nsec3_iterations=21, nsec3_salt_bits=128, local_vars_configuration=None):  # noqa: E501
        """NsecParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._nsec_mode = None
        self._nsec3_iterations = None
        self._nsec3_salt_bits = None
        self.discriminator = None

        if nsec_mode is not None:
            self.nsec_mode = nsec_mode
        if nsec3_iterations is not None:
            self.nsec3_iterations = nsec3_iterations
        if nsec3_salt_bits is not None:
            self.nsec3_salt_bits = nsec3_salt_bits


    @property
    def nsec_mode(self):
        """Gets the nsec_mode of this NsecParameters.  # noqa: E501

        NSEC mode.   # noqa: E501

        :return: The nsec_mode of this NsecParameters.  # noqa: E501
        :rtype: str
        """
        return self._nsec_mode

    @nsec_mode.setter
    def nsec_mode(self, nsec_mode):
        """Sets the nsec_mode of this NsecParameters.

        NSEC mode.   # noqa: E501

        :param nsec_mode: The nsec_mode of this NsecParameters.  # noqa: E501
        :type nsec_mode: str
        """
        allowed_values = ["NSEC", "NSEC3"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and nsec_mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `nsec_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(nsec_mode, allowed_values)
            )

        self._nsec_mode = nsec_mode

    @property
    def nsec3_iterations(self):
        """Gets the nsec3_iterations of this NsecParameters.  # noqa: E501

        Number of iterations for NSEC3. (between 0 and 50)   # noqa: E501

        :return: The nsec3_iterations of this NsecParameters.  # noqa: E501
        :rtype: int
        """
        return self._nsec3_iterations

    @nsec3_iterations.setter
    def nsec3_iterations(self, nsec3_iterations):
        """Sets the nsec3_iterations of this NsecParameters.

        Number of iterations for NSEC3. (between 0 and 50)   # noqa: E501

        :param nsec3_iterations: The nsec3_iterations of this NsecParameters.  # noqa: E501
        :type nsec3_iterations: int
        """

        self._nsec3_iterations = nsec3_iterations

    @property
    def nsec3_salt_bits(self):
        """Gets the nsec3_salt_bits of this NsecParameters.  # noqa: E501

        Salt length in bits for NSEC3. (between 64 and 128, multiples of 8)   # noqa: E501

        :return: The nsec3_salt_bits of this NsecParameters.  # noqa: E501
        :rtype: int
        """
        return self._nsec3_salt_bits

    @nsec3_salt_bits.setter
    def nsec3_salt_bits(self, nsec3_salt_bits):
        """Sets the nsec3_salt_bits of this NsecParameters.

        Salt length in bits for NSEC3. (between 64 and 128, multiples of 8)   # noqa: E501

        :param nsec3_salt_bits: The nsec3_salt_bits of this NsecParameters.  # noqa: E501
        :type nsec3_salt_bits: int
        """

        self._nsec3_salt_bits = nsec3_salt_bits
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
        if not isinstance(other, NsecParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NsecParameters):
            return True

        return self.to_dict() != other.to_dict()
