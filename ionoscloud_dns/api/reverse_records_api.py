from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_dns.api_client import ApiClient
from ionoscloud_dns.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ReverseRecordsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def reverserecords_delete(self, reverserecord_id, **kwargs):  # noqa: E501
        """Delete a reverse DNS record  # noqa: E501

        Deletes a reverse DNS record.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reverserecords_delete(reverserecord_id, async_req=True)
        >>> result = thread.get()

        :param reverserecord_id: The ID (UUID) of the reverse DNS record. (required)
        :type reverserecord_id: str
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
        return self.reverserecords_delete_with_http_info(reverserecord_id, **kwargs)  # noqa: E501

    def reverserecords_delete_with_http_info(self, reverserecord_id, **kwargs):  # noqa: E501
        """Delete a reverse DNS record  # noqa: E501

        Deletes a reverse DNS record.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reverserecords_delete_with_http_info(reverserecord_id, async_req=True)
        >>> result = thread.get()

        :param reverserecord_id: The ID (UUID) of the reverse DNS record. (required)
        :type reverserecord_id: str
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
            'reverserecord_id'
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
                    " to method reverserecords_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'reverserecord_id' is set
        if self.api_client.client_side_validation and ('reverserecord_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['reverserecord_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `reverserecord_id` when calling `reverserecords_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'reverserecord_id' in local_var_params:
            path_params['reverserecordId'] = local_var_params['reverserecord_id']  # noqa: E501

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
            '/reverserecords/{reverserecordId}', 'DELETE',
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

    def reverserecords_find_by_id(self, reverserecord_id, **kwargs):  # noqa: E501
        """Retrieve a reverse DNS record  # noqa: E501

        Returns the record with the specified record ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reverserecords_find_by_id(reverserecord_id, async_req=True)
        >>> result = thread.get()

        :param reverserecord_id: The ID (UUID) of the reverse DNS record. (required)
        :type reverserecord_id: str
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
        :rtype: ReverseRecordRead
        """
        kwargs['_return_http_data_only'] = True
        return self.reverserecords_find_by_id_with_http_info(reverserecord_id, **kwargs)  # noqa: E501

    def reverserecords_find_by_id_with_http_info(self, reverserecord_id, **kwargs):  # noqa: E501
        """Retrieve a reverse DNS record  # noqa: E501

        Returns the record with the specified record ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reverserecords_find_by_id_with_http_info(reverserecord_id, async_req=True)
        >>> result = thread.get()

        :param reverserecord_id: The ID (UUID) of the reverse DNS record. (required)
        :type reverserecord_id: str
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
        :rtype: tuple(ReverseRecordRead, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'reverserecord_id'
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
                    " to method reverserecords_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'reverserecord_id' is set
        if self.api_client.client_side_validation and ('reverserecord_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['reverserecord_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `reverserecord_id` when calling `reverserecords_find_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'reverserecord_id' in local_var_params:
            path_params['reverserecordId'] = local_var_params['reverserecord_id']  # noqa: E501

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

        response_type = 'ReverseRecordRead'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/reverserecords/{reverserecordId}', 'GET',
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

    def reverserecords_get(self, **kwargs):  # noqa: E501
        """Retrieves existing reverse DNS records  # noqa: E501

        Returns a list of the reverse records of the customer. Default limit is the first 100 items. Use pagination query parameters to list more items.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reverserecords_get(async_req=True)
        >>> result = thread.get()

        :param filter_record_ip: Filter is used to fetch only the reverse records for the specified IPs. It's an array of IP records. IP can be any valid IPv4 or IPv6 address. Parameter has to be sent in query as many times as values (filter.recordIp=1.2.3.4&filter.recordIp=2.3.4.5) 
        :type filter_record_ip: list[str]
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
        :rtype: ReverseRecordsReadList
        """
        kwargs['_return_http_data_only'] = True
        return self.reverserecords_get_with_http_info(**kwargs)  # noqa: E501

    def reverserecords_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves existing reverse DNS records  # noqa: E501

        Returns a list of the reverse records of the customer. Default limit is the first 100 items. Use pagination query parameters to list more items.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reverserecords_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param filter_record_ip: Filter is used to fetch only the reverse records for the specified IPs. It's an array of IP records. IP can be any valid IPv4 or IPv6 address. Parameter has to be sent in query as many times as values (filter.recordIp=1.2.3.4&filter.recordIp=2.3.4.5) 
        :type filter_record_ip: list[str]
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
        :rtype: tuple(ReverseRecordsReadList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'filter_record_ip',
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
                    " to method reverserecords_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `reverserecords_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `reverserecords_get`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `reverserecords_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'filter_record_ip' in local_var_params and local_var_params['filter_record_ip'] is not None:  # noqa: E501
            query_params.append(('filter.recordIp', local_var_params['filter_record_ip']))  # noqa: E501
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

        response_type = 'ReverseRecordsReadList'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/reverserecords', 'GET',
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

    def reverserecords_post(self, reverse_record_create, **kwargs):  # noqa: E501
        """Create a reverse DNS record  # noqa: E501

        Creates a new reverse DNS record. Reverse DNS is applicable to IPv4 addresses within IP Blocks and IPv6 addresses of the VDC.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reverserecords_post(reverse_record_create, async_req=True)
        >>> result = thread.get()

        :param reverse_record_create: reverserecord (required)
        :type reverse_record_create: ReverseRecordCreate
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
        :rtype: ReverseRecordRead
        """
        kwargs['_return_http_data_only'] = True
        return self.reverserecords_post_with_http_info(reverse_record_create, **kwargs)  # noqa: E501

    def reverserecords_post_with_http_info(self, reverse_record_create, **kwargs):  # noqa: E501
        """Create a reverse DNS record  # noqa: E501

        Creates a new reverse DNS record. Reverse DNS is applicable to IPv4 addresses within IP Blocks and IPv6 addresses of the VDC.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reverserecords_post_with_http_info(reverse_record_create, async_req=True)
        >>> result = thread.get()

        :param reverse_record_create: reverserecord (required)
        :type reverse_record_create: ReverseRecordCreate
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
        :rtype: tuple(ReverseRecordRead, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'reverse_record_create'
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
                    " to method reverserecords_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'reverse_record_create' is set
        if self.api_client.client_side_validation and ('reverse_record_create' not in local_var_params or  # noqa: E501
                                                        local_var_params['reverse_record_create'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `reverse_record_create` when calling `reverserecords_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'reverse_record_create' in local_var_params:
            body_params = local_var_params['reverse_record_create']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'ReverseRecordRead'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/reverserecords', 'POST',
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

    def reverserecords_put(self, reverserecord_id, reverse_record_ensure, **kwargs):  # noqa: E501
        """Update a reverse DNS record  # noqa: E501

        Updates or creates a reverse DNS record for the provided reverse DNS record ID.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reverserecords_put(reverserecord_id, reverse_record_ensure, async_req=True)
        >>> result = thread.get()

        :param reverserecord_id: The ID (UUID) of the reverse DNS record. (required)
        :type reverserecord_id: str
        :param reverse_record_ensure: (required)
        :type reverse_record_ensure: ReverseRecordEnsure
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
        :rtype: ReverseRecordRead
        """
        kwargs['_return_http_data_only'] = True
        return self.reverserecords_put_with_http_info(reverserecord_id, reverse_record_ensure, **kwargs)  # noqa: E501

    def reverserecords_put_with_http_info(self, reverserecord_id, reverse_record_ensure, **kwargs):  # noqa: E501
        """Update a reverse DNS record  # noqa: E501

        Updates or creates a reverse DNS record for the provided reverse DNS record ID.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reverserecords_put_with_http_info(reverserecord_id, reverse_record_ensure, async_req=True)
        >>> result = thread.get()

        :param reverserecord_id: The ID (UUID) of the reverse DNS record. (required)
        :type reverserecord_id: str
        :param reverse_record_ensure: (required)
        :type reverse_record_ensure: ReverseRecordEnsure
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
        :rtype: tuple(ReverseRecordRead, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'reverserecord_id',
            'reverse_record_ensure'
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
                    " to method reverserecords_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'reverserecord_id' is set
        if self.api_client.client_side_validation and ('reverserecord_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['reverserecord_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `reverserecord_id` when calling `reverserecords_put`")  # noqa: E501
        # verify the required parameter 'reverse_record_ensure' is set
        if self.api_client.client_side_validation and ('reverse_record_ensure' not in local_var_params or  # noqa: E501
                                                        local_var_params['reverse_record_ensure'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `reverse_record_ensure` when calling `reverserecords_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'reverserecord_id' in local_var_params:
            path_params['reverserecordId'] = local_var_params['reverserecord_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'reverse_record_ensure' in local_var_params:
            body_params = local_var_params['reverse_record_ensure']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'ReverseRecordRead'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/reverserecords/{reverserecordId}', 'PUT',
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
