# ReverseRecordsReadList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID (UUID) created to identify this action. | 
**type** | **str** |  | 
**href** | **str** |  | [readonly] 
**items** | [**list[ReverseRecordRead]**](ReverseRecordRead.md) |  | 
**offset** | **float** | Pagination offset. | [readonly] 
**limit** | **float** | Pagination limit. | [readonly] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from ionoscloud_dns.models.reverse_records_read_list import ReverseRecordsReadList

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseRecordsReadList from a JSON string
reverse_records_read_list_instance = ReverseRecordsReadList.from_json(json)
# print the JSON string representation of the object
print(ReverseRecordsReadList.to_json())

# convert the object into a dict
reverse_records_read_list_dict = reverse_records_read_list_instance.to_dict()
# create an instance of ReverseRecordsReadList from a dict
reverse_records_read_list_from_dict = ReverseRecordsReadList.from_dict(reverse_records_read_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


