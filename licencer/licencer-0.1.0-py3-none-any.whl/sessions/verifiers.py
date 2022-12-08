from uuid import UUID

from fastapi import status
from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.session_verifier import SessionVerifier

from be.errors.exceptions import ApiException
from be.sessions.schemas import SessionData, VerifiedSessionData
from be.sessions.repositories import session_repository


class BasicVerifier(SessionVerifier[UUID, SessionData]):
    def __init__(
        self,
        *,
        identifier: str,
        auto_error: bool,
        backend: InMemoryBackend[UUID, SessionData],
        auth_http_exception: Exception,
    ):
        self._identifier = identifier
        self._auto_error = auto_error
        self._backend = backend
        self._auth_http_exception = auth_http_exception

    @property
    def identifier(self):
        return self._identifier

    @property
    def backend(self):
        return self._backend

    @property
    def auto_error(self):
        return self._auto_error

    @property
    def auth_http_exception(self):
        return self._auth_http_exception

    def verify_session(self, data: SessionData) -> bool:
        return isinstance(data, VerifiedSessionData)


basic_verifier = BasicVerifier(
    identifier="general_verifier",
    auto_error=True,
    backend=session_repository,
    auth_http_exception=ApiException.single(
        code="UNAUTHORIZED",
        message="Unauthorized",
        status=status.HTTP_401_UNAUTHORIZED,
    ),
)
