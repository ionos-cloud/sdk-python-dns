# DnssecKeyReadListProperties

Properties of the key. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_parameters** | [**DnssecKeyReadListPropertiesKeyParameters**](DnssecKeyReadListPropertiesKeyParameters.md) |  | 
**nsec_parameters** | [**DnssecKeyReadListPropertiesNsecParameters**](DnssecKeyReadListPropertiesNsecParameters.md) |  | 

## Example

```python
from ionoscloud_dns.models.dnssec_key_read_list_properties import DnssecKeyReadListProperties

# TODO update the JSON string below
json = "{}"
# create an instance of DnssecKeyReadListProperties from a JSON string
dnssec_key_read_list_properties_instance = DnssecKeyReadListProperties.from_json(json)
# print the JSON string representation of the object
print(DnssecKeyReadListProperties.to_json())

# convert the object into a dict
dnssec_key_read_list_properties_dict = dnssec_key_read_list_properties_instance.to_dict()
# create an instance of DnssecKeyReadListProperties from a dict
dnssec_key_read_list_properties_from_dict = DnssecKeyReadListProperties.from_dict(dnssec_key_read_list_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


