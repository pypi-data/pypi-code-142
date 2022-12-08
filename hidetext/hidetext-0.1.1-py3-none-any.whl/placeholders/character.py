from typing import Optional

from .placeholder import Placeholder
from hidetext.textspan import TextSpan


class Character(Placeholder):
    def __init__(
        self, character: str = "*", fixed_length: Optional[int] = None
    ) -> None:
        self._character = character
        self._fixed_length = fixed_length
        super().__init__()

    def replace(self, span: TextSpan) -> str:
        if self._fixed_length is not None:
            return self._character * self._fixed_length
        return self._character * span.length
