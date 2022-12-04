from typing import Iterator, List

from palign.character import TextLineCharacter
from palign.style import Style
from palign.types import GetTextLength


class TextLine:
    def __init__(
        self,
        style: Style,
        get_length: GetTextLength,
    ) -> None:
        self._characters: List[TextLineCharacter] = []
        self._get_length = get_length
        self._style = style
        self._width: float = 0

    def __iter__(self) -> Iterator[TextLineCharacter]:
        for character in self._characters:
            yield character

    def __repr__(self) -> str:
        r = ""
        for tlc in self:
            r += tlc.character
        return r

    def append(self, text: str) -> None:
        for char in text:
            if self._characters:
                self._width += self._style.tracking or 0

            self._characters.append(TextLineCharacter(char, self._width))
            self._width += self._get_length(char, self._style.font)

    @property
    def width(self) -> float:
        return self._width
