# SecondaryZoneRecordReadList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The resource&#39;s unique identifier. | [readonly] 
**type** | **str** |  | 
**href** | **str** |  | [readonly] 
**metadata** | [**SecondaryZoneRecordReadListMetadata**](SecondaryZoneRecordReadListMetadata.md) |  | 
**items** | [**list[SecondaryZoneRecordRead]**](SecondaryZoneRecordRead.md) |  | 
**offset** | **float** | Pagination offset. | [readonly] 
**limit** | **float** | Pagination limit. | [readonly] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from ionoscloud_dns.models.secondary_zone_record_read_list import SecondaryZoneRecordReadList

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryZoneRecordReadList from a JSON string
secondary_zone_record_read_list_instance = SecondaryZoneRecordReadList.from_json(json)
# print the JSON string representation of the object
print(SecondaryZoneRecordReadList.to_json())

# convert the object into a dict
secondary_zone_record_read_list_dict = secondary_zone_record_read_list_instance.to_dict()
# create an instance of SecondaryZoneRecordReadList from a dict
secondary_zone_record_read_list_from_dict = SecondaryZoneRecordReadList.from_dict(secondary_zone_record_read_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


