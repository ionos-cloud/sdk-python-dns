# ZoneRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The zone ID (UUID). | 
**type** | **str** |  | 
**href** | **str** |  | [readonly] 
**metadata** | [**MetadataWithStateNameservers**](MetadataWithStateNameservers.md) |  | 
**properties** | [**Zone**](Zone.md) |  | 

## Example

```python
from ionoscloud_dns.models.zone_read import ZoneRead

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneRead from a JSON string
zone_read_instance = ZoneRead.from_json(json)
# print the JSON string representation of the object
print(ZoneRead.to_json())

# convert the object into a dict
zone_read_dict = zone_read_instance.to_dict()
# create an instance of ZoneRead from a dict
zone_read_from_dict = ZoneRead.from_dict(zone_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


