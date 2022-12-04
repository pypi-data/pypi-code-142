from __future__ import annotations

import asyncio
from enum import Enum
from typing import TYPE_CHECKING, Optional

from .response import Response
from .utils import truncate_url

if TYPE_CHECKING:
    from .engine import Engine


class RequestState(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2


class RequestError(Exception):
    pass


class RequestTimeoutError(RequestError):
    def __str__(self) -> str:
        return "Request timeout"


class RequestConnectionError(RequestError):
    def __str__(self) -> str:
        return "Connection error"


class Request:
    def __init__(self, url: str, max_retry: int = 1, timeout: int = 20, depth: int = 0):
        self.url = url
        self.max_retry = max_retry
        self.timeout = timeout
        self.state = RequestState.NOT_STARTED
        self.depth = depth
        self.response: Optional[Response] = None
        self.error: Optional[RequestError] = None
        self.duration: Optional[float] = None
        self.retry_count = -1

    async def fetch(self, engine: "Engine") -> Optional[Response]:
        loop = asyncio.get_running_loop()
        while self.retry_count < self.max_retry:
            self.retry_count += 1
            start_time = loop.time()
            try:
                self.response = await engine.fetch(request=self)
                self.error = None
            except RequestError as request_error:
                self.error = request_error
            self.duration = loop.time() - start_time
            if self.response:
                return self.response

    def ok(self) -> bool:
        return self.response.ok() if self.response else False

    def result(self) -> str:
        content = self.response and self.response.status or self.error
        if self.state is RequestState.COMPLETED:
            url = truncate_url(self.url, 79, "...")
            return f"{url} {content} {self.duration}"
        elif self.state is RequestState.IN_PROGRESS:
            url = truncate_url(self.url, 77, "...")
            retry = (
                f"({self.error}, retrying {self.retry_count} /" f" {self.max_retry})"
                if self.retry_count > 0
                else ""
            )
            return f"{url} {retry}"
        else:
            return f"{self.url} request not started"

    def __hash__(self) -> int:
        return hash(self.url)

    def __eq__(self, other: Request) -> bool:  # type: ignore
        return self.url == other.url
