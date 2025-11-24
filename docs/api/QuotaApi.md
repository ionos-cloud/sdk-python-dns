# ionoscloud_dns.QuotaApi

All URIs are relative to *https://dns.de-fra.ionos.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quota_get**](QuotaApi.md#quota_get) | **GET** /quota | Retrieve resources quota


# **quota_get**
> Quota quota_get()

Retrieve resources quota

Get quota details for zones, secondary zones, and records.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_dns
from ionoscloud_dns.models.quota import Quota
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
    api_instance = ionoscloud_dns.QuotaApi(api_client)

    try:
        # Retrieve resources quota
        api_response = api_instance.quota_get()
        print("The response of QuotaApi->quota_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->quota_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Quota**](Quota.md)

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

