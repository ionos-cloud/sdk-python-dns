# Links

URLs to navigate the different pages. As of now we always only return a single page. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | **str** | URL (with offset and limit parameters) of the previous page; only present if offset is greater than 0.  | [optional] [readonly] 
**var_self** | **str** | URL (with offset and limit parameters) of the current page.  | [optional] [readonly] 
**next** | **str** | URL (with offset and limit parameters) of the next page; only present if offset + limit is less than the total number of elements.  | [optional] [readonly] 

## Example

```python
from ionoscloud_dns.models.links import Links

# TODO update the JSON string below
json = "{}"
# create an instance of Links from a JSON string
links_instance = Links.from_json(json)
# print the JSON string representation of the object
print(Links.to_json())

# convert the object into a dict
links_dict = links_instance.to_dict()
# create an instance of Links from a dict
links_from_dict = Links.from_dict(links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


