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


class SplitCSV(CSVUtils):
    prog = "csv-split"
    usage = "%(prog)s file number_of_records [options]"
    description = "This utility is designed to split a large CSV file into small CSV files."

    def add_arguments(self) -> None:
        super().add_arguments()
        self.parser.add_argument(
            "records",
            metavar="number_of_records",
            type=int,
            help="Number of records one file will contain.",
        )
        self.parser.add_argument(
            "--output-prefix",
            type=str,
            metavar="",
            dest="prefix",
            help="Split CSV files prefix. Defaults to split",
            default=f"split-{int(time())}",
        )

    def main(self) -> None:
        with open(self.args.input, "r", encoding=self.args.encoding) as r:
            if self.args.records == 0:
                self.log("number_of_records can not be 0.")
                raise SystemExit()

            line, counter, split_counter = r.readline(), 0, 0

            get_writer = lambda c: open(
                file=f"{self.args.prefix}-{split_counter:03d}.csv",
                mode="w",
                encoding=self.args.encoding,
            )
            writer = get_writer(split_counter)

            while line:
                writer.write(line)
                counter += 1
                line = r.readline()

                if counter % self.args.records == 0 and len(line) > 1:
                    writer.close()
                    split_counter += 1
                    writer = get_writer(split_counter)


def run() -> None:
    SplitCSV().run()


if __name__ == "__main__":
    run()
