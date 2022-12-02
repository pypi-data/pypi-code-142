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

from argparse import ArgumentParser
from sys import stdout
from time import time

from source.helpers import path_validate


class CLIUtils:
    prog = ""
    description = ""
    usage = ""
    epilog = "Feel free to suggest new features / improvements at https://github.com/itsthevp"

    def __init__(self) -> None:
        self.__log_stream = stdout
        self.__base_parser()
        self.add_arguments()
        self.args = self.parser.parse_args()

        # Checking for output stream
        if self.args.log_file != stdout:
            self.__log_stream = open(self.args.log_file, mode="w")

    def add_arguments(self) -> None:
        """This method is for adding utility specific arguments"""
        self.parser.add_argument(
            "--log-file",
            metavar="",
            type=path_validate,
            default=stdout,
            help="File to write logs. Defaults to stdout.",
        )

    def run(self) -> None:
        start_time = time()
        try:
            self.main()
        except Exception as ex:
            self.log("Operation Failed: %s" % str(ex))
        finally:
            self.log(
                "Execution completed in %s seconds" % (time() - start_time)
            )
            # Closing the log stream
            self.__log_stream.close()

    def log(self, text: str) -> None:
        """logs the message to output stream

        Args:
            text (str): text to log
        """
        print(text, file=self.__log_stream)

    def main(self) -> None:
        """Utility's main logic block

        Raises:
            NotImplementedError: This needs to be defined by every utility
        """
        raise NotImplementedError

    def __base_parser(self):
        # Base parser initialization
        self.parser = ArgumentParser(
            prog=self.prog,
            usage=self.usage,
            description=self.description,
            epilog=self.epilog,
        )
