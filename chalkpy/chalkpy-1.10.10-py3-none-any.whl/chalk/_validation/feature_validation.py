import dataclasses
from typing import Optional, TypeVar

T = TypeVar("T")


@dataclasses.dataclass
class FeatureValidation:
    min: Optional[T]
    max: Optional[T]
    min_length: Optional[int]
    max_length: Optional[int]
    contains: Optional[T]
