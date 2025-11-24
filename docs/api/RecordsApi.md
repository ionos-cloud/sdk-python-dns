# ionoscloud_dns.RecordsApi

All URIs are relative to *https://dns.de-fra.ionos.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**records_get**](RecordsApi.md#records_get) | **GET** /records | Retrieve all records from primary zones
[**secondaryzones_records_get**](RecordsApi.md#secondaryzones_records_get) | **GET** /secondaryzones/{secondaryZoneId}/records | Retrieve records for a secondary zone
[**zones_records_delete**](RecordsApi.md#zones_records_delete) | **DELETE** /zones/{zoneId}/records/{recordId} | Delete a record
[**zones_records_find_by_id**](RecordsApi.md#zones_records_find_by_id) | **GET** /zones/{zoneId}/records/{recordId} | Retrieve a record
[**zones_records_get**](RecordsApi.md#zones_records_get) | **GET** /zones/{zoneId}/records | Retrieve records
[**zones_records_post**](RecordsApi.md#zones_records_post) | **POST** /zones/{zoneId}/records | Create a record
[**zones_records_put**](RecordsApi.md#zones_records_put) | **PUT** /zones/{zoneId}/records/{recordId} | Update a record


# **records_get**
> RecordReadList records_get(filter_zone_id=filter_zone_id, filter_name=filter_name, filter_state=filter_state, filter_type=filter_type, offset=offset, limit=limit)

Retrieve all records from primary zones

Returns the list of all records for all customer DNS zones with the possibility to filter them.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.provisioning_state import ProvisioningState
from ionoscloud_dns.models.record_read_list import RecordReadList
from ionoscloud_dns.models.record_type import RecordType
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
    api_instance = ionoscloud_dns.RecordsApi(api_client)
    filter_zone_id = '1d6ca576-7162-4700-8df7-208bbe28fc44' # str | Filter used to fetch only the records that contain specified zoneId. (optional)
    filter_name = 'app' # str | Filter used to fetch only the records that contain specified record name. (optional)
    filter_state = ionoscloud_dns.ProvisioningState() # ProvisioningState | Filter used to fetch only the records that are in certain state. (optional)
    filter_type = ionoscloud_dns.RecordType() # RecordType | Filter used to fetch only the records with specified type. (optional)
    offset = 0 # int | The first element (of the total list of elements) to include in the response. Use together with limit for pagination. (optional) (default to 0)
    limit = 100 # int | The maximum number of elements to return. Use together with offset for pagination. (optional) (default to 100)

    try:
        # Retrieve all records from primary zones
        api_response = api_instance.records_get(filter_zone_id=filter_zone_id, filter_name=filter_name, filter_state=filter_state, filter_type=filter_type, offset=offset, limit=limit)
        print("The response of RecordsApi->records_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->records_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_zone_id** | **str**| Filter used to fetch only the records that contain specified zoneId. | [optional] 
 **filter_name** | **str**| Filter used to fetch only the records that contain specified record name. | [optional] 
 **filter_state** | [**ProvisioningState**](.md)| Filter used to fetch only the records that are in certain state. | [optional] 
 **filter_type** | [**RecordType**](.md)| Filter used to fetch only the records with specified type. | [optional] 
 **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100]

### Return type

[**RecordReadList**](RecordReadList.md)

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
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secondaryzones_records_get**
> SecondaryZoneRecordReadList secondaryzones_records_get(secondary_zone_id, offset=offset, limit=limit)

Retrieve records for a secondary zone

Returns the list of records for a secondary zone. Those are the records created for its primary IPs

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.secondary_zone_record_read_list import SecondaryZoneRecordReadList
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
    api_instance = ionoscloud_dns.RecordsApi(api_client)
    secondary_zone_id = 'secondary_zone_id_example' # str | The ID (UUID) of the DNS secondary zone.
    offset = 0 # int | The first element (of the total list of elements) to include in the response. Use together with limit for pagination. (optional) (default to 0)
    limit = 100 # int | The maximum number of elements to return. Use together with offset for pagination. (optional) (default to 100)

    try:
        # Retrieve records for a secondary zone
        api_response = api_instance.secondaryzones_records_get(secondary_zone_id, offset=offset, limit=limit)
        print("The response of RecordsApi->secondaryzones_records_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->secondaryzones_records_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secondary_zone_id** | **str**| The ID (UUID) of the DNS secondary zone. | 
 **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100]

### Return type

[**SecondaryZoneRecordReadList**](SecondaryZoneRecordReadList.md)

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
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_records_delete**
> object zones_records_delete(zone_id, record_id)

Delete a record

Deletes a specified record from the DNS zone.

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
    api_instance = ionoscloud_dns.RecordsApi(api_client)
    zone_id = 'zone_id_example' # str | The ID (UUID) of the DNS zone.
    record_id = 'record_id_example' # str | The ID (UUID) of the record.

    try:
        # Delete a record
        api_response = api_instance.zones_records_delete(zone_id, record_id)
        print("The response of RecordsApi->zones_records_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->zones_records_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID (UUID) of the DNS zone. | 
 **record_id** | **str**| The ID (UUID) of the record. | 

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

# **zones_records_find_by_id**
> RecordRead zones_records_find_by_id(zone_id, record_id)

Retrieve a record

Returns the record with the specified record ID.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.record_read import RecordRead
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
    api_instance = ionoscloud_dns.RecordsApi(api_client)
    zone_id = 'zone_id_example' # str | The ID (UUID) of the DNS zone.
    record_id = 'record_id_example' # str | The ID (UUID) of the record.

    try:
        # Retrieve a record
        api_response = api_instance.zones_records_find_by_id(zone_id, record_id)
        print("The response of RecordsApi->zones_records_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->zones_records_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID (UUID) of the DNS zone. | 
 **record_id** | **str**| The ID (UUID) of the record. | 

### Return type

[**RecordRead**](RecordRead.md)

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

# **zones_records_get**
> RecordReadList zones_records_get(zone_id)

Retrieve records

Returns the list of records for the specific DNS zone.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.record_read_list import RecordReadList
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
    api_instance = ionoscloud_dns.RecordsApi(api_client)
    zone_id = 'zone_id_example' # str | The ID (UUID) of the DNS zone.

    try:
        # Retrieve records
        api_response = api_instance.zones_records_get(zone_id)
        print("The response of RecordsApi->zones_records_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->zones_records_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID (UUID) of the DNS zone. | 

### Return type

[**RecordReadList**](RecordReadList.md)

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
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_records_post**
> RecordRead zones_records_post(zone_id, record_create)

Create a record

Creates a new record for the DNS zone.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.record_create import RecordCreate
from ionoscloud_dns.models.record_read import RecordRead
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
    api_instance = ionoscloud_dns.RecordsApi(api_client)
    zone_id = 'zone_id_example' # str | The ID (UUID) of the DNS zone.
    record_create = ionoscloud_dns.RecordCreate() # RecordCreate | record

    try:
        # Create a record
        api_response = api_instance.zones_records_post(zone_id, record_create)
        print("The response of RecordsApi->zones_records_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->zones_records_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID (UUID) of the DNS zone. | 
 **record_create** | [**RecordCreate**](RecordCreate.md)| record | 

### Return type

[**RecordRead**](RecordRead.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful operation. |  -  |
**400** | ### Bad Request The request send to the API was malformed.  |  -  |
**401** | ### Unauthorized The request is missing authorization information or the authorization information provided are expired.  |  -  |
**403** | ### Not Allowed The user issuing the request does not have the needed permissions.  |  -  |
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_records_put**
> RecordRead zones_records_put(zone_id, record_id, record_ensure)

Update a record

Updates or creates a DNS record for the provided record ID.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.record_ensure import RecordEnsure
from ionoscloud_dns.models.record_read import RecordRead
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
    api_instance = ionoscloud_dns.RecordsApi(api_client)
    zone_id = 'zone_id_example' # str | The ID (UUID) of the DNS zone.
    record_id = 'record_id_example' # str | The ID (UUID) of the DNS record.
    record_ensure = ionoscloud_dns.RecordEnsure() # RecordEnsure | 

    try:
        # Update a record
        api_response = api_instance.zones_records_put(zone_id, record_id, record_ensure)
        print("The response of RecordsApi->zones_records_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->zones_records_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID (UUID) of the DNS zone. | 
 **record_id** | **str**| The ID (UUID) of the DNS record. | 
 **record_ensure** | [**RecordEnsure**](RecordEnsure.md)|  | 

### Return type

[**RecordRead**](RecordRead.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

