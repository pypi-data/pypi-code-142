import pydantic


class GetTokenRequest(pydantic.BaseModel):
    username: str
    password: str


class GetTokenResponse(pydantic.BaseModel):
    access_token: str
    refresh_token: str


class GetTokenInfoRequest(pydantic.BaseModel):
    access_token: str


class GetTokenInfoResponse(pydantic.BaseModel):
    access_token: str
    server_uuid: str
    user_uuid: str
    email: str
    is_api_enabled: bool


class RenewTokenRequest(pydantic.BaseModel):
    refresh_token: str


class RenewTokenResponse(pydantic.BaseModel):
    access_token: str
    refresh_token: str
