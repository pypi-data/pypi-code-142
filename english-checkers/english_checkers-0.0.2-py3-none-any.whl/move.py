"""This module is for representing moves of the English checkers game.

Move object consists of the start positions and sequence of the steps
that should be done from oint to point/ Each step is a next position
for checker.

This file can also be imported as module and contains the following
classes:

    * WrongMoveError - (Exception) exception for wrong move
    * Move - represents player's move.
"""


from __future__ import annotations


class WrongMoveError(Exception):
    pass


class Move:
    """
    Class represents player's possible move.

    Move is a sequence of steps for a single checker.
    Steps are tuples of two 0-indexed coordinates.
    Start is a current checker's coordinates.
    For example start = (5, 0) and steps = [(4, 1), (2, 3)]
    means that cheker with coordinates (5, 0) goes (4, 1) and then go (2, 3).

    Attributes
    ----------
    start :  tuple[int, int]
        initial checker's coordinates
    steps : list[tuple[int, int]]
        sequence of steps

    Methods
    -------
    add(step: tuple[int, int]) -> None:
        Add step to the end of the list steps
        First int in the step is a row, second - is a column
    """

    def __init__(
            self,
            start: tuple[int, int],
            steps: list[tuple[int, int]] = []):
        """
        Step is a tuple of two coordinates.
        Steps are sequence of steps in the move.
        Start is an initial coordinates.
        """

        self.start = start
        self.steps = steps

    def add(self, step: tuple[int, int]) -> None:
        """
        Add step to the end of the list steps

        First int in the step is a row, second - is a column
        """

        self.steps.append(step)

    def __iter__(self) -> Move:
        """
        Iterator goes through items of the steps.
        """

        self.index = 0
        return self

    def __next__(self) -> tuple[int, int]:
        """
        Next item of the steps

        Returns
        -------
        tuple[int, int]

        Raises
        ------
        StopIteration
        """

        if self.index < len(self.steps):
            result = self.steps[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __str__(self):
        """
        String representation of the move.
        """

        return f'start: {self.start}\tsteps: {self.steps}'
