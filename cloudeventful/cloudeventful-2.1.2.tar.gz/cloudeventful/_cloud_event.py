"""Cloud event Pydantic model."""
import datetime
from typing import Generic, TypeVar

from pydantic.generics import GenericModel

DataType = TypeVar("DataType")


class CloudEvent(GenericModel, Generic[DataType]):
    """Cloud event from spec 1.0."""

    id: str
    source: str
    specversion: str = "1.0"
    type: str
    data: DataType
    datacontenttype: str | None = None
    dataschema: str | None = None
    subject: str | None = None
    time: datetime.datetime | None = None
