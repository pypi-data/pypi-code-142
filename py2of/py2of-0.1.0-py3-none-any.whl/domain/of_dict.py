from collections import UserDict
from collections.abc import Mapping
from dataclasses import dataclass
from textwrap import indent
from typing import Any
from typing import Collection

from py2of.domain.dimensions import Dimensions


@dataclass(init=False)
class OfDict(
    UserDict[str, Mapping[str, Any] | str | float | int | Dimensions | Collection[str]]
):
    """OfDict."""

    def __str__(self) -> str:
        string = ""

        for key, value in self.data.items():
            if isinstance(value, Mapping):
                string += f"{key}\n"
                string += "{\n"
                string += indent(str(OfDict(value)), "    ")
                string += "}\n"
            else:
                string += f"{key} {value};\n"

        return string
