from uuid import UUID

from fastapi_sessions.backends.implementations import InMemoryBackend

from be.sessions.schemas import SessionData

session_repository = InMemoryBackend[UUID, SessionData]()
