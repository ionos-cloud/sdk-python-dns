# MetadataWithStateFqdnZoneId

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **last_modified_date** | **datetime** | The date of the last change formatted as yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;. | [optional] [readonly]  |
| **created_date** | **datetime** | The date of creation of the zone formatted as yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;. | [optional] [readonly]  |
| **state** | [**ProvisioningState**](ProvisioningState.md) |  |  |
| **fqdn** | **str** | A fully qualified domain name. FQDN consists of two parts - the hostname and the domain name. | [readonly]  |
| **zone_id** | **str** | The ID (UUID) of the DNS zone of which record belongs to. | [readonly]  |


