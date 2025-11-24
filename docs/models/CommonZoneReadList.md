# CommonZoneReadList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID (UUID) created to identify this action. | 
**type** | **str** |  | 
**href** | **str** |  | [readonly] 
**offset** | **float** | Pagination offset. | [readonly] 
**limit** | **float** | Pagination limit. | [readonly] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from ionoscloud_dns.models.common_zone_read_list import CommonZoneReadList

# TODO update the JSON string below
json = "{}"
# create an instance of CommonZoneReadList from a JSON string
common_zone_read_list_instance = CommonZoneReadList.from_json(json)
# print the JSON string representation of the object
print(CommonZoneReadList.to_json())

# convert the object into a dict
common_zone_read_list_dict = common_zone_read_list_instance.to_dict()
# create an instance of CommonZoneReadList from a dict
common_zone_read_list_from_dict = CommonZoneReadList.from_dict(common_zone_read_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


