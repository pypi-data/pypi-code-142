from typing import cast

from bounden.axes import Axis, XAxisT, YAxisT
from bounden.resolved.resolved_region import ResolvedRegion


class ResolvedRegion2(ResolvedRegion[tuple[XAxisT, YAxisT]]):
    """
    A resolved region of two-dimensional space.
    """

    @property
    def bottom(self) -> YAxisT:
        """
        Bottom.
        """

        return self.y_axis.add(self.top, self.height)

    @property
    def height(self) -> float | int:
        """
        Height.
        """

        return self._volume[1]

    @property
    def left(self) -> XAxisT:
        """
        Left.
        """

        return self.x

    @property
    def right(self) -> XAxisT:
        """
        Right.
        """

        return self.x_axis.add(self.left, self.width)

    @property
    def top(self) -> YAxisT:
        """
        Top.
        """

        return self.y

    @property
    def width(self) -> float | int:
        """
        Width.
        """

        return self._volume[0]

    @property
    def x(self) -> XAxisT:
        """
        X coordinate.
        """

        return self._position.coordinates[0]

    @property
    def x_axis(self) -> Axis[XAxisT]:
        """
        X axis.
        """

        return cast(Axis[XAxisT], self._axes[0])

    @property
    def y(self) -> YAxisT:
        """
        Y coordinate.
        """

        return self._position.coordinates[1]

    @property
    def y_axis(self) -> Axis[YAxisT]:
        """
        Y axis.
        """

        return cast(Axis[YAxisT], self._axes[1])
