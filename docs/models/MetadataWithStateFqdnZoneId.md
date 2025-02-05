# MetadataWithStateFqdnZoneId

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
| **fqdn** | **str** | A fully qualified domain name. FQDN consists of two parts - the hostname and the domain name. | [readonly]  |
| **zone_id** | **str** | The ID (UUID) of the DNS zone of which record belongs to. | [readonly]  |


