"""Exceptions for easy-aoc.

All exceptions derive from EasyAocException.
"""
from easy_aoc import domain


class EasyAocException(Exception):
    """Base class for easy-aoc exceptions."""


class MissingEnvironmentVariable(EasyAocException):
    """Raised when an environment variable is not found."""

    def __init__(self, name: str) -> None:
        msg = f"Please set the environment variable {name!r}"
        super().__init__(msg)
        self.name = name

    def __repr__(self) -> str:
        """Return the representation of the exception."""
        return f"{type(self).__name__}(name={self.name!r})"


class PuzzleException(EasyAocException):
    """Base class for puzzle-related exceptions."""

    def __init__(self, puzzle: domain.Puzzle, msg: str) -> None:
        super().__init__(msg)
        self.puzzle = puzzle
        self.msg = msg

    def __repr__(self) -> str:
        """Get the representation of a PuzzleException."""
        cls_name = type(self).__name__
        return f"{cls_name}(puzzle={self.puzzle!r}, msg={self.msg!r})"

    def __str__(self) -> str:
        """Get a user-friendly representation for a PuzzleException."""
        return f"Error with {self.puzzle!r}: {self.msg}"


class PuzzleInputUnavailable(PuzzleException):
    """Raised when a puzzle input is not available."""

    def __init__(self, puzzle: domain.Puzzle) -> None:
        super().__init__(puzzle=puzzle, msg="Puzzle input not available")
