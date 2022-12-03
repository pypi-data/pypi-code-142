import inspect
import json
from enum import Enum
from waitress import serve
from webob import Response, Request
from .response import UserResponse
from parse import parse


class Errors(Enum):
    METHOD_NOT_ALLOWED = 1
    PAGE_NOT_FOUND = 2


class Tpw:

    def __init__(self, content_type="application/json"):
        self.routes = dict()
        self.content_type = content_type

    def __call__(self, environ, start_response):
        response = self.handle_request(environ)
        return response(environ, start_response)

    def route(self, path, methods=("GET",)):
        def wrapper(handler):
            self.routes[path] = {"handler": handler, "methods": methods}
            print(self.routes)
            return handler
        return wrapper

    def find_handler(self, requested_path, request_method):
        for path, info in self.routes.items():
            parse_result = parse(path, requested_path)
            if parse_result is not None:
                if inspect.isclass(info["handler"]):
                    handler = getattr(
                        info["handler"],
                        request_method.lower(),
                        Errors.METHOD_NOT_ALLOWED
                    )
                    return {
                            "handler": handler,
                            "path_params": parse_result.named
                            }

                if request_method in info["methods"]:
                    return {
                            "handler": info["handler"],
                            "path_params": parse_result.named
                            }
                    # return info["handler"], parse_result.named
                else:
                    handler = Errors.METHOD_NOT_ALLOWED
                    path_params = {}
                    return {"handler": handler, "path_params": path_params}
        return {"handler": Errors.PAGE_NOT_FOUND}

    def handle_request(self, environ):
        resp = Response()
        req = Request(environ)
        find_result = self.find_handler(req.path, req.method)
        handler = find_result["handler"]

        if handler == Errors.PAGE_NOT_FOUND:
            print("pnf")
            return self.default_resp(resp)

        if handler == Errors.METHOD_NOT_ALLOWED:
            print("ena")
            return self.method_not_allowed(resp)

        print(handler)
        path_params = find_result["path_params"]
        parsed_body = None
        if req.body:
            parsed_body = json.loads(req.body)
        result: UserResponse = handler(req, parsed_body, **path_params)
        resp.text = result.body
        resp.status = result.status
        resp.headers = result.headers

        return resp

    def default_resp(self, resp):
        resp.status_code = 404
        resp.text = "Not found :("
        resp.content_type = self.content_type
        return resp

    def method_not_allowed(self, resp):
        resp.status_code = 400
        resp.text = "Method not allowed"
        resp.content_type = self.content_type
        return resp

    def run(self, port=8000, host="127.0.0.1"):
        serve(self, port=port, host=host)




