# MetadataWithStateNameservers


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
**nameservers** | **list[str]** | The list of nameservers associated to the zone.  Nameservers are different for primary and secondary zones. For primary zones it would be: - ns-ic.ui-dns.com - ns-ic.ui-dns.de - ns-ic.ui-dns.org - ns-ic.ui-dns.biz  And for secondary zones: - nscs.ui-dns.com - nscs.ui-dns.de - nscs.ui-dns.org - nscs.ui-dns.biz  | 

## Example

```python
from ionoscloud_dns.models.metadata_with_state_nameservers import MetadataWithStateNameservers

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataWithStateNameservers from a JSON string
metadata_with_state_nameservers_instance = MetadataWithStateNameservers.from_json(json)
# print the JSON string representation of the object
print(MetadataWithStateNameservers.to_json())

# convert the object into a dict
metadata_with_state_nameservers_dict = metadata_with_state_nameservers_instance.to_dict()
# create an instance of MetadataWithStateNameservers from a dict
metadata_with_state_nameservers_from_dict = MetadataWithStateNameservers.from_dict(metadata_with_state_nameservers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


