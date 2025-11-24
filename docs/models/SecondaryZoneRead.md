# SecondaryZoneRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The zone ID (UUID). | 
**type** | **str** |  | 
**href** | **str** |  | [readonly] 
**metadata** | [**MetadataWithStateNameservers**](MetadataWithStateNameservers.md) |  | 
**properties** | [**SecondaryZone**](SecondaryZone.md) |  | 

## Example

```python
from ionoscloud_dns.models.secondary_zone_read import SecondaryZoneRead

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryZoneRead from a JSON string
secondary_zone_read_instance = SecondaryZoneRead.from_json(json)
# print the JSON string representation of the object
print(SecondaryZoneRead.to_json())

# convert the object into a dict
secondary_zone_read_dict = secondary_zone_read_instance.to_dict()
# create an instance of SecondaryZoneRead from a dict
secondary_zone_read_from_dict = SecondaryZoneRead.from_dict(secondary_zone_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


