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

from source.utilities.csv.cli import CSVUtils


class RemoveColumnCSV(CSVUtils):
    prog = "csv-remove-column"
    description = (
        "This utility is designed to remove specific column from a CSV file."
    )
    usage = "%(prog)s file column_number [options]"

    def add_arguments(self) -> None:
        super().add_arguments()
        self.parser.add_argument(
            "column_number",
            metavar="column_number",
            type=int,
            help="Column's number which needs to be removed (Starting from 1).",
        )
        self.parser.add_argument(
            "--output-file",
            type=str,
            metavar="",
            dest="output",
            help="Output CSV file name",
            default=f"column-removed-csv-{int(time())}.csv",
        )

    def main(self) -> None:
        with (
            open(self.args.input, "r", encoding=self.args.encoding) as r,
            open(self.args.output, "w", encoding=self.args.encoding) as w,
        ):
            line = r.readline()

            # Checking that supplied column number is valid
            col_count = line.count(self.args.separator)
            if not 0 < self.args.column_number <= col_count + 1:
                self.log("Invalid column number provided for removal.")
                raise SystemExit()

            while line:
                cols = line.split(self.args.separator)
                cols.pop(self.args.column_number - 1)
                # Appening new line char to second last column if last column was removed
                if self.args.column_number == col_count + 1:
                    cols[-1] += "\n"
                w.write(self.args.separator.join(cols))
                line = r.readline()


def run() -> None:
    RemoveColumnCSV().run()


if __name__ == "__main__":
    run()
