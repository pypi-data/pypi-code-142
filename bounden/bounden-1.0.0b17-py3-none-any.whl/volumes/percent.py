from typing import Any


class Percent:
    """
    Perecentage of a length.
    """

    def __init__(self, percent: float | int) -> None:
        self._percent = float(percent)

    def __eq__(self, other: Any) -> bool:
        try:
            return self._percent == float(other)
        except ValueError:
            return False

    def __float__(self) -> float:
        return self._percent

    def __repr__(self) -> str:
        return str(self._percent) + "%"

    def calculate(self, length: float) -> float:
        """
        Calculates the percentage of `length`.
        """

        return length * (self._percent / 100)
