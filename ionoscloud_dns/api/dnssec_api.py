from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_dns.api_client import ApiClient
from ionoscloud_dns.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DNSSECApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def zones_keys_delete(self, zone_id, **kwargs):  # noqa: E501
        """Delete a DNSSEC key  # noqa: E501

        Disable DNSSEC keys and remove associated DNSKEY records for your DNS zone.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_keys_delete(zone_id, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.zones_keys_delete_with_http_info(zone_id, **kwargs)  # noqa: E501

    def zones_keys_delete_with_http_info(self, zone_id, **kwargs):  # noqa: E501
        """Delete a DNSSEC key  # noqa: E501

        Disable DNSSEC keys and remove associated DNSKEY records for your DNS zone.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_keys_delete_with_http_info(zone_id, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'zone_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method zones_keys_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'zone_id' is set
        if self.api_client.client_side_validation and ('zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `zone_id` when calling `zones_keys_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zoneId'] = local_var_params['zone_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'object'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/zones/{zoneId}/keys', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def zones_keys_get(self, zone_id, **kwargs):  # noqa: E501
        """Retrieve a DNSSEC key  # noqa: E501

        Get DNSSEC keys for your DNS zone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_keys_get(zone_id, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DnssecKeyReadList
        """
        kwargs['_return_http_data_only'] = True
        return self.zones_keys_get_with_http_info(zone_id, **kwargs)  # noqa: E501

    def zones_keys_get_with_http_info(self, zone_id, **kwargs):  # noqa: E501
        """Retrieve a DNSSEC key  # noqa: E501

        Get DNSSEC keys for your DNS zone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_keys_get_with_http_info(zone_id, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(DnssecKeyReadList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'zone_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method zones_keys_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'zone_id' is set
        if self.api_client.client_side_validation and ('zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `zone_id` when calling `zones_keys_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zoneId'] = local_var_params['zone_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'DnssecKeyReadList'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/zones/{zoneId}/keys', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def zones_keys_post(self, zone_id, dnssec_key_create, **kwargs):  # noqa: E501
        """Create a DNSSEC key  # noqa: E501

        Enable DNSSEC keys and create associated DNSKEY records for your DNS zone.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_keys_post(zone_id, dnssec_key_create, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param dnssec_key_create: Enable DNSSEC request. (required)
        :type dnssec_key_create: DnssecKeyCreate
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.zones_keys_post_with_http_info(zone_id, dnssec_key_create, **kwargs)  # noqa: E501

    def zones_keys_post_with_http_info(self, zone_id, dnssec_key_create, **kwargs):  # noqa: E501
        """Create a DNSSEC key  # noqa: E501

        Enable DNSSEC keys and create associated DNSKEY records for your DNS zone.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_keys_post_with_http_info(zone_id, dnssec_key_create, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param dnssec_key_create: Enable DNSSEC request. (required)
        :type dnssec_key_create: DnssecKeyCreate
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'zone_id',
            'dnssec_key_create'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method zones_keys_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'zone_id' is set
        if self.api_client.client_side_validation and ('zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `zone_id` when calling `zones_keys_post`")  # noqa: E501
        # verify the required parameter 'dnssec_key_create' is set
        if self.api_client.client_side_validation and ('dnssec_key_create' not in local_var_params or  # noqa: E501
                                                        local_var_params['dnssec_key_create'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dnssec_key_create` when calling `zones_keys_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zoneId'] = local_var_params['zone_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'dnssec_key_create' in local_var_params:
            body_params = local_var_params['dnssec_key_create']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'object'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/zones/{zoneId}/keys', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
