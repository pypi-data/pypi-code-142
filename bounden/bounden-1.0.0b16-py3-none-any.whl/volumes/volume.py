from typing import Any, Iterator, List, Optional, TypeVar

from bounden.resolution.types import GetResolvedVolume
from bounden.resolved import ResolvedVolume
from bounden.volumes.percent import Percent


class Volume:
    """
    An n-dimensional volume.

    `lengths` describes the length of each dimension.
    """

    def __init__(
        self,
        *lengths: float | int | Percent,
        within: Optional[GetResolvedVolume] = None,
    ) -> None:
        self._lengths = lengths
        self._within = within
        self._resolved: Optional[ResolvedVolume] = None

    def __eq__(self, other: Any) -> bool:
        return bool(list(self) == list(other))

    def __getitem__(self, dimension: int) -> float | int | Percent:
        return self._lengths[dimension]

    def __iter__(self) -> Iterator[float | int | Percent]:
        return iter(self._lengths)

    def __len__(self) -> int:
        return len(self._lengths)

    def __repr__(self) -> str:
        return str(self._lengths)

    def resolve(self) -> ResolvedVolume:
        """
        Resolves relative lengths to absolute.
        """

        if self._resolved is None:
            lengths: List[float | int] = []

            for index, length in enumerate(self._lengths):
                if isinstance(length, Percent):
                    within = self._within() if self._within else None
                    if within is None:
                        raise ValueError(
                            f"{self.__class__.__name__} {self} has no "
                            "parent so cannot fit to volume"
                        )
                    length = length.calculate(within[index])

                lengths.append(length)

            self._resolved = ResolvedVolume(*lengths)

        return self._resolved

    def volume(self: "VolumeT", *lengths: float | int | Percent) -> "VolumeT":
        """
        Creates and returns a child volume.
        """

        return self.__class__(*lengths, within=self.resolve)


VolumeT = TypeVar("VolumeT", bound=Volume)
