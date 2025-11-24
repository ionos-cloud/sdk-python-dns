# SecondaryZoneCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**SecondaryZone**](SecondaryZone.md) |  | 

## Example

```python
from ionoscloud_dns.models.secondary_zone_create import SecondaryZoneCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryZoneCreate from a JSON string
secondary_zone_create_instance = SecondaryZoneCreate.from_json(json)
# print the JSON string representation of the object
print(SecondaryZoneCreate.to_json())

# convert the object into a dict
secondary_zone_create_dict = secondary_zone_create_instance.to_dict()
# create an instance of SecondaryZoneCreate from a dict
secondary_zone_create_from_dict = SecondaryZoneCreate.from_dict(secondary_zone_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


