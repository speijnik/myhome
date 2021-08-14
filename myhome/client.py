"""API client implementation."""
from http.cookies import SimpleCookie
import typing

from . import __version__
from .exception import LoginDenied, RemoteAccessDenied, UnknownLoginFailure
from .gen import ApiClient, Configuration  # type: ignore
from .gen.api.default_api import DefaultApi  # type: ignore
from .gen.models.login_request import LoginRequest  # type: ignore
from .gen.models.room import Room  # type: ignore
from .gen.models.zone import Zone  # type: ignore
from .object import ObjectList

LOGIN_ERROR_EXCEPTION_CLASSES: typing.Dict[str, typing.Any] = {
    "notRemote": RemoteAccessDenied,
    "error": LoginDenied,
}


class Client:
    """Client object."""

    def __init__(self, ip_address: str, port: int = 3443):
        """Construct client."""
        self._ip_address = ip_address
        api_config = Configuration(
            host=f"https://{ip_address}:{port}",
            api_key={
                "JSESSIONID": "",
            },
        )
        api_config.refresh_api_key_hook = self._refresh_api_key_hook
        self._api_key_refresh_inflight = False

        api_config.verify_ssl = False
        self._client = ApiClient(configuration=api_config)
        self._client.user_agent = f"python-myhome/{__version__}"
        self._api = DefaultApi(api_client=self._client)

    def _refresh_api_key_hook(self, api_config: Configuration):
        session_id = api_config.api_key.get("JSESSIONID", "")
        if not session_id and not self._api_key_refresh_inflight:
            self._api_key_refresh_inflight = True
            api_config.api_key = {
                "JSESSIONID": "invalid",
            }
            _, _, headers = self._api.get_serial_server_with_http_info({})

            cookie: SimpleCookie[str] = SimpleCookie()
            cookie.load(headers.get("Set-Cookie"))

            session_id_cookie = cookie.get("JSESSIONID")
            if session_id_cookie:
                session_id = session_id_cookie.key + "=" + session_id_cookie.value
                api_config.api_key = {
                    "JSESSIONID": session_id,
                }

        self._api_key_refresh_inflight = False

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
        raw_objects = self._api.get_object_list({})
        zones = self.get_zone_list()
        rooms = self.get_room_list()
        return ObjectList(self._api, raw_objects, zones, rooms)

    def get_room_list(self) -> typing.List[Room]:
        """Return list of rooms."""
        return self._api.get_room_list({})

    def get_zone_list(self) -> typing.List[Zone]:
        """Return list of zones."""
        return self._api.get_zone_list({})
