from __future__ import annotations
from pathlib import Path
from types import ModuleType
from .interface import IExternal

external: IExternal = None

try:
    from .vmware import VmwareExternal
    if not external:
        external = VmwareExternal()
        if not external.is_enabled:
            external = None
except ImportError:
    pass # Python package missing: pyvmomi
