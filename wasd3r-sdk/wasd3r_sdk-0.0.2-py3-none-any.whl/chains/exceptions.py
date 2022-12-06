class BaseWasd3rChainsException(Exception):
    """Base exception from wasd3r.chains module"""


class SdkNotFoundError(BaseWasd3rChainsException, ModuleNotFoundError):
    """SDK module is not installed."""


class DifferentChainInfoError(BaseWasd3rChainsException):
    """Chain info is different
    * between user input and remote.
    """


class CommunicationError(BaseWasd3rChainsException):
    """Communication with a remote node/wasd3r API server is not ready."""


class CompilerError(BaseWasd3rChainsException):
    """Compiler is not ready or has an error."""
