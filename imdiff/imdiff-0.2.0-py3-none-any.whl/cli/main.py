import argparse
import logging
import pathlib

from . import dir_diff


def parse_args():
    parser = argparse.ArgumentParser(
        prog='imdiff',
        description='''Compare images one by one or directory by directory''')
    parser.add_argument(
        'left', default='.', type=pathlib.Path,
        help='''Image or directory of images to compare.''')
    parser.add_argument(
        'right', default='.', type=pathlib.Path,
        help='''Image or directory of images to compare.''')
    args = parser.parse_args()
    return args


def main():
    #logging.basicConfig(level=logging.DEBUG)
    args = parse_args()
    dir_diff.app(args.left, args.right)
