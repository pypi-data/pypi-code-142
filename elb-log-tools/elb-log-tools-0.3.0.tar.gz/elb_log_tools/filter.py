#!/usr/bin/env python3
"""
Accepts ELB log records from stdin, emits the requested PATH (sans domain)
Also does not emit lines where the application server responded with a 404
or 30x redirect.

"""
# Copyright 2022 Pymetrics, Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import argparse
import sys
from urllib.parse import urlparse

EXCLUDE_RESPONSE_CODES = ("404", "302", "301")


def filter_logs(opts):
    for line in opts.input_stream:
        parts = line.split(" ")
        try:
            response_code = int(parts[8])
            if response_code in opts.exclude_statuses and not opts.include_statuses:
                continue
            if opts.include_statuses and response_code not in opts.include_statuses:
                continue
            url = parts[12]
            parseresult = urlparse(url)
            print(parseresult.path, file=opts.output_stream)
        except (IndexError, TypeError):
            pass


def main():

    parser = argparse.ArgumentParser()
    status_opts = parser.add_mutually_exclusive_group()
    status_opts.add_argument(
        "-x",
        "--exclude-statuses",
        help="Exclude these HTTP status codes from the output. "
        "Separate multiple values with spaces. "
        f"by default, the following status codes are excluded: {EXCLUDE_RESPONSE_CODES}",
        nargs="*",
        type=int,
        default=EXCLUDE_RESPONSE_CODES,
    )
    status_opts.add_argument(
        "-i",
        "--include-statuses",
        help="Only pass through these HTTP status codes. Separate multiple values "
        "with spaces",
        nargs="*",
        type=int,
        default=[],
    )
    parser.add_argument(
        "--input-stream", type=argparse.FileType("r"), default=sys.stdin
    )
    parser.add_argument(
        "--output-stream", type=argparse.FileType("w"), default=sys.stdout
    )
    opts = parser.parse_args()
    try:
        filter_logs(opts)
    except BrokenPipeError:
        # Happens if e.g. we're being piped into head
        sys.stderr.close()
        sys.exit()


if __name__ == "__main__":
    main()
