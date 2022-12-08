"""The main Advent of Code module."""
from __future__ import annotations

import enum

import attrs
from attrs import validators

from easy_aoc import utils


@attrs.define(frozen=True, repr=False)
class Puzzle(utils.FlatAttributeMixin):
    """A puzzle denoted by day and a year."""

    year: int = attrs.field(validator=[validators.ge(2015)])
    day: int = attrs.field(validator=[validators.ge(1), validators.le(25)])

    def get_part(self, part: int) -> PuzzlePart:
        """Get a part of this puzzle.

        :param part: The part to get
        :return: An instance of PuzzlePart
        """
        return PuzzlePart(puzzle=self, part=part)

    __repr__ = utils.flat_repr


@attrs.define(frozen=True, repr=False)  # pylint: disable-next=too-few-public-methods
class PuzzleInput(utils.FlatAttributeMixin):
    """An input for a specific puzzle."""

    puzzle: Puzzle
    text: str

    __repr__ = utils.flat_repr


@attrs.define(frozen=True, repr=False)
class PuzzlePart(utils.FlatAttributeMixin):
    puzzle: Puzzle
    part: int = attrs.field(validator=[validators.in_({1, 2})])

    def answer(self, answer: str) -> Answer:
        """Answer this puzzle part.

        :param answer: The answer
        :return: An unsubmitted instance of Answer
        """
        return Answer(self, answer)

    __repr__ = utils.flat_repr


class Result(enum.Enum):
    CORRECT = 1
    INCORRECT = 2


@attrs.define(frozen=True, repr=False)
class Answer(utils.FlatAttributeMixin):
    """A puzzle answer."""

    part: PuzzlePart
    answer: str = attrs.field(converter=str)

    __repr__ = utils.flat_repr


@attrs.define(frozen=True, repr=False)
class Submission(utils.FlatAttributeMixin):
    """A submitted answer with the result."""

    answer: Answer
    result: Result

    __repr__ = utils.flat_repr
