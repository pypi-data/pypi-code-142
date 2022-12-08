from typing import Any, Dict, List

from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class ErrorApiResponse(BaseModel):
    code: str
    message: str | None
    path: List[str] | None = None
    context: Dict[str, Any] | None = None


class ErrorsApiResponse(BaseModel):
    errors: List[ErrorApiResponse]


def errors_response(
    *errors: ErrorApiResponse, status: int = status.HTTP_400_BAD_REQUEST
) -> JSONResponse:
    content = ErrorsApiResponse(errors=list(errors)).dict()
    return JSONResponse(content=content, status_code=status)
