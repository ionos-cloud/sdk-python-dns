# KeyParameters

Key parameters used to sign the zone. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | [**Algorithm**](Algorithm.md) |  | 
**ksk_bits** | [**KskBits**](KskBits.md) |  | 
**zsk_bits** | [**ZskBits**](ZskBits.md) |  | 

## Example

```python
from ionoscloud_dns.models.key_parameters import KeyParameters

# TODO update the JSON string below
json = "{}"
# create an instance of KeyParameters from a JSON string
key_parameters_instance = KeyParameters.from_json(json)
# print the JSON string representation of the object
print(KeyParameters.to_json())

# convert the object into a dict
key_parameters_dict = key_parameters_instance.to_dict()
# create an instance of KeyParameters from a dict
key_parameters_from_dict = KeyParameters.from_dict(key_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


