__all__ = (
    'NotRegistered',
    'InvalidInput',
    'TooRequests',
    'InvaildAuth',
    'Repeated',
)

class NotRegistered(Exception):
    pass

class InvalidInput(Exception):
    pass

class TooRequests(Exception):
    pass

class InvaildAuth(Exception):
    pass

class Repeated(Exception):
    pass