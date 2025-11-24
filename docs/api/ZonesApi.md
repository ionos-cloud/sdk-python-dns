# ionoscloud_dns.ZonesApi

All URIs are relative to *https://dns.de-fra.ionos.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_delete**](ZonesApi.md#zones_delete) | **DELETE** /zones/{zoneId} | Delete a zone
[**zones_find_by_id**](ZonesApi.md#zones_find_by_id) | **GET** /zones/{zoneId} | Retrieve a zone
[**zones_get**](ZonesApi.md#zones_get) | **GET** /zones | Retrieve zones
[**zones_post**](ZonesApi.md#zones_post) | **POST** /zones | Create a zone
[**zones_put**](ZonesApi.md#zones_put) | **PUT** /zones/{zoneId} | Update a zone


# **zones_delete**
> object zones_delete(zone_id)

Delete a zone

Deletes the specified zone and all of the records it contains.

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
    api_instance = ionoscloud_dns.ZonesApi(api_client)
    zone_id = 'zone_id_example' # str | The ID (UUID) of the DNS zone.

    try:
        # Delete a zone
        api_response = api_instance.zones_delete(zone_id)
        print("The response of ZonesApi->zones_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->zones_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID (UUID) of the DNS zone. | 

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

# **zones_find_by_id**
> ZoneRead zones_find_by_id(zone_id)

Retrieve a zone

Returns a DNS zone by given ID.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.zone_read import ZoneRead
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
    api_instance = ionoscloud_dns.ZonesApi(api_client)
    zone_id = 'zone_id_example' # str | The ID (UUID) of the DNS zone.

    try:
        # Retrieve a zone
        api_response = api_instance.zones_find_by_id(zone_id)
        print("The response of ZonesApi->zones_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->zones_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID (UUID) of the DNS zone. | 

### Return type

[**ZoneRead**](ZoneRead.md)

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

# **zones_get**
> ZoneReadList zones_get(filter_state=filter_state, filter_zone_name=filter_zone_name, offset=offset, limit=limit)

Retrieve zones

Returns a list of the DNS zones for the customer. Default limit is the first 100 items. Use pagination query parameters for listing more items (up to 1000).

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.provisioning_state import ProvisioningState
from ionoscloud_dns.models.zone_read_list import ZoneReadList
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
    api_instance = ionoscloud_dns.ZonesApi(api_client)
    filter_state = ionoscloud_dns.ProvisioningState() # ProvisioningState | Filter used to fetch all zones in a particular state. (optional)
    filter_zone_name = 'example.com' # str | Filter used to fetch only the zones that contain the specified zone name. (optional)
    offset = 0 # int | The first element (of the total list of elements) to include in the response. Use together with limit for pagination. (optional) (default to 0)
    limit = 100 # int | The maximum number of elements to return. Use together with offset for pagination. (optional) (default to 100)

    try:
        # Retrieve zones
        api_response = api_instance.zones_get(filter_state=filter_state, filter_zone_name=filter_zone_name, offset=offset, limit=limit)
        print("The response of ZonesApi->zones_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->zones_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_state** | [**ProvisioningState**](.md)| Filter used to fetch all zones in a particular state. | [optional] 
 **filter_zone_name** | **str**| Filter used to fetch only the zones that contain the specified zone name. | [optional] 
 **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100]

### Return type

[**ZoneReadList**](ZoneReadList.md)

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

# **zones_post**
> ZoneRead zones_post(zone_create)

Create a zone

Creates a new zone with default NS and SOA records.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.zone_create import ZoneCreate
from ionoscloud_dns.models.zone_read import ZoneRead
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
    api_instance = ionoscloud_dns.ZonesApi(api_client)
    zone_create = ionoscloud_dns.ZoneCreate() # ZoneCreate | zone

    try:
        # Create a zone
        api_response = api_instance.zones_post(zone_create)
        print("The response of ZonesApi->zones_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->zones_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_create** | [**ZoneCreate**](ZoneCreate.md)| zone | 

### Return type

[**ZoneRead**](ZoneRead.md)

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

# **zones_put**
> ZoneRead zones_put(zone_id, zone_ensure)

Update a zone

Updates or creates a zone for the provided zone ID.


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.zone_ensure import ZoneEnsure
from ionoscloud_dns.models.zone_read import ZoneRead
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
    api_instance = ionoscloud_dns.ZonesApi(api_client)
    zone_id = 'zone_id_example' # str | The ID (UUID) of the DNS zone.
    zone_ensure = ionoscloud_dns.ZoneEnsure() # ZoneEnsure | update zone

    try:
        # Update a zone
        api_response = api_instance.zones_put(zone_id, zone_ensure)
        print("The response of ZonesApi->zones_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->zones_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID (UUID) of the DNS zone. | 
 **zone_ensure** | [**ZoneEnsure**](ZoneEnsure.md)| update zone | 

### Return type

[**ZoneRead**](ZoneRead.md)

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

