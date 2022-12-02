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


class ShiftColumnCSV(CSVUtils):
    prog = "csv-shift-column"
    usage = "%(prog)s file from_location to_location [options]"
    description = "This utility is designed to shift (not swap) particular column of a CSV file."

    def add_arguments(self) -> None:
        super().add_arguments()
        self.parser.add_argument(
            "from_location",
            metavar="from_location",
            type=int,
            help="Column's number which needs to be shifted (Starting from 1).",
        )
        self.parser.add_argument(
            "to_location",
            metavar="to_location",
            type=int,
            help="Column's number where column needs to be placed (Starting from 1).",
        )
        self.parser.add_argument(
            "--output-file",
            type=str,
            metavar="",
            dest="output",
            help="Output CSV file name",
            default=f"column-shifted-csv-{int(time())}.csv",
        )

    def main(self) -> None:
        with (
            open(self.args.input, "r", encoding=self.args.encoding) as r,
            open(self.args.output, "w", encoding=self.args.encoding) as w,
        ):
            line = r.readline()
            col_count = line.count(self.args.separator) + 1

            # Validating shifting locations
            if (
                not 1 <= self.args.from_location <= col_count
                and not 1 <= self.args.to_location <= col_count
            ):
                self.log("Invalid shift locations passed !!")
                raise SystemExit()

            while line:
                columns = line.split(self.args.separator)
                shift_content = columns.pop(self.args.from_location - 1)

                # Handling new line
                if self.args.from_location == col_count:
                    shift_content = shift_content.rstrip("\n")
                    columns[-1] += "\n"
                if self.args.to_location == col_count:
                    columns[-1] = columns[-1].rstrip("\n")
                    shift_content += "\n"

                columns.insert(self.args.to_location - 1, shift_content)
                w.write(self.args.separator.join(columns))

                line = r.readline()


def run() -> None:
    ShiftColumnCSV().run()


if __name__ == "__main__":
    run()
