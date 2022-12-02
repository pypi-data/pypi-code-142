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

from json import dumps
from json import loads
from time import time

from source.utilities.ndjson.cli import NDJSONUtils


class MergeKeysNDJSON(NDJSONUtils):
    prog = "ndjson-merge-keys"
    usage = "%(prog)s file --keys key1 key2 ... [options]"
    description = (
        "This utility is designed to merge two or more keys of a NDJSON file."
    )

    def add_arguments(self) -> None:
        super().add_arguments()
        self.parser.add_argument(
            "--keys",
            metavar="",
            nargs="+",
            help="Keys that are needs to be merged (Separated by space)",
        )
        self.parser.add_argument(
            "--join-character",
            metavar="",
            type=str,
            default="",
            help="Character to be placed in between while joining the keys. Defaults to nothing",
        )
        self.parser.add_argument(
            "--merge-key-name",
            metavar="",
            type=str,
            help="Key name that you want to give to the merged values",
        )
        self.parser.add_argument(
            "--keep-keys",
            action="store_true",
            default=False,
            help="Flag to control whether to keep individual keys that are merged or not. Default to False",
        )
        self.parser.add_argument(
            "--output-file",
            type=str,
            metavar="",
            dest="output",
            help="Output NDJSON file name",
            default=f"keys-merged-{int(time())}.ndjson",
        )

    def main(self) -> None:
        # Checking Input
        if not self.args.keys:
            self.log("Please specify valid keys to merge.")
            raise SystemExit(1)
        elif len(self.args.keys) == 1:
            self.log("Nothing to merge")
            raise SystemExit(0)

        with (
            open(self.args.input, "r", encoding=self.args.encoding) as r,
            open(self.args.output, "w", encoding=self.args.encoding) as w,
        ):

            # Selecting Merger
            merger = None
            if self.args.keep_keys:
                # Will keep individual keys
                merger = lambda r: list(
                    map(
                        str,
                        filter(
                            lambda v: v is not None,
                            [r.get(key) for key in self.args.keys],
                        ),
                    )
                )
            else:
                # Will remove keys that are going to be merged
                merger = lambda r: list(
                    map(
                        str,
                        filter(
                            lambda v: v is not None,
                            [r.pop(key, None) for key in self.args.keys],
                        ),
                    )
                )

            # Selecting Merging Key Name
            key_name = (
                self.args.merge_key_name
                if self.args.merge_key_name
                else self.args.join_character.join(self.args.keys)
            )

            # Merging Columns
            line = r.readline()
            while line:
                record = loads(line)
                text_to_merge = merger(record)
                record[key_name] = self.args.join_character.join(text_to_merge)
                w.write(dumps(record) + "\n")
                line = r.readline()


def run() -> None:
    MergeKeysNDJSON().run()


if __name__ == "__main__":
    run()
