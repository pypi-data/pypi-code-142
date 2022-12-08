from datetime import datetime
from ssl import SSLContext
from typing import Optional, Union

import httpx

from esetconnect.const import RequestMethod
from esetconnect.models import *
from esetconnect.urls import *


class EsetConnect:
    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        refresh_token: Optional[str] = None,
        verify: Union[bool, str, SSLContext] = True,
    ) -> None:
        if refresh_token == None and (username == None and password == None):
            raise ValueError("Username / password and refresh token cannot both be empty")

        if refresh_token != None and (username != None and password != None):
            raise ValueError("Username / password and refresh token cannot both be set")

        self.username = username
        self.password = password
        self.refresh_token = refresh_token
        self._access_token: Optional[str] = None
        self._client = httpx.Client(verify=verify)

    def update_tokens(self, token_response: Union[GetTokenResponse, RenewTokenResponse]) -> None:
        self._access_token = token_response.access_token
        self.refresh_token = token_response.refresh_token
        self._client.headers.update({"access-token": self._access_token})

    def get_token(self) -> GetTokenResponse:
        if self.username == None or self.password == None:
            raise ValueError("Cannot get token, credentials not set")

        req = GetTokenRequest(username=self.username, password=self.password)
        url = Authorization.GET_TOKEN
        method = RequestMethod.POST
        json = req.dict()
        return GetTokenResponse(**self._request(url=url, method=method, json=json).json())

    def get_token_info(self) -> GetTokenInfoResponse:
        if self._access_token == None:
            raise ValueError("Access token is None")

        req = GetTokenInfoRequest(access_token=self._access_token)
        url = Authorization.GET_TOKEN_INFO
        method = RequestMethod.POST
        json = req.dict()
        return GetTokenInfoResponse(**self._request(url=url, method=method, json=json).json())

    def renew_token(self) -> RenewTokenResponse:
        if self.refresh_token == None:
            raise ValueError("Cannot renew token, refresh token not set.")

        req = RenewTokenRequest(refresh_token=self.refresh_token)
        url = Authorization.RENEW_TOKEN
        method = RequestMethod.POST
        json = req.dict()
        return RenewTokenResponse(**self._request(url=url, method=method, json=json).json())

    def get_detections(
        self,
        device_uuid: Optional[str] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        page_size: Optional[int] = None,
        page_token: Optional[str] = None,
    ) -> GetDetectionsResponse:
        url = Detections.GET_DETECTIONS
        method = RequestMethod.GET
        params = GetDetectionsParams(
            device_uuid=device_uuid,
            start_time=start_time,
            end_time=end_time,
            page_size=page_size,
            page_token=page_token,
        ).dict(exclude_none=True)

        return GetDetectionsResponse(**self._request(url=url, method=method, params=params).json())

    def _request(
        self,
        url: str,
        method: RequestMethod = RequestMethod.GET,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
    ) -> httpx.Response:
        http_req = getattr(self._client, method)
        http_kwargs: dict[str, dict] = dict()

        if params is not None:
            http_kwargs.update({"params": params})

        if method == RequestMethod.POST and data is not None:
            http_kwargs.update({"data": data})

        if method == RequestMethod.POST and json is not None:
            http_kwargs.update({"json": json})

        resp = http_req(url, **http_kwargs)
        resp.raise_for_status()
        return resp
