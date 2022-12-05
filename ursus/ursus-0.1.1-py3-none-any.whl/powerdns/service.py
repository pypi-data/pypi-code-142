from abc import ABC, abstractmethod
from typing import Optional, Union, overload

from .models import Zone


class PowerdnsService(ABC):
    @overload
    async def get_zones(self, *, dnssec: bool = True) -> list[Zone]: ...
    @overload
    async def get_zones(self, zone: str, *, dnssec: bool = True) -> Zone: ...

    @abstractmethod
    async def get_zones(
        self,
        zone: Optional[str] = None,
        *,
        dnssec: bool = True
    ) -> Union[Zone, list[Zone]]: ...
