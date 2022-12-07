#!/usr/bin/env python3
"""
Icinga2/Nagios plugin using the `tftp` command to monitor a TFTP server by
downloading a file from the server and optionally verifying its contents
"""

import argparse
import hashlib
import io
import logging
import math
import re
import sys
import time
from typing import Optional

import nagiosplugin  # type:ignore
import tftpy  # type:ignore


# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
class TftpDownload:
    """
    Manage the configuration and execution of the tftp download
    """

    def __init__(
        self,
        *,
        rfile: str,
        host: str,
        lfile: str,
        port: int,
        retries: int = 0,
        timeout: Optional[int] = None,
    ):
        self.rfile = rfile
        self.host = host
        self.lfile = lfile
        self.port = port
        self.retries = retries
        self.timeout = timeout

    def run(self):
        """
        Run tftp as configured and return the results
        """
        tclient = tftpy.TftpClient(
            self.host,
            self.port,
            {"blksize": 512},
            "",  # Can hook a progress bar here
        )
        try:
            tclient.download(
                self.rfile,
                self.lfile,
                timeout=self.timeout,
                retries=0,
            )
        except tftpy.TftpException as err:
            raise Exception(err) from err


# pylint: enable=too-few-public-methods
# pylint: enable=too-many-instance-attributes


def parse_args(argv=None) -> argparse.Namespace:
    """Parse args"""

    usage_examples: str = """examples:

        # Check that a file can be downloaded from a tftp server:

        %(prog)s --hostname host.name.tld some.file

        # As above, but check for pattern in the file:

        %(prog)s --hostname host.name.tld --pattern 'some text' some.file

        # Or verify the file by md5 checksum:

        %(prog)s --hostname host.name.tld \\
            --checksum 75170fc230cd88f32e475ff4087f81d9 some.file

        # WARN if download takes longer than 5s, CRIT if longer than 10s:

        %(prog)s --hostname host.name.tld --warning 5 --critical 10 some.file

        # For more on how to set ranges for warning or critical, see Nagios
        # Plugin Development Guidelines:
        #
        # https://nagios-plugins.org/doc/guidelines.html#THRESHOLDFORMAT

    """
    descr: str = """
        Icinga2/Nagios plugin monitors a TFTP server by downloading a file from
        the server and optionally verifying its contents
        """
    parser = argparse.ArgumentParser(
        description=descr,
        epilog=usage_examples,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "--checksum",
        "-k",
        help=("MD5 checksum to verify the remote file"),
        type=str,
    )
    group.add_argument(
        "--pattern",
        "-r",
        help=(
            "Python regular expression to look for in the remote file. The "
            "check will fail if the pattern is not present."
        ),
        type=str,
    )

    parser.add_argument(
        "--critical",
        "-c",
        help=("Critical range for download duration in seconds"),
        type=str,
    )

    parser.add_argument(
        "--hostname",
        "-H",
        dest="host",
        help=("The TFTP server address"),
        required=True,
        type=str,
    )

    parser.add_argument(
        "--port",
        "-p",
        default=69,
        help=("The TFTP server port"),
        type=int,
    )

    parser.add_argument(
        "--timeout",
        "-t",
        help=("Total transmission timeout for the file transfer."),
        type=int,
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        default=0,
        dest="verbosity",
        help="Set output verbosity (-v=warning, -vv=debug)",
    )

    parser.add_argument(
        "--warning",
        "-w",
        help=("Warning range for download duration in seconds"),
        type=str,
    )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    def string_not_containing_error(string) -> str:
        if "error" in string.lower():
            raise argparse.ArgumentTypeError("value must not contain `/error/i`")
        return string

    parser.add_argument(
        "file",
        help="The remote path of the file to check",
        metavar="files",
        type=string_not_containing_error,
    )

    args = parser.parse_args(argv) if argv else parser.parse_args()

    if args.verbosity >= 2:
        log_level = logging.DEBUG
    elif args.verbosity >= 1:
        log_level = logging.INFO
    else:
        log_level = logging.WARNING

    logging.basicConfig(level=log_level)

    return args


# pylint: disable=too-few-public-methods
class TftpReq(nagiosplugin.Resource):
    """
    Nagios plugin to check a file on a tftp server
    """

    def __init__(
        self,
        *,
        checksum: Optional[str],
        lfile: Optional[str],
        pattern: Optional[str],
        tftp: TftpDownload,
        timeout: int,
    ):
        if (checksum or pattern) and not lfile:
            raise ValueError(
                "If `checksum` or `pattern` are provided, a file path is also required"
            )
        self.checksum: Optional[str] = checksum
        self.pattern: Optional[str] = pattern
        self.lfile: Optional[str] = lfile
        self.tftp: TftpDownload = tftp
        self.timeout: int = timeout

    def probe(self):
        """
        Run the check itself
        """
        tstart = time.time()
        self.tftp.run()
        duration = math.ceil(time.time() - tstart)
        if self.checksum:
            if hashlib.md5(self.lfile.getvalue()).hexdigest() != self.checksum:
                raise Exception(f"File did not match checksum /{self.checksum}/")
            logging.info("File checksum matches")
        if self.pattern:
            if not re.search(
                re.compile(self.pattern), self.lfile.getvalue().decode("utf-8")
            ):
                raise Exception(f"File did not contain regex /{self.pattern}/")
            logging.info("Pattern is present in the file")
        yield nagiosplugin.Metric(
            "download_duration",
            duration,
            context="duration",
        )


# pylint: enable=too-few-public-methods


@nagiosplugin.guarded
def main():
    """Main"""

    args = parse_args(sys.argv[1:])
    logging.debug("Argparse results: %s", args)

    with io.BytesIO() as tempfileobj:
        tftp = TftpDownload(
            rfile=args.file,
            host=args.host,
            lfile=tempfileobj,
            port=args.port,
            timeout=args.timeout,
        )
        tftpfile = TftpReq(
            checksum=args.checksum,
            lfile=tempfileobj,
            pattern=args.pattern,
            tftp=tftp,
            timeout=args.timeout,
        )
        context = nagiosplugin.ScalarContext(
            "duration",
            args.warning,
            args.critical,
            fmt_metric=f"File {args.file} downloaded in {{value}}s",
        )
        check = nagiosplugin.Check(tftpfile, context)
        check.main(args.verbosity)


if __name__ == "__main__":
    main()
