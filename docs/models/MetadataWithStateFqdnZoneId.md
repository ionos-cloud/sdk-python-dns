# MetadataWithStateFqdnZoneId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** | The creation date formatted as yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;. | [optional] [readonly] 
**created_by** | **str** | Unique name of the identity that created the resource. | [optional] [readonly] 
**created_by_user_id** | **str** | The unique ID of the user who created the resource. | [optional] [readonly] 
**last_modified_date** | **datetime** | The date of the last change formatted as yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;. | [optional] [readonly] 
**last_modified_by** | **str** | Unique name of the identity that created the resource. | [optional] [readonly] 
**last_modified_by_user_id** | **str** | The unique ID of the user who last modified the resource. | [optional] [readonly] 
**resource_urn** | **str** | Unique name of the resource. | [optional] [readonly] 
**state** | [**ProvisioningState**](ProvisioningState.md) |  | 
**fqdn** | **str** | A fully qualified domain name. FQDN consists of two parts - the hostname and the domain name. | [readonly] 
**zone_id** | **str** | The ID (UUID) of the DNS zone of which record belongs to. | [readonly] 

## Example

```python
from ionoscloud_dns.models.metadata_with_state_fqdn_zone_id import MetadataWithStateFqdnZoneId

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataWithStateFqdnZoneId from a JSON string
metadata_with_state_fqdn_zone_id_instance = MetadataWithStateFqdnZoneId.from_json(json)
# print the JSON string representation of the object
print(MetadataWithStateFqdnZoneId.to_json())

# convert the object into a dict
metadata_with_state_fqdn_zone_id_dict = metadata_with_state_fqdn_zone_id_instance.to_dict()
# create an instance of MetadataWithStateFqdnZoneId from a dict
metadata_with_state_fqdn_zone_id_from_dict = MetadataWithStateFqdnZoneId.from_dict(metadata_with_state_fqdn_zone_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


