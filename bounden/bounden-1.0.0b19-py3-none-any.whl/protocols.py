from typing import Any, Protocol


class ResolvedPointProtocol(Protocol):
    def __getitem__(self, dimension: int) -> Any:
        """ """


class ResolvedVolumeProtocol(Protocol):
    def __getitem__(self, dimension: int) -> float | int:
        """ """
