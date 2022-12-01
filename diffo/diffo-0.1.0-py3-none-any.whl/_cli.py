import argparse
from pathlib import Path
from sys import version_info

from .__about__ import __version__
from ._paths import diff_paths


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u",
        action="store_true",
        default=False,
        help="Produce a unified format diff (default)",
    )
    parser.add_argument(
        "-c",
        action="store_true",
        default=False,
        help="Produce a context format diff",
    )
    parser.add_argument(
        "-m",
        action="store_true",
        default=False,
        help="Produce HTML side by side diff (can use -c and -l in conjunction)",
    )
    parser.add_argument(
        "-n",
        action="store_true",
        default=False,
        help="Produce a ndiff format diff",
    )
    parser.add_argument(
        "-l",
        "--lines",
        type=int,
        default=3,
        help="Set number of context lines (default: 3)",
    )
    parser.add_argument(
        "-nc",
        "--no-color",
        action="store_true",
        default=False,
        help="Don't color output (default: do color)",
    )
    parser.add_argument("frompath")
    parser.add_argument("topath")

    python_version = f"{version_info.major}.{version_info.minor}.{version_info.micro}"
    version_text = f"diffo {__version__}, Python {python_version}"

    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=version_text,
    )

    options = parser.parse_args()

    if options.c:
        fmt = "c"
    elif options.n:
        fmt = "n"
    elif options.m:
        fmt = "m"
    else:
        fmt = "u"

    a = Path(options.frompath)
    b = Path(options.topath)

    diffs = diff_paths(a, b, num_context_lines=options.lines, fmt=fmt)

    for k, d in enumerate(diffs):
        d.print(color=not options.no_color)
        # interleave with empty line
        if k < len(diffs) - 1:
            print()
