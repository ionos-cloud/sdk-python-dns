# Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_status** | **int** | HTTP status code of the operation as specified by [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#section-6).  | [optional] 
**messages** | [**list[ErrorMessagesInner]**](ErrorMessagesInner.md) |  | [optional] 

## Example

```python
from ionoscloud_dns.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


