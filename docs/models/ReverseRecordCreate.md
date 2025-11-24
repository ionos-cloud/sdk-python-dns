# ReverseRecordCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**ReverseRecord**](ReverseRecord.md) |  | 

## Example

```python
from ionoscloud_dns.models.reverse_record_create import ReverseRecordCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseRecordCreate from a JSON string
reverse_record_create_instance = ReverseRecordCreate.from_json(json)
# print the JSON string representation of the object
print(ReverseRecordCreate.to_json())

# convert the object into a dict
reverse_record_create_dict = reverse_record_create_instance.to_dict()
# create an instance of ReverseRecordCreate from a dict
reverse_record_create_from_dict = ReverseRecordCreate.from_dict(reverse_record_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


