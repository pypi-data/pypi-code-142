class Response:
    def __init__(
            self,
            status_code=None,
            content_type=None,
            error_message=None,
            headers={},
            body=None):
        self.__status_code = status_code
        self.__content_type = content_type
        self.__error_message = error_message
        self.__headers = headers
        self.__body = body

    def set_status_code(self, status_code):
        self.__status_code = status_code

    def get_status_code(self):
        return self.__status_code

    def set_content_type(self, content_type):
        self.__content_type = content_type

    def get_content_type(self):
        return self.__content_type

    def set_error_message(self, error_message):
        self.__error_message = error_message

    def get_error_message(self):
        return self.__error_message

    def set_headers(self, headers):
        self.__headers = headers

    def get_headers(self):
        return self.__headers

    def set_body(self, body):
        self.__body = body

    def get_body(self):
        return self.__body