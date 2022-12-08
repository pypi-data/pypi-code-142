from typing import Any

from fastapi import status

from be.errors.schemas import ErrorApiResponse, ErrorsApiResponse


class ApiException(Exception):
    def __init__(self, *errors: ErrorApiResponse, status=status.HTTP_400_BAD_REQUEST):
        self.errors = ErrorsApiResponse(errors=list(errors))
        self.status = status
        super().__init__(f"ApiException: {self.errors.dict()}")

    @classmethod
    def single(cls, *, status=status.HTTP_400_BAD_REQUEST, **kwargs):
        return cls(ErrorApiResponse(**kwargs), status=status)


class ApiExceptionFactory:
    def __init__(self, resource: str):
        self._resource = resource

    def not_found(self, resource_id: Any):
        return ApiException.single(
            code="NOT_FOUND",
            message=f"Resource '{self._resource}' not found.",
            context={"id": resource_id},
            status=status.HTTP_404_NOT_FOUND,
        )
