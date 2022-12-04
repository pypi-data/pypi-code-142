#   calct: Easily do calculations on hours and minutes using the command line
#   Copyright (C) 2022  Philippe Warren
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

from enum import IntEnum
from typing import Tuple

from calct._common import Number


class Sign(IntEnum):
    """Sign of a number."""

    NULL = 0
    POSITIVE = 1
    NEGATIVE = -1

    @property
    def char(self):
        return "-" if self == Sign.NEGATIVE else ""


def sign(number: Number) -> Sign:
    if number == 0:
        return Sign.NULL
    return Sign(int(number) // int(abs(number)))


def duration_friendly_divmod(numerator: int, denominator: int) -> Tuple[Sign, int, int]:
    """Return a tuple (sign, quotient, remainder) such that
    numerator = (sign * quotient) * denominator + (sign * remainder).
    """

    return (sign(numerator * denominator), *divmod(abs(numerator), abs(denominator)))
