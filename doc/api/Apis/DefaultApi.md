# DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getActualUser**](DefaultApi.md#getActualUser) | **POST** /rest/users/getActualUser | Retrieves current user&#39;s ID
[**getObjectList**](DefaultApi.md#getObjectList) | **POST** /rest/objects/list | Retrieves list of objects (devices)
[**getObjectValue**](DefaultApi.md#getObjectValue) | **POST** /rest/objects/getValue | Retrieves current object value
[**getRoleUser**](DefaultApi.md#getRoleUser) | **POST** /rest/users/getRoleUser | Retrieves user&#39;s role
[**getRoomList**](DefaultApi.md#getRoomList) | **POST** /rest/rooms/list | Retrieves list of rooms
[**getSceneList**](DefaultApi.md#getSceneList) | **POST** /rest/actions/list | Retrieves list of scenes (actions)
[**getSerialServer**](DefaultApi.md#getSerialServer) | **POST** /rest/system/getSerialServer | Retrieves system serial number
[**getSystemInfo**](DefaultApi.md#getSystemInfo) | **POST** /rest/system/getSystemInfo | Retrieves basic system information
[**getZoneList**](DefaultApi.md#getZoneList) | **POST** /rest/zone/list | Retrieves list of zones
[**initCheck**](DefaultApi.md#initCheck) | **POST** /rest/plugins/bticino/initCheck | Checks if system has fully started
[**login**](DefaultApi.md#login) | **POST** /rest/login/access | Authenticates with the MyHomeSERVER1 system
[**setObjectValue**](DefaultApi.md#setObjectValue) | **POST** /rest/objects/setValue | Retrieves current object value


<a name="getActualUser"></a>
# **getActualUser**
> get-actual-user-response getActualUser(body)

Retrieves current user&#39;s ID

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**|  |

### Return type

[**get-actual-user-response**](/Models/get-actual-user-response.md)

### Authorization

[sesssionAuth](../README.md#sesssionAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getObjectList"></a>
# **getObjectList**
> List getObjectList(body)

Retrieves list of objects (devices)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**|  |

### Return type

[**List**](/Models/object-info.md)

### Authorization

[sesssionAuth](../README.md#sesssionAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getObjectValue"></a>
# **getObjectValue**
> object-value getObjectValue(specificObjectRequest)

Retrieves current object value

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **specificObjectRequest** | [**SpecificObjectRequest**](/Models/SpecificObjectRequest.md)|  |

### Return type

[**object-value**](/Models/object-value.md)

### Authorization

[sesssionAuth](../README.md#sesssionAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getRoleUser"></a>
# **getRoleUser**
> get-role-user-response getRoleUser(body)

Retrieves user&#39;s role

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**|  |

### Return type

[**get-role-user-response**](/Models/get-role-user-response.md)

### Authorization

[sesssionAuth](../README.md#sesssionAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getRoomList"></a>
# **getRoomList**
> List getRoomList(body)

Retrieves list of rooms

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**|  |

### Return type

[**List**](/Models/room.md)

### Authorization

[sesssionAuth](../README.md#sesssionAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getSceneList"></a>
# **getSceneList**
> List getSceneList(body)

Retrieves list of scenes (actions)

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**|  |

### Return type

[**List**](/Models/action.md)

### Authorization

[sesssionAuth](../README.md#sesssionAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getSerialServer"></a>
# **getSerialServer**
> serial-server getSerialServer(body)

Retrieves system serial number

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**|  |

### Return type

[**serial-server**](/Models/serial-server.md)

### Authorization

[sesssionAuth](../README.md#sesssionAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getSystemInfo"></a>
# **getSystemInfo**
> system-info getSystemInfo(body)

Retrieves basic system information

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**|  |

### Return type

[**system-info**](/Models/system-info.md)

### Authorization

[sesssionAuth](../README.md#sesssionAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getZoneList"></a>
# **getZoneList**
> List getZoneList(body)

Retrieves list of zones

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**|  |

### Return type

[**List**](/Models/zone.md)

### Authorization

[sesssionAuth](../README.md#sesssionAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="initCheck"></a>
# **initCheck**
> init-check-response initCheck()

Checks if system has fully started

    This operation is invoked to check if system startup has fully completed.  The meaning of this method needs some further research.

### Parameters
This endpoint does not need any parameter.

### Return type

[**init-check-response**](/Models/init-check-response.md)

### Authorization

[sesssionAuth](../README.md#sesssionAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="login"></a>
# **login**
> login-response login(xRealIP, loginRequest)

Authenticates with the MyHomeSERVER1 system

    A successful call causes the session to become authenticated

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xRealIP** | **String**|  | [default to null]
 **loginRequest** | [**LoginRequest**](/Models/LoginRequest.md)|  |

### Return type

[**login-response**](/Models/login-response.md)

### Authorization

[sesssionAuth](../README.md#sesssionAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="setObjectValue"></a>
# **setObjectValue**
> set-object-value-response setObjectValue(setObjectValueRequest)

Retrieves current object value

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setObjectValueRequest** | [**SetObjectValueRequest**](/Models/SetObjectValueRequest.md)|  |

### Return type

[**set-object-value-response**](/Models/set-object-value-response.md)

### Authorization

[sesssionAuth](../README.md#sesssionAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json
