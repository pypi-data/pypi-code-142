import sys
from argparse import ArgumentParser, Namespace

import cpast.check as check
import cpast.core as core


parser = ArgumentParser()
parser.add_argument('-d', '--date',
                    help='Commit date, example: 2021-12-25',
                    required=True, type=str, default=None)
parser.add_argument('-t', '--time',
                    help='Commit time, example: 22:13:05',
                    required=True, type=str, default=None)
parser.add_argument('-m', '--message',
                    help='Commit message, example: "init :)"',
                    required=True, type=str, default=None)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args: Namespace = parser.parse_args()
        if (check.run(args.date, args.time)):
            core.run(args.date, args.time, args.message)
