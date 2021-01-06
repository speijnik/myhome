# MyHomeSERVER1 API

This document contains a very likely incomplete description of the
MyHomeSERVER1 API. The description has been obtained by intercepting network
traffic between the MyHomeUp mobile application and a MyHomeSERVER1 instance.

The setup used during analysis is described in detail in
[analysis-setup](analysis_setup.md).

## Discovery

The server exposes itself via UPnP with a device type of *urn:schemas-bticino-it:device:myhomeserver1:1*.
This means the existence of the server can be discovered via UPnP, even though
the HTTPS server on port 3443 is not exposed this way.

## Basics

* The API is an HTTPS-encrypted RESTful API, using the *rest/* path prefix for
all its operations.
* Request and response bodies are JSON-encoded.
* Authentication is seemingly based on sessions, with the *JSESSIONID* cookie transporting the session ID.
* All API calls seemingly use the *POST* method, so no further note of the corresponding method will be made unless it deviates from this.

## Organization of API

Below the *rest/* prefix further common prefixes organize the API:

* *actions*
* *geoloc*
* *login*
* *objects*
* *plugins*
* *rooms*
* *system*
* *users*
* *zone*

## Workflows

### initial workflow

When the app connects to the API it runs the following flow:

* *POST /rest/system/getSerialServer*
* *GET /* (this is technically not an API call)
* *POST /rest/login/access*
* *POST /rest/users/getRoleUser*
* *POST /rest/plugins/bticino/initCheck*
* *POST /rest/users/getActualUser*
* *POST /rest/system/getDataCertificateRamains*
* *POST /rest/system/updateCheck*
* *POST /rest/geoloc/listGeolocConditions*
* *POST /rest/geoloc/getGeoloc*
* *POST /rest/users/tokenDevice*
* *POST /rest/objects/list*
* *POST /rest/users/tokenDevice*
* *POST /rest/plugins/bticinoThermo/checkCentralUnit*
* *POST /rest/system/getSystemInfo*
* *POST /rest/zone/list*
* *POST /rest/plugins/ksenia/config*
* *POST /rest/plugins/bticinoThermoScheduler/getZonesList*
* *POST /rest/rooms/list*
* *POST /rest/rooms/getImage* - once for each room returned in room list
* *POST /rest/actions/list*
* *POST /rest/actions/getImage* - once for each action returned in action list
* *POST /rest/system/getGlobalConfigurations*

## API documentation

The API documentation is generated from our OpenAPI spec automatically and can be found in the
separate [API](./api/README.md) section.
This section contains those operations that have been documented so far and all bodies required,
as well as the authentication mechanism.
