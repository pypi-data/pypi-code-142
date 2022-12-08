from .placeholder import Placeholder
from hidetext.textspan import TextSpan


class Kind(Placeholder):
    def __init__(self, start_character: str = "<", end_character: str = ">") -> None:
        self._start_character = start_character
        self._end_character = end_character
        super().__init__()

    def replace(self, span: TextSpan) -> str:
        return f"{self._start_character}{span.kind}{self._end_character}"
