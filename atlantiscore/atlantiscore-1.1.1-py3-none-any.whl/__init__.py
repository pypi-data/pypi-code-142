import sys
from importlib.abc import MetaPathFinder
from importlib.machinery import ModuleSpec
from importlib.util import find_spec
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
        return find_spec(fullname.replace("atlantis", "coder"))


sys.meta_path.append(AtlantisFinder())
