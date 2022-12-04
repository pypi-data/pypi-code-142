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

from calct._divmod import Sign, duration_friendly_divmod, sign


def test_sign():
    assert sign(0) is Sign.NULL
    assert sign(1) is Sign.POSITIVE
    assert sign(-1) is Sign.NEGATIVE
    assert sign(13542) is Sign.POSITIVE
    assert sign(-13542) is Sign.NEGATIVE


def test_sign_char():
    assert Sign.NULL.char == ""
    assert Sign.POSITIVE.char == ""
    assert Sign.NEGATIVE.char == "-"


def test_positive():
    assert duration_friendly_divmod(5, 2) == (Sign.POSITIVE, *divmod(5, 2))
    assert duration_friendly_divmod(90, 60) == (Sign.POSITIVE, *divmod(90, 60))
    assert duration_friendly_divmod(92, 60) == (Sign.POSITIVE, *divmod(92, 60))


def test_negative():
    assert duration_friendly_divmod(-90, 60) == (Sign.NEGATIVE, 1, 30)
    assert duration_friendly_divmod(-92, 60) == (Sign.NEGATIVE, 1, 32)


def test_postcondition_positive():
    numerator = 92
    denominator = 60
    sign_, quotient, remainder = duration_friendly_divmod(numerator, denominator)
    assert numerator == sign_ * quotient * denominator + sign_ * remainder


def test_postcondition_negative():
    numerator = -92
    denominator = 60
    sign_, quotient, remainder = duration_friendly_divmod(numerator, denominator)
    assert numerator == sign_ * quotient * denominator + sign_ * remainder
    assert sign(remainder) is Sign.POSITIVE
    assert sign(quotient) is Sign.POSITIVE
