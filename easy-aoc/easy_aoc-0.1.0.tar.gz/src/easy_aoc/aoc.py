"""The main Advent of Code module."""
import attrs
from attrs import validators


@attrs.define
class Puzzle:
    """An Advent of Code puzzle."""

    # pylint: disable=too-few-public-methods

    year: int = attrs.field(validator=validators.ge(2015))
    day: int = attrs.field(validator=[validators.ge(1), validators.le(25)])
