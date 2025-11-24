# ionoscloud_dns.ReverseRecordsApi

All URIs are relative to *https://dns.de-fra.ionos.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reverserecords_delete**](ReverseRecordsApi.md#reverserecords_delete) | **DELETE** /reverserecords/{reverserecordId} | Delete a reverse DNS record
[**reverserecords_find_by_id**](ReverseRecordsApi.md#reverserecords_find_by_id) | **GET** /reverserecords/{reverserecordId} | Retrieve a reverse DNS record
[**reverserecords_get**](ReverseRecordsApi.md#reverserecords_get) | **GET** /reverserecords | Retrieves existing reverse DNS records
[**reverserecords_post**](ReverseRecordsApi.md#reverserecords_post) | **POST** /reverserecords | Create a reverse DNS record
[**reverserecords_put**](ReverseRecordsApi.md#reverserecords_put) | **PUT** /reverserecords/{reverserecordId} | Update a reverse DNS record


# **reverserecords_delete**
> object reverserecords_delete(reverserecord_id)

Delete a reverse DNS record

Deletes a reverse DNS record.


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dns.de-fra.ionos.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_dns.Configuration(
    host = "https://dns.de-fra.ionos.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_dns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dns.ReverseRecordsApi(api_client)
    reverserecord_id = 'reverserecord_id_example' # str | The ID (UUID) of the reverse DNS record.

    try:
        # Delete a reverse DNS record
        api_response = api_instance.reverserecords_delete(reverserecord_id)
        print("The response of ReverseRecordsApi->reverserecords_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReverseRecordsApi->reverserecords_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reverserecord_id** | **str**| The ID (UUID) of the reverse DNS record. | 

### Return type

**object**

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation. |  -  |
**400** | ### Bad Request The request send to the API was malformed.  |  -  |
**401** | ### Unauthorized The request is missing authorization information or the authorization information provided are expired.  |  -  |
**403** | ### Not Allowed The user issuing the request does not have the needed permissions.  |  -  |
**404** | ### Not Found The resource that was requested could not be found.  |  -  |
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reverserecords_find_by_id**
> ReverseRecordRead reverserecords_find_by_id(reverserecord_id)

Retrieve a reverse DNS record

Returns the record with the specified record ID.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.reverse_record_read import ReverseRecordRead
from ionoscloud_dns.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dns.de-fra.ionos.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_dns.Configuration(
    host = "https://dns.de-fra.ionos.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_dns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dns.ReverseRecordsApi(api_client)
    reverserecord_id = 'reverserecord_id_example' # str | The ID (UUID) of the reverse DNS record.

    try:
        # Retrieve a reverse DNS record
        api_response = api_instance.reverserecords_find_by_id(reverserecord_id)
        print("The response of ReverseRecordsApi->reverserecords_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReverseRecordsApi->reverserecords_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reverserecord_id** | **str**| The ID (UUID) of the reverse DNS record. | 

### Return type

[**ReverseRecordRead**](ReverseRecordRead.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | ### Bad Request The request send to the API was malformed.  |  -  |
**401** | ### Unauthorized The request is missing authorization information or the authorization information provided are expired.  |  -  |
**403** | ### Not Allowed The user issuing the request does not have the needed permissions.  |  -  |
**404** | ### Not Found The resource that was requested could not be found.  |  -  |
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reverserecords_get**
> ReverseRecordsReadList reverserecords_get(filter_record_ip=filter_record_ip, offset=offset, limit=limit)

Retrieves existing reverse DNS records

Returns a list of the reverse records of the customer. Default limit is the first 100 items. Use pagination query parameters to list more items.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.reverse_records_read_list import ReverseRecordsReadList
from ionoscloud_dns.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dns.de-fra.ionos.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_dns.Configuration(
    host = "https://dns.de-fra.ionos.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_dns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dns.ReverseRecordsApi(api_client)
    filter_record_ip = ['filter_record_ip_example'] # list[str] | Filter is used to fetch only the reverse records for the specified IPs. It's an array of IP records. IP can be any valid IPv4 or IPv6 address. Parameter has to be sent in query as many times as values (filter.recordIp=1.2.3.4&filter.recordIp=2.3.4.5)  (optional)
    offset = 0 # int | The first element (of the total list of elements) to include in the response. Use together with limit for pagination. (optional) (default to 0)
    limit = 100 # int | The maximum number of elements to return. Use together with offset for pagination. (optional) (default to 100)

    try:
        # Retrieves existing reverse DNS records
        api_response = api_instance.reverserecords_get(filter_record_ip=filter_record_ip, offset=offset, limit=limit)
        print("The response of ReverseRecordsApi->reverserecords_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReverseRecordsApi->reverserecords_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_record_ip** | [**list[str]**](str.md)| Filter is used to fetch only the reverse records for the specified IPs. It&#39;s an array of IP records. IP can be any valid IPv4 or IPv6 address. Parameter has to be sent in query as many times as values (filter.recordIp&#x3D;1.2.3.4&amp;filter.recordIp&#x3D;2.3.4.5)  | [optional] 
 **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100]

### Return type

[**ReverseRecordsReadList**](ReverseRecordsReadList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | ### Bad Request The request send to the API was malformed.  |  -  |
**401** | ### Unauthorized The request is missing authorization information or the authorization information provided are expired.  |  -  |
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reverserecords_post**
> ReverseRecordRead reverserecords_post(reverse_record_create)

Create a reverse DNS record

Creates a new reverse DNS record. Reverse DNS is applicable to IPv4 addresses within IP Blocks and IPv6 addresses of the VDC.


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.reverse_record_create import ReverseRecordCreate
from ionoscloud_dns.models.reverse_record_read import ReverseRecordRead
from ionoscloud_dns.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dns.de-fra.ionos.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_dns.Configuration(
    host = "https://dns.de-fra.ionos.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_dns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dns.ReverseRecordsApi(api_client)
    reverse_record_create = ionoscloud_dns.ReverseRecordCreate() # ReverseRecordCreate | reverserecord

    try:
        # Create a reverse DNS record
        api_response = api_instance.reverserecords_post(reverse_record_create)
        print("The response of ReverseRecordsApi->reverserecords_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReverseRecordsApi->reverserecords_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reverse_record_create** | [**ReverseRecordCreate**](ReverseRecordCreate.md)| reverserecord | 

### Return type

[**ReverseRecordRead**](ReverseRecordRead.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation. |  -  |
**400** | ### Bad Request The request send to the API was malformed.  |  -  |
**401** | ### Unauthorized The request is missing authorization information or the authorization information provided are expired.  |  -  |
**403** | ### Not Allowed The user issuing the request does not have the needed permissions.  |  -  |
**409** | ### Conflict Error This IP is not available to create a reverse DNS record.  |  -  |
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reverserecords_put**
> ReverseRecordRead reverserecords_put(reverserecord_id, reverse_record_ensure)

Update a reverse DNS record

Updates or creates a reverse DNS record for the provided reverse DNS record ID.


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.reverse_record_ensure import ReverseRecordEnsure
from ionoscloud_dns.models.reverse_record_read import ReverseRecordRead
from ionoscloud_dns.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dns.de-fra.ionos.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_dns.Configuration(
    host = "https://dns.de-fra.ionos.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_dns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_dns.ReverseRecordsApi(api_client)
    reverserecord_id = 'reverserecord_id_example' # str | The ID (UUID) of the reverse DNS record.
    reverse_record_ensure = ionoscloud_dns.ReverseRecordEnsure() # ReverseRecordEnsure | 

    try:
        # Update a reverse DNS record
        api_response = api_instance.reverserecords_put(reverserecord_id, reverse_record_ensure)
        print("The response of ReverseRecordsApi->reverserecords_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReverseRecordsApi->reverserecords_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reverserecord_id** | **str**| The ID (UUID) of the reverse DNS record. | 
 **reverse_record_ensure** | [**ReverseRecordEnsure**](ReverseRecordEnsure.md)|  | 

### Return type

[**ReverseRecordRead**](ReverseRecordRead.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | ### Bad Request The request send to the API was malformed.  |  -  |
**401** | ### Unauthorized The request is missing authorization information or the authorization information provided are expired.  |  -  |
**403** | ### Not Allowed The user issuing the request does not have the needed permissions.  |  -  |
**404** | ### Not Found The resource that was requested could not be found.  |  -  |
**409** | ### Conflict Error This IP is not available to create a reverse DNS record.  |  -  |
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

