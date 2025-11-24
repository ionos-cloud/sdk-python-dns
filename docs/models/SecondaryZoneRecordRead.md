# SecondaryZoneRecordRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**metadata** | [**MetadataForSecondaryZoneRecords**](MetadataForSecondaryZoneRecords.md) |  | 
**properties** | [**Record**](Record.md) |  | 

## Example

```python
from ionoscloud_dns.models.secondary_zone_record_read import SecondaryZoneRecordRead

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryZoneRecordRead from a JSON string
secondary_zone_record_read_instance = SecondaryZoneRecordRead.from_json(json)
# print the JSON string representation of the object
print(SecondaryZoneRecordRead.to_json())

# convert the object into a dict
secondary_zone_record_read_dict = secondary_zone_record_read_instance.to_dict()
# create an instance of SecondaryZoneRecordRead from a dict
secondary_zone_record_read_from_dict = SecondaryZoneRecordRead.from_dict(secondary_zone_record_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


