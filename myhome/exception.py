"""Exception classes."""
import urllib3


class MyHomeException(Exception):
    """Base exception class."""


class LoginFailure(MyHomeException):
    """Login failure."""

    def __init__(self, resp: urllib3.response.HTTPResponse, message: str):
        """Construct exception."""
        self.resp = resp
        super().__init__(message)


class RemoteAccessDenied(LoginFailure):
    """Remote access is not permitted for given user."""

    def __init__(self, resp: urllib3.response.Response):
        """Construct exception."""
        super().__init__(resp, "Remote access denied for user")


class UnknownLoginFailure(LoginFailure):
    """Unknown login failure."""

    def __init__(self, resp: urllib3.response.Response):
        """Construct exception."""
        super().__init__(resp, "An unknown issue has occurred during login")


class LoginDenied(LoginFailure):
    """Username and/or password incorrect."""

    def __init__(self, resp: urllib3.response.Response):
        """Construct exception."""
        super().__init__(resp, "Username and/or password incorrect")
