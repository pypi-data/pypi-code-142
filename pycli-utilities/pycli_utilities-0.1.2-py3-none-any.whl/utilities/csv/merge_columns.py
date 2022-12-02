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


class MergeColumnsCSV(CSVUtils):
    prog = "csv-merge-columns"
    usage = "%(prog)s file [options]"
    description = "This utility is designed to merge two or more columns from a CSV file."

    def add_arguments(self) -> None:
        super().add_arguments()
        self.parser.add_argument(
            "--columns",
            metavar="",
            nargs="+",
            help="Column numbers separated by space to merge (Starts from 1).",
        )
        self.parser.add_argument(
            "--join-character",
            metavar="",
            type=str,
            default="",
            help="Character to be placed in between while joining the columns. Defaults to nothing",
        )
        self.parser.add_argument(
            "--keep-columns",
            action="store_true",
            default=False,
            help="Flag to control whether to keep individual columns that are merged or not. Default to False",
        )
        self.parser.add_argument(
            "--output-file",
            type=str,
            metavar="",
            dest="output",
            help="Output CSV file name",
            default=f"column-merged-{int(time())}.csv",
        )

    def main(self) -> None:
        merge_cols = []

        # Checking Input
        try:
            merge_cols = tuple(map(int, self.args.columns))
        except Exception as ex:
            self.log(f"Operation Failed\nReason: {str(ex)}")
        finally:
            if not merge_cols:
                self.log("Please specify valid columns to merge.")
                raise SystemExit(1)
            elif len(merge_cols) == 1:
                self.log("Nothing to merge")
                raise SystemExit(0)

        with (
            open(self.args.input, "r", encoding=self.args.encoding) as r,
            open(self.args.output, "w", encoding=self.args.encoding) as w,
        ):
            line = r.readline()
            file_columns = line.split(self.args.separator)

            # Validating Input
            if min(merge_cols) < 1 or max(merge_cols) > len(file_columns) + 1:
                self.log("Please specify the correct column locations.")
                raise SystemExit(1)

            # Selecting Merger
            merger = None
            if self.args.keep_columns:
                # Will keep individual columns
                merger = lambda l: [l[col_num - 1] for col_num in merge_cols]
            else:
                # Will remove columns that are going to be merged
                merger = lambda l: [
                    l.pop(col_num - (1 + i))
                    for i, col_num in enumerate(merge_cols)
                ]

            # Merging Columns
            while line:
                _line = line.rstrip("\n")
                _cols = _line.split(self.args.separator)
                _text_to_merge = merger(_cols)
                _cols.append(self.args.join_character.join(_text_to_merge))
                _line = self.args.separator.join(_cols)

                w.write(_line + "\n")
                line = r.readline()


def run() -> None:
    MergeColumnsCSV().run()


if __name__ == "__main__":
    run()
