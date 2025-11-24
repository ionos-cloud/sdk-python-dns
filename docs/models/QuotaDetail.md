# QuotaDetail

Count of zones and records. This schema is used to show both usage and defined limits (quota)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zones** | **int** | count of the number of zones | [default to 0]
**secondary_zones** | **int** | count of the number of secondary zones | [default to 0]
**records** | **int** | count of the number of records | [default to 0]
**reverse_records** | **int** | count of the number of reverse DNS records | [default to 0]

## Example

```python
from ionoscloud_dns.models.quota_detail import QuotaDetail

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaDetail from a JSON string
quota_detail_instance = QuotaDetail.from_json(json)
# print the JSON string representation of the object
print(QuotaDetail.to_json())

# convert the object into a dict
quota_detail_dict = quota_detail_instance.to_dict()
# create an instance of QuotaDetail from a dict
quota_detail_from_dict = QuotaDetail.from_dict(quota_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


