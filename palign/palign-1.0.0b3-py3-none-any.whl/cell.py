from dataclasses import dataclass
from typing import Optional

from palign.style import Style


@dataclass
class Cell:
    style: Style
    text: Optional[str] = None
