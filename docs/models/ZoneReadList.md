# ZoneReadList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID (UUID) created to identify this action. | 
**type** | **str** |  | 
**href** | **str** |  | [readonly] 
**offset** | **float** | Pagination offset. | [readonly] 
**limit** | **float** | Pagination limit. | [readonly] 
**links** | [**Links**](Links.md) |  | 
**items** | [**list[ZoneRead]**](ZoneRead.md) |  | 

## Example

```python
from ionoscloud_dns.models.zone_read_list import ZoneReadList

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneReadList from a JSON string
zone_read_list_instance = ZoneReadList.from_json(json)
# print the JSON string representation of the object
print(ZoneReadList.to_json())

# convert the object into a dict
zone_read_list_dict = zone_read_list_instance.to_dict()
# create an instance of ZoneReadList from a dict
zone_read_list_from_dict = ZoneReadList.from_dict(zone_read_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


