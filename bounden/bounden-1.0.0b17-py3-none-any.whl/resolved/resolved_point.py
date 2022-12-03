from typing import Any, Generic, Iterator, TypeVar

from bounden.axes import AxesT, Axis, AxisOperation
from bounden.vectors import transform_coordinates


class ResolvedPoint(Generic[AxesT]):
    """
    A resolved point in n-dimensional space.
    """

    def __init__(
        self,
        axes: tuple[Axis[Any], ...],
        coordinates: AxesT,
    ) -> None:
        self._axes = axes
        self._coordinates = coordinates

    def __add__(self: "ResolvedPointT", other: Any) -> "ResolvedPointT":
        return self._operate(other, AxisOperation.Add)

    def __eq__(self, other: Any) -> bool:
        return list(self) == list(other)

    def __getitem__(self, dimension: int) -> Any:
        return self._coordinates[dimension]

    def __iter__(self) -> Iterator[Any]:
        return iter(self._coordinates)

    def __repr__(self) -> str:
        return repr(self._coordinates)

    def _operate(
        self: "ResolvedPointT",
        vector: Any,
        operation: AxisOperation,
    ) -> "ResolvedPointT":
        """
        Returns a new point based on the `operation` between this and `vector`.
        """

        coordinates = transform_coordinates(
            self._axes,
            self._coordinates,
            vector,
            operation,
        )

        return self.__class__(self._axes, coordinates)

    @property
    def coordinates(self) -> AxesT:
        """
        Coordinates.
        """

        return self._coordinates


ResolvedPointT = TypeVar("ResolvedPointT", bound=ResolvedPoint[Any])
