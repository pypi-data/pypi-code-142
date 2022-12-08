from enum import StrEnum

from esetconnect.urls.base import Base


class Authorization(StrEnum):
    CHECK_TOKEN = f"{Base.BASE_URL}/auth:checkToken"
    GET_TOKEN = f"{Base.BASE_URL}/auth:getToken"
    GET_TOKEN_INFO = f"{Base.BASE_URL}/auth:getTokenInfo"
    RENEW_TOKEN = f"{Base.BASE_URL}/auth:renewToken"
