from bounden.protocols import ResolvedPointProtocol, ResolvedVolumeProtocol
from bounden.resolution.types import GetResolvedPoint, GetResolvedVolume


class RegionResolver:
    """
    Region resolver.
    """

    def __init__(
        self,
        position: GetResolvedPoint | ResolvedPointProtocol,
        volume: GetResolvedVolume | ResolvedVolumeProtocol,
    ) -> None:
        self._position = position
        self._volume = volume

    def position(self) -> ResolvedPointProtocol:
        """
        Gets the resolved position.
        """

        return self._position() if callable(self._position) else self._position

    def volume(self) -> ResolvedVolumeProtocol:
        """
        Gets the resolved volume.
        """

        return self._volume() if callable(self._volume) else self._volume
