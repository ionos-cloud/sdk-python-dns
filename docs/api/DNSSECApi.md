# DNSSECApi

All URIs are relative to *https://dns.de-fra.ionos.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**zones_keys_delete**](DNSSECApi.md#zones_keys_delete) | **DELETE** /zones/{zoneId}/keys | Delete a DNSSEC key |
| [**zones_keys_get**](DNSSECApi.md#zones_keys_get) | **GET** /zones/{zoneId}/keys | Retrieve a DNSSEC key |
| [**zones_keys_post**](DNSSECApi.md#zones_keys_post) | **POST** /zones/{zoneId}/keys | Create a DNSSEC key |


# **zones_keys_delete**
> object zones_keys_delete(zone_id)

Delete a DNSSEC key

Disable DNSSEC keys and remove associated DNSKEY records for your DNS zone. 

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

# **zones_keys_get**
> DnssecKeyReadList zones_keys_get(zone_id)

Retrieve a DNSSEC key

Get DNSSEC keys for your DNS zone.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **zone_id** | **str**| The ID (UUID) of the DNS zone. |  |

### Return type

[**DnssecKeyReadList**](../models/DnssecKeyReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **zones_keys_post**
> DnssecKeyReadCreation zones_keys_post(zone_id, dnssec_key_create)

Create a DNSSEC key

Enable DNSSEC keys and create associated DNSKEY records for your DNS zone. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **zone_id** | **str**| The ID (UUID) of the DNS zone. |  |
| **dnssec_key_create** | [**DnssecKeyCreate**](../models/DnssecKeyCreate.md)| Enable DNSSEC request. |  |

### Return type

[**DnssecKeyReadCreation**](../models/DnssecKeyReadCreation.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

