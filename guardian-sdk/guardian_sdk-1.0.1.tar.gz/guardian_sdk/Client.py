from guardian_sdk import Request, Response
from guardian_sdk.util import http_util


class Client:

    @staticmethod
    def execute(request: Request) -> Response:
        resp = http_util.execute(request)
        return resp
