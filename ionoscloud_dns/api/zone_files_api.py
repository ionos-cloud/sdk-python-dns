from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_dns.api_client import ApiClient
from ionoscloud_dns.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ZoneFilesApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def zones_zonefile_get(self, zone_id, **kwargs):  # noqa: E501
        """Retrieve a zone file  # noqa: E501

        Returns an exported zone file in BIND format (RFC 1035).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_zonefile_get(zone_id, async_req=True)
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
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.zones_zonefile_get_with_http_info(zone_id, **kwargs)  # noqa: E501

    def zones_zonefile_get_with_http_info(self, zone_id, **kwargs):  # noqa: E501
        """Retrieve a zone file  # noqa: E501

        Returns an exported zone file in BIND format (RFC 1035).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_zonefile_get_with_http_info(zone_id, async_req=True)
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
        :rtype: None
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
                    " to method zones_zonefile_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'zone_id' is set
        if self.api_client.client_side_validation and ('zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `zone_id` when calling `zones_zonefile_get`")  # noqa: E501

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
            ['text/plain', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = None
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/zones/{zoneId}/zonefile', 'GET',
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

    def zones_zonefile_put(self, zone_id, body, **kwargs):  # noqa: E501
        """Updates a zone with a file  # noqa: E501

        Updates a zone with zone file in BIND format (RFC 1035). All records in the zone are replaced with the ones provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_zonefile_put(zone_id, body, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param body: Zone file in BIND format (RFC 1035). In order to support import files from other sources, the bind zone file can contain SOA and NS records, but these records will be ignored. (required)
        :type body: str
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
        :rtype: RecordReadList
        """
        kwargs['_return_http_data_only'] = True
        return self.zones_zonefile_put_with_http_info(zone_id, body, **kwargs)  # noqa: E501

    def zones_zonefile_put_with_http_info(self, zone_id, body, **kwargs):  # noqa: E501
        """Updates a zone with a file  # noqa: E501

        Updates a zone with zone file in BIND format (RFC 1035). All records in the zone are replaced with the ones provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_zonefile_put_with_http_info(zone_id, body, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param body: Zone file in BIND format (RFC 1035). In order to support import files from other sources, the bind zone file can contain SOA and NS records, but these records will be ignored. (required)
        :type body: str
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
        :rtype: tuple(RecordReadList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'zone_id',
            'body'
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
                    " to method zones_zonefile_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'zone_id' is set
        if self.api_client.client_side_validation and ('zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `zone_id` when calling `zones_zonefile_put`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in local_var_params or  # noqa: E501
                                                        local_var_params['body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `body` when calling `zones_zonefile_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zoneId'] = local_var_params['zone_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'RecordReadList'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/zones/{zoneId}/zonefile', 'PUT',
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
