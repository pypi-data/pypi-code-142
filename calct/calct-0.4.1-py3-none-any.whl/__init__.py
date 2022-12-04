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


from calct.__version__ import __version__
from calct.duration import Duration
from calct.main import __author__, __license__, __year__, run_loop, run_once
from calct.parser import compute, evaluate_rpn, lex, parse

__all__ = [
    "Duration",
    "evaluate_rpn",
    "lex",
    "parse",
    "compute",
    "__version__",
    "__year__",
    "__author__",
    "__license__",
    "run_loop",
    "run_once",
]
