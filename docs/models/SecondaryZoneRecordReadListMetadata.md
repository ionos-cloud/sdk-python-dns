# SecondaryZoneRecordReadListMetadata

Shows the specific properties for secondary zones

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_ips** | **list[str]** | Indicates IP addresses of primary nameservers for a secondary zone. Accepts IPv4 and IPv6 addresses | 

## Example

```python
from ionoscloud_dns.models.secondary_zone_record_read_list_metadata import SecondaryZoneRecordReadListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryZoneRecordReadListMetadata from a JSON string
secondary_zone_record_read_list_metadata_instance = SecondaryZoneRecordReadListMetadata.from_json(json)
# print the JSON string representation of the object
print(SecondaryZoneRecordReadListMetadata.to_json())

# convert the object into a dict
secondary_zone_record_read_list_metadata_dict = secondary_zone_record_read_list_metadata_instance.to_dict()
# create an instance of SecondaryZoneRecordReadListMetadata from a dict
secondary_zone_record_read_list_metadata_from_dict = SecondaryZoneRecordReadListMetadata.from_dict(secondary_zone_record_read_list_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


