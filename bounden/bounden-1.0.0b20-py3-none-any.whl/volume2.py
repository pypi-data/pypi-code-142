from typing import Optional, Type, TypeVar

from bounden.resolution import GetResolvedVolume
from bounden.resolved import ResolvedVolume
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


class ResolvedVolume2(ResolvedVolume):
    """
    A resolved two-dimensional volume.
    """

    @property
    def height(self) -> float | int:
        """
        Height.
        """

        return self[1]

    @classmethod
    def new(
        cls: Type["ResolvedVolume2T"],
        width: float | int,
        height: float | int,
    ) -> "ResolvedVolume2T":
        """
        Creates a new resolved two-dimensional volume.
        """

        return cls(width, height)

    @property
    def width(self) -> float | int:
        """
        Width.
        """

        return self[0]


ResolvedVolume2T = TypeVar("ResolvedVolume2T", bound=ResolvedVolume2)
Volume2T = TypeVar("Volume2T", bound=Volume2)
