from __future__ import annotations

from typing import Final

import attrs
from attrs import validators

from . import app, domain

_FIRST_AOC_EDITION: Final = 2015


@attrs.define
class Puzzle:
    """An Advent of Code puzzle."""

    year: int = attrs.field(validator=[validators.ge(_FIRST_AOC_EDITION)])
    day: int = attrs.field(validator=[validators.ge(1), validators.le(25)])
    app: app.App = attrs.field(repr=False, factory=app.App.get_default_app)
    _puzzle: domain.Puzzle = attrs.field(init=False, repr=False)
    _input: domain.PuzzleInput = attrs.field(init=False, repr=False, default=None)

    def __attrs_post_init__(self) -> None:
        """Create and set an instance of the Puzzle domain model."""
        self._puzzle = domain.Puzzle(year=self.year, day=self.day)

    def get_input(self) -> domain.PuzzleInput:
        """Get the input for this puzzle.

        :return: An instance of PuzzleInput
        """
        if self._input is None:
            self._input = self.app.get_puzzle_input(puzzle=self._puzzle)
        return self._input

    def submit_answer(self, part: int, answer: str) -> domain.Submission:
        """Submit an answer to this puzzle to the Advent of Code.

        :param part: The part of the puzzle
        :param answer: The answer to submit
        :return: An instance of Submission
        """
        puzzle_part = self._puzzle.get_part(part)
        answer = domain.Answer(part=puzzle_part, answer=answer)
        return self.app.submit_answer(answer)
