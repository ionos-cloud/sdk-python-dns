from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_dns.api_client import ApiClient
from ionoscloud_dns.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RecordsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def records_get(self, **kwargs):  # noqa: E501
        """Retrieve all records from primary zones  # noqa: E501

        Returns the list of all records for all customer DNS zones with the possibility to filter them.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.records_get(async_req=True)
        >>> result = thread.get()

        :param filter_zone_id: Filter used to fetch only the records that contain specified zoneId.
        :type filter_zone_id: str
        :param filter_name: Filter used to fetch only the records that contain specified record name.
        :type filter_name: str
        :param filter_state: Filter used to fetch only the records that are in certain state.
        :type filter_state: ProvisioningState
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
        :rtype: RecordReadList
        """
        kwargs['_return_http_data_only'] = True
        return self.records_get_with_http_info(**kwargs)  # noqa: E501

    def records_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve all records from primary zones  # noqa: E501

        Returns the list of all records for all customer DNS zones with the possibility to filter them.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.records_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param filter_zone_id: Filter used to fetch only the records that contain specified zoneId.
        :type filter_zone_id: str
        :param filter_name: Filter used to fetch only the records that contain specified record name.
        :type filter_name: str
        :param filter_state: Filter used to fetch only the records that are in certain state.
        :type filter_state: ProvisioningState
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
        :rtype: tuple(RecordReadList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'filter_zone_id',
            'filter_name',
            'filter_state',
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
                    " to method records_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `records_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `records_get`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `records_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = list(local_var_params.get('query_params', {}).items())
        if 'filter_zone_id' in local_var_params and local_var_params['filter_zone_id'] is not None:  # noqa: E501
            query_params.append(('filter.zoneId', local_var_params['filter_zone_id']))  # noqa: E501
        if 'filter_name' in local_var_params and local_var_params['filter_name'] is not None:  # noqa: E501
            query_params.append(('filter.name', local_var_params['filter_name']))  # noqa: E501
        if 'filter_state' in local_var_params and local_var_params['filter_state'] is not None:  # noqa: E501
            query_params.append(('filter.state', local_var_params['filter_state']))  # noqa: E501
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

        response_type = 'RecordReadList'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/records', 'GET',
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

    def secondaryzones_records_get(self, secondary_zone_id, **kwargs):  # noqa: E501
        """Retrieve records for a secondary zone  # noqa: E501

        Returns the list of records for a secondary zone. Those are the records created for its primary IPs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_records_get(secondary_zone_id, async_req=True)
        >>> result = thread.get()

        :param secondary_zone_id: The ID (UUID) of the DNS secondary zone. (required)
        :type secondary_zone_id: str
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
        :rtype: SecondaryZoneRecordReadList
        """
        kwargs['_return_http_data_only'] = True
        return self.secondaryzones_records_get_with_http_info(secondary_zone_id, **kwargs)  # noqa: E501

    def secondaryzones_records_get_with_http_info(self, secondary_zone_id, **kwargs):  # noqa: E501
        """Retrieve records for a secondary zone  # noqa: E501

        Returns the list of records for a secondary zone. Those are the records created for its primary IPs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.secondaryzones_records_get_with_http_info(secondary_zone_id, async_req=True)
        >>> result = thread.get()

        :param secondary_zone_id: The ID (UUID) of the DNS secondary zone. (required)
        :type secondary_zone_id: str
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
        :rtype: tuple(SecondaryZoneRecordReadList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'secondary_zone_id',
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
                    " to method secondaryzones_records_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'secondary_zone_id' is set
        if self.api_client.client_side_validation and ('secondary_zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['secondary_zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `secondary_zone_id` when calling `secondaryzones_records_get`")  # noqa: E501

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `secondaryzones_records_get`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `secondaryzones_records_get`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `secondaryzones_records_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'secondary_zone_id' in local_var_params:
            path_params['secondaryZoneId'] = local_var_params['secondary_zone_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())
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

        response_type = 'SecondaryZoneRecordReadList'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/secondaryzones/{secondaryZoneId}/records', 'GET',
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

    def zones_records_delete(self, zone_id, record_id, **kwargs):  # noqa: E501
        """Delete a record  # noqa: E501

        Deletes a specified record from the DNS zone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_records_delete(zone_id, record_id, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param record_id: The ID (UUID) of the record. (required)
        :type record_id: str
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
        return self.zones_records_delete_with_http_info(zone_id, record_id, **kwargs)  # noqa: E501

    def zones_records_delete_with_http_info(self, zone_id, record_id, **kwargs):  # noqa: E501
        """Delete a record  # noqa: E501

        Deletes a specified record from the DNS zone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_records_delete_with_http_info(zone_id, record_id, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param record_id: The ID (UUID) of the record. (required)
        :type record_id: str
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
            'record_id'
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
                    " to method zones_records_delete" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'zone_id' is set
        if self.api_client.client_side_validation and ('zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `zone_id` when calling `zones_records_delete`")  # noqa: E501
        # verify the required parameter 'record_id' is set
        if self.api_client.client_side_validation and ('record_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['record_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `record_id` when calling `zones_records_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zoneId'] = local_var_params['zone_id']  # noqa: E501
        if 'record_id' in local_var_params:
            path_params['recordId'] = local_var_params['record_id']  # noqa: E501

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
            '/zones/{zoneId}/records/{recordId}', 'DELETE',
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

    def zones_records_find_by_id(self, zone_id, record_id, **kwargs):  # noqa: E501
        """Retrieve a record  # noqa: E501

        Returns the record with the specified record ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_records_find_by_id(zone_id, record_id, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param record_id: The ID (UUID) of the record. (required)
        :type record_id: str
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
        :rtype: RecordRead
        """
        kwargs['_return_http_data_only'] = True
        return self.zones_records_find_by_id_with_http_info(zone_id, record_id, **kwargs)  # noqa: E501

    def zones_records_find_by_id_with_http_info(self, zone_id, record_id, **kwargs):  # noqa: E501
        """Retrieve a record  # noqa: E501

        Returns the record with the specified record ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_records_find_by_id_with_http_info(zone_id, record_id, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param record_id: The ID (UUID) of the record. (required)
        :type record_id: str
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
        :rtype: tuple(RecordRead, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'zone_id',
            'record_id'
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
                    " to method zones_records_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'zone_id' is set
        if self.api_client.client_side_validation and ('zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `zone_id` when calling `zones_records_find_by_id`")  # noqa: E501
        # verify the required parameter 'record_id' is set
        if self.api_client.client_side_validation and ('record_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['record_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `record_id` when calling `zones_records_find_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zoneId'] = local_var_params['zone_id']  # noqa: E501
        if 'record_id' in local_var_params:
            path_params['recordId'] = local_var_params['record_id']  # noqa: E501

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

        response_type = 'RecordRead'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/zones/{zoneId}/records/{recordId}', 'GET',
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

    def zones_records_get(self, zone_id, **kwargs):  # noqa: E501
        """Retrieve records  # noqa: E501

        Returns the list of records for the specific DNS zone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_records_get(zone_id, async_req=True)
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
        :rtype: RecordReadList
        """
        kwargs['_return_http_data_only'] = True
        return self.zones_records_get_with_http_info(zone_id, **kwargs)  # noqa: E501

    def zones_records_get_with_http_info(self, zone_id, **kwargs):  # noqa: E501
        """Retrieve records  # noqa: E501

        Returns the list of records for the specific DNS zone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_records_get_with_http_info(zone_id, async_req=True)
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
        :rtype: tuple(RecordReadList, status_code(int), headers(HTTPHeaderDict))
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
                    " to method zones_records_get" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'zone_id' is set
        if self.api_client.client_side_validation and ('zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `zone_id` when calling `zones_records_get`")  # noqa: E501

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

        response_type = 'RecordReadList'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/zones/{zoneId}/records', 'GET',
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

    def zones_records_post(self, zone_id, record_create, **kwargs):  # noqa: E501
        """Create a record  # noqa: E501

        Creates a new record for the DNS zone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_records_post(zone_id, record_create, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param record_create: record (required)
        :type record_create: RecordCreate
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
        :rtype: RecordRead
        """
        kwargs['_return_http_data_only'] = True
        return self.zones_records_post_with_http_info(zone_id, record_create, **kwargs)  # noqa: E501

    def zones_records_post_with_http_info(self, zone_id, record_create, **kwargs):  # noqa: E501
        """Create a record  # noqa: E501

        Creates a new record for the DNS zone.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_records_post_with_http_info(zone_id, record_create, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param record_create: record (required)
        :type record_create: RecordCreate
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
        :rtype: tuple(RecordRead, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'zone_id',
            'record_create'
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
                    " to method zones_records_post" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'zone_id' is set
        if self.api_client.client_side_validation and ('zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `zone_id` when calling `zones_records_post`")  # noqa: E501
        # verify the required parameter 'record_create' is set
        if self.api_client.client_side_validation and ('record_create' not in local_var_params or  # noqa: E501
                                                        local_var_params['record_create'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `record_create` when calling `zones_records_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zoneId'] = local_var_params['zone_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'record_create' in local_var_params:
            body_params = local_var_params['record_create']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'RecordRead'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/zones/{zoneId}/records', 'POST',
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

    def zones_records_put(self, zone_id, record_id, record_ensure, **kwargs):  # noqa: E501
        """Ensure a record  # noqa: E501

        Ensures that a DNS record with the provided ID is created or modified. In order to successfully update record - all JSON parameters must be passed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_records_put(zone_id, record_id, record_ensure, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param record_id: The ID (UUID) of the DNS record. (required)
        :type record_id: str
        :param record_ensure: (required)
        :type record_ensure: RecordEnsure
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
        :rtype: RecordRead
        """
        kwargs['_return_http_data_only'] = True
        return self.zones_records_put_with_http_info(zone_id, record_id, record_ensure, **kwargs)  # noqa: E501

    def zones_records_put_with_http_info(self, zone_id, record_id, record_ensure, **kwargs):  # noqa: E501
        """Ensure a record  # noqa: E501

        Ensures that a DNS record with the provided ID is created or modified. In order to successfully update record - all JSON parameters must be passed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.zones_records_put_with_http_info(zone_id, record_id, record_ensure, async_req=True)
        >>> result = thread.get()

        :param zone_id: The ID (UUID) of the DNS zone. (required)
        :type zone_id: str
        :param record_id: The ID (UUID) of the DNS record. (required)
        :type record_id: str
        :param record_ensure: (required)
        :type record_ensure: RecordEnsure
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
        :rtype: tuple(RecordRead, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'zone_id',
            'record_id',
            'record_ensure'
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
                    " to method zones_records_put" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'zone_id' is set
        if self.api_client.client_side_validation and ('zone_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['zone_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `zone_id` when calling `zones_records_put`")  # noqa: E501
        # verify the required parameter 'record_id' is set
        if self.api_client.client_side_validation and ('record_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['record_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `record_id` when calling `zones_records_put`")  # noqa: E501
        # verify the required parameter 'record_ensure' is set
        if self.api_client.client_side_validation and ('record_ensure' not in local_var_params or  # noqa: E501
                                                        local_var_params['record_ensure'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `record_ensure` when calling `zones_records_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone_id' in local_var_params:
            path_params['zoneId'] = local_var_params['zone_id']  # noqa: E501
        if 'record_id' in local_var_params:
            path_params['recordId'] = local_var_params['record_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'record_ensure' in local_var_params:
            body_params = local_var_params['record_ensure']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'RecordRead'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/zones/{zoneId}/records/{recordId}', 'PUT',
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
