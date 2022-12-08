from typing import Awaitable, Callable, Mapping, Optional, Sequence

from dependency_injector.containers import Container
from fastapi import FastAPI, Request, Response
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware

from dropland.app.application import Application
from dropland.app.base import ModuleFactory, ResourceFactory, ServiceFactory
from .json import JsonResponse
from ...data.context import get_context


class FastAPIApplication(Application):
    def __init__(self, container: Container, name: str, debug: bool, version: str,
                 title: str, api_root: str, cors: Optional[Sequence[str]] = None,
                 resources: Optional[Mapping[str, ResourceFactory]] = None,
                 services: Optional[Mapping[str, ServiceFactory]] = None,
                 modules: Optional[Mapping[str, ModuleFactory]] = None):
        super().__init__(container, name, debug, version, resources=resources, services=services, modules=modules)

        self._server = self._create_server(title, debug, self.version, api_root, cors)
        self._server.state.application = self

    @property
    def server(self):
        return self._server

    def _create_server(self, title: str, debug: bool, version: str,
                       api_root: str, cors: Optional[Sequence[str]] = None):
        from starlette.authentication import AuthenticationBackend, AuthCredentials, UnauthenticatedUser
        from starlette.middleware.authentication import AuthenticationMiddleware
        from fastapi.middleware.cors import CORSMiddleware

        class AuthBackend(AuthenticationBackend):
            async def authenticate(self, request):
                return AuthCredentials(), UnauthenticatedUser()

        middlewares = [
            Middleware(
                CORSMiddleware,
                allow_origins=[str(origin) for origin in cors] if cors else ['*'],
                allow_credentials=True, allow_methods=['*'], allow_headers=['*'],
            ),
            Middleware(AuthenticationMiddleware, backend=AuthBackend()),
        ]

        server = FastAPI(
            title=title, version=version, debug=debug,
            default_response_class=JsonResponse, root_path=api_root,
            on_startup=[self.startup, self.sync_startup],
            on_shutdown=[self.shutdown, self.sync_shutdown],
            middleware=middlewares
        )

        server.add_middleware(BaseHTTPMiddleware, dispatch=self._server_entrypoint)

        return server

    async def _server_entrypoint(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]):
        ctx = get_context()
        if not ctx.raw_id:
            old_id, ctx.session_id = ctx.session_id, id(request)
        else:
            old_id = ctx.session_id

        try:
            async with self.with_app_sessions():
                return await call_next(request)
        finally:
            ctx.session_id = old_id
