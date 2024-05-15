# ZonesApi

All URIs are relative to *https://dns.de-fra.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**zones_delete**](ZonesApi.md#zones_delete) | **DELETE** /zones/{zoneId} | Delete a zone |
| [**zones_find_by_id**](ZonesApi.md#zones_find_by_id) | **GET** /zones/{zoneId} | Retrieve a zone |
| [**zones_get**](ZonesApi.md#zones_get) | **GET** /zones | Retrieve zones |
| [**zones_post**](ZonesApi.md#zones_post) | **POST** /zones | Create a zone |
| [**zones_put**](ZonesApi.md#zones_put) | **PUT** /zones/{zoneId} | Update a zone |


# **zones_delete**
> object zones_delete(zone_id)

Delete a zone

Deletes the specified zone and all of the records it contains.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **zone_id** | **str**| The ID (UUID) of the DNS zone. |  |

### Return type

**object**

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **zones_find_by_id**
> ZoneRead zones_find_by_id(zone_id)

Retrieve a zone

Returns a DNS zone by given ID.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **zone_id** | **str**| The ID (UUID) of the DNS zone. |  |

### Return type

[**ZoneRead**](../models/ZoneRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **zones_get**
> ZoneReadList zones_get(filter_state=filter_state, filter_zone_name=filter_zone_name, offset=offset, limit=limit)

Retrieve zones

Returns a list of the DNS zones for the customer. Default limit is the first 100 items. Use pagination query parameters for listing more items (up to 1000).

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **filter_state** | [**ProvisioningState**](../models/.md)| Filter used to fetch all zones in a particular state. | [optional]  |
| **filter_zone_name** | **str**| Filter used to fetch only the zones that contain the specified zone name. | [optional]  |
| **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100] |

### Return type

[**ZoneReadList**](../models/ZoneReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **zones_post**
> ZoneRead zones_post(zone_create)

Create a zone

Creates a new zone with default NS and SOA records.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **zone_create** | [**ZoneCreate**](../models/ZoneCreate.md)| zone |  |

### Return type

[**ZoneRead**](../models/ZoneRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **zones_put**
> ZoneRead zones_put(zone_id, zone_ensure)

Update a zone

Updates or creates a zone for the provided zone ID. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **zone_id** | **str**| The ID (UUID) of the DNS zone. |  |
| **zone_ensure** | [**ZoneEnsure**](../models/ZoneEnsure.md)| update zone |  |

### Return type

[**ZoneRead**](../models/ZoneRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

