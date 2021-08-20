"""API client implementation."""
from http.cookies import SimpleCookie
import io
import typing

from . import __version__
from ._gen import ApiClient, Configuration  # type: ignore
from ._gen.api.default_api import DefaultApi  # type: ignore
from ._gen.model.login_request import LoginRequest  # type: ignore
from ._gen.model.room import Room  # type: ignore
from ._gen.model.zone import Zone  # type: ignore
from .exception import LoginDenied, RemoteAccessDenied, UnknownLoginFailure
from .object import ObjectList

LOGIN_ERROR_EXCEPTION_CLASSES: typing.Dict[str, typing.Any] = {
    "notRemote": RemoteAccessDenied,
    "error": LoginDenied,
}


class CustomAPIClient(ApiClient):
    """Customized ApiClient variant that handles the session cookie."""

    def call_api(
        self,
        resource_path: str,
        method: str,
        path_params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        query_params: typing.Optional[
            typing.List[typing.Tuple[str, typing.Any]]
        ] = None,
        header_params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        body: typing.Optional[typing.Any] = None,
        post_params: typing.Optional[typing.List[typing.Tuple[str, typing.Any]]] = None,
        files: typing.Optional[typing.Dict[str, typing.List[io.IOBase]]] = None,
        response_type: typing.Optional[typing.Tuple[typing.Any]] = None,
        auth_settings: typing.Optional[typing.List[str]] = None,
        async_req: typing.Optional[bool] = None,
        _return_http_data_only: typing.Optional[bool] = None,
        collection_formats: typing.Optional[typing.Dict[str, str]] = None,
        _preload_content: bool = True,
        _request_timeout: typing.Optional[
            typing.Union[int, float, typing.Tuple]
        ] = None,
        _host: typing.Optional[str] = None,
        _check_type: typing.Optional[bool] = None,
    ):
        """Eended version of call_api."""
        return_data, response_status, response_headers = super().call_api(
            resource_path,
            method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            files=files,
            response_type=response_type,
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=False,
            collection_formats=collection_formats,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            _host=_host,
            _check_type=_check_type,
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

    def __init__(self, ip_address: str, port: int = 3443):
        """Construct client."""
        self._ip_address = ip_address
        api_config = Configuration(
            host=f"https://{ip_address}:{port}",
        )
        api_config.debug = True
        api_config.verify_ssl = False

        self._client = CustomAPIClient(configuration=api_config)

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
