# KeyData

Represents the separate components of the RDATA for a DNSKEY. The values must conform to the guidelines in [RFC-4034 Section 2.1](https://www.rfc-editor.org/rfc/rfc4034#section-2.1). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | **int** | Represents the key&#39;s metadata and usage information. | [optional] 
**pub_key** | **str** | Represents the public key data in Base64 encoding. | [optional] 

## Example

```python
from ionoscloud_dns.models.key_data import KeyData

# TODO update the JSON string below
json = "{}"
# create an instance of KeyData from a JSON string
key_data_instance = KeyData.from_json(json)
# print the JSON string representation of the object
print(KeyData.to_json())

# convert the object into a dict
key_data_dict = key_data_instance.to_dict()
# create an instance of KeyData from a dict
key_data_from_dict = KeyData.from_dict(key_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


