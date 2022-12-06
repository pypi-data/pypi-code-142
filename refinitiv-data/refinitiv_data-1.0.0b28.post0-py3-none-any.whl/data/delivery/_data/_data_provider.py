__all__ = (
    "_check_response",
    "BaseResponse",
    "ContentTypeValidator",
    "ContentValidator",
    "Data",
    "DataProvider",
    "DataProviderLayer",
    "emit_event",
    "EndpointData",
    "Error",
    "ParsedData",
    "Parser",
    "Request",
    "RequestFactory",
    "Response",
    "ResponseFactory",
    "success_http_codes",
    "UniverseData",
    "ValidatorContainer",
)

from typing import TYPE_CHECKING

from ._connection import HttpSessionConnection
from ._content_data import Data, UniverseData
from ._data_provider_layer import DataProviderLayer, emit_event, _check_response
from ._endpoint_data import EndpointData, Error
from ._parsed_data import ParsedData
from ._raw_data_parser import Parser, success_http_codes
from ._request import Request
from ._request_factory import RequestFactory
from ._response import BaseResponse, Response
from ._response_factory import ResponseFactory
from ._validators import ValidatorContainer, ContentValidator, ContentTypeValidator
from ..._core.session import raise_if_closed

if TYPE_CHECKING:
    import httpx


class DataProvider:
    def __init__(
        self,
        connection=HttpSessionConnection(),
        request=RequestFactory(),
        response=ResponseFactory(),
        parser=Parser(),
        validator=ValidatorContainer(),
    ):
        self.connection = connection
        self.request = request
        self.response = response
        self.parser = parser
        self.validator = validator

    def _process_response(
        self, raw_response: "httpx.Response", session, *args, **kwargs
    ) -> BaseResponse:
        is_success, data = self.parser.parse_raw_response(raw_response)

        is_success = is_success and self.validator.validate(data)

        if is_success:
            response = self.response.create_success(data, session, **kwargs)

        else:
            response = self.response.create_fail(data, **kwargs)

        return response

    def get_data(self, session, *args, **kwargs) -> BaseResponse:
        raise_if_closed(session)
        request = self.request.create(session, *args, **kwargs)
        raw_response = self.connection.send(request, session, *args, **kwargs)
        return self._process_response(raw_response, session, *args, **kwargs)

    async def get_data_async(self, session, *args, **kwargs) -> BaseResponse:
        raise_if_closed(session)
        request = self.request.create(session, *args, **kwargs)
        raw_response = await self.connection.send_async(
            request, session, *args, **kwargs
        )
        return self._process_response(raw_response, session, *args, **kwargs)


default_data_provider = DataProvider()
