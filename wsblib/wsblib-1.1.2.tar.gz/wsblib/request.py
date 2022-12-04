"""
Contains a `ProcessRequest` class to process and get a response
from a given route and requested method. Use to process client requests.
"""

import json
from typing import List, Union

import http_pyparser

from .errors import Error, default_errors
from .route import Route
from .server import Client


class RequestData:
    def __init__(
        self,
        parsed_http: http_pyparser.parser.HTTPData,
        remote_addr: tuple
    ):
        self.real_path = parsed_http.real_path

        self.path = parsed_http.path
        self.method = parsed_http.method
        self.version = parsed_http.version
        
        self.host = parsed_http.host
        self.user_agent = parsed_http.user_agent
        self.accept = parsed_http.accept

        self.body = parsed_http.body
        self.headers = parsed_http.headers
        self.cookies = parsed_http.cookies
        self.query = parsed_http.query

        self.remote_addr = remote_addr
        self.parameters = {}

    def json(self) -> Union[None, dict]:
        """Return body as JSON.

        If None is returned, it means that the request
        does not have a body. This method does not handle exceptions,
        decoding errors will be thrown by the `json` module.

        :return: Body as JSON format or None
        :rtype: Union[None, dict]
        """

        if self.body:
            data = json.loads(self.body)
        else:
            data = None

        return data

    def __repr__(self) -> str:
        return (f'RequestData(real_path="{self.real_path}", path="{self.path}", method="{self.method}", '
                f'version="{self.version}", host="{self.host}", user_agent="{self.user_agent}", '
                f'accept="{self.accept}", body={self.body}, headers={self.headers}, cookies={self.cookies}, '
                f'query={self.query}, remote_addr={self.remote_addr}, parameters={self.parameters})')


class RequestProcessed:
    def __init__(self, route: Union[Route, Error], request: RequestData) -> None:
        self.route = route
        self.request = request

        if isinstance(route, Route):
            self.type = 'route'
        elif isinstance(route, Error):
            self.type = 'error'

    def get_response(self, use_globals: bool = False) -> http_pyparser.Response:
        if self.type == 'route':
            response = self.route.get_route_response(self.request, use_globals=use_globals)
        elif self.type == 'error':
            response = self.route.get_callback_response(self.request)

        return response


class ProcessRequest:
    def __init__(self, routes: List[Route], errors_callback: List[Error] = []) -> None:
        self._routes = routes
        self._errors_callback = errors_callback
        self._errors_callback.extend(default_errors)

    def _get_route_by_path(self, path: str) -> Union[Route, None]:
        for route in self._routes:
            if route.match_route(path):
                return route

    def process(self, client: Client) -> RequestProcessed:
        """Processes raw HTTP data and creates a `ProcessedRequest`
        object. This object has route information with a `Route`
        object and the request that was made by the client, with
        the `RequestData` object.

        All manipulation of these data are done as you wish.

        :param client: A `Client` instance
        :type client: Client
        :return: Return a RequestProcessed object
        :rtype: RequestProcessed
        """

        # get client request
        message = client.get_message()

        if not message:
            client.destroy()
        else:
            http_parser = http_pyparser.parser.HTTPParser()
            parsed_http = http_parser.parser(message)
            remote_addr = client.get_address()

            route = self._get_route_by_path(parsed_http.path)
            request = RequestData(parsed_http, remote_addr)

            if route:
                request.parameters = route.get_parameters(parsed_http.path)

                if route.accept_method(request.method):
                    processed_request = RequestProcessed(route, request)
                else:
                    for error_handle in self._errors_callback:
                        if error_handle.match_status_code(405):
                            processed_request = RequestProcessed(error_handle, request)
                            break
            else:
                for error_handle in self._errors_callback:
                    if error_handle.match_status_code(404):
                        processed_request = RequestProcessed(error_handle, request)
                        break

            return processed_request
