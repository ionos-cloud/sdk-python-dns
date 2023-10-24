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


class DnssecKey(object):
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

        'key_tag': 'int',

        'sign_algorithm_mnemonic': 'str',

        'sign_algorithm_number': 'int',

        'digest_algorithm_mnemonic': 'str',

        'digest_algorithm_number': 'int',

        'digest': 'str',

        'key_data': 'KeyData',

        'composed_key_data': 'str',
    }

    attribute_map = {

        'key_tag': 'keyTag',

        'sign_algorithm_mnemonic': 'signAlgorithmMnemonic',

        'sign_algorithm_number': 'signAlgorithmNumber',

        'digest_algorithm_mnemonic': 'digestAlgorithmMnemonic',

        'digest_algorithm_number': 'digestAlgorithmNumber',

        'digest': 'digest',

        'key_data': 'keyData',

        'composed_key_data': 'composedKeyData',
    }

    def __init__(self, key_tag=None, sign_algorithm_mnemonic=None, sign_algorithm_number=None, digest_algorithm_mnemonic=None, digest_algorithm_number=None, digest=None, key_data=None, composed_key_data=None, local_vars_configuration=None):  # noqa: E501
        """DnssecKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key_tag = None
        self._sign_algorithm_mnemonic = None
        self._sign_algorithm_number = None
        self._digest_algorithm_mnemonic = None
        self._digest_algorithm_number = None
        self._digest = None
        self._key_data = None
        self._composed_key_data = None
        self.discriminator = None

        if key_tag is not None:
            self.key_tag = key_tag
        if sign_algorithm_mnemonic is not None:
            self.sign_algorithm_mnemonic = sign_algorithm_mnemonic
        if sign_algorithm_number is not None:
            self.sign_algorithm_number = sign_algorithm_number
        if digest_algorithm_mnemonic is not None:
            self.digest_algorithm_mnemonic = digest_algorithm_mnemonic
        if digest_algorithm_number is not None:
            self.digest_algorithm_number = digest_algorithm_number
        if digest is not None:
            self.digest = digest
        if key_data is not None:
            self.key_data = key_data
        if composed_key_data is not None:
            self.composed_key_data = composed_key_data


    @property
    def key_tag(self):
        """Gets the key_tag of this DnssecKey.  # noqa: E501


        :return: The key_tag of this DnssecKey.  # noqa: E501
        :rtype: int
        """
        return self._key_tag

    @key_tag.setter
    def key_tag(self, key_tag):
        """Sets the key_tag of this DnssecKey.


        :param key_tag: The key_tag of this DnssecKey.  # noqa: E501
        :type key_tag: int
        """

        self._key_tag = key_tag

    @property
    def sign_algorithm_mnemonic(self):
        """Gets the sign_algorithm_mnemonic of this DnssecKey.  # noqa: E501

        A string that denotes the signing algorithm. This value must conform to the guidelines in [RFC-8624 Section 3.1](https://datatracker.ietf.org/doc/html/rfc8624#section-3.1).   # noqa: E501

        :return: The sign_algorithm_mnemonic of this DnssecKey.  # noqa: E501
        :rtype: str
        """
        return self._sign_algorithm_mnemonic

    @sign_algorithm_mnemonic.setter
    def sign_algorithm_mnemonic(self, sign_algorithm_mnemonic):
        """Sets the sign_algorithm_mnemonic of this DnssecKey.

        A string that denotes the signing algorithm. This value must conform to the guidelines in [RFC-8624 Section 3.1](https://datatracker.ietf.org/doc/html/rfc8624#section-3.1).   # noqa: E501

        :param sign_algorithm_mnemonic: The sign_algorithm_mnemonic of this DnssecKey.  # noqa: E501
        :type sign_algorithm_mnemonic: str
        """

        self._sign_algorithm_mnemonic = sign_algorithm_mnemonic

    @property
    def sign_algorithm_number(self):
        """Gets the sign_algorithm_number of this DnssecKey.  # noqa: E501

        An integer that denotes the signing algorithm. This value must conform to the guidelines in [RFC-8624 Section 3.1](https://datatracker.ietf.org/doc/html/rfc8624#section-3.1).   # noqa: E501

        :return: The sign_algorithm_number of this DnssecKey.  # noqa: E501
        :rtype: int
        """
        return self._sign_algorithm_number

    @sign_algorithm_number.setter
    def sign_algorithm_number(self, sign_algorithm_number):
        """Sets the sign_algorithm_number of this DnssecKey.

        An integer that denotes the signing algorithm. This value must conform to the guidelines in [RFC-8624 Section 3.1](https://datatracker.ietf.org/doc/html/rfc8624#section-3.1).   # noqa: E501

        :param sign_algorithm_number: The sign_algorithm_number of this DnssecKey.  # noqa: E501
        :type sign_algorithm_number: int
        """

        self._sign_algorithm_number = sign_algorithm_number

    @property
    def digest_algorithm_mnemonic(self):
        """Gets the digest_algorithm_mnemonic of this DnssecKey.  # noqa: E501

        A string that denotes the digest algorithm. This value must conform to the guidelines in [RFC-8624 Section 3.3](https://datatracker.ietf.org/doc/html/rfc8624#section-3.3).   # noqa: E501

        :return: The digest_algorithm_mnemonic of this DnssecKey.  # noqa: E501
        :rtype: str
        """
        return self._digest_algorithm_mnemonic

    @digest_algorithm_mnemonic.setter
    def digest_algorithm_mnemonic(self, digest_algorithm_mnemonic):
        """Sets the digest_algorithm_mnemonic of this DnssecKey.

        A string that denotes the digest algorithm. This value must conform to the guidelines in [RFC-8624 Section 3.3](https://datatracker.ietf.org/doc/html/rfc8624#section-3.3).   # noqa: E501

        :param digest_algorithm_mnemonic: The digest_algorithm_mnemonic of this DnssecKey.  # noqa: E501
        :type digest_algorithm_mnemonic: str
        """

        self._digest_algorithm_mnemonic = digest_algorithm_mnemonic

    @property
    def digest_algorithm_number(self):
        """Gets the digest_algorithm_number of this DnssecKey.  # noqa: E501

        An integer that denotes the digest algorithm. This value must conform to the guidelines in [RFC-8624 Section 3.3](https://datatracker.ietf.org/doc/html/rfc8624#section-3.3).   # noqa: E501

        :return: The digest_algorithm_number of this DnssecKey.  # noqa: E501
        :rtype: int
        """
        return self._digest_algorithm_number

    @digest_algorithm_number.setter
    def digest_algorithm_number(self, digest_algorithm_number):
        """Sets the digest_algorithm_number of this DnssecKey.

        An integer that denotes the digest algorithm. This value must conform to the guidelines in [RFC-8624 Section 3.3](https://datatracker.ietf.org/doc/html/rfc8624#section-3.3).   # noqa: E501

        :param digest_algorithm_number: The digest_algorithm_number of this DnssecKey.  # noqa: E501
        :type digest_algorithm_number: int
        """

        self._digest_algorithm_number = digest_algorithm_number

    @property
    def digest(self):
        """Gets the digest of this DnssecKey.  # noqa: E501


        :return: The digest of this DnssecKey.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this DnssecKey.


        :param digest: The digest of this DnssecKey.  # noqa: E501
        :type digest: str
        """

        self._digest = digest

    @property
    def key_data(self):
        """Gets the key_data of this DnssecKey.  # noqa: E501


        :return: The key_data of this DnssecKey.  # noqa: E501
        :rtype: KeyData
        """
        return self._key_data

    @key_data.setter
    def key_data(self, key_data):
        """Sets the key_data of this DnssecKey.


        :param key_data: The key_data of this DnssecKey.  # noqa: E501
        :type key_data: KeyData
        """

        self._key_data = key_data

    @property
    def composed_key_data(self):
        """Gets the composed_key_data of this DnssecKey.  # noqa: E501

        Represents the composed value of the The RDATA for a DNSKEY. The format should be the following: Flags | Protocol | Algorithm | Public Key The values must conform to the guidelines in [RFC-4034 Section 2.1](https://www.rfc-editor.org/rfc/rfc4034#section-2.1).   # noqa: E501

        :return: The composed_key_data of this DnssecKey.  # noqa: E501
        :rtype: str
        """
        return self._composed_key_data

    @composed_key_data.setter
    def composed_key_data(self, composed_key_data):
        """Sets the composed_key_data of this DnssecKey.

        Represents the composed value of the The RDATA for a DNSKEY. The format should be the following: Flags | Protocol | Algorithm | Public Key The values must conform to the guidelines in [RFC-4034 Section 2.1](https://www.rfc-editor.org/rfc/rfc4034#section-2.1).   # noqa: E501

        :param composed_key_data: The composed_key_data of this DnssecKey.  # noqa: E501
        :type composed_key_data: str
        """

        self._composed_key_data = composed_key_data
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
        if not isinstance(other, DnssecKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DnssecKey):
            return True

        return self.to_dict() != other.to_dict()
