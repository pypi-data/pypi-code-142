from dataclasses import dataclass, field
from typing import Optional

from koil import koilable
from koil.composition import Composition
from koil.koil import Koil
from pydantic import Field

from fluss.rath import FlussRath


class Fluss(Composition):
    rath: FlussRath = Field(default_factory=FlussRath)
