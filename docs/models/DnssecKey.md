# DnssecKey

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **key_tag** | **int** |  | [optional]  |
| **sign_algorithm_mnemonic** | **str** | A string that denotes the signing algorithm. This value must conform to the guidelines in [RFC-8624 Section 3.1](https://datatracker.ietf.org/doc/html/rfc8624#section-3.1).  | [optional]  |
| **sign_algorithm_number** | **int** | An integer that denotes the signing algorithm. This value must conform to the guidelines in [RFC-8624 Section 3.1](https://datatracker.ietf.org/doc/html/rfc8624#section-3.1).  | [optional]  |
| **digest_algorithm_mnemonic** | **str** | A string that denotes the digest algorithm. This value must conform to the guidelines in [RFC-8624 Section 3.3](https://datatracker.ietf.org/doc/html/rfc8624#section-3.3).  | [optional]  |
| **digest_algorithm_number** | **int** | An integer that denotes the digest algorithm. This value must conform to the guidelines in [RFC-8624 Section 3.3](https://datatracker.ietf.org/doc/html/rfc8624#section-3.3).  | [optional]  |
| **digest** | **str** |  | [optional]  |
| **key_data** | [**KeyData**](KeyData.md) |  | [optional]  |
| **composed_key_data** | **str** | Represents the composed value of the The RDATA for a DNSKEY. The format should be the following: Flags | Protocol | Algorithm | Public Key The values must conform to the guidelines in [RFC-4034 Section 2.1](https://www.rfc-editor.org/rfc/rfc4034#section-2.1).  | [optional]  |


