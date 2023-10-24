# MetadataWithStateNameserversAllOf

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **state** | [**ProvisioningState**](ProvisioningState.md) |  |  |
| **nameservers** | **list[str]** | The list of nameservers associated to the zone.  Nameservers are different for primary and secondary zones. For primary zones it would be: - ns-ic.ui-dns.com - ns-ic.ui-dns.de - ns-ic.ui-dns.org - ns-ic.ui-dns.biz  And for secondary zones: - nscs.ui-dns.com - nscs.ui-dns.de - nscs.ui-dns.org - nscs.ui-dns.biz  |  |


