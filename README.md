![CI](https://github.com/ionos-cloud/sdk-resources/workflows/[%20CI%20]%20DNS%20/%20Python/badge.svg)
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

DNS API Specification


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

The username and password **or** the authentication token can be manually specified when initializing the SDK client:

```python
configuration = ionoscloud_dns.Configuration(
                username='YOUR_USERNAME',
                password='YOUR_PASSWORD',
                token='YOUR_TOKEN'
                )
client = ionoscloud_dns.ApiClient(configuration)
```

Environment variables can also be used. This is an example of how one would do that:

```python
import os

configuration = ionoscloud_dns.Configuration(
                username=os.environ.get('IONOS_USERNAME'),
                password=os.environ.get('IONOS_PASSWORD'),
                token=os.environ.get('IONOS_TOKEN')
                )
client = ionoscloud_dns.ApiClient(configuration)
```

**Warning**: Make sure to follow the Information Security Best Practices when using credentials within your code or storing them in a file.


### HTTP proxies

You can use http proxies by setting the following environment variables:
- `IONOS_HTTP_PROXY` - proxy URL
- `IONOS_HTTP_PROXY_HEADERS` - proxy headers

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
| RecordsApi | [**records_get**](docs/api/RecordsApi.md#records_get) | **GET** /records | Retrieve all records |
| RecordsApi | [**zones_records_delete**](docs/api/RecordsApi.md#zones_records_delete) | **DELETE** /zones/{zoneId}/records/{recordId} | Delete a record |
| RecordsApi | [**zones_records_find_by_id**](docs/api/RecordsApi.md#zones_records_find_by_id) | **GET** /zones/{zoneId}/records/{recordId} | Retrieve a record |
| RecordsApi | [**zones_records_get**](docs/api/RecordsApi.md#zones_records_get) | **GET** /zones/{zoneId}/records | Retrieve records |
| RecordsApi | [**zones_records_post**](docs/api/RecordsApi.md#zones_records_post) | **POST** /zones/{zoneId}/records | Create a record |
| RecordsApi | [**zones_records_put**](docs/api/RecordsApi.md#zones_records_put) | **PUT** /zones/{zoneId}/records/{recordId} | Ensure a record |
| ZonesApi | [**zones_delete**](docs/api/ZonesApi.md#zones_delete) | **DELETE** /zones/{zoneId} | Delete a zone |
| ZonesApi | [**zones_find_by_id**](docs/api/ZonesApi.md#zones_find_by_id) | **GET** /zones/{zoneId} | Retrieve a zone |
| ZonesApi | [**zones_get**](docs/api/ZonesApi.md#zones_get) | **GET** /zones | Retrieve zones |
| ZonesApi | [**zones_post**](docs/api/ZonesApi.md#zones_post) | **POST** /zones | Create a zone |
| ZonesApi | [**zones_put**](docs/api/ZonesApi.md#zones_put) | **PUT** /zones/{zoneId} | Ensure a zone |

</details>

## Documentation For Models

All URIs are relative to *https://dns.de-fra.ionos.com*
<details >
<summary title="Click to toggle">API models list</summary>

 - [Error](docs/models/Error)
 - [ErrorMessages](docs/models/ErrorMessages)
 - [Links](docs/models/Links)
 - [Metadata](docs/models/Metadata)
 - [MetadataWithStateFqdnZoneId](docs/models/MetadataWithStateFqdnZoneId)
 - [MetadataWithStateFqdnZoneIdAllOf](docs/models/MetadataWithStateFqdnZoneIdAllOf)
 - [MetadataWithStateNameservers](docs/models/MetadataWithStateNameservers)
 - [MetadataWithStateNameserversAllOf](docs/models/MetadataWithStateNameserversAllOf)
 - [ProvisioningState](docs/models/ProvisioningState)
 - [Record](docs/models/Record)
 - [RecordCreate](docs/models/RecordCreate)
 - [RecordEnsure](docs/models/RecordEnsure)
 - [RecordRead](docs/models/RecordRead)
 - [RecordReadList](docs/models/RecordReadList)
 - [Zone](docs/models/Zone)
 - [ZoneCreate](docs/models/ZoneCreate)
 - [ZoneEnsure](docs/models/ZoneEnsure)
 - [ZoneRead](docs/models/ZoneRead)
 - [ZoneReadList](docs/models/ZoneReadList)


[[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

</details>