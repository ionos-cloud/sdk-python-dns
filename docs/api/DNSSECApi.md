# ionoscloud_dns.DNSSECApi

All URIs are relative to *https://dns.de-fra.ionos.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_keys_delete**](DNSSECApi.md#zones_keys_delete) | **DELETE** /zones/{zoneId}/keys | Delete a DNSSEC key
[**zones_keys_get**](DNSSECApi.md#zones_keys_get) | **GET** /zones/{zoneId}/keys | Retrieve a DNSSEC key
[**zones_keys_post**](DNSSECApi.md#zones_keys_post) | **POST** /zones/{zoneId}/keys | Create a DNSSEC key


# **zones_keys_delete**
> object zones_keys_delete(zone_id)

Delete a DNSSEC key

Disable DNSSEC keys and remove associated DNSKEY records for your DNS zone.


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
    api_instance = ionoscloud_dns.DNSSECApi(api_client)
    zone_id = 'zone_id_example' # str | The ID (UUID) of the DNS zone.

    try:
        # Delete a DNSSEC key
        api_response = api_instance.zones_keys_delete(zone_id)
        print("The response of DNSSECApi->zones_keys_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->zones_keys_delete: %s\n" % e)
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

# **zones_keys_get**
> DnssecKeyReadList zones_keys_get(zone_id)

Retrieve a DNSSEC key

Get DNSSEC keys for your DNS zone.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.dnssec_key_read_list import DnssecKeyReadList
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
    api_instance = ionoscloud_dns.DNSSECApi(api_client)
    zone_id = 'zone_id_example' # str | The ID (UUID) of the DNS zone.

    try:
        # Retrieve a DNSSEC key
        api_response = api_instance.zones_keys_get(zone_id)
        print("The response of DNSSECApi->zones_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->zones_keys_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID (UUID) of the DNS zone. | 

### Return type

[**DnssecKeyReadList**](DnssecKeyReadList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success case, dnssec keys returned. |  -  |
**400** | ### Bad Request The request send to the API was malformed.  |  -  |
**401** | ### Unauthorized The request is missing authorization information or the authorization information provided are expired.  |  -  |
**403** | ### Not Allowed The user issuing the request does not have the needed permissions.  |  -  |
**404** | ### Not Found The resource that was requested could not be found.  |  -  |
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_keys_post**
> DnssecKeyReadCreation zones_keys_post(zone_id, dnssec_key_create)

Create a DNSSEC key

Enable DNSSEC keys and create associated DNSKEY records for your DNS zone.


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.dnssec_key_create import DnssecKeyCreate
from ionoscloud_dns.models.dnssec_key_read_creation import DnssecKeyReadCreation
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
    api_instance = ionoscloud_dns.DNSSECApi(api_client)
    zone_id = 'zone_id_example' # str | The ID (UUID) of the DNS zone.
    dnssec_key_create = ionoscloud_dns.DnssecKeyCreate() # DnssecKeyCreate | Enable DNSSEC request.

    try:
        # Create a DNSSEC key
        api_response = api_instance.zones_keys_post(zone_id, dnssec_key_create)
        print("The response of DNSSECApi->zones_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->zones_keys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID (UUID) of the DNS zone. | 
 **dnssec_key_create** | [**DnssecKeyCreate**](DnssecKeyCreate.md)| Enable DNSSEC request. | 

### Return type

[**DnssecKeyReadCreation**](DnssecKeyReadCreation.md)

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
**409** | ### Conflict Error You can only have one DNSSEC per zone, and this zone already has one in place.  |  -  |
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

