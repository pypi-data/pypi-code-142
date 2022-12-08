from typing import Literal
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi_sessions.frontends.implementations import CookieParameters, SessionCookie
from fastapi_sessions.frontends.implementations.cookie import Response

from be.sessions.repositories import session_repository
from be.sessions.schemas import OauthApiResponse, SessionData, VerifiedSessionData
from be.sessions.services import session_service
from be.sessions.verifiers import basic_verifier
from be.settings import settings

router = APIRouter(prefix="/sessions", tags=["authentication"])

session_cookie = SessionCookie(
    cookie_name="session",
    identifier="general_verifier",
    auto_error=True,
    secret_key=settings.session_secret,
    cookie_params=CookieParameters(),
)


@router.post("")
async def create_session(callback: Literal["oob"] | str):
    session_id, authorize_url = await session_service.create(callback)
    response_content = jsonable_encoder(OauthApiResponse(authorize_url=authorize_url))

    response = JSONResponse(content=response_content)
    session_cookie.attach_to_response(response, session_id)
    return response


@router.post("/verification")
async def verify_session(
    verifier: str,
    session_id: UUID = Depends(session_cookie),
):
    await session_service.verify(session_id, verifier)
    return Response()


@router.delete("")
async def delete_session(
    response: Response,
    session_id: UUID = Depends(session_cookie),
):
    await session_repository.delete(session_id)
    session_cookie.delete_from_response(response)
    return Response()


@router.get("", dependencies=[Depends(session_cookie)])
async def read_session(session_data: VerifiedSessionData = Depends(basic_verifier)):
    return session_data
