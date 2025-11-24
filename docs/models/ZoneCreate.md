# ZoneCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Zone**](Zone.md) |  | 

## Example

```python
from ionoscloud_dns.models.zone_create import ZoneCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneCreate from a JSON string
zone_create_instance = ZoneCreate.from_json(json)
# print the JSON string representation of the object
print(ZoneCreate.to_json())

# convert the object into a dict
zone_create_dict = zone_create_instance.to_dict()
# create an instance of ZoneCreate from a dict
zone_create_from_dict = ZoneCreate.from_dict(zone_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


