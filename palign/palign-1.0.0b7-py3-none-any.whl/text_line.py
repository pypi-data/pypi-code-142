from typing import Iterator, List

from palign.character import TextLineCharacter
from palign.style import StyledTextLineFragment
from palign.types import GetTextLength

DEFAULT_FONT_SIZE = 21


class TextLine:
    def __init__(self, get_length: GetTextLength) -> None:
        self._characters: List[TextLineCharacter] = []
        self._get_length = get_length
        self._height = 0
        self._width: float = 0

    def __iter__(self) -> Iterator[TextLineCharacter]:
        for character in self._characters:
            yield character

    def __repr__(self) -> str:
        r = ""
        for tlc in self:
            r += tlc.character
        return r

    def append(self, fragment: StyledTextLineFragment) -> None:
        style = fragment.style
        font_size = style.font.size if style.font else DEFAULT_FONT_SIZE
        self._height = max(self._height, font_size)

        for char in fragment.text:
            if self._characters:
                self._width += style.tracking or 0

            tlc = TextLineCharacter(char, style, self._width)
            self._characters.append(tlc)

            self._width += self._get_length(char, style.font)

    @property
    def height(self) -> int:
        return self._height

    @property
    def width(self) -> float:
        return self._width
