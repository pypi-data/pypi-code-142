from .custom_exception import CustomException


class UnauthorizedException(CustomException):

    status_code = 401

    def __init__(self):
        super().__init__("Unauthorized")

    def serialize_errors(self):
        return [{"message": "Not authorized to access the resourse"}]
