# DnssecKeyReadListPropertiesKeyParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | [**Algorithm**](Algorithm.md) |  | [optional] 

## Example

```python
from ionoscloud_dns.models.dnssec_key_read_list_properties_key_parameters import DnssecKeyReadListPropertiesKeyParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DnssecKeyReadListPropertiesKeyParameters from a JSON string
dnssec_key_read_list_properties_key_parameters_instance = DnssecKeyReadListPropertiesKeyParameters.from_json(json)
# print the JSON string representation of the object
print(DnssecKeyReadListPropertiesKeyParameters.to_json())

# convert the object into a dict
dnssec_key_read_list_properties_key_parameters_dict = dnssec_key_read_list_properties_key_parameters_instance.to_dict()
# create an instance of DnssecKeyReadListPropertiesKeyParameters from a dict
dnssec_key_read_list_properties_key_parameters_from_dict = DnssecKeyReadListPropertiesKeyParameters.from_dict(dnssec_key_read_list_properties_key_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


