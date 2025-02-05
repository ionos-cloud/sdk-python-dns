# Record

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **name** | **str** |  |  |
| **type** | [**RecordType**](RecordType.md) |  |  |
| **content** | **str** |  |  |
| **ttl** | **int** | Time to live for the record, recommended 3600. | [optional] [default to 3600] |
| **priority** | **int** | Priority value is between 0 and 65535. Priority is mandatory for MX, SRV and URI record types and ignored for all other types. | [optional]  |
| **enabled** | **bool** | When true - the record is visible for lookup. | [optional] [default to True] |


