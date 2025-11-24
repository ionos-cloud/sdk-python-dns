# CommonZone

Indicates the fields for a zone to be created

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_name** | **str** | The zone name | 
**description** | **str** | The hosted zone is used for... | [optional] 

## Example

```python
from ionoscloud_dns.models.common_zone import CommonZone

# TODO update the JSON string below
json = "{}"
# create an instance of CommonZone from a JSON string
common_zone_instance = CommonZone.from_json(json)
# print the JSON string representation of the object
print(CommonZone.to_json())

# convert the object into a dict
common_zone_dict = common_zone_instance.to_dict()
# create an instance of CommonZone from a dict
common_zone_from_dict = CommonZone.from_dict(common_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


