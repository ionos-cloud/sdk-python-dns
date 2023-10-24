# ZoneFilesApi

All URIs are relative to *https://dns.de-fra.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**zones_zonefile_get**](ZoneFilesApi.md#zones_zonefile_get) | **GET** /zones/{zoneId}/zonefile | Retrieve a zone file |
| [**zones_zonefile_put**](ZoneFilesApi.md#zones_zonefile_put) | **PUT** /zones/{zoneId}/zonefile | Updates a zone with a file |


# **zones_zonefile_get**
> zones_zonefile_get(zone_id)

Retrieve a zone file

Returns an exported zone file in BIND format (RFC 1035).

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **zone_id** | **str**| The ID (UUID) of the DNS zone. |  |

### Return type

void (empty response body)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

# **zones_zonefile_put**
> RecordReadList zones_zonefile_put(zone_id, body)

Updates a zone with a file

Updates a zone with zone file in BIND format (RFC 1035). All records in the zone are replaced with the ones provided.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **zone_id** | **str**| The ID (UUID) of the DNS zone. |  |
| **body** | **str**| Zone file in BIND format (RFC 1035). In order to support import files from other sources, the bind zone file can contain SOA and NS records, but these records will be ignored. |  |

### Return type

[**RecordReadList**](../models/RecordReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

