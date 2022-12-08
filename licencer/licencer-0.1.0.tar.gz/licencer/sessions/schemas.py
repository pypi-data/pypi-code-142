from pydantic import BaseModel


class OauthApiResponse(BaseModel):
    authorize_url: str


class SessionData(BaseModel):
    pass


class UnverifiedSessionData(SessionData):
    oauth_token: str
    oauth_token_secret: str


class VerifiedSessionData(SessionData):
    usos_user_id: str
