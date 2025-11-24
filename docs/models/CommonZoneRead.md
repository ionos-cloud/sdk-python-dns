# CommonZoneRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The zone ID (UUID). | 
**type** | **str** |  | 
**href** | **str** |  | [readonly] 
**metadata** | [**MetadataWithStateNameservers**](MetadataWithStateNameservers.md) |  | 

## Example

```python
from ionoscloud_dns.models.common_zone_read import CommonZoneRead

# TODO update the JSON string below
json = "{}"
# create an instance of CommonZoneRead from a JSON string
common_zone_read_instance = CommonZoneRead.from_json(json)
# print the JSON string representation of the object
print(CommonZoneRead.to_json())

# convert the object into a dict
common_zone_read_dict = common_zone_read_instance.to_dict()
# create an instance of CommonZoneRead from a dict
common_zone_read_from_dict = CommonZoneRead.from_dict(common_zone_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


