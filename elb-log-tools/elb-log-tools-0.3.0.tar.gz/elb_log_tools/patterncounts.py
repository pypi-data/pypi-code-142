#!/usr/bin/env python3
"""
Accepts URL paths from stdin, and compares them to a provided list of regex
patterns.

Outputs the patterns + counts as a CSV
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
import csv
import re
import sys
from collections import Counter
from typing import Dict, Optional
from typing.re import Pattern


def load_patterns(filename) -> Dict[Pattern, str]:
    patterns = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line.startswith("/"):
                line = f"/{line}"
            patterns[re.compile(line)] = line
    return patterns


def match_line(pattern_dict: Dict[Pattern, str], line) -> Optional[str]:
    line = line.strip()
    for rgx, pattern in pattern_dict.items():
        if rgx.match(line):
            return pattern
    return None


def print_counter(c: Counter, stream=sys.stdout) -> None:
    writer = csv.writer(stream)
    writer.writerow(["Path", "Hits"])
    for key, value in c.most_common():
        writer.writerow([key, value])


def patterncounts(opts):
    patterns = load_patterns(opts.patternfile)
    ignore_patterns = (
        load_patterns(opts.ignore_patternfile) if opts.ignore_patternfile else {}
    )

    counts = Counter()
    if opts.all:
        # intialize with zero counts, so we can see which patterns never match
        counts.update({pattern: 0 for pattern in patterns.keys()})
    for line in sys.stdin:
        line = line.strip()
        ignore = match_line(ignore_patterns, line)
        if ignore:
            continue
        match = match_line(patterns, line)
        if match:
            counts.update([match])
        else:
            if opts.verbose:
                print(f"No match for path: {line}", file=sys.stderr)
    if opts.output:
        with open(opts.output, "w") as outfile:
            print_counter(counts, stream=outfile)
    else:
        print_counter(counts)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p", "--patternfile", help="File path to a file containing regex patterns."
    )
    parser.add_argument(
        "-i", "--ignore-patternfile", help="File containing regex patterns to ignore"
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Write CSV to this file. Defaults to stdout",
        default=None,
    )
    parser.add_argument(
        "-v", "--verbose", help="Increased verbosity", action="store_true"
    )
    parser.add_argument(
        "-a",
        "--all",
        help="Include patterns with zero matches in the CSV output",
        action="store_true",
    )
    opts = parser.parse_args()
    patterncounts(opts)


if __name__ == "__main__":
    main()
