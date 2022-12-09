import argparse
import os
import sys

from imxdparser import SubParser

from . import duplicate


def main(main_parser, parser_error):
    project_badge = SubParser(main_parser, "project-badge")
    project_badge.set_defaults(func=parser_error)

    duplicate.main(project_badge)
