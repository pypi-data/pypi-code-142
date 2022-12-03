import json


class UserResponse:
    __slots__ = (
        "__resp_body", "__resp_status",
        "__resp_headers", "__resp_cookies"
        )

    def __init__(self, body=None, status=200, headers=None, cookies=None):
        self.__resp_body = body
        self.__resp_status = status
        self.__resp_headers = headers
        self.__resp_cookies = cookies

    @property
    def body(self):
        return json.dumps(self.__resp_body)

    @body.setter
    def body(self, val):
        self.__resp_body = val

    @property
    def status(self):
        return self.__resp_status

    @status.setter
    def status(self, val):
        if type(val) == int and 100 <= val <= 500:
            self.__resp_status = val
        else:
            raise ValueError("Status must be a valid integer between 100 and 500")

    @property
    def headers(self):
        default_headers = [("content-type", "application/json")]
        return self.__resp_headers or default_headers

    @headers.setter
    def headers(self, val):
        if type(val) == dict:
            if "content-type" not in [key.lower() for key in val.keys()]:
                val["content-type"] = "application/json"
            # valid_headers = [(key, value) for key, value in val.items()]
            self.__resp_headers = val
        else:
            raise ValueError("Headers must be a dict")

    def add_header(self, key, value):
        self.__resp_headers[key] = value

    def add_cookie(self, key, value):
        self.__resp_headers["set-cookie"] = f"{key}={value}"

    def remove_cookie(self, key):
        self.__resp_headers["set-cookie"] = f"{key}=deleted; expires=Thu, 01 Jan 1970 00:00:00 GMT"




    # @property
    # def cookies(self):
    #     return self.__resp_cookies
    #
    # @cookies.setter
    # def cookies(self, val):









