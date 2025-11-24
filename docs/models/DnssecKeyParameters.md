# DnssecKeyParameters

Parameters used to sign zone. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_parameters** | [**KeyParameters**](KeyParameters.md) |  | 
**nsec_parameters** | [**NsecParameters**](NsecParameters.md) |  | 
**validity** | **int** | Signature validity in days  | 

## Example

```python
from ionoscloud_dns.models.dnssec_key_parameters import DnssecKeyParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DnssecKeyParameters from a JSON string
dnssec_key_parameters_instance = DnssecKeyParameters.from_json(json)
# print the JSON string representation of the object
print(DnssecKeyParameters.to_json())

# convert the object into a dict
dnssec_key_parameters_dict = dnssec_key_parameters_instance.to_dict()
# create an instance of DnssecKeyParameters from a dict
dnssec_key_parameters_from_dict = DnssecKeyParameters.from_dict(dnssec_key_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


