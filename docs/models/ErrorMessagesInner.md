# ErrorMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** | Internal error code.  | [optional] 
**message** | **str** | Human readable explanation of the issue.  | [optional] 

## Example

```python
from ionoscloud_dns.models.error_messages_inner import ErrorMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorMessagesInner from a JSON string
error_messages_inner_instance = ErrorMessagesInner.from_json(json)
# print the JSON string representation of the object
print(ErrorMessagesInner.to_json())

# convert the object into a dict
error_messages_inner_dict = error_messages_inner_instance.to_dict()
# create an instance of ErrorMessagesInner from a dict
error_messages_inner_from_dict = ErrorMessagesInner.from_dict(error_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


