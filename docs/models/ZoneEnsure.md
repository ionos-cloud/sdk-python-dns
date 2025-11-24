# ZoneEnsure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**Zone**](Zone.md) |  | 

## Example

```python
from ionoscloud_dns.models.zone_ensure import ZoneEnsure

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneEnsure from a JSON string
zone_ensure_instance = ZoneEnsure.from_json(json)
# print the JSON string representation of the object
print(ZoneEnsure.to_json())

# convert the object into a dict
zone_ensure_dict = zone_ensure_instance.to_dict()
# create an instance of ZoneEnsure from a dict
zone_ensure_from_dict = ZoneEnsure.from_dict(zone_ensure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


