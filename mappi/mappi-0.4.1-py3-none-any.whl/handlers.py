import json
import os

from fastapi import Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from starlette.staticfiles import StaticFiles

from mappi import schema
from mappi.utils import logger


def body_factory(route: schema.Route):
    async def body_handler():
        return "Hello buddy"

    return body_handler


def text_factory(route: schema.Route):
    async def text_handler():
        # return Response("Text response", media_type="text/plain")
        return PlainTextResponse(
            content=route.text,
            status_code=route.status,
        )

    return text_handler


def html_factory(route: schema.Route):
    async def html_handler():
        return HTMLResponse(
            content=route.html,
            status_code=route.status,
        )

    return html_handler


def static_factory(route: schema.Route):
    filepath = route.file
    stat_result = os.stat(filepath)
    static = StaticFiles()
    logger.debug(f"Creating handler for {filepath}")

    async def static_handler(request: Request):
        return static.file_response(
            filepath, stat_result=stat_result, scope=request.scope
        )

    return static_handler


def json_factory(route: schema.Route):
    content = json.loads(route.json_data)

    async def json_handler():
        return JSONResponse(
            content=content,
            status_code=route.status,
        )

    return json_handler


def handler_factory(route: schema.Route):
    match route.route_type:
        case schema.RouteType.FILE:
            logger.debug(f"Path {route.path}: attaching file handler")
            handler = static_factory(route)
            return handler
        case schema.RouteType.JSON:
            logger.debug(f"Path {route.path}: attaching json handler")
            handler = json_factory(route)
            return handler
        case schema.RouteType.TEXT:
            logger.debug(f"Path {route.path}: attaching text handler")
            handler = text_factory(route)
            return handler
        case schema.RouteType.HTML:
            logger.debug(f"Path {route.path}: attaching html handler")
            handler = html_factory(route)
            return handler
        case _:
            # TODO: should raise on pydantic validation level
            raise ValueError("Improper configuratoin")
