from types import FunctionType

from .exceptions import InvalidResponseError

from http_pyparser import response
from http_pyparser.parser import HTTPData


class Error:
    def __init__(self, callback: FunctionType, status_code: int) -> None:
        self._callback = callback
        self._status_code = status_code

    def match_status_code(self, status_code: int) -> bool:
        return self._status_code == status_code

    def get_callback_response(self, request: HTTPData) -> response.Response:
        """Gets the response from the error handler.

        The `request` argument is only passed as
        an argument to the callback function, if it
        requests, so that it can get data from the request.

        :param request: Request data
        :type request: RequestData
        :raises InvalidResponseError: If the route returns None,
        or a boolean value.
        :return: Callback response in Response object;
        :rtype: http_pyparser.parser.HTTPData
        """

        try:
            callback_response = self._callback.__call__(request)
        except TypeError:
            callback_response = self._callback.__call__()

        if not callback_response:
            raise InvalidResponseError(f'Error callback to "{self._status_code}" '
                                        'status code returned a invalid response')
        else:
            if isinstance(callback_response, tuple):
                # getting body and status of response
                # in use cases of: return "Hello", 200.
                body, status = callback_response
                final_response = response.Response(body, status=status)
            elif isinstance(callback_response, response.Response):
                final_response = callback_response
            else:
                final_response = response.Response(callback_response)

            return final_response


def not_found_error_404():
    return '<h1>404: Not Found</h1>', 404


def method_not_allowed_405():
    return '<h1><b>405</b>: Method Not Allowed</h1>', 405


default_errors = [
    Error(not_found_error_404, 404),
    Error(method_not_allowed_405, 405)
]
