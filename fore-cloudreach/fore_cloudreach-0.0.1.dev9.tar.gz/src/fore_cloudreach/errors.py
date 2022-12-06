class AuthenticationError(BaseException):
    def __init__(self, msg: str):
        __str__ = msg
        return None

class ReadingMapFileError(BaseException):
    def __init__(self, msg: str):
        __str__ = msg
        return None

class EmptyMapFileError(BaseException):
    def __init__(self, msg: str):
        __str__ = msg
        return None

class ReportCreationError(BaseException):
    def __init__(self, msg: str):
        __str__ = msg
        return None