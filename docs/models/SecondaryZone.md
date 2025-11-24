# SecondaryZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_name** | **str** | The zone name | 
**description** | **str** | The hosted zone is used for... | [optional] 
**primary_ips** | **list[str]** | Indicates IP addresses of primary nameservers for a secondary zone. Accepts IPv4 and IPv6 addresses | 

## Example

```python
from ionoscloud_dns.models.secondary_zone import SecondaryZone

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryZone from a JSON string
secondary_zone_instance = SecondaryZone.from_json(json)
# print the JSON string representation of the object
print(SecondaryZone.to_json())

# convert the object into a dict
secondary_zone_dict = secondary_zone_instance.to_dict()
# create an instance of SecondaryZone from a dict
secondary_zone_from_dict = SecondaryZone.from_dict(secondary_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


