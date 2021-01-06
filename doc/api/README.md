# Documentation for MyHomeSERVER1 API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**getActualUser**](Apis/DefaultApi.md#getactualuser) | **POST** /rest/users/getActualUser | Retrieves current user's ID
*DefaultApi* | [**getObjectList**](Apis/DefaultApi.md#getobjectlist) | **POST** /rest/objects/list | Retrieves list of objects (devices)
*DefaultApi* | [**getObjectValue**](Apis/DefaultApi.md#getobjectvalue) | **POST** /rest/objects/getValue | Retrieves current object value
*DefaultApi* | [**getRoleUser**](Apis/DefaultApi.md#getroleuser) | **POST** /rest/users/getRoleUser | Retrieves user's role
*DefaultApi* | [**getRoomList**](Apis/DefaultApi.md#getroomlist) | **POST** /rest/rooms/list | Retrieves list of rooms
*DefaultApi* | [**getSceneList**](Apis/DefaultApi.md#getscenelist) | **POST** /rest/actions/list | Retrieves list of scenes (actions)
*DefaultApi* | [**getSerialServer**](Apis/DefaultApi.md#getserialserver) | **POST** /rest/system/getSerialServer | Retrieves system serial number
*DefaultApi* | [**getSystemInfo**](Apis/DefaultApi.md#getsysteminfo) | **POST** /rest/system/getSystemInfo | Retrieves basic system information
*DefaultApi* | [**getZoneList**](Apis/DefaultApi.md#getzonelist) | **POST** /rest/zone/list | Retrieves list of zones
*DefaultApi* | [**initCheck**](Apis/DefaultApi.md#initcheck) | **POST** /rest/plugins/bticino/initCheck | Checks if system has fully started
*DefaultApi* | [**login**](Apis/DefaultApi.md#login) | **POST** /rest/login/access | Authenticates with the MyHomeSERVER1 system
*DefaultApi* | [**setObjectValue**](Apis/DefaultApi.md#setobjectvalue) | **POST** /rest/objects/setValue | Retrieves current object value


<a name="documentation-for-models"></a>
## Documentation for Models

 - [/Models.Action](Models/Action.md)
 - [/Models.Event](Models/Event.md)
 - [/Models.GetActualUserResponse](Models/GetActualUserResponse.md)
 - [/Models.GetRoleUserResponse](Models/GetRoleUserResponse.md)
 - [/Models.InitCheckResponse](Models/InitCheckResponse.md)
 - [/Models.LoginRequest](Models/LoginRequest.md)
 - [/Models.LoginResponse](Models/LoginResponse.md)
 - [/Models.ObjectInfo](Models/ObjectInfo.md)
 - [/Models.ObjectValue](Models/ObjectValue.md)
 - [/Models.ObjectValueDimmer](Models/ObjectValueDimmer.md)
 - [/Models.ObjectValueLight](Models/ObjectValueLight.md)
 - [/Models.ObjectValueShutter](Models/ObjectValueShutter.md)
 - [/Models.ObjectValueThermostat](Models/ObjectValueThermostat.md)
 - [/Models.Room](Models/Room.md)
 - [/Models.SerialServer](Models/SerialServer.md)
 - [/Models.SetObjectValueRequest](Models/SetObjectValueRequest.md)
 - [/Models.SetObjectValueResponse](Models/SetObjectValueResponse.md)
 - [/Models.SpecificObjectRequest](Models/SpecificObjectRequest.md)
 - [/Models.SystemInfo](Models/SystemInfo.md)
 - [/Models.Zone](Models/Zone.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="sesssionAuth"></a>
### sesssionAuth

- **Type**: API key
- **API key parameter name**: JSESSIONID
- **Location**:
