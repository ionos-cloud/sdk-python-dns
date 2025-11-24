# RecordReadList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [readonly] 
**type** | **str** |  | 
**href** | **str** |  | [readonly] 
**items** | [**list[RecordRead]**](RecordRead.md) |  | 
**offset** | **float** | Pagination offset. | [readonly] 
**limit** | **float** | Pagination limit. | [readonly] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from ionoscloud_dns.models.record_read_list import RecordReadList

# TODO update the JSON string below
json = "{}"
# create an instance of RecordReadList from a JSON string
record_read_list_instance = RecordReadList.from_json(json)
# print the JSON string representation of the object
print(RecordReadList.to_json())

# convert the object into a dict
record_read_list_dict = record_read_list_instance.to_dict()
# create an instance of RecordReadList from a dict
record_read_list_from_dict = RecordReadList.from_dict(record_read_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


