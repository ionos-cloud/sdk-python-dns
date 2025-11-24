# RecordCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Record**](Record.md) |  | 

## Example

```python
from ionoscloud_dns.models.record_create import RecordCreate

# TODO update the JSON string below
json = "{}"
# create an instance of RecordCreate from a JSON string
record_create_instance = RecordCreate.from_json(json)
# print the JSON string representation of the object
print(RecordCreate.to_json())

# convert the object into a dict
record_create_dict = record_create_instance.to_dict()
# create an instance of RecordCreate from a dict
record_create_from_dict = RecordCreate.from_dict(record_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


