# Record


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | [**RecordType**](RecordType.md) |  | 
**content** | **str** |  | 
**ttl** | **int** | Time to live for the record, recommended 3600. | [optional] [default to 3600]
**priority** | **int** | Priority value is between 0 and 65535. Priority is mandatory for MX, SRV and URI record types and ignored for all other types. | [optional] 
**enabled** | **bool** | When true - the record is visible for lookup. | [optional] [default to True]

## Example

```python
from ionoscloud_dns.models.record import Record

# TODO update the JSON string below
json = "{}"
# create an instance of Record from a JSON string
record_instance = Record.from_json(json)
# print the JSON string representation of the object
print(Record.to_json())

# convert the object into a dict
record_dict = record_instance.to_dict()
# create an instance of Record from a dict
record_from_dict = Record.from_dict(record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


