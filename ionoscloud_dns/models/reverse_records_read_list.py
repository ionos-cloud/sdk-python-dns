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


class ReverseRecordsReadList(object):
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

        'type': 'str',

        'href': 'str',

        'items': 'list[ReverseRecordRead]',

        'offset': 'float',

        'limit': 'float',

        'links': 'Links',
    }

    attribute_map = {

        'id': 'id',

        'type': 'type',

        'href': 'href',

        'items': 'items',

        'offset': 'offset',

        'limit': 'limit',

        'links': '_links',
    }

    def __init__(self, id=None, type=None, href=None, items=None, offset=None, limit=None, links=None, local_vars_configuration=None):  # noqa: E501
        """ReverseRecordsReadList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._href = None
        self._items = None
        self._offset = None
        self._limit = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.href = href
        self.items = items
        self.offset = offset
        self.limit = limit
        self.links = links


    @property
    def id(self):
        """Gets the id of this ReverseRecordsReadList.  # noqa: E501

        ID (UUID) created to identify this action.  # noqa: E501

        :return: The id of this ReverseRecordsReadList.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReverseRecordsReadList.

        ID (UUID) created to identify this action.  # noqa: E501

        :param id: The id of this ReverseRecordsReadList.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this ReverseRecordsReadList.  # noqa: E501


        :return: The type of this ReverseRecordsReadList.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReverseRecordsReadList.


        :param type: The type of this ReverseRecordsReadList.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["collection"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def href(self):
        """Gets the href of this ReverseRecordsReadList.  # noqa: E501


        :return: The href of this ReverseRecordsReadList.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ReverseRecordsReadList.


        :param href: The href of this ReverseRecordsReadList.  # noqa: E501
        :type href: str
        """
        if self.local_vars_configuration.client_side_validation and href is None:  # noqa: E501
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def items(self):
        """Gets the items of this ReverseRecordsReadList.  # noqa: E501


        :return: The items of this ReverseRecordsReadList.  # noqa: E501
        :rtype: list[ReverseRecordRead]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ReverseRecordsReadList.


        :param items: The items of this ReverseRecordsReadList.  # noqa: E501
        :type items: list[ReverseRecordRead]
        """
        if self.local_vars_configuration.client_side_validation and items is None:  # noqa: E501
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def offset(self):
        """Gets the offset of this ReverseRecordsReadList.  # noqa: E501

        Pagination offset.  # noqa: E501

        :return: The offset of this ReverseRecordsReadList.  # noqa: E501
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ReverseRecordsReadList.

        Pagination offset.  # noqa: E501

        :param offset: The offset of this ReverseRecordsReadList.  # noqa: E501
        :type offset: float
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ReverseRecordsReadList.  # noqa: E501

        Pagination limit.  # noqa: E501

        :return: The limit of this ReverseRecordsReadList.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ReverseRecordsReadList.

        Pagination limit.  # noqa: E501

        :param limit: The limit of this ReverseRecordsReadList.  # noqa: E501
        :type limit: float
        """
        if self.local_vars_configuration.client_side_validation and limit is None:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def links(self):
        """Gets the links of this ReverseRecordsReadList.  # noqa: E501


        :return: The links of this ReverseRecordsReadList.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ReverseRecordsReadList.


        :param links: The links of this ReverseRecordsReadList.  # noqa: E501
        :type links: Links
        """
        if self.local_vars_configuration.client_side_validation and links is None:  # noqa: E501
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links
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
        if not isinstance(other, ReverseRecordsReadList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReverseRecordsReadList):
            return True

        return self.to_dict() != other.to_dict()
