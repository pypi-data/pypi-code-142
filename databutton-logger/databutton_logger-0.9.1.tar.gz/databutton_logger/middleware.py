import contextvars
import sys
from typing import Any, Awaitable, Callable

from fastapi import Request, Response

http_request_context = contextvars.ContextVar[dict[str, Any]](
    "http_request_context", default=None
)
cloud_trace_context = contextvars.ContextVar[str]("cloud_trace_context", default=None)


async def http_request_middleware_func(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
):
    """Middleware function that can"""
    http_request = {
        "requestMethod": request.method,
        "requestUrl": request.url.path,
        "requestSize": sys.getsizeof(request),
        "remoteIp": request.client.host,
        "protocol": request.url.scheme,
    }
    if "referrer" in request.headers:
        http_request["referrer"] = request.headers.get("referrer")

    if "user-agent" in request.headers:
        http_request["userAgent"] = request.headers.get("user-agent")
    token = http_request_context.set(http_request)
    trace_token = None
    if "x-cloud-trace-context" in request.headers:
        trace_token = cloud_trace_context.set(
            request.headers.get("x-cloud-trace-context")
        )
    try:
        return await call_next(request)
    finally:
        http_request_context.reset(token)
        if trace_token:
            cloud_trace_context.reset(trace_token)
