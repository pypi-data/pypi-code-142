from typing import Iterator, List

from palign.style import Style
from palign.text_line import TextLine
from palign.types import GetTextLength


class Text:
    def __init__(
        self,
        text: str,
        style: Style,
        get_length: GetTextLength,
    ) -> None:

        curr_line = TextLine(style, get_length)
        self._lines: List[TextLine] = [curr_line]

        self._height = 0

        for char in text:
            if char == "\n":
                curr_line = TextLine(style, get_length)
                self._lines.append(curr_line)
            else:
                curr_line.append(char)

        if not style.font:
            raise ValueError("Text requires font")

        self._height = style.font.size * len(self._lines)

    def __iter__(self) -> Iterator[TextLine]:
        for line in self._lines:
            yield line

    @property
    def height(self) -> float:
        return self._height
