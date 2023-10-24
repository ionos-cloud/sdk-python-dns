# SecondaryZonesApi

All URIs are relative to *https://dns.de-fra.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**secondaryzones_axfr_get**](SecondaryZonesApi.md#secondaryzones_axfr_get) | **GET** /secondaryzones/{secondaryZoneId}/axfr | Get status of zone transfer |
| [**secondaryzones_axfr_put**](SecondaryZonesApi.md#secondaryzones_axfr_put) | **PUT** /secondaryzones/{secondaryZoneId}/axfr | Start zone transfer |
| [**secondaryzones_delete**](SecondaryZonesApi.md#secondaryzones_delete) | **DELETE** /secondaryzones/{secondaryZoneId} | Delete a secondary zone |
| [**secondaryzones_find_by_id**](SecondaryZonesApi.md#secondaryzones_find_by_id) | **GET** /secondaryzones/{secondaryZoneId} | Retrieve a secondary zone |
| [**secondaryzones_get**](SecondaryZonesApi.md#secondaryzones_get) | **GET** /secondaryzones | Retrieve secondary zones |
| [**secondaryzones_post**](SecondaryZonesApi.md#secondaryzones_post) | **POST** /secondaryzones | Create a secondary zone |
| [**secondaryzones_put**](SecondaryZonesApi.md#secondaryzones_put) | **PUT** /secondaryzones/{secondaryZoneId} | Ensure a secondary zone |


# **secondaryzones_axfr_get**
> ZoneTransferPrimaryIpsStatus secondaryzones_axfr_get(secondary_zone_id)

Get status of zone transfer

Get status of zone transfer.  Note that Cloud DNS relies on the following Anycast addresses for sending DNS notify messages. Make sure to whitelist on your end:   - IPv4: 212.227.123.25   - IPv6: 2001:8d8:fe:53::5cd:25 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **secondary_zone_id** | **str**| The ID (UUID) of the DNS zone. |  |

### Return type

[**ZoneTransferPrimaryIpsStatus**](../models/ZoneTransferPrimaryIpsStatus.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **secondaryzones_axfr_put**
> object secondaryzones_axfr_put(secondary_zone_id)

Start zone transfer

Initiate zone transfer. Note that Cloud DNS relies on the following Anycast addresses for sending DNS notify messages. Make sure to whitelist on your end:   - IPv4: 212.227.123.25   - IPv6: 2001:8d8:fe:53::5cd:25 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **secondary_zone_id** | **str**| The ID (UUID) of the DNS zone. |  |

### Return type

**object**

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **secondaryzones_delete**
> object secondaryzones_delete(secondary_zone_id)

Delete a secondary zone

Deletes the specified secondary zone.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **secondary_zone_id** | **str**| The ID (UUID) of the DNS zone. |  |

### Return type

**object**

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **secondaryzones_find_by_id**
> SecondaryZoneRead secondaryzones_find_by_id(secondary_zone_id)

Retrieve a secondary zone

Returns a DNS secondary zone by given ID.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **secondary_zone_id** | **str**| The ID (UUID) of the DNS zone. |  |

### Return type

[**SecondaryZoneRead**](../models/SecondaryZoneRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **secondaryzones_get**
> SecondaryZoneReadList secondaryzones_get(filter_state=filter_state, filter_zone_name=filter_zone_name, offset=offset, limit=limit)

Retrieve secondary zones

Returns a list of the secondary DNS zones for the customer. Default limit is the first 100 items. Use pagination query parameters for listing more items (up to 1000).

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **filter_state** | [**ProvisioningState**](../models/.md)| Filter used to fetch all zones in a particular state. | [optional]  |
| **filter_zone_name** | **str**| Filter used to fetch only the zones that contain the specified zone name. | [optional]  |
| **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100] |

### Return type

[**SecondaryZoneReadList**](../models/SecondaryZoneReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **secondaryzones_post**
> SecondaryZoneRead secondaryzones_post(secondary_zone_create)

Create a secondary zone

Creates a new secondary zone with default NS and SOA records. Note that Cloud DNS relies on the following Anycast addresses for sending DNS notify messages. Make sure to whitelist on your end:   - IPv4: 212.227.123.25   - IPv6: 2001:8d8:fe:53::5cd:25 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **secondary_zone_create** | [**SecondaryZoneCreate**](../models/SecondaryZoneCreate.md)| zone |  |

### Return type

[**SecondaryZoneRead**](../models/SecondaryZoneRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **secondaryzones_put**
> SecondaryZoneRead secondaryzones_put(secondary_zone_id, secondary_zone_ensure)

Ensure a secondary zone

Ensures that a secondary zone with the provided ID is created or modified. In order to successfully update secondary zone - all JSON parameters must be passed.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **secondary_zone_id** | **str**| The ID (UUID) of the DNS zone. |  |
| **secondary_zone_ensure** | [**SecondaryZoneEnsure**](../models/SecondaryZoneEnsure.md)| update zone |  |

### Return type

[**SecondaryZoneRead**](../models/SecondaryZoneRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

