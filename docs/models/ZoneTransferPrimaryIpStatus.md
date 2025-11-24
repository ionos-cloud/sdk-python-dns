# ZoneTransferPrimaryIpStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_ip** | **str** | one single IP from the primaryIps field for secondary zones | 
**status** | **str** | Human readable status of the zone transfer status for the IP | 
**error_message** | **str** | Human readable explanation of the error when status is not ok | [optional] 

## Example

```python
from ionoscloud_dns.models.zone_transfer_primary_ip_status import ZoneTransferPrimaryIpStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneTransferPrimaryIpStatus from a JSON string
zone_transfer_primary_ip_status_instance = ZoneTransferPrimaryIpStatus.from_json(json)
# print the JSON string representation of the object
print(ZoneTransferPrimaryIpStatus.to_json())

# convert the object into a dict
zone_transfer_primary_ip_status_dict = zone_transfer_primary_ip_status_instance.to_dict()
# create an instance of ZoneTransferPrimaryIpStatus from a dict
zone_transfer_primary_ip_status_from_dict = ZoneTransferPrimaryIpStatus.from_dict(zone_transfer_primary_ip_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


