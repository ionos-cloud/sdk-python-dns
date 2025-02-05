[![Gitter](https://img.shields.io/gitter/room/ionos-cloud/sdk-general)](https://gitter.im/ionos-cloud/sdk-general)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-dns&metric=alert_status)](https://sonarcloud.io/summary?id=sdk-python-dns)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-dns&metric=bugs)](https://sonarcloud.io/summary/new_code?id=sdk-python-dns)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-dns&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=sdk-python-dns)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-dns&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=sdk-python-dns)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-dns&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=sdk-python-dns)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=sdk-python-dns&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=sdk-python-dns)
[![Release](https://img.shields.io/github/v/release/ionos-cloud/sdk-python-dns.svg)](https://github.com/ionos-cloud/sdk-python-dns/releases/latest)
[![Release Date](https://img.shields.io/github/release-date/ionos-cloud/sdk-python-dns.svg)](https://github.com/ionos-cloud/sdk-python-dns/releases/latest)
[![PyPI version](https://img.shields.io/pypi/v/ionoscloud-dns)](https://pypi.org/project/ionoscloud-dns/)

![Alt text](.github/IONOS.CLOUD.BLU.svg?raw=true "Title")


# Python API client for ionoscloud_dns

Cloud DNS service helps IONOS Cloud customers to automate DNS Zone and Record management.


## Overview
The IONOS Cloud SDK for Python provides you with access to the IONOS Cloud API. The client library supports both simple and complex requests. It is designed for developers who are building applications in Python. All API operations are performed over SSL and authenticated using your IONOS Cloud portal credentials. The API can be accessed within an instance running in IONOS Cloud or directly over the Internet from any application that can send an HTTPS request and receive an HTTPS response.


### Installation & Usage

**Requirements:**
- Python >= 3.5

### pip install

Since this package is hosted on [Pypi](https://pypi.org/) you can install it by using:

```bash
pip install ionoscloud-dns
```

If the python package is hosted on a repository, you can install directly using:

```bash
pip install git+https://github.com/ionos-cloud/sdk-python-dns.git
```

Note: you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ionos-cloud/sdk-python-dns.git`

Then import the package:

```python
import ionoscloud_dns
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```bash
python setup.py install --user
```

or `sudo python setup.py install` to install the package for all users

Then import the package:

```python
import ionoscloud_dns
```

> **_NOTE:_**  The Python SDK does not support Python 2. It only supports Python >= 3.5.

### Authentication

All available server URLs are:

- *https://dns.de-fra.ionos.com* - Frankfurt

By default, *https://dns.de-fra.ionos.com* is used, however this can be overriden at authentication, either
by setting the `IONOS_API_URL` environment variable or by specifying the `host` parameter when
initializing the sdk client.

The username and password **or** the authentication token can be manually specified when initializing the SDK client:

```python
configuration = ionoscloud_dns.Configuration(
                username='YOUR_USERNAME',
                password='YOUR_PASSWORD',
                token='YOUR_TOKEN',
                host='SERVER_API_URL'
                )
client = ionoscloud_dns.ApiClient(configuration)
```

Environment variables can also be used. This is an example of how one would do that:

```python
import os

configuration = ionoscloud_dns.Configuration(
                username=os.environ.get('IONOS_USERNAME'),
                password=os.environ.get('IONOS_PASSWORD'),
                token=os.environ.get('IONOS_TOKEN'),
                host=os.environ.get('IONOS_API_URL')
                )
client = ionoscloud_dns.ApiClient(configuration)
```

**Warning**: Make sure to follow the Information Security Best Practices when using credentials within your code or storing them in a file.


### HTTP proxies

You can use http proxies by setting the following environment variables:
- `IONOS_HTTP_PROXY` - proxy URL
- `IONOS_HTTP_PROXY_HEADERS` - proxy headers

Each line in `IONOS_HTTP_PROXY_HEADERS` represents one header, where the header name and value is separated by a colon. Newline characters within a value need to be escaped. See this example:
```
Connection: Keep-Alive
User-Info: MyID
User-Group: my long\nheader value
```


### Changing the base URL

Base URL for the HTTP operation can be changed in the following way:

```python
import os

configuration = ionoscloud_dns.Configuration(
                username=os.environ.get('IONOS_USERNAME'),
                password=os.environ.get('IONOS_PASSWORD'),
                host=os.environ.get('IONOS_API_URL'),
                server_index=None,
                )
client = ionoscloud_dns.ApiClient(configuration)
```

## Certificate pinning:

You can enable certificate pinning if you want to bypass the normal certificate checking procedure,
by doing the following:

Set env variable IONOS_PINNED_CERT=<insert_sha256_public_fingerprint_here>

You can get the sha256 fingerprint most easily from the browser by inspecting the certificate.


## Documentation for API Endpoints

All URIs are relative to *https://dns.de-fra.ionos.com*
<details >
    <summary title="Click to toggle">API Endpoints table</summary>


| Class | Method | HTTP request | Description |
| ------------- | ------------- | ------------- | ------------- |
| DNSSECApi | [**zones_keys_delete**](docs/api/DNSSECApi.md#zones_keys_delete) | **DELETE** /zones/{zoneId}/keys | Delete a DNSSEC key |
| DNSSECApi | [**zones_keys_get**](docs/api/DNSSECApi.md#zones_keys_get) | **GET** /zones/{zoneId}/keys | Retrieve a DNSSEC key |
| DNSSECApi | [**zones_keys_post**](docs/api/DNSSECApi.md#zones_keys_post) | **POST** /zones/{zoneId}/keys | Create a DNSSEC key |
| QuotaApi | [**quota_get**](docs/api/QuotaApi.md#quota_get) | **GET** /quota | Retrieve resources quota |
| RecordsApi | [**records_get**](docs/api/RecordsApi.md#records_get) | **GET** /records | Retrieve all records from primary zones |
| RecordsApi | [**secondaryzones_records_get**](docs/api/RecordsApi.md#secondaryzones_records_get) | **GET** /secondaryzones/{secondaryZoneId}/records | Retrieve records for a secondary zone |
| RecordsApi | [**zones_records_delete**](docs/api/RecordsApi.md#zones_records_delete) | **DELETE** /zones/{zoneId}/records/{recordId} | Delete a record |
| RecordsApi | [**zones_records_find_by_id**](docs/api/RecordsApi.md#zones_records_find_by_id) | **GET** /zones/{zoneId}/records/{recordId} | Retrieve a record |
| RecordsApi | [**zones_records_get**](docs/api/RecordsApi.md#zones_records_get) | **GET** /zones/{zoneId}/records | Retrieve records |
| RecordsApi | [**zones_records_post**](docs/api/RecordsApi.md#zones_records_post) | **POST** /zones/{zoneId}/records | Create a record |
| RecordsApi | [**zones_records_put**](docs/api/RecordsApi.md#zones_records_put) | **PUT** /zones/{zoneId}/records/{recordId} | Update a record |
| ReverseRecordsApi | [**reverserecords_delete**](docs/api/ReverseRecordsApi.md#reverserecords_delete) | **DELETE** /reverserecords/{reverserecordId} | Delete a reverse DNS record |
| ReverseRecordsApi | [**reverserecords_find_by_id**](docs/api/ReverseRecordsApi.md#reverserecords_find_by_id) | **GET** /reverserecords/{reverserecordId} | Retrieve a reverse DNS record |
| ReverseRecordsApi | [**reverserecords_get**](docs/api/ReverseRecordsApi.md#reverserecords_get) | **GET** /reverserecords | Retrieves existing reverse DNS records |
| ReverseRecordsApi | [**reverserecords_post**](docs/api/ReverseRecordsApi.md#reverserecords_post) | **POST** /reverserecords | Create a reverse DNS record |
| ReverseRecordsApi | [**reverserecords_put**](docs/api/ReverseRecordsApi.md#reverserecords_put) | **PUT** /reverserecords/{reverserecordId} | Update a reverse DNS record |
| SecondaryZonesApi | [**secondaryzones_axfr_get**](docs/api/SecondaryZonesApi.md#secondaryzones_axfr_get) | **GET** /secondaryzones/{secondaryZoneId}/axfr | Get status of zone transfer |
| SecondaryZonesApi | [**secondaryzones_axfr_put**](docs/api/SecondaryZonesApi.md#secondaryzones_axfr_put) | **PUT** /secondaryzones/{secondaryZoneId}/axfr | Start zone transfer |
| SecondaryZonesApi | [**secondaryzones_delete**](docs/api/SecondaryZonesApi.md#secondaryzones_delete) | **DELETE** /secondaryzones/{secondaryZoneId} | Delete a secondary zone |
| SecondaryZonesApi | [**secondaryzones_find_by_id**](docs/api/SecondaryZonesApi.md#secondaryzones_find_by_id) | **GET** /secondaryzones/{secondaryZoneId} | Retrieve a secondary zone |
| SecondaryZonesApi | [**secondaryzones_get**](docs/api/SecondaryZonesApi.md#secondaryzones_get) | **GET** /secondaryzones | Retrieve secondary zones |
| SecondaryZonesApi | [**secondaryzones_post**](docs/api/SecondaryZonesApi.md#secondaryzones_post) | **POST** /secondaryzones | Create a secondary zone |
| SecondaryZonesApi | [**secondaryzones_put**](docs/api/SecondaryZonesApi.md#secondaryzones_put) | **PUT** /secondaryzones/{secondaryZoneId} | Update a secondary zone |
| ZoneFilesApi | [**zones_zonefile_get**](docs/api/ZoneFilesApi.md#zones_zonefile_get) | **GET** /zones/{zoneId}/zonefile | Retrieve a zone file |
| ZoneFilesApi | [**zones_zonefile_put**](docs/api/ZoneFilesApi.md#zones_zonefile_put) | **PUT** /zones/{zoneId}/zonefile | Updates a zone with a file |
| ZonesApi | [**zones_delete**](docs/api/ZonesApi.md#zones_delete) | **DELETE** /zones/{zoneId} | Delete a zone |
| ZonesApi | [**zones_find_by_id**](docs/api/ZonesApi.md#zones_find_by_id) | **GET** /zones/{zoneId} | Retrieve a zone |
| ZonesApi | [**zones_get**](docs/api/ZonesApi.md#zones_get) | **GET** /zones | Retrieve zones |
| ZonesApi | [**zones_post**](docs/api/ZonesApi.md#zones_post) | **POST** /zones | Create a zone |
| ZonesApi | [**zones_put**](docs/api/ZonesApi.md#zones_put) | **PUT** /zones/{zoneId} | Update a zone |

</details>

## Documentation For Models

All URIs are relative to *https://dns.de-fra.ionos.com*
<details >
<summary title="Click to toggle">API models list</summary>

 - [Algorithm](docs/models/Algorithm)
 - [CommonZone](docs/models/CommonZone)
 - [CommonZoneRead](docs/models/CommonZoneRead)
 - [CommonZoneReadList](docs/models/CommonZoneReadList)
 - [DnssecKey](docs/models/DnssecKey)
 - [DnssecKeyCreate](docs/models/DnssecKeyCreate)
 - [DnssecKeyParameters](docs/models/DnssecKeyParameters)
 - [DnssecKeyReadCreation](docs/models/DnssecKeyReadCreation)
 - [DnssecKeyReadList](docs/models/DnssecKeyReadList)
 - [DnssecKeyReadListMetadata](docs/models/DnssecKeyReadListMetadata)
 - [DnssecKeyReadListProperties](docs/models/DnssecKeyReadListProperties)
 - [DnssecKeyReadListPropertiesKeyParameters](docs/models/DnssecKeyReadListPropertiesKeyParameters)
 - [DnssecKeyReadListPropertiesNsecParameters](docs/models/DnssecKeyReadListPropertiesNsecParameters)
 - [Error](docs/models/Error)
 - [ErrorMessages](docs/models/ErrorMessages)
 - [KeyData](docs/models/KeyData)
 - [KeyParameters](docs/models/KeyParameters)
 - [KskBits](docs/models/KskBits)
 - [Links](docs/models/Links)
 - [Metadata](docs/models/Metadata)
 - [MetadataForSecondaryZoneRecords](docs/models/MetadataForSecondaryZoneRecords)
 - [MetadataWithStateFqdnZoneId](docs/models/MetadataWithStateFqdnZoneId)
 - [MetadataWithStateFqdnZoneIdAllOf](docs/models/MetadataWithStateFqdnZoneIdAllOf)
 - [MetadataWithStateNameservers](docs/models/MetadataWithStateNameservers)
 - [MetadataWithStateNameserversAllOf](docs/models/MetadataWithStateNameserversAllOf)
 - [NsecMode](docs/models/NsecMode)
 - [NsecParameters](docs/models/NsecParameters)
 - [ProvisioningState](docs/models/ProvisioningState)
 - [Quota](docs/models/Quota)
 - [QuotaDetail](docs/models/QuotaDetail)
 - [Record](docs/models/Record)
 - [RecordCreate](docs/models/RecordCreate)
 - [RecordEnsure](docs/models/RecordEnsure)
 - [RecordRead](docs/models/RecordRead)
 - [RecordReadList](docs/models/RecordReadList)
 - [RecordType](docs/models/RecordType)
 - [ReverseRecord](docs/models/ReverseRecord)
 - [ReverseRecordCreate](docs/models/ReverseRecordCreate)
 - [ReverseRecordEnsure](docs/models/ReverseRecordEnsure)
 - [ReverseRecordRead](docs/models/ReverseRecordRead)
 - [ReverseRecordsReadList](docs/models/ReverseRecordsReadList)
 - [SecondaryZone](docs/models/SecondaryZone)
 - [SecondaryZoneAllOf](docs/models/SecondaryZoneAllOf)
 - [SecondaryZoneCreate](docs/models/SecondaryZoneCreate)
 - [SecondaryZoneEnsure](docs/models/SecondaryZoneEnsure)
 - [SecondaryZoneRead](docs/models/SecondaryZoneRead)
 - [SecondaryZoneReadAllOf](docs/models/SecondaryZoneReadAllOf)
 - [SecondaryZoneReadList](docs/models/SecondaryZoneReadList)
 - [SecondaryZoneReadListAllOf](docs/models/SecondaryZoneReadListAllOf)
 - [SecondaryZoneRecordRead](docs/models/SecondaryZoneRecordRead)
 - [SecondaryZoneRecordReadList](docs/models/SecondaryZoneRecordReadList)
 - [SecondaryZoneRecordReadListMetadata](docs/models/SecondaryZoneRecordReadListMetadata)
 - [Zone](docs/models/Zone)
 - [ZoneAllOf](docs/models/ZoneAllOf)
 - [ZoneCreate](docs/models/ZoneCreate)
 - [ZoneEnsure](docs/models/ZoneEnsure)
 - [ZoneRead](docs/models/ZoneRead)
 - [ZoneReadAllOf](docs/models/ZoneReadAllOf)
 - [ZoneReadList](docs/models/ZoneReadList)
 - [ZoneReadListAllOf](docs/models/ZoneReadListAllOf)
 - [ZoneTransferPrimaryIpStatus](docs/models/ZoneTransferPrimaryIpStatus)
 - [ZoneTransferPrimaryIpsStatus](docs/models/ZoneTransferPrimaryIpsStatus)
 - [ZskBits](docs/models/ZskBits)


[[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

</details>
