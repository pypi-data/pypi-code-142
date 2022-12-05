from guardian_sdk.common import constant


class Request:
    def __init__(
            self,
            app_key: str,
            app_secret: str,
            timeout: int,
            method: constant.HTTP_METHOD,
            host: str,
            path: str,
            headers={},
            querys={},
            bodys={},
            string_body=None,
            bytes_body=None,
            sign_headers=None
    ):
        self.__app_key = app_key
        self.__app_secret = app_secret
        self.__timeout = timeout
        self.__method = method
        self.__host = host
        self.__path = path
        self.__headers = headers
        self.__querys = querys
        self.__bodys = bodys
        self.__string_body = string_body
        self.__bytes_body = bytes_body
        self.__sign_headers = sign_headers

    def set_app_key(self, app_key):
        self.__app_key = app_key

    def get_app_key(self):
        return self.__app_key

    def set_app_secret(self, app_secret):
        self.__app_secret = app_secret

    def get_app_secret(self):
        return self.__app_secret

    def set_timeout(self, timeout):
        self.__timeout = timeout

    def get_timeout(self):
        return self.__timeout

    def set_method(self, method):
        self.__method = method

    def get_method(self):
        return self.__method

    def set_host(self, host):
        self.__host = host

    def get_host(self):
        return self.__host

    def set_path(self, path):
        self.__path = path

    def get_path(self):
        return self.__path

    def set_headers(self, headers):
        self.__headers = headers

    def get_headers(self):
        return self.__headers

    def set_querys(self, querys):
        self.__querys = querys

    def get_querys(self):
        return self.__querys

    def set_bodys(self, bodys):
        self.__bodys = bodys

    def get_bodys(self):
        return self.__bodys

    def set_string_body(self, string_body):
        self.__string_body = string_body

    def get_string_body(self):
        return self.__string_body

    def set_bytes_body(self, bytes_body):
        self.__bytes_body = bytes_body

    def get_bytes_body(self):
        return self.__bytes_body

    def set_sign_headers(self, sign_headers):
        self.__sign_headers = sign_headers

    def get_sign_headers(self):
        return self.__sign_headers
