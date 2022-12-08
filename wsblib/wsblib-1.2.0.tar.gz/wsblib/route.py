"""
Contains a `Route` class that stores and manipulates information
of a created route, such as path, accepted methods and the callback function.
"""

from types import FunctionType
from typing import Union
from http_pyparser import response, parser

from .exceptions import InvalidResponseError


class Route:
    def __init__(self, callback: FunctionType, path: str, methods: tuple = ('GET',)) -> None:
        """Creating a new `Route` instance.

        This class is used to manipulate and obtain data
        from the route requested by the user, being able to check
        methods, obtain parameters (for dynamic routes) and others.

        :param callback: Function to be called when the route is requested
        :type callback: FunctionType
        :param path: Route path
        :type path: str
        :param methods: Route allowed methods, defaults to ('GET',)
        :type methods: tuple, optional
        """

        self._path = path
        self._methods = methods
        self._callback = callback

        self._parameters = []
        self._no_parameters = []

        if '<' in path and '>' in path:
            self._register_dynamic_route()

    def _register_dynamic_route(self) -> None:
        split_path = self._path.split('/')        
        split_path.remove('')

        parameters = []
        no_parameters = []

        for index, i in enumerate(split_path):
            if i.startswith('<') and i.endswith('>'):
                i = i.replace('<', '')
                i = i.replace('>', '')
                i = i.replace(' ', '')

                parameter = i.split(':')

                if len(parameter) == 2:
                    var_type, name = parameter
                else:
                    var_type = 'any'
                    name = i

                parameters.append({'index': index, 'var_type': var_type, 'name': name})
            else:
                no_parameters.append({'index': index, 'name': i})

        # register registering dynamic route variables
        self._parameters = parameters
        self._no_parameters = no_parameters

    def _get_route_parameters(self, path_split) -> dict:
        result = {}

        for d in self._parameters:
            index = d['index']
            var_type = d['var_type']
            name = d['name']

            variable = path_split[index]
            
            if var_type == 'str':
                variable = str(variable)
            elif var_type == 'int':
                variable = int(variable)
            elif var_type == 'float':
                variable = float(variable)

            result[name] = variable

        return result

    def get_parameters(self, requested_path: str) -> Union[dict, bool]:
        """Gets the route path parameters.

        If the route is dynamic, this method will get
        the parameters and return them in a dictionary,
        if the route does not match the original route,
        `False` is returned.

        :param requested_path: Path requested by client;
        :type requested_path: str
        :return: Return the parameters or False if route does
        not match the original route.
        :rtype: Union[dict, bool]
        """

        path_split = requested_path.split('/')

        while '' in path_split:
            path_split.remove('')

        if self._path == requested_path:
            return {}
        elif len(path_split) == (len(self._parameters) + len(self._no_parameters)):
            # checking if routes that are not parameters are available
            for a in self._no_parameters:
                if path_split[a['index']] == a['name']:
                    return self._get_route_parameters(path_split)
                else:
                    break

        return False

    def match_route(self, path: str) -> bool:
        """Checks if the path specified by the "path"
        argument is the same as the path of the registered route.

        :param path: Path to check
        :type path: str
        :return: Comparison result
        :rtype: bool
        """

        return self._path == path or self.get_parameters(path) is not False

    def accept_method(self, method: str) -> bool:
        """Checks if the method passed by the
        argument is accepted by the route.

        :param method: HTTP method
        :type method: str
        :return: Check result
        :rtype: bool
        """

        return method in self._methods

    def get_route_response(
        self,
        request: parser.HTTPData,
        use_globals: bool = False
    ) -> response.Response:
        """Gets the return of the route's callback
        function to use as the route's response.

        The `request` argument is only passed as
        an argument to the callback function, if it
        requests, so that it can get data from the request.

        :param request: Request data
        :type request: parser.HTTPData
        :param use_globals: Use `__globals__` to make request data available
        :type use_globals: bool, defaults to False
        :raises InvalidRouteResponseError: If the route returns None,
        or a boolean value.
        :return: Route response in Response object;
        :rtype: response.Response
        """

        if use_globals:
            self._callback.__globals__['request'] = request
            callback_response = self._callback.__call__()
        else:
            try:
                callback_response = self._callback.__call__(request)
            except TypeError:
                callback_response = self._callback.__call__()

        if not callback_response:
            raise InvalidResponseError(f'Route "{self._path}" returned a invalid response')
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
