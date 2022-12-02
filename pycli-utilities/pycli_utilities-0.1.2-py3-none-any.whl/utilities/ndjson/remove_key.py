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


class RemoveKeyNDJSON(NDJSONUtils):
    prog = "ndjson-remove-key"
    usage = "%(prog)s file keyName [options]"
    description = "This utility is designed to remove a particular key from every record of NDJSON file."

    def add_arguments(self) -> None:
        super().add_arguments()
        self.parser.add_argument(
            "key_name",
            metavar="key",
            type=str,
            help="Key's name that you want to remove from every record.",
        )
        self.parser.add_argument(
            "--output-file",
            type=str,
            metavar="",
            dest="output",
            help="Output NDJSON file name",
            default=f"key-removed-ndjson-{int(time())}.ndjson",
        )

    def main(self) -> None:
        with (
            open(self.args.input, "r", encoding=self.args.encoding) as ro,
            open(self.args.output, "w", encoding=self.args.encoding) as wo,
        ):
            line = ro.readline()
            while line:
                try:
                    record: dict = loads(line)
                    if record.get(self.args.key_name, None) is not None:
                        record.pop(self.args.key_name)
                    wo.write(
                        dumps(record, sort_keys=self.args.sort_keys) + "\n"
                    )
                except Exception as ex:
                    self.log(f"Operation Failed\nReason: {str(ex)}")
                    break
                line = ro.readline()
            else:
                self.log("Operation Completed Successfully")


def run() -> None:
    RemoveKeyNDJSON().run()


if __name__ == "__main__":
    run()
