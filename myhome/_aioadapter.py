from __future__ import annotations

import io
import logging
import re

import aiohttp

from ._gen.exceptions import (
    ApiException,
    ApiValueError,
    ForbiddenException,
    NotFoundException,
    ServiceException,
    UnauthorizedException,
)

LOGGER = logging.getLogger(__name__)


class RESTResponse(io.IOBase):
    """RESTResponse represents an aiohttp-based HTTP response."""

    def __init__(self, resp: aiohttp.ClientResponse):
        """Construct response object."""
        self.aiohttp_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data: bytes | None = None

    async def wait_for_data(self):
        """Wait for data and will self.data."""
        self.data = await self.aiohttp_response.read()

    def getheaders(self):
        """Return a dictionary of the response headers."""
        return self.aiohttp_response.headers

    def getheader(self, name, default=None):
        """Return a given response header."""
        return self.aiohttp_response.headers.get(name, default)


class RESTClientObject:
    """Representation of an aiohttp-based REST client."""

    def __init__(self, configuration):
        """Construct REST client."""
        self._verify_ssl = configuration.verify_ssl
        # we need to allow "unsafe" cookies as we may be receiving cookies from IP addresses, see
        # https://docs.aiohttp.org/en/stable/client_advanced.html#cookie-safety for details
        self._client_session = aiohttp.ClientSession(
            cookie_jar=aiohttp.CookieJar(unsafe=True)
        )

    async def request(
        self,
        method,
        url,
        query_params=None,
        headers=None,
        body=None,
        post_params=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """
        method = method.upper()
        assert method in ["GET", "HEAD", "DELETE", "POST", "PUT", "PATCH", "OPTIONS"]

        if post_params and body:
            raise ApiValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}

        timeout = None
        if _request_timeout:
            if isinstance(_request_timeout, (int, float)):
                timeout = aiohttp.ClientTimeout(total=_request_timeout)
            elif isinstance(_request_timeout, tuple) and len(_request_timeout) == 2:
                timeout = aiohttp.ClientTimeout(
                    connect=_request_timeout[0],
                    total=_request_timeout[0] + _request_timeout[1],
                )

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ["POST", "PUT", "PATCH", "OPTIONS", "DELETE"]:
                # Only set a default Content-Type for POST, PUT, PATCH and OPTIONS requests
                if (method != "DELETE") and ("Content-Type" not in headers):
                    headers["Content-Type"] = "application/json"

                if ("Content-Type" not in headers) or (
                    re.search("json", headers["Content-Type"], re.IGNORECASE)
                ):
                    pass
                    r = await self._client_session.request(
                        method,
                        url,
                        json=body,
                        timeout=timeout,
                        headers=headers,
                        verify_ssl=self._verify_ssl,
                    )
                elif headers["Content-Type"] in (
                    "application/x-www-form-urlencoded",
                    "multipart/form-data",
                ):
                    r = await self._client_session.request(
                        method,
                        url,
                        data=aiohttp.FormData(post_params),
                        timeout=timeout,
                        headers=headers,
                        verify_ssl=self._verify_ssl,
                    )
                # Pass a `string` parameter directly in the body to support
                # other content types than Json when `body` argument is
                # provided in serialized form
                elif isinstance(body, str) or isinstance(body, bytes):
                    r = await self._client_session.request(
                        method,
                        url,
                        data=body,
                        timeout=timeout,
                        headers=headers,
                        verify_ssl=self._verify_ssl,
                    )
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided
                             arguments. Please check that your arguments match
                             declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                r = await self._client_session.request(
                    method,
                    url,
                    params=query_params,
                    timeout=timeout,
                    headers=headers,
                    verify_ssl=self._verify_ssl,
                )
        except aiohttp.ClientSSLError as e:
            msg = f"{type(e).__name__}\n{str(e)}"
            raise ApiException(status=0, reason=msg)

        r = RESTResponse(r)
        await r.wait_for_data()

        if _preload_content:
            # log response body
            LOGGER.debug("response body: %s", r.data)

        if not 200 <= r.status <= 299:
            if r.status == 401:
                raise UnauthorizedException(http_resp=r)

            if r.status == 403:
                raise ForbiddenException(http_resp=r)

            if r.status == 404:
                raise NotFoundException(http_resp=r)

            if 500 <= r.status <= 599:
                raise ServiceException(http_resp=r)

            raise ApiException(http_resp=r)

        return r

    def GET(
        self,
        url,
        headers=None,
        query_params=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Perform GET request."""
        return self.request(
            "GET",
            url,
            headers=headers,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            query_params=query_params,
        )

    def HEAD(
        self,
        url,
        headers=None,
        query_params=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Perform HEAD request."""
        return self.request(
            "HEAD",
            url,
            headers=headers,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            query_params=query_params,
        )

    def OPTIONS(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Perform OPTIONS request."""
        return self.request(
            "OPTIONS",
            url,
            headers=headers,
            query_params=query_params,
            post_params=post_params,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    def DELETE(
        self,
        url,
        headers=None,
        query_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Perform DELETE request."""
        return self.request(
            "DELETE",
            url,
            headers=headers,
            query_params=query_params,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    def POST(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Perform POST request."""
        return self.request(
            "POST",
            url,
            headers=headers,
            query_params=query_params,
            post_params=post_params,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    def PUT(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Perform PUT request."""
        return self.request(
            "PUT",
            url,
            headers=headers,
            query_params=query_params,
            post_params=post_params,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    def PATCH(
        self,
        url,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        """Perform PATCH request."""
        return self.request(
            "PATCH",
            url,
            headers=headers,
            query_params=query_params,
            post_params=post_params,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )
