from http import HTTPStatus
from typing import List

import pkg_resources
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from mappi import schema
from mappi.handlers import handler_factory
from mappi.utils import logger


class MappiMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        version = pkg_resources.get_distribution(__package__).version
        server_header = f"{__package__} {version}"
        logger.debug(f"Adding header {server_header}")
        response.headers["server"] = server_header
        return response


async def http_exception_handler(request: Request, exc: HTTPException) -> Response:
    content = exc.detail
    if exc.status_code == HTTPStatus.NOT_FOUND:
        path = request.scope["path"]
        content = f"No mapping registered for {path} route"

    return PlainTextResponse(
        content=content,
        status_code=exc.status_code,
    )


def create_app(routes: List[schema.Route]):
    app = FastAPI()
    for route in routes:
        handler = handler_factory(route)
        app.router.add_api_route(route.path, handler)

    app.add_middleware(MappiMiddleware)
    app.add_exception_handler(HTTPException, http_exception_handler)

    return app
