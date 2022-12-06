from types import SimpleNamespace
from typing import List, Union

from ..delivery._data._data_provider import (
    Response,
    Data,
    ParsedData,
)


def historical_join_responses(
    responses: List[Response], data: Union["Data", dict]
) -> Response:
    errors = []
    http_statuses = []
    http_headers = []
    http_responses = []
    request_messages = []

    for response in responses:
        http_statuses.append(response.http_status)
        http_headers.append(response.http_headers)
        request_messages.append(response.request_message)
        http_responses.append(response.http_response)

        if response.errors:
            errors += response.errors

    raw_response = SimpleNamespace()
    raw_response.request = request_messages
    raw_response.headers = http_headers
    response = Response(
        any(r.is_success for r in responses), ParsedData({}, raw_response)
    )
    response.errors += errors
    response.data = data if isinstance(data, Data) else Data(data)
    response._status = http_statuses
    response.http_response = http_responses

    return response
