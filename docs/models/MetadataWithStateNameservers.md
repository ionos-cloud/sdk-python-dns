# MetadataWithStateNameservers

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **created_date** | **datetime** | The creation date formatted as yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;. | [optional] [readonly]  |
| **created_by** | **str** | Unique name of the identity that created the resource. | [optional] [readonly]  |
| **created_by_user_id** | **str** | The unique ID of the user who created the resource. | [optional] [readonly]  |
| **last_modified_date** | **datetime** | The date of the last change formatted as yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;. | [optional] [readonly]  |
| **last_modified_by** | **str** | Unique name of the identity that created the resource. | [optional] [readonly]  |
| **last_modified_by_user_id** | **str** | The unique ID of the user who last modified the resource. | [optional] [readonly]  |
| **resource_urn** | **str** | Unique name of the resource. | [optional] [readonly]  |
| **state** | [**ProvisioningState**](ProvisioningState.md) |  |  |
| **nameservers** | **list[str]** | The list of nameservers associated to the zone.  Nameservers are different for primary and secondary zones. For primary zones it would be: - ns-ic.ui-dns.com - ns-ic.ui-dns.de - ns-ic.ui-dns.org - ns-ic.ui-dns.biz  And for secondary zones: - nscs.ui-dns.com - nscs.ui-dns.de - nscs.ui-dns.org - nscs.ui-dns.biz  |  |


