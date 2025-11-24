# ZoneTransferPrimaryIpsStatus

Indicates, for secondary zones, the transfer status for each one single IP defined on primaryIps field 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**items** | [**list[ZoneTransferPrimaryIpStatus]**](ZoneTransferPrimaryIpStatus.md) |  | 

## Example

```python
from ionoscloud_dns.models.zone_transfer_primary_ips_status import ZoneTransferPrimaryIpsStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneTransferPrimaryIpsStatus from a JSON string
zone_transfer_primary_ips_status_instance = ZoneTransferPrimaryIpsStatus.from_json(json)
# print the JSON string representation of the object
print(ZoneTransferPrimaryIpsStatus.to_json())

# convert the object into a dict
zone_transfer_primary_ips_status_dict = zone_transfer_primary_ips_status_instance.to_dict()
# create an instance of ZoneTransferPrimaryIpsStatus from a dict
zone_transfer_primary_ips_status_from_dict = ZoneTransferPrimaryIpsStatus.from_dict(zone_transfer_primary_ips_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


