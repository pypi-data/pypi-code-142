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

from time import time

from source.helpers import null_striper
from source.utilities.csv.cli import CSVUtils


class DeNULLCSV(CSVUtils):
    prog = "csv-remove-nulls"
    description = "This utility is designed to remove null characters and rows from a CSV file."
    usage = "%(prog)s file [options]"

    def add_arguments(self) -> None:
        super().add_arguments()
        self.parser.add_argument(
            "--output-file",
            type=str,
            metavar="",
            dest="output",
            help="Output CSV file name",
            default=f"nulls-removed-csv-{int(time())}.csv",
        )

    def main(self) -> None:
        with (
            open(self.args.input, "r", encoding=self.args.encoding) as r,
            open(self.args.output, "w", encoding=self.args.encoding) as w,
        ):
            line = r.readline()
            while line:
                stripped_line = null_striper(line)
                if len(stripped_line) > 1:
                    # >1 is to make sure we don't write empty lines
                    if len(stripped_line) == len(line):
                        # Nothing modified which implies that the line was without NULLs
                        # So, writing as it is
                        w.write(line)
                    else:
                        # Length modified means Line was having NULL
                        # So, here we have to check for NULL row as well (containing only separators)
                        if (
                            len(stripped_line.replace(self.args.separator, ""))
                            > 1
                        ):
                            w.write(stripped_line)
                line = r.readline()


def run() -> None:
    DeNULLCSV().run()


if __name__ == "__main__":
    run()
