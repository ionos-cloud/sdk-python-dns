# DnssecKeyReadListMetadata

Metadata of the resource with not state information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_id** | **str** | The ID (UUID) of the DNS zone of which record belongs to. | [optional] [readonly] 
**items** | [**list[DnssecKey]**](DnssecKey.md) |  | [optional] 

## Example

```python
from ionoscloud_dns.models.dnssec_key_read_list_metadata import DnssecKeyReadListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DnssecKeyReadListMetadata from a JSON string
dnssec_key_read_list_metadata_instance = DnssecKeyReadListMetadata.from_json(json)
# print the JSON string representation of the object
print(DnssecKeyReadListMetadata.to_json())

# convert the object into a dict
dnssec_key_read_list_metadata_dict = dnssec_key_read_list_metadata_instance.to_dict()
# create an instance of DnssecKeyReadListMetadata from a dict
dnssec_key_read_list_metadata_from_dict = DnssecKeyReadListMetadata.from_dict(dnssec_key_read_list_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


