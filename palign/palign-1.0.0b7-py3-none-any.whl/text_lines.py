from typing import Iterator, Sequence

from bounden import ResolvedVolume2

from palign.style import StyledText
from palign.text_line import TextLine
from palign.types import GetTextLength


class TextLines:
    """
    An ordered set of text lines.
    """

    def __init__(
        self,
        many_fragments: Sequence[StyledText],
        get_length: GetTextLength,
    ) -> None:
        curr_line = TextLine(get_length)
        self._lines = [curr_line]

        for fragments in many_fragments:
            curr_line_index = 0

            for line_index, styled_line in enumerate(fragments.lines):
                if line_index > curr_line_index:
                    curr_line_index = line_index
                    curr_line = TextLine(get_length)
                    self._lines.append(curr_line)

                curr_line.append(styled_line)

        self._volume = ResolvedVolume2.new(
            max(line.width for line in self._lines),
            sum(line.height for line in self._lines),
        )

    def __iter__(self) -> Iterator[TextLine]:
        return iter(self._lines)

    def __str__(self) -> str:
        return "\n".join(str(line) for line in self._lines)

    @property
    def volume(self) -> ResolvedVolume2:
        """
        Volume.
        """

        return self._volume
