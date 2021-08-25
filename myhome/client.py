"""API client implementation."""
from http.cookies import SimpleCookie
import typing

from . import __version__
from ._gen import ApiClient, Configuration  # type: ignore
from ._gen.api.default_api import DefaultApi  # type: ignore
from ._gen.models.login_request import LoginRequest  # type: ignore
from ._gen.models.room import Room  # type: ignore
from ._gen.models.serial_server import SerialServer
from ._gen.models.system_info import SystemInfo
from ._gen.models.zone import Zone  # type: ignore
from .exception import LoginDenied, RemoteAccessDenied, UnknownLoginFailure
from .object import ObjectList

LOGIN_ERROR_EXCEPTION_CLASSES: typing.Dict[str, typing.Any] = {
    "notRemote": RemoteAccessDenied,
    "error": LoginDenied,
}


class CustomAPIClient(ApiClient):
    """Customized ApiClient variant that handles the session cookie."""

    async def __call_api(
        self,
        resource_path,
        method,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        files=None,
        response_types_map=None,
        auth_settings=None,
        _return_http_data_only=None,
        collection_formats=None,
        _preload_content=True,
        _request_timeout=None,
        _host=None,
        _request_auth=None,
    ):
        """Implement extended version of call_api."""
        return_data, response_status, response_headers = super().call_api(
            resource_path,
            method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            files=files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            _return_http_data_only=False,
            collection_formats=collection_formats,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            _host=_host,
            _request_auth=_request_auth,
        )

        if "Set-Cookie" in response_headers:
            cookie = SimpleCookie(response_headers["Set-Cookie"])
            if "JSESSIONID" in cookie:
                self.configuration.api_key = {
                    "cookieAuth": "JSESSIONID=" + cookie["JSESSIONID"].value,
                }

        if _return_http_data_only:
            return return_data
        return return_data, response_status, response_headers


class Client:
    """Client object."""

    def __init__(self, ip_address: str, port: int = 3443, api_debug: bool = False):
        """Construct client."""
        self._ip_address = ip_address
        api_config = Configuration(
            host=f"https://{ip_address}:{port}",
        )
        api_config.debug = api_debug
        api_config.discard_unknown_keys = False
        api_config.verify_ssl = False

        self._client = CustomAPIClient(configuration=api_config, pool_threads=16)

        self._client.user_agent = f"python-myhome/{__version__}"
        self._api = DefaultApi(api_client=self._client)

    def login(self, username: str, password: str) -> None:
        """Authenticate with server."""
        resp = self._api.login(
            self._ip_address, LoginRequest(user=username, password=password)
        )

        if resp.access != "success":
            login_error_exception_class = LOGIN_ERROR_EXCEPTION_CLASSES.get(
                resp.access, UnknownLoginFailure
            )
            raise login_error_exception_class(resp)
        return resp

    def get_server_serial(self) -> str:
        """Return the server serial number."""
        resp: SerialServer = self._api.get_serial_server({})
        return resp.serial_server

    def get_system_info(self) -> SystemInfo:
        """Return system information."""
        return self._api.get_system_info({})

    def get_object_list(self) -> ObjectList:
        """Return list of objects."""
        raw_objects = self._api.get_object_list({}).value
        zones = self.get_zone_list()
        rooms = self.get_room_list()
        return ObjectList(self._api, raw_objects, zones, rooms)

    def get_room_list(self) -> typing.List[Room]:
        """Return list of rooms."""
        return self._api.get_room_list({}).value

    def get_zone_list(self) -> typing.List[Zone]:
        """Return list of zones."""
        return self._api.get_zone_list({}).value
