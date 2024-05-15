# ReverseRecordsApi

All URIs are relative to *https://dns.de-fra.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**reverserecords_delete**](ReverseRecordsApi.md#reverserecords_delete) | **DELETE** /reverserecords/{reverserecordId} | Delete a reverse DNS record |
| [**reverserecords_find_by_id**](ReverseRecordsApi.md#reverserecords_find_by_id) | **GET** /reverserecords/{reverserecordId} | Retrieve a reverse DNS record |
| [**reverserecords_get**](ReverseRecordsApi.md#reverserecords_get) | **GET** /reverserecords | Retrieves existing reverse DNS records |
| [**reverserecords_post**](ReverseRecordsApi.md#reverserecords_post) | **POST** /reverserecords | Create a reverse DNS record |
| [**reverserecords_put**](ReverseRecordsApi.md#reverserecords_put) | **PUT** /reverserecords/{reverserecordId} | Update a reverse DNS record |


# **reverserecords_delete**
> object reverserecords_delete(reverserecord_id)

Delete a reverse DNS record

Deletes a reverse DNS record. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **reverserecord_id** | **str**| The ID (UUID) of the reverse DNS record. |  |

### Return type

**object**

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **reverserecords_find_by_id**
> ReverseRecordRead reverserecords_find_by_id(reverserecord_id)

Retrieve a reverse DNS record

Returns the record with the specified record ID.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **reverserecord_id** | **str**| The ID (UUID) of the reverse DNS record. |  |

### Return type

[**ReverseRecordRead**](../models/ReverseRecordRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **reverserecords_get**
> ReverseRecordsReadList reverserecords_get(filter_record_ip=filter_record_ip, offset=offset, limit=limit)

Retrieves existing reverse DNS records

Returns a list of the reverse records of the customer. Default limit is the first 100 items. Use pagination query parameters to list more items.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **filter_record_ip** | [**list[str]**](../models/str.md)| Filter is used to fetch only the reverse records for the specified IPs. It&#39;s an array of IP records. IP can be any valid IPv4 or IPv6 address. Parameter has to be sent in query as many times as values (filter.recordIp&#x3D;1.2.3.4&amp;filter.recordIp&#x3D;2.3.4.5)  | [optional]  |
| **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100] |

### Return type

[**ReverseRecordsReadList**](../models/ReverseRecordsReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **reverserecords_post**
> ReverseRecordRead reverserecords_post(reverse_record_create)

Create a reverse DNS record

Creates a new reverse DNS record. Reverse DNS is applicable to IPv4 addresses within IP Blocks and IPv6 addresses of the VDC. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **reverse_record_create** | [**ReverseRecordCreate**](../models/ReverseRecordCreate.md)| reverserecord |  |

### Return type

[**ReverseRecordRead**](../models/ReverseRecordRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **reverserecords_put**
> ReverseRecordRead reverserecords_put(reverserecord_id, reverse_record_ensure)

Update a reverse DNS record

Updates or creates a reverse DNS record for the provided reverse DNS record ID. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **reverserecord_id** | **str**| The ID (UUID) of the reverse DNS record. |  |
| **reverse_record_ensure** | [**ReverseRecordEnsure**](../models/ReverseRecordEnsure.md)|  |  |

### Return type

[**ReverseRecordRead**](../models/ReverseRecordRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

