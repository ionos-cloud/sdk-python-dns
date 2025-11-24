# ionoscloud_dns.ZoneFilesApi

All URIs are relative to *https://dns.de-fra.ionos.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_zonefile_get**](ZoneFilesApi.md#zones_zonefile_get) | **GET** /zones/{zoneId}/zonefile | Retrieve a zone file
[**zones_zonefile_put**](ZoneFilesApi.md#zones_zonefile_put) | **PUT** /zones/{zoneId}/zonefile | Updates a zone with a file


# **zones_zonefile_get**
> zones_zonefile_get(zone_id)

Retrieve a zone file

Returns an exported zone file in BIND format (RFC 1035).

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
    api_instance = ionoscloud_dns.ZoneFilesApi(api_client)
    zone_id = 'zone_id_example' # str | The ID (UUID) of the DNS zone.

    try:
        # Retrieve a zone file
        api_instance.zones_zonefile_get(zone_id)
    except Exception as e:
        print("Exception when calling ZoneFilesApi->zones_zonefile_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID (UUID) of the DNS zone. | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

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

# **zones_zonefile_put**
> RecordReadList zones_zonefile_put(zone_id, body)

Updates a zone with a file

Updates a zone with zone file in BIND format (RFC 1035). All records in the zone are replaced with the ones provided.

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
    api_instance = ionoscloud_dns.ZoneFilesApi(api_client)
    zone_id = 'zone_id_example' # str | The ID (UUID) of the DNS zone.
    body = 'body_example' # str | Zone file in BIND format (RFC 1035). In order to support import files from other sources, the bind zone file can contain SOA and NS records, but these records will be ignored.

    try:
        # Updates a zone with a file
        api_response = api_instance.zones_zonefile_put(zone_id, body)
        print("The response of ZoneFilesApi->zones_zonefile_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneFilesApi->zones_zonefile_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| The ID (UUID) of the DNS zone. | 
 **body** | **str**| Zone file in BIND format (RFC 1035). In order to support import files from other sources, the bind zone file can contain SOA and NS records, but these records will be ignored. | 

### Return type

[**RecordReadList**](RecordReadList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: text/plain
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

