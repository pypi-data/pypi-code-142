from typing import Any, Optional, Type, TypeVar

from bounden.axes import Axis, XAxisT, YAxisT
from bounden.enums import Alignment
from bounden.points.point import Point
from bounden.resolution import GetResolvedVolume, RegionResolver


class Point2(Point[tuple[XAxisT, YAxisT]]):
    """
    A point in two-dimensional space.
    """

    @classmethod
    def new(
        cls: Type["Point2T"],
        x: Alignment | XAxisT,
        y: Alignment | YAxisT,
        axes: Optional[tuple[Axis[Any], ...]] = None,
        origin_of: Optional[GetResolvedVolume] = None,
        within: Optional[RegionResolver[tuple[XAxisT, YAxisT]]] = None,
    ) -> "Point2T":
        """
        Creates a new `Point2`.
        """

        return cls(
            (x, y),
            axes=axes,
            origin_of=origin_of,
            within=within,
        )

    @property
    def left(self) -> Alignment | XAxisT:
        """
        Left.
        """

        return self.x

    @property
    def top(self) -> Alignment | YAxisT:
        """
        Top.
        """

        return self.y

    @property
    def x(self) -> Alignment | XAxisT:
        """
        X coordinate.
        """

        return self.coordinates[0]

    @property
    def y(self) -> Alignment | YAxisT:
        """
        Y coordinate.
        """

        return self.coordinates[1]


Point2T = TypeVar("Point2T", bound=Point2[Any, Any])
