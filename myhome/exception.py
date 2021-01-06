# -*- coding: utf-8 -*-
import requests


class BaseException(Exception):
    """Base exception class"""

    pass


class LoginFailure(BaseException):
    """Login failure"""

    def __init__(self, resp: requests.Response, message: str):
        self.resp = resp
        super().__init__(message)


class RemoteAccessDenied(LoginFailure):
    """Remote access is not permitted for given user"""

    def __init__(self, resp: requests.Response):
        super().__init__(resp, "Remote access denied for user")


class UnknownLoginFailure(LoginFailure):
    """Unknown login failure"""

    def __init__(self, resp: requests.Response):
        super().__init__(resp, "An unknown issue has occured during login")


class LoginDenied(LoginFailure):
    """Username and/or password incorrect"""

    def __init__(self, resp: requests.Response):
        super().__init__(resp, "Username and/or password incorrect")
