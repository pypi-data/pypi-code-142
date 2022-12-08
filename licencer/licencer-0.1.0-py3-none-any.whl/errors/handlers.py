from typing import Any

from fastapi import Request, Response, status
from fastapi.exceptions import RequestValidationError

from be.errors.exceptions import ApiException
from be.errors.schemas import ErrorApiResponse, errors_response


def validation_exception_handler(_: Request, exc: RequestValidationError) -> Response:
    errors = [*map(_from_pydantic, exc.errors())]
    return errors_response(*errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


def _from_pydantic(error: Any) -> ErrorApiResponse:
    code = "VALIDATION_ERROR"
    message = error["msg"]
    path = [*map(str, error["loc"])]

    context = error.get("ctx", dict())
    context["type"] = error.get("type")

    return ErrorApiResponse(code=code, message=message, path=path, context=context)


def api_exception_handler(_: Request, exc: ApiException) -> Response:
    return errors_response(*exc.errors.errors, status=exc.status)


def regular_exception_handler(_: Request, __: Exception) -> Response:
    internal_error = ErrorApiResponse(
        code="INTERNAL_SERVER_ERROR", message="Internal server error"
    )

    return errors_response(internal_error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
