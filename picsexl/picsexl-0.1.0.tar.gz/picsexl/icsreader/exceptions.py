import typing


class ICSReaderException(Exception):
    def __init__(self, exc: typing.Optional[Exception] = None):
        self.exc = exc
