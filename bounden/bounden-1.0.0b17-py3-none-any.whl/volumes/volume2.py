from typing import Optional, Type, TypeVar

from bounden.resolution import GetResolvedVolume
from bounden.volumes.percent import Percent
from bounden.volumes.volume import Volume


class Volume2(Volume):
    """
    A two-dimensional volume.
    """

    @classmethod
    def new(
        cls: Type["Volume2T"],
        width: float | int | Percent,
        height: float | int | Percent,
        within: Optional[GetResolvedVolume] = None,
    ) -> "Volume2T":
        """
        Creates a new `Volume2`.
        """

        return cls(width, height, within=within)

    @property
    def height(self) -> float | int | Percent:
        """
        Height.
        """

        return self[1]

    @property
    def width(self) -> float | int | Percent:
        """
        Width.
        """

        return self[0]


Volume2T = TypeVar("Volume2T", bound=Volume2)
