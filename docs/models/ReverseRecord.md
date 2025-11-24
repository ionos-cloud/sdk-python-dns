# ReverseRecord

The reverse DNS record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The reverse DNS record name | 
**description** | **str** | Description stored along with the reverse DNS record to describe its usage. | [optional] 
**ip** | **str** | Specifies for which IP address the reverse record should be created. The IP addresses needs to be owned by the contract. Accepts IPv4 and IPv6 addresses. | 

## Example

```python
from ionoscloud_dns.models.reverse_record import ReverseRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseRecord from a JSON string
reverse_record_instance = ReverseRecord.from_json(json)
# print the JSON string representation of the object
print(ReverseRecord.to_json())

# convert the object into a dict
reverse_record_dict = reverse_record_instance.to_dict()
# create an instance of ReverseRecord from a dict
reverse_record_from_dict = ReverseRecord.from_dict(reverse_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


