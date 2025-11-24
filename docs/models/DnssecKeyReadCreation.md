# DnssecKeyReadCreation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**DnssecKeyParameters**](DnssecKeyParameters.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 
**href** | **str** |  | [readonly] 

## Example

```python
from ionoscloud_dns.models.dnssec_key_read_creation import DnssecKeyReadCreation

# TODO update the JSON string below
json = "{}"
# create an instance of DnssecKeyReadCreation from a JSON string
dnssec_key_read_creation_instance = DnssecKeyReadCreation.from_json(json)
# print the JSON string representation of the object
print(DnssecKeyReadCreation.to_json())

# convert the object into a dict
dnssec_key_read_creation_dict = dnssec_key_read_creation_instance.to_dict()
# create an instance of DnssecKeyReadCreation from a dict
dnssec_key_read_creation_from_dict = DnssecKeyReadCreation.from_dict(dnssec_key_read_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


