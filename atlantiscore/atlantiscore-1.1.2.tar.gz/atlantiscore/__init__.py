import sys
from importlib import import_module
from importlib.abc import MetaPathFinder
from importlib.machinery import ModuleSpec
from importlib.util import find_spec
from types import ModuleType
from typing import Optional


class AtlantisFinder(MetaPathFinder):
    finding_in_atlantis: bool = False

    @classmethod
    def find_spec(cls, fullname: str, *args, **kwargs) -> Optional[ModuleSpec]:
        if "atlantiscore" not in fullname:
            return None

        if cls.finding_in_atlantis:
            return None

        cls.finding_in_atlantis = True
        if find_spec(fullname):
            cls.finding_in_atlantis = False
            return None

        cls.finding_in_atlantis = False
        return ModuleSpec(fullname, cls)

    @staticmethod
    def create_module(spec: ModuleSpec) -> ModuleType:
        return import_module(spec.name.replace("atlantis", "coder"))

    @staticmethod
    def exec_module(module: ModuleType) -> None:
        # Intentionally left blank.
        pass


sys.meta_path.append(AtlantisFinder())
