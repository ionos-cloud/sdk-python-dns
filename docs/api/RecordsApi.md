# RecordsApi

All URIs are relative to *https://dns.de-fra.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**records_get**](RecordsApi.md#records_get) | **GET** /records | Retrieve all records from primary zones |
| [**secondaryzones_records_get**](RecordsApi.md#secondaryzones_records_get) | **GET** /secondaryzones/{secondaryZoneId}/records | Retrieve records for a secondary zone |
| [**zones_records_delete**](RecordsApi.md#zones_records_delete) | **DELETE** /zones/{zoneId}/records/{recordId} | Delete a record |
| [**zones_records_find_by_id**](RecordsApi.md#zones_records_find_by_id) | **GET** /zones/{zoneId}/records/{recordId} | Retrieve a record |
| [**zones_records_get**](RecordsApi.md#zones_records_get) | **GET** /zones/{zoneId}/records | Retrieve records |
| [**zones_records_post**](RecordsApi.md#zones_records_post) | **POST** /zones/{zoneId}/records | Create a record |
| [**zones_records_put**](RecordsApi.md#zones_records_put) | **PUT** /zones/{zoneId}/records/{recordId} | Update a record |


# **records_get**
> RecordReadList records_get(filter_zone_id=filter_zone_id, filter_name=filter_name, filter_state=filter_state, filter_type=filter_type, offset=offset, limit=limit)

Retrieve all records from primary zones

Returns the list of all records for all customer DNS zones with the possibility to filter them.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **filter_zone_id** | **str**| Filter used to fetch only the records that contain specified zoneId. | [optional]  |
| **filter_name** | **str**| Filter used to fetch only the records that contain specified record name. | [optional]  |
| **filter_state** | [**ProvisioningState**](../models/.md)| Filter used to fetch only the records that are in certain state. | [optional]  |
| **filter_type** | [**RecordType**](../models/.md)| Filter used to fetch only the records with specified type. | [optional]  |
| **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100] |

### Return type

[**RecordReadList**](../models/RecordReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **secondaryzones_records_get**
> SecondaryZoneRecordReadList secondaryzones_records_get(secondary_zone_id, offset=offset, limit=limit)

Retrieve records for a secondary zone

Returns the list of records for a secondary zone. Those are the records created for its primary IPs

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **secondary_zone_id** | **str**| The ID (UUID) of the DNS secondary zone. |  |
| **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100] |

### Return type

[**SecondaryZoneRecordReadList**](../models/SecondaryZoneRecordReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **zones_records_delete**
> object zones_records_delete(zone_id, record_id)

Delete a record

Deletes a specified record from the DNS zone.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **zone_id** | **str**| The ID (UUID) of the DNS zone. |  |
| **record_id** | **str**| The ID (UUID) of the record. |  |

### Return type

**object**

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **zones_records_find_by_id**
> RecordRead zones_records_find_by_id(zone_id, record_id)

Retrieve a record

Returns the record with the specified record ID.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **zone_id** | **str**| The ID (UUID) of the DNS zone. |  |
| **record_id** | **str**| The ID (UUID) of the record. |  |

### Return type

[**RecordRead**](../models/RecordRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **zones_records_get**
> RecordReadList zones_records_get(zone_id)

Retrieve records

Returns the list of records for the specific DNS zone.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **zone_id** | **str**| The ID (UUID) of the DNS zone. |  |

### Return type

[**RecordReadList**](../models/RecordReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **zones_records_post**
> RecordRead zones_records_post(zone_id, record_create)

Create a record

Creates a new record for the DNS zone.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **zone_id** | **str**| The ID (UUID) of the DNS zone. |  |
| **record_create** | [**RecordCreate**](../models/RecordCreate.md)| record |  |

### Return type

[**RecordRead**](../models/RecordRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **zones_records_put**
> RecordRead zones_records_put(zone_id, record_id, record_ensure)

Update a record

Updates or creates a DNS record for the provided record ID.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **zone_id** | **str**| The ID (UUID) of the DNS zone. |  |
| **record_id** | **str**| The ID (UUID) of the DNS record. |  |
| **record_ensure** | [**RecordEnsure**](../models/RecordEnsure.md)|  |  |

### Return type

[**RecordRead**](../models/RecordRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

