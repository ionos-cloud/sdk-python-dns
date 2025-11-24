# DnssecKeyReadList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**href** | **str** |  | [optional] [readonly] 
**metadata** | [**DnssecKeyReadListMetadata**](DnssecKeyReadListMetadata.md) |  | [optional] 
**properties** | [**DnssecKeyReadListProperties**](DnssecKeyReadListProperties.md) |  | [optional] 

## Example

```python
from ionoscloud_dns.models.dnssec_key_read_list import DnssecKeyReadList

# TODO update the JSON string below
json = "{}"
# create an instance of DnssecKeyReadList from a JSON string
dnssec_key_read_list_instance = DnssecKeyReadList.from_json(json)
# print the JSON string representation of the object
print(DnssecKeyReadList.to_json())

# convert the object into a dict
dnssec_key_read_list_dict = dnssec_key_read_list_instance.to_dict()
# create an instance of DnssecKeyReadList from a dict
dnssec_key_read_list_from_dict = DnssecKeyReadList.from_dict(dnssec_key_read_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


