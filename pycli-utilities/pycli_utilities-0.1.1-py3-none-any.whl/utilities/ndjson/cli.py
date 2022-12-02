"""
    Copyright (c) 2022 Vishv Patel (https://github.com/itsthevp)

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
    the Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
    FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
    COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
    IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from source.cli import CLIUtils
from source.helpers import path_validate


class NDJSONUtils(CLIUtils):
    def add_arguments(self) -> None:
        super().add_arguments()
        self.parser.add_argument(
            "input",
            type=path_validate,
            metavar="file",
            help="Input NDJSON file's path",
        )
        self.parser.add_argument(
            "--encoding",
            dest="encoding",
            type=str,
            metavar="",
            default="utf-8",
            help="Specifies the encoding for input NDJSON file. Defaults to UTF-8.",
        )
        self.parser.add_argument(
            "--sort-keys",
            dest="sort_keys",
            action="store_true",
            default=False,
            help="Sorts the keys of every record of the NDJSON file. Defaults to False",
        )
