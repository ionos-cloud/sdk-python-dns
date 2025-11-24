# DnssecKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_tag** | **int** |  | [optional] 
**digest_algorithm_mnemonic** | **str** | A string that denotes the digest algorithm. This value must conform to the guidelines in [RFC-8624 Section 3.3](https://datatracker.ietf.org/doc/html/rfc8624#section-3.3).  | [optional] 
**digest** | **str** |  | [optional] 
**key_data** | [**KeyData**](KeyData.md) |  | [optional] 
**composed_key_data** | **str** | Represents the composed value of the The RDATA for a DNSKEY. The format should be the following: Flags | Protocol | Algorithm | Public Key The values must conform to the guidelines in [RFC-4034 Section 2.1](https://www.rfc-editor.org/rfc/rfc4034#section-2.1).  | [optional] 

## Example

```python
from ionoscloud_dns.models.dnssec_key import DnssecKey

# TODO update the JSON string below
json = "{}"
# create an instance of DnssecKey from a JSON string
dnssec_key_instance = DnssecKey.from_json(json)
# print the JSON string representation of the object
print(DnssecKey.to_json())

# convert the object into a dict
dnssec_key_dict = dnssec_key_instance.to_dict()
# create an instance of DnssecKey from a dict
dnssec_key_from_dict = DnssecKey.from_dict(dnssec_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


