from __future__ import annotations
from pathlib import Path
from ..utils import ElementInfo

class IExternal:
    def find(self) -> list[ElementInfo]:
        raise NotImplementedError()

    def exists(self, local: Path) -> str|None:
        raise NotImplementedError()

    def publish(self, local: Path):
        raise NotImplementedError()
