import json
from secrets import token_hex
from typing import Any, Dict, List, Tuple, cast
from urllib.parse import parse_qs
from uuid import UUID

import requests
from requests_oauthlib import OAuth1

from be.errors.exceptions import ApiException
from be.sessions import usos_urls
from be.sessions.repositories import session_repository
from be.sessions.schemas import UnverifiedSessionData, VerifiedSessionData
from be.settings import settings

_TOKEN_BYTES = 16

_HEADERS = {"Accept": "application/json"}
_USER_FIELDS = [
    "id",
    "first_name",
    "middle_names",
    "last_name",
    "titles",
    "student_status",
    "staff_status",
    "student_number",
]


def _secure_random_uuid():
    return UUID(hex=token_hex(_TOKEN_BYTES))


class SessionService:
    async def create(self, callback: str) -> Tuple[UUID, str]:
        session_id = _secure_random_uuid()

        oauth_token, oauth_token_secret = self._get_new_request_token(callback)
        data = UnverifiedSessionData(
            oauth_token=oauth_token, oauth_token_secret=oauth_token_secret
        )

        await session_repository.create(session_id, data)
        authorize_url = self._get_authorize_url(oauth_token)

        return (session_id, authorize_url)

    def _get_new_request_token(self, callback: str) -> Tuple[str, str]:
        oauth = OAuth1(
            client_key=settings.usos_api_key,
            client_secret=settings.usos_api_secret,
            callback_uri=callback,
        )
        response = requests.post(usos_urls.REQUEST_TOKEN, auth=oauth)
        return self._extract_tokens(response.content)

    def _get_authorize_url(self, oauth_token: str) -> str:
        return usos_urls.AUTHORIZE + f"?oauth_token={oauth_token}"

    async def verify(self, session_id: UUID, verifier: str) -> VerifiedSessionData:
        session_data = await session_repository.read(session_id)

        match session_data:
            case UnverifiedSessionData():
                new_session_data = self._verify(session_data, verifier)
                await session_repository.update(session_id, new_session_data)
                return new_session_data
            case VerifiedSessionData():
                raise ApiException.single(
                    code="ALREADY_VERIFIED", message="Session already verified"
                )
            case None:
                raise ApiException.single(
                    code="NO_SESSION", message="No session to verify"
                )
            case _:
                raise ValueError("Illegal state")

    def _verify(
        self, session_data: UnverifiedSessionData, verifier: str
    ) -> VerifiedSessionData:
        oauth = OAuth1(
            client_key=settings.usos_api_key,
            client_secret=settings.usos_api_secret,
            resource_owner_key=session_data.oauth_token,
            resource_owner_secret=session_data.oauth_token_secret,
            verifier=verifier,
        )

        response = requests.post(usos_urls.ACCESS_TOKEN, auth=oauth)

        oauth_token, oauth_token_secret = self._extract_tokens(response.content)
        oauth = OAuth1(
            client_key=settings.usos_api_key,
            client_secret=settings.usos_api_secret,
            resource_owner_key=oauth_token,
            resource_owner_secret=oauth_token_secret,
        )

        user_data = self._get_user_data(oauth)

        return VerifiedSessionData(usos_user_id=user_data["id"])

    def _extract_tokens(self, response_content: bytes):
        parsed = parse_qs(response_content)
        oauth_token = cast(List[bytes], parsed.get(b"oauth_token"))[0]
        oauth_token_secret = cast(List[bytes], parsed.get(b"oauth_token_secret"))[0]
        return oauth_token.decode("ascii"), oauth_token_secret.decode("ascii")

    def _get_user_data(self, oauth: OAuth1) -> Dict[str, Any]:
        params = {"fields": "|".join(_USER_FIELDS)}
        response = requests.get(
            usos_urls.USER, auth=oauth, params=params, headers=_HEADERS
        )
        return json.loads(response.content)

    async def delete(self, session_id: UUID) -> None:
        await session_repository.delete(session_id)


session_service = SessionService()
