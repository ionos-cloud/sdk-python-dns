# MetadataForSecondaryZoneRecords

Metadata for records of secondary zones.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | A fully qualified domain name. FQDN consists of two parts - the hostname and the domain name. | [readonly] 
**zone_id** | **str** | The ID (UUID) of the DNS zone of which record belongs to. | [readonly] 
**root_name** | **str** | Indicates the root name (from the primary zone) for the record | 

## Example

```python
from ionoscloud_dns.models.metadata_for_secondary_zone_records import MetadataForSecondaryZoneRecords

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataForSecondaryZoneRecords from a JSON string
metadata_for_secondary_zone_records_instance = MetadataForSecondaryZoneRecords.from_json(json)
# print the JSON string representation of the object
print(MetadataForSecondaryZoneRecords.to_json())

# convert the object into a dict
metadata_for_secondary_zone_records_dict = metadata_for_secondary_zone_records_instance.to_dict()
# create an instance of MetadataForSecondaryZoneRecords from a dict
metadata_for_secondary_zone_records_from_dict = MetadataForSecondaryZoneRecords.from_dict(metadata_for_secondary_zone_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


