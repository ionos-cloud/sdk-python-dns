# KeyData

Represents the separate components of the RDATA for a DNSKEY. The values must conform to the guidelines in [RFC-4034 Section 2.1](https://www.rfc-editor.org/rfc/rfc4034#section-2.1). 
## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **flags** | **int** | Represents the key&#39;s metadata and usage information. | [optional]  |
| **pub_key** | **str** | Represents the public key data in Base64 encoding. | [optional]  |


