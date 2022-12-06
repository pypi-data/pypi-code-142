from itertools import zip_longest
from typing import Generic, TypeVar

from ._content_data import Data
from ._endpoint_data import Error
from ._parsed_data import ParsedData
from ..._tools import cached_property

T = TypeVar("T")


class BaseResponse(Generic[T]):
    def __init__(self, is_success: bool, data: ParsedData) -> None:
        self.is_success: bool = is_success
        self.data: T = data.content_data
        self._status = data.status
        self.errors = [
            Error(code, msg)
            for code, msg in zip_longest(data.error_codes, data.error_messages)
        ]
        self._raw_response = data.raw_response
        self.http_response = self._raw_response

    @cached_property
    def requests_count(self):
        if isinstance(self.http_response, list):
            return len(self.http_response)
        return 1

    @property
    def request_message(self):
        if self._raw_response:
            return self._raw_response.request
        return None

    @property
    def closure(self):
        if self._raw_response:
            request = self._raw_response.request
            if isinstance(request, list):
                if isinstance(request[0], list):
                    request = request[0]
                closure = [_request.headers.get("closure") for _request in request]
            else:
                closure = request.headers.get("closure")
            return closure
        return None

    @property
    def http_status(self):
        return self._status

    @property
    def http_headers(self):
        if self._raw_response:
            return self._raw_response.headers
        return None


class Response(BaseResponse[Data]):
    pass
