# DnssecKeyCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**DnssecKeyParameters**](DnssecKeyParameters.md) |  | 

## Example

```python
from ionoscloud_dns.models.dnssec_key_create import DnssecKeyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DnssecKeyCreate from a JSON string
dnssec_key_create_instance = DnssecKeyCreate.from_json(json)
# print the JSON string representation of the object
print(DnssecKeyCreate.to_json())

# convert the object into a dict
dnssec_key_create_dict = dnssec_key_create_instance.to_dict()
# create an instance of DnssecKeyCreate from a dict
dnssec_key_create_from_dict = DnssecKeyCreate.from_dict(dnssec_key_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


