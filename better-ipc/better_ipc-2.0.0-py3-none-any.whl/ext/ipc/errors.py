class BaseException(Exception):
    """Common base class for all exceptions"""
    def __init__(self, name: str, details: str) -> None:
        self.name = name
        self.details = details

class NoEndpointFoundError(BaseException):
    """Raised when trying to request an unknown endpoint"""

class MulticastFailure(BaseException):
    """Raised when calling route that is not multicasted"""

class InvalidReturn(BaseException):
    """Raiseed when getting un-serializable objects as response from a route"""
    pass

class ServerAlreadyStarted(BaseException):
    """Raise trying to start already running server"""

