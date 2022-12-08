"""Base class for all units."""

from abc import ABC

from . import const


class BaseUnit(ABC):
    """Base class for all units."""

    __slots__: tuple[str] = ("_value",)

    def __init__(self) -> None:
        """Create unit."""
        self._value: float

        self._value = const.DEFAULT_VALUE
