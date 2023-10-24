from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_dns.api_client import ApiClient
from ionoscloud_dns.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SecondaryZonesApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def secondaryzones_axfr_get(self, secondary_zone_id, **kwargs):  # noqa: E501
        """Get status of zone transfer  # noqa: E501

        Get status of zone transfer.  Note that Cloud DNS relies on the following Anycast addresses for sending DNS notify messages. Make sure to whitelist on your end:   - IPv4: 212.227.123.25   - IPv6: 2001:8d8:fe:53::5cd:25   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_axfr_get(secondary_zone_id, async_req=True)
        >>> result = thread.get()

        :param secondary_zone_id: The ID (UUID) of the DNS zone. (required)
        :type secondary_zone_id: str
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
        :rtype: ZoneTransferPrimaryIpsStatus
        """
        kwargs['_return_http_data_only'] = True
        return self.secondaryzones_axfr_get_with_http_info(secondary_zone_id, **kwargs)  # noqa: E501

    def secondaryzones_axfr_get_with_http_info(self, secondary_zone_id, **kwargs):  # noqa: E501
        """Get status of zone transfer  # noqa: E501

        Get status of zone transfer.  Note that Cloud DNS relies on the following Anycast addresses for sending DNS notify messages. Make sure to whitelist on your end:   - IPv4: 212.227.123.25   - IPv6: 2001:8d8:fe:53::5cd:25   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_axfr_get_with_http_info(secondary_zone_id, async_req=True)
        >>> result = thread.get()

        :param secondary_zone_id: The ID (UUID) of the DNS zone. (required)
        :type secondary_zone_id: str
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
        :rtype: tuple(ZoneTransferPrimaryIpsStatus, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'secondary_zone_id'
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
                    " to method secondaryzones_axfr_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'secondary_zone_id' is set
        if self.api_client.client_side_validation and ('secondary_zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['secondary_zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `secondary_zone_id` when calling `secondaryzones_axfr_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'secondary_zone_id' in local_var_params:
            path_params['secondaryZoneId'] = local_var_params['secondary_zone_id']  # noqa: E501

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

        response_type = 'ZoneTransferPrimaryIpsStatus'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/secondaryzones/{secondaryZoneId}/axfr', 'GET',
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

    def secondaryzones_axfr_put(self, secondary_zone_id, **kwargs):  # noqa: E501
        """Start zone transfer  # noqa: E501

        Initiate zone transfer. Note that Cloud DNS relies on the following Anycast addresses for sending DNS notify messages. Make sure to whitelist on your end:   - IPv4: 212.227.123.25   - IPv6: 2001:8d8:fe:53::5cd:25   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_axfr_put(secondary_zone_id, async_req=True)
        >>> result = thread.get()

        :param secondary_zone_id: The ID (UUID) of the DNS zone. (required)
        :type secondary_zone_id: str
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
        return self.secondaryzones_axfr_put_with_http_info(secondary_zone_id, **kwargs)  # noqa: E501

    def secondaryzones_axfr_put_with_http_info(self, secondary_zone_id, **kwargs):  # noqa: E501
        """Start zone transfer  # noqa: E501

        Initiate zone transfer. Note that Cloud DNS relies on the following Anycast addresses for sending DNS notify messages. Make sure to whitelist on your end:   - IPv4: 212.227.123.25   - IPv6: 2001:8d8:fe:53::5cd:25   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_axfr_put_with_http_info(secondary_zone_id, async_req=True)
        >>> result = thread.get()

        :param secondary_zone_id: The ID (UUID) of the DNS zone. (required)
        :type secondary_zone_id: str
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
            'secondary_zone_id'
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
                    " to method secondaryzones_axfr_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'secondary_zone_id' is set
        if self.api_client.client_side_validation and ('secondary_zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['secondary_zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `secondary_zone_id` when calling `secondaryzones_axfr_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'secondary_zone_id' in local_var_params:
            path_params['secondaryZoneId'] = local_var_params['secondary_zone_id']  # noqa: E501

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
            '/secondaryzones/{secondaryZoneId}/axfr', 'PUT',
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

    def secondaryzones_delete(self, secondary_zone_id, **kwargs):  # noqa: E501
        """Delete a secondary zone  # noqa: E501

        Deletes the specified secondary zone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_delete(secondary_zone_id, async_req=True)
        >>> result = thread.get()

        :param secondary_zone_id: The ID (UUID) of the DNS zone. (required)
        :type secondary_zone_id: str
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
        return self.secondaryzones_delete_with_http_info(secondary_zone_id, **kwargs)  # noqa: E501

    def secondaryzones_delete_with_http_info(self, secondary_zone_id, **kwargs):  # noqa: E501
        """Delete a secondary zone  # noqa: E501

        Deletes the specified secondary zone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_delete_with_http_info(secondary_zone_id, async_req=True)
        >>> result = thread.get()

        :param secondary_zone_id: The ID (UUID) of the DNS zone. (required)
        :type secondary_zone_id: str
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
            'secondary_zone_id'
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
                    " to method secondaryzones_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'secondary_zone_id' is set
        if self.api_client.client_side_validation and ('secondary_zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['secondary_zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `secondary_zone_id` when calling `secondaryzones_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'secondary_zone_id' in local_var_params:
            path_params['secondaryZoneId'] = local_var_params['secondary_zone_id']  # noqa: E501

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
            '/secondaryzones/{secondaryZoneId}', 'DELETE',
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

    def secondaryzones_find_by_id(self, secondary_zone_id, **kwargs):  # noqa: E501
        """Retrieve a secondary zone  # noqa: E501

        Returns a DNS secondary zone by given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_find_by_id(secondary_zone_id, async_req=True)
        >>> result = thread.get()

        :param secondary_zone_id: The ID (UUID) of the DNS zone. (required)
        :type secondary_zone_id: str
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
        :rtype: SecondaryZoneRead
        """
        kwargs['_return_http_data_only'] = True
        return self.secondaryzones_find_by_id_with_http_info(secondary_zone_id, **kwargs)  # noqa: E501

    def secondaryzones_find_by_id_with_http_info(self, secondary_zone_id, **kwargs):  # noqa: E501
        """Retrieve a secondary zone  # noqa: E501

        Returns a DNS secondary zone by given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_find_by_id_with_http_info(secondary_zone_id, async_req=True)
        >>> result = thread.get()

        :param secondary_zone_id: The ID (UUID) of the DNS zone. (required)
        :type secondary_zone_id: str
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
        :rtype: tuple(SecondaryZoneRead, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'secondary_zone_id'
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
                    " to method secondaryzones_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'secondary_zone_id' is set
        if self.api_client.client_side_validation and ('secondary_zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['secondary_zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `secondary_zone_id` when calling `secondaryzones_find_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'secondary_zone_id' in local_var_params:
            path_params['secondaryZoneId'] = local_var_params['secondary_zone_id']  # noqa: E501

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

        response_type = 'SecondaryZoneRead'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/secondaryzones/{secondaryZoneId}', 'GET',
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

    def secondaryzones_get(self, **kwargs):  # noqa: E501
        """Retrieve secondary zones  # noqa: E501

        Returns a list of the secondary DNS zones for the customer. Default limit is the first 100 items. Use pagination query parameters for listing more items (up to 1000).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_get(async_req=True)
        >>> result = thread.get()

        :param filter_state: Filter used to fetch all zones in a particular state.
        :type filter_state: ProvisioningState
        :param filter_zone_name: Filter used to fetch only the zones that contain the specified zone name.
        :type filter_zone_name: str
        :param offset: The first element (of the total list of elements) to include in the response. Use together with limit for pagination.
        :type offset: int
        :param limit: The maximum number of elements to return. Use together with offset for pagination.
        :type limit: int
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
        :rtype: SecondaryZoneReadList
        """
        kwargs['_return_http_data_only'] = True
        return self.secondaryzones_get_with_http_info(**kwargs)  # noqa: E501

    def secondaryzones_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve secondary zones  # noqa: E501

        Returns a list of the secondary DNS zones for the customer. Default limit is the first 100 items. Use pagination query parameters for listing more items (up to 1000).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param filter_state: Filter used to fetch all zones in a particular state.
        :type filter_state: ProvisioningState
        :param filter_zone_name: Filter used to fetch only the zones that contain the specified zone name.
        :type filter_zone_name: str
        :param offset: The first element (of the total list of elements) to include in the response. Use together with limit for pagination.
        :type offset: int
        :param limit: The maximum number of elements to return. Use together with offset for pagination.
        :type limit: int
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
        :rtype: tuple(SecondaryZoneReadList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'filter_state',
            'filter_zone_name',
            'offset',
            'limit'
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
                    " to method secondaryzones_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `secondaryzones_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `secondaryzones_get`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `secondaryzones_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'filter_state' in local_var_params and local_var_params['filter_state'] is not None:  # noqa: E501
            query_params.append(('filter.state', local_var_params['filter_state']))  # noqa: E501
        if 'filter_zone_name' in local_var_params and local_var_params['filter_zone_name'] is not None:  # noqa: E501
            query_params.append(('filter.zoneName', local_var_params['filter_zone_name']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'SecondaryZoneReadList'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/secondaryzones', 'GET',
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

    def secondaryzones_post(self, secondary_zone_create, **kwargs):  # noqa: E501
        """Create a secondary zone  # noqa: E501

        Creates a new secondary zone with default NS and SOA records. Note that Cloud DNS relies on the following Anycast addresses for sending DNS notify messages. Make sure to whitelist on your end:   - IPv4: 212.227.123.25   - IPv6: 2001:8d8:fe:53::5cd:25   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_post(secondary_zone_create, async_req=True)
        >>> result = thread.get()

        :param secondary_zone_create: zone (required)
        :type secondary_zone_create: SecondaryZoneCreate
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
        :rtype: SecondaryZoneRead
        """
        kwargs['_return_http_data_only'] = True
        return self.secondaryzones_post_with_http_info(secondary_zone_create, **kwargs)  # noqa: E501

    def secondaryzones_post_with_http_info(self, secondary_zone_create, **kwargs):  # noqa: E501
        """Create a secondary zone  # noqa: E501

        Creates a new secondary zone with default NS and SOA records. Note that Cloud DNS relies on the following Anycast addresses for sending DNS notify messages. Make sure to whitelist on your end:   - IPv4: 212.227.123.25   - IPv6: 2001:8d8:fe:53::5cd:25   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_post_with_http_info(secondary_zone_create, async_req=True)
        >>> result = thread.get()

        :param secondary_zone_create: zone (required)
        :type secondary_zone_create: SecondaryZoneCreate
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
        :rtype: tuple(SecondaryZoneRead, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'secondary_zone_create'
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
                    " to method secondaryzones_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'secondary_zone_create' is set
        if self.api_client.client_side_validation and ('secondary_zone_create' not in local_var_params or  # noqa: E501
                                                        local_var_params['secondary_zone_create'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `secondary_zone_create` when calling `secondaryzones_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'secondary_zone_create' in local_var_params:
            body_params = local_var_params['secondary_zone_create']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'SecondaryZoneRead'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/secondaryzones', 'POST',
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

    def secondaryzones_put(self, secondary_zone_id, secondary_zone_ensure, **kwargs):  # noqa: E501
        """Ensure a secondary zone  # noqa: E501

        Ensures that a secondary zone with the provided ID is created or modified. In order to successfully update secondary zone - all JSON parameters must be passed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_put(secondary_zone_id, secondary_zone_ensure, async_req=True)
        >>> result = thread.get()

        :param secondary_zone_id: The ID (UUID) of the DNS zone. (required)
        :type secondary_zone_id: str
        :param secondary_zone_ensure: update zone (required)
        :type secondary_zone_ensure: SecondaryZoneEnsure
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
        :rtype: SecondaryZoneRead
        """
        kwargs['_return_http_data_only'] = True
        return self.secondaryzones_put_with_http_info(secondary_zone_id, secondary_zone_ensure, **kwargs)  # noqa: E501

    def secondaryzones_put_with_http_info(self, secondary_zone_id, secondary_zone_ensure, **kwargs):  # noqa: E501
        """Ensure a secondary zone  # noqa: E501

        Ensures that a secondary zone with the provided ID is created or modified. In order to successfully update secondary zone - all JSON parameters must be passed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_put_with_http_info(secondary_zone_id, secondary_zone_ensure, async_req=True)
        >>> result = thread.get()

        :param secondary_zone_id: The ID (UUID) of the DNS zone. (required)
        :type secondary_zone_id: str
        :param secondary_zone_ensure: update zone (required)
        :type secondary_zone_ensure: SecondaryZoneEnsure
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
        :rtype: tuple(SecondaryZoneRead, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'secondary_zone_id',
            'secondary_zone_ensure'
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
                    " to method secondaryzones_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'secondary_zone_id' is set
        if self.api_client.client_side_validation and ('secondary_zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['secondary_zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `secondary_zone_id` when calling `secondaryzones_put`")  # noqa: E501
        # verify the required parameter 'secondary_zone_ensure' is set
        if self.api_client.client_side_validation and ('secondary_zone_ensure' not in local_var_params or  # noqa: E501
                                                        local_var_params['secondary_zone_ensure'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `secondary_zone_ensure` when calling `secondaryzones_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'secondary_zone_id' in local_var_params:
            path_params['secondaryZoneId'] = local_var_params['secondary_zone_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'secondary_zone_ensure' in local_var_params:
            body_params = local_var_params['secondary_zone_ensure']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'SecondaryZoneRead'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/secondaryzones/{secondaryZoneId}', 'PUT',
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
