"""Time.

Internal value in seconds.
"""

from . import const
from .base import BaseUnit


class Time(BaseUnit):
    """Time."""

    @property
    def s(self) -> float:
        """Seconds."""
        return self._value

    @s.setter
    def s(self, value: float) -> None:
        """Seconds."""
        self._value = value

    @property
    def ns(self) -> float:
        """Nanoseconds."""
        return self._value / const.NANO

    @ns.setter
    def ns(self, value: float) -> None:
        """Nanoseconds."""
        self._value = value * const.NANO
