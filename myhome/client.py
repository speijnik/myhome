# -*- coding: utf-8 -*-
import typing
from http.cookies import SimpleCookie

from . import __version__
from .exception import LoginDenied, RemoteAccessDenied, UnknownLoginFailure
from .gen import ApiClient, Configuration  # type: ignore
from .gen.api.default_api import DefaultApi  # type: ignore
from .gen.models.login_request import LoginRequest  # type: ignore
from .object import ObjectList

LOGIN_ERROR_EXCEPTION_CLASSES: typing.Dict[str, typing.Any] = {
    "notRemote": RemoteAccessDenied,
    "error": LoginDenied,
}


class Client(object):
    """Client object"""

    def __init__(self, ip_address: str, port: int = 3443):
        self._ip_address = ip_address
        api_config = Configuration(
            host="https://{}:{}".format(ip_address, port),
            api_key={
                "JSESSIONID": "",
            },
        )
        api_config.refresh_api_key_hook = self._refresh_api_key_hook
        self._api_key_refresh_inflight = False

        api_config.verify_ssl = False
        self._client = ApiClient(configuration=api_config)
        self._client.user_agent = "python-myhome/{}".format(__version__)
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
                api_config.api_key = {
                    "JSESSIONID": session_id_cookie.key + "=" + session_id_cookie.value,
                }

        self._api_key_refresh_inflight = False

    def login(self, username: str, password: str) -> None:
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
        raw_objects = self._api.get_object_list({})
        return ObjectList(self._api, raw_objects)
