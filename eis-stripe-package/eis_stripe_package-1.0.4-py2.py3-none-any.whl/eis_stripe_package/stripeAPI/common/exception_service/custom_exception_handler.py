from http import HTTPStatus

class CoreGenericException(Exception):
    status_code = HTTPStatus.INTERNAL_SERVER_ERROR.value

    def __init__(self, exception_code=None, method_name=None,
                 exception_detail="There is some issue. Please contact support.",
                 exception_traceback=None):
        super().__init__(exception_detail, exception_code)
        self.method_name = method_name
        self.exception_code = exception_code
        self.exception_detail = exception_detail
        self.exception_traceback = exception_traceback


class CoreBadRequest(Exception):
    status_code = HTTPStatus.BAD_REQUEST.value

    def __init__(self, exception_code=None, method_name=None,
                 exception_detail="Bad Request", exception_traceback=None):
        super().__init__(exception_detail, exception_code)
        self.method_name = method_name
        self.exception_code = exception_code
        self.exception_detail = exception_detail
        self.exception_traceback = exception_traceback


class CoreNotFound(Exception):
    status_code = HTTPStatus.NOT_FOUND.value

    def __init__(self, exception_code=None, method_name=None,
                 exception_detail="Not Found", exception_traceback=None):
        super().__init__(exception_detail, exception_code)
        self.method_name = method_name
        self.exception_code = exception_code
        self.exception_detail = exception_detail
        self.exception_traceback = exception_traceback


class CoreAuthenticationFailed(Exception):
    status_code = HTTPStatus.UNAUTHORIZED.value

    def __init__(self, exception_code=None, method_name=None,
                 exception_detail="Authentication Failed", exception_traceback=None):
        super().__init__(exception_detail, exception_code)
        self.method_name = method_name
        self.exception_code = exception_code
        self.exception_detail = exception_detail
        self.exception_traceback = exception_traceback


class CorePermissionDenied(Exception):
    status_code = HTTPStatus.FORBIDDEN

    def __init__(self, exception_code=None, method_name=None,
                 exception_detail="Permission Denied", exception_traceback=None):
        super().__init__(exception_detail, exception_code)
        self.method_name = method_name
        self.exception_code = exception_code
        self.exception_detail = exception_detail
        self.exception_traceback = exception_traceback


class CoreStripeException(Exception):
    status_code = HTTPStatus.INTERNAL_SERVER_ERROR.value

    def __init__(self, exception_code=None, method_name=None,
                 exception_detail="There is some issue occurred during transaction. Please contact support.",
                 exception_traceback=None):
        super().__init__(exception_detail, exception_code)
        self.method_name = method_name
        self.exception_code = exception_code
        self.exception_detail = exception_detail
        self.exception_traceback = exception_traceback
