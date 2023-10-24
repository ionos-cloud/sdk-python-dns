# MetadataWithStateNameservers

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **last_modified_date** | **datetime** | The date of the last change formatted as yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;. | [optional] [readonly]  |
| **created_date** | **datetime** | The date of creation of the zone formatted as yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;. | [optional] [readonly]  |
| **state** | [**ProvisioningState**](ProvisioningState.md) |  |  |
| **nameservers** | **list[str]** | The list of nameservers associated to the zone.  Nameservers are different for primary and secondary zones. For primary zones it would be: - ns-ic.ui-dns.com - ns-ic.ui-dns.de - ns-ic.ui-dns.org - ns-ic.ui-dns.biz  And for secondary zones: - nscs.ui-dns.com - nscs.ui-dns.de - nscs.ui-dns.org - nscs.ui-dns.biz  |  |


