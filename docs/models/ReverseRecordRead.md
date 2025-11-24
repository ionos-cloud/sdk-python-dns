# ReverseRecordRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The reverse DNS record ID (UUID). | 
**type** | **str** |  | 
**href** | **str** |  | [readonly] 
**metadata** | [**Metadata**](Metadata.md) |  | 
**properties** | [**ReverseRecord**](ReverseRecord.md) |  | 

## Example

```python
from ionoscloud_dns.models.reverse_record_read import ReverseRecordRead

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseRecordRead from a JSON string
reverse_record_read_instance = ReverseRecordRead.from_json(json)
# print the JSON string representation of the object
print(ReverseRecordRead.to_json())

# convert the object into a dict
reverse_record_read_dict = reverse_record_read_instance.to_dict()
# create an instance of ReverseRecordRead from a dict
reverse_record_read_from_dict = ReverseRecordRead.from_dict(reverse_record_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


