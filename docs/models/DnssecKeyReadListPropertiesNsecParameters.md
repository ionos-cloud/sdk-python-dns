# DnssecKeyReadListPropertiesNsecParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nsec_mode** | [**NsecMode**](NsecMode.md) |  | [optional] 

## Example

```python
from ionoscloud_dns.models.dnssec_key_read_list_properties_nsec_parameters import DnssecKeyReadListPropertiesNsecParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DnssecKeyReadListPropertiesNsecParameters from a JSON string
dnssec_key_read_list_properties_nsec_parameters_instance = DnssecKeyReadListPropertiesNsecParameters.from_json(json)
# print the JSON string representation of the object
print(DnssecKeyReadListPropertiesNsecParameters.to_json())

# convert the object into a dict
dnssec_key_read_list_properties_nsec_parameters_dict = dnssec_key_read_list_properties_nsec_parameters_instance.to_dict()
# create an instance of DnssecKeyReadListPropertiesNsecParameters from a dict
dnssec_key_read_list_properties_nsec_parameters_from_dict = DnssecKeyReadListPropertiesNsecParameters.from_dict(dnssec_key_read_list_properties_nsec_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


