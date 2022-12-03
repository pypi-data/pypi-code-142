from typing import Any, Generic, Iterator

from bounden.axes import AxesT


class ResolvedPoint(Generic[AxesT]):
    """
    A resolved point in n-dimensional space.
    """

    def __init__(self, coordinates: AxesT) -> None:
        self._coordinates = coordinates

    def __eq__(self, other: Any) -> bool:
        return list(self) == list(other)

    def __getitem__(self, dimension: int) -> Any:
        return self._coordinates[dimension]

    def __iter__(self) -> Iterator[Any]:
        return iter(self._coordinates)

    def __repr__(self) -> str:
        return repr(self._coordinates)

    @property
    def coordinates(self) -> AxesT:
        """
        Coordinates.
        """

        return self._coordinates
