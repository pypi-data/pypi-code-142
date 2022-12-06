from typing import List

import pkg_resources
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

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


def create_app(routes: List[schema.Route]):
    app = FastAPI()
    for route in routes:
        handler = handler_factory(route)
        app.router.add_api_route(route.path, handler)

    app.add_middleware(MappiMiddleware)

    return app
