from typing import Any, Iterator


class ResolvedVolume:
    """
    An resolved n-dimensional volume.
    """

    def __init__(self, *lengths: float | int) -> None:
        self._lengths = lengths

    def __eq__(self, other: Any) -> bool:
        return bool(list(self) == list(other))

    def __iter__(self) -> Iterator[float | int]:
        return iter(self._lengths)

    def __getitem__(self, dimension: int) -> float | int:
        return self._lengths[dimension]

    def __repr__(self) -> str:
        return str(self._lengths)
