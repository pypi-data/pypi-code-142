class ConnectivityException(Exception):
    pass


class InvalidIdentityException(ConnectivityException):
    pass


class LoopbackConfigException(ConnectivityException):
    pass
