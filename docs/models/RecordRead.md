# RecordRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The record ID (UUID). | [readonly] 
**type** | **str** |  | 
**href** | **str** |  | [readonly] 
**metadata** | [**MetadataWithStateFqdnZoneId**](MetadataWithStateFqdnZoneId.md) |  | 
**properties** | [**Record**](Record.md) |  | 

## Example

```python
from ionoscloud_dns.models.record_read import RecordRead

# TODO update the JSON string below
json = "{}"
# create an instance of RecordRead from a JSON string
record_read_instance = RecordRead.from_json(json)
# print the JSON string representation of the object
print(RecordRead.to_json())

# convert the object into a dict
record_read_dict = record_read_instance.to_dict()
# create an instance of RecordRead from a dict
record_read_from_dict = RecordRead.from_dict(record_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


