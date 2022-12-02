import uuid
from typing import Callable

import structlog
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpRequest, HttpResponse

from payla_utils.settings import payla_utils_settings

logger = structlog.get_logger(__name__)


def get_request_header(request, header_key, meta_key):
    if hasattr(request, "headers"):
        return request.headers.get(header_key)

    return request.META.get(meta_key)


class RequestMiddleware:
    """``RequestMiddleware`` adds request metadata to ``structlog``'s logger context automatically.
    >>> MIDDLEWARE = [
    ...     # ...
    ...     'payla_utils.middlewares.RequestMiddleware',
    ... ]
    """

    def __init__(self, get_response: Callable) -> None:
        self.get_response = get_response
        self._raised_exception = False

    def __call__(self, request: HttpRequest) -> HttpResponse:
        from ipware import get_client_ip

        request_id_header = payla_utils_settings.REQUEST_ID_HEADER or "X-Request-ID"

        request_id = get_request_header(
            request, request_id_header.lower(), f"HTTP_{request_id_header.upper().replace('-', '_')}"
        ) or str(uuid.uuid4())

        if payla_utils_settings.TRACING_ENABLED:
            try:
                from opentelemetry import trace
                from opentelemetry.trace.span import format_trace_id
            except ImportError:
                pass
            else:
                trace_id = format_trace_id(trace.get_current_span().get_span_context().trace_id)
                if trace_id:
                    structlog.contextvars.bind_contextvars(trace_id=trace_id)

        structlog.contextvars.bind_contextvars(request_id=request_id)
        self.bind_user_id(request)

        ip, _ = get_client_ip(request)
        structlog.contextvars.bind_contextvars(ip=ip)

        self._raised_exception = False

        response = self.get_response(request)
        if not self._raised_exception:
            self.bind_user_id(request)

        structlog.contextvars.clear_contextvars()
        return response

    @staticmethod
    def format_request(request: HttpRequest) -> str:
        return f"{request.method} {request.get_full_path()}"

    def process_exception(self, request: HttpRequest, exception: Exception) -> None:
        if isinstance(exception, (Http404, PermissionDenied)):
            # We don't log an exception here, and we don't set that we handled
            # an error as we want the standard `request_finished` log message
            # to be emitted.
            return

        self._raised_exception = True

        self.bind_user_id(request)
        logger.exception(
            "request_failed",
            code=500,
            request=self.format_request(request),
        )

    @staticmethod
    def bind_user_id(request: HttpRequest) -> None:
        if hasattr(request, "user") and request.user is not None:
            user_id = None
            if hasattr(request.user, "pk"):
                user_id = request.user.pk
                if isinstance(user_id, uuid.UUID):
                    user_id = str(user_id)
            structlog.contextvars.bind_contextvars(user_id=user_id)
