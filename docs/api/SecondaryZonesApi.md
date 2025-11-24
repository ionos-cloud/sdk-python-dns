# ionoscloud_dns.SecondaryZonesApi

All URIs are relative to *https://dns.de-fra.ionos.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secondaryzones_axfr_get**](SecondaryZonesApi.md#secondaryzones_axfr_get) | **GET** /secondaryzones/{secondaryZoneId}/axfr | Get status of zone transfer
[**secondaryzones_axfr_put**](SecondaryZonesApi.md#secondaryzones_axfr_put) | **PUT** /secondaryzones/{secondaryZoneId}/axfr | Start zone transfer
[**secondaryzones_delete**](SecondaryZonesApi.md#secondaryzones_delete) | **DELETE** /secondaryzones/{secondaryZoneId} | Delete a secondary zone
[**secondaryzones_find_by_id**](SecondaryZonesApi.md#secondaryzones_find_by_id) | **GET** /secondaryzones/{secondaryZoneId} | Retrieve a secondary zone
[**secondaryzones_get**](SecondaryZonesApi.md#secondaryzones_get) | **GET** /secondaryzones | Retrieve secondary zones
[**secondaryzones_post**](SecondaryZonesApi.md#secondaryzones_post) | **POST** /secondaryzones | Create a secondary zone
[**secondaryzones_put**](SecondaryZonesApi.md#secondaryzones_put) | **PUT** /secondaryzones/{secondaryZoneId} | Update a secondary zone


# **secondaryzones_axfr_get**
> ZoneTransferPrimaryIpsStatus secondaryzones_axfr_get(secondary_zone_id)

Get status of zone transfer

Get status of zone transfer. 
Note that Cloud DNS relies on the following Anycast addresses for sending DNS notify messages.
Make sure to whitelist on your end:
  - IPv4: 212.227.123.25
  - IPv6: 2001:8d8:fe:53::5cd:25


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.zone_transfer_primary_ips_status import ZoneTransferPrimaryIpsStatus
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
    api_instance = ionoscloud_dns.SecondaryZonesApi(api_client)
    secondary_zone_id = 'secondary_zone_id_example' # str | The ID (UUID) of the DNS zone.

    try:
        # Get status of zone transfer
        api_response = api_instance.secondaryzones_axfr_get(secondary_zone_id)
        print("The response of SecondaryZonesApi->secondaryzones_axfr_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecondaryZonesApi->secondaryzones_axfr_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secondary_zone_id** | **str**| The ID (UUID) of the DNS zone. | 

### Return type

[**ZoneTransferPrimaryIpsStatus**](ZoneTransferPrimaryIpsStatus.md)

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

# **secondaryzones_axfr_put**
> object secondaryzones_axfr_put(secondary_zone_id)

Start zone transfer

Initiate zone transfer.
Note that Cloud DNS relies on the following Anycast addresses for sending DNS notify messages.
Make sure to whitelist on your end:
  - IPv4: 212.227.123.25
  - IPv6: 2001:8d8:fe:53::5cd:25


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
    api_instance = ionoscloud_dns.SecondaryZonesApi(api_client)
    secondary_zone_id = 'secondary_zone_id_example' # str | The ID (UUID) of the DNS zone.

    try:
        # Start zone transfer
        api_response = api_instance.secondaryzones_axfr_put(secondary_zone_id)
        print("The response of SecondaryZonesApi->secondaryzones_axfr_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecondaryZonesApi->secondaryzones_axfr_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secondary_zone_id** | **str**| The ID (UUID) of the DNS zone. | 

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

# **secondaryzones_delete**
> object secondaryzones_delete(secondary_zone_id)

Delete a secondary zone

Deletes the specified secondary zone.

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
    api_instance = ionoscloud_dns.SecondaryZonesApi(api_client)
    secondary_zone_id = 'secondary_zone_id_example' # str | The ID (UUID) of the DNS zone.

    try:
        # Delete a secondary zone
        api_response = api_instance.secondaryzones_delete(secondary_zone_id)
        print("The response of SecondaryZonesApi->secondaryzones_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecondaryZonesApi->secondaryzones_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secondary_zone_id** | **str**| The ID (UUID) of the DNS zone. | 

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

# **secondaryzones_find_by_id**
> SecondaryZoneRead secondaryzones_find_by_id(secondary_zone_id)

Retrieve a secondary zone

Returns a DNS secondary zone by given ID.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.secondary_zone_read import SecondaryZoneRead
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
    api_instance = ionoscloud_dns.SecondaryZonesApi(api_client)
    secondary_zone_id = 'secondary_zone_id_example' # str | The ID (UUID) of the DNS zone.

    try:
        # Retrieve a secondary zone
        api_response = api_instance.secondaryzones_find_by_id(secondary_zone_id)
        print("The response of SecondaryZonesApi->secondaryzones_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecondaryZonesApi->secondaryzones_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secondary_zone_id** | **str**| The ID (UUID) of the DNS zone. | 

### Return type

[**SecondaryZoneRead**](SecondaryZoneRead.md)

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

# **secondaryzones_get**
> SecondaryZoneReadList secondaryzones_get(filter_state=filter_state, filter_zone_name=filter_zone_name, offset=offset, limit=limit)

Retrieve secondary zones

Returns a list of the secondary DNS zones for the customer. Default limit is the first 100 items. Use pagination query parameters for listing more items (up to 1000).

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.provisioning_state import ProvisioningState
from ionoscloud_dns.models.secondary_zone_read_list import SecondaryZoneReadList
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
    api_instance = ionoscloud_dns.SecondaryZonesApi(api_client)
    filter_state = ionoscloud_dns.ProvisioningState() # ProvisioningState | Filter used to fetch all zones in a particular state. (optional)
    filter_zone_name = 'example.com' # str | Filter used to fetch only the zones that contain the specified zone name. (optional)
    offset = 0 # int | The first element (of the total list of elements) to include in the response. Use together with limit for pagination. (optional) (default to 0)
    limit = 100 # int | The maximum number of elements to return. Use together with offset for pagination. (optional) (default to 100)

    try:
        # Retrieve secondary zones
        api_response = api_instance.secondaryzones_get(filter_state=filter_state, filter_zone_name=filter_zone_name, offset=offset, limit=limit)
        print("The response of SecondaryZonesApi->secondaryzones_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecondaryZonesApi->secondaryzones_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_state** | [**ProvisioningState**](.md)| Filter used to fetch all zones in a particular state. | [optional] 
 **filter_zone_name** | **str**| Filter used to fetch only the zones that contain the specified zone name. | [optional] 
 **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100]

### Return type

[**SecondaryZoneReadList**](SecondaryZoneReadList.md)

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

# **secondaryzones_post**
> SecondaryZoneRead secondaryzones_post(secondary_zone_create)

Create a secondary zone

Creates a new secondary zone with default NS and SOA records.
Note that Cloud DNS relies on the following Anycast addresses for sending DNS notify messages.
Make sure to whitelist on your end:
  - IPv4: 212.227.123.25
  - IPv6: 2001:8d8:fe:53::5cd:25


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.secondary_zone_create import SecondaryZoneCreate
from ionoscloud_dns.models.secondary_zone_read import SecondaryZoneRead
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
    api_instance = ionoscloud_dns.SecondaryZonesApi(api_client)
    secondary_zone_create = ionoscloud_dns.SecondaryZoneCreate() # SecondaryZoneCreate | zone

    try:
        # Create a secondary zone
        api_response = api_instance.secondaryzones_post(secondary_zone_create)
        print("The response of SecondaryZonesApi->secondaryzones_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecondaryZonesApi->secondaryzones_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secondary_zone_create** | [**SecondaryZoneCreate**](SecondaryZoneCreate.md)| zone | 

### Return type

[**SecondaryZoneRead**](SecondaryZoneRead.md)

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

# **secondaryzones_put**
> SecondaryZoneRead secondaryzones_put(secondary_zone_id, secondary_zone_ensure)

Update a secondary zone

Updates or creates a secondary zone for the provided secondary Zone ID.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.secondary_zone_ensure import SecondaryZoneEnsure
from ionoscloud_dns.models.secondary_zone_read import SecondaryZoneRead
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
    api_instance = ionoscloud_dns.SecondaryZonesApi(api_client)
    secondary_zone_id = 'secondary_zone_id_example' # str | The ID (UUID) of the DNS zone.
    secondary_zone_ensure = ionoscloud_dns.SecondaryZoneEnsure() # SecondaryZoneEnsure | update zone

    try:
        # Update a secondary zone
        api_response = api_instance.secondaryzones_put(secondary_zone_id, secondary_zone_ensure)
        print("The response of SecondaryZonesApi->secondaryzones_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecondaryZonesApi->secondaryzones_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secondary_zone_id** | **str**| The ID (UUID) of the DNS zone. | 
 **secondary_zone_ensure** | [**SecondaryZoneEnsure**](SecondaryZoneEnsure.md)| update zone | 

### Return type

[**SecondaryZoneRead**](SecondaryZoneRead.md)

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

