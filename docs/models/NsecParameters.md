# NsecParameters

Nsec parameters. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nsec_mode** | [**NsecMode**](NsecMode.md) |  | 
**nsec3_iterations** | **int** | Number of iterations for NSEC3. (between 0 and 50)  | 
**nsec3_salt_bits** | **int** | Salt length in bits for NSEC3. (between 64 and 128, multiples of 8)  | 

## Example

```python
from ionoscloud_dns.models.nsec_parameters import NsecParameters

# TODO update the JSON string below
json = "{}"
# create an instance of NsecParameters from a JSON string
nsec_parameters_instance = NsecParameters.from_json(json)
# print the JSON string representation of the object
print(NsecParameters.to_json())

# convert the object into a dict
nsec_parameters_dict = nsec_parameters_instance.to_dict()
# create an instance of NsecParameters from a dict
nsec_parameters_from_dict = NsecParameters.from_dict(nsec_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


