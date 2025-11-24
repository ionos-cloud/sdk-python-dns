# SecondaryZoneReadList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID (UUID) created to identify this action. | 
**type** | **str** |  | 
**href** | **str** |  | [readonly] 
**offset** | **float** | Pagination offset. | [readonly] 
**limit** | **float** | Pagination limit. | [readonly] 
**links** | [**Links**](Links.md) |  | 
**items** | [**list[SecondaryZoneRead]**](SecondaryZoneRead.md) |  | 

## Example

```python
from ionoscloud_dns.models.secondary_zone_read_list import SecondaryZoneReadList

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryZoneReadList from a JSON string
secondary_zone_read_list_instance = SecondaryZoneReadList.from_json(json)
# print the JSON string representation of the object
print(SecondaryZoneReadList.to_json())

# convert the object into a dict
secondary_zone_read_list_dict = secondary_zone_read_list_instance.to_dict()
# create an instance of SecondaryZoneReadList from a dict
secondary_zone_read_list_from_dict = SecondaryZoneReadList.from_dict(secondary_zone_read_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


