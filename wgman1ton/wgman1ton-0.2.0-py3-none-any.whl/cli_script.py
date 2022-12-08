#!/usr/bin/env python
import sys
import wgman1ton


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    manager = wgman1ton.Manager(args)
    manager.execute()


if __name__ == "__main__":
    main()
