"""Type definitions / aliases for the sbft API."""
import typing as t

from pydantic import BaseModel

P = t.ParamSpec("P")
R = t.TypeVar("R")
R_co = t.TypeVar("R_co", covariant=True)
PydanticModel = t.TypeVar("PydanticModel", bound=BaseModel)


class EmptyModel(BaseModel):
    """A model with no fields."""

    class Config:
        allow_mutation = False


class BaseConfig(BaseModel):
    """Base config for all models."""

    class Config:
        allow_mutation = False
        arbitrary_types_allowed = True
