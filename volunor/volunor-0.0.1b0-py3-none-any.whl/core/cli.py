"""
SPDX-FileCopyrightText: 2022. Thomas Mahe <contact@tmahe.dev>
SPDX-License-Identifier: MIT

This work is licensed under the terms of the MIT license.
For a copy, see <https://opensource.org/licenses/MIT>.
"""

import argparse
import os
import sys
import textwrap
import typing

from .command import Command


class VolunorHelpFormatter(argparse.RawTextHelpFormatter):

    def __init__(self, prog: str):
        super().__init__(prog, width=80, max_help_position=35)

    def _format_action(self, action):
        if type(action) == argparse._SubParsersAction:
            # inject new class variable for subcommand formatting
            subactions = action._get_subactions()
            invocations = [self._format_action_invocation(a) for a in subactions]
            self._subcommand_max_length = max(len(i) for i in invocations)

        if type(action) == argparse._SubParsersAction._ChoicesPseudoAction:
            # format subcommand help line
            subcommand = self._format_action_invocation(action)  # type: str
            width = self._subcommand_max_length
            help_text = ""
            if action.help:
                help_text = self._expand_help(action)

            if len(help_text) > 0:
                first_section = "  {} {} ".format(subcommand, "." * (width + 4 - len(subcommand)))
                return "{}{}\n".format(first_section,
                                       textwrap.shorten(help_text, width=80 - len(first_section), placeholder="..."),
                                       width=width)
            else:
                return "  {}\n".format(subcommand, width=width)

        elif type(action) == argparse._SubParsersAction:
            # process subcommand help section
            msg = ''
            for subaction in action._get_subactions():
                msg += self._format_action(subaction)
            return msg
        else:
            return super(VolunorHelpFormatter, self)._format_action(action)

    def _format_action_invocation(self, action):
        # print(action)
        if not action.option_strings:
            metavar, = self._metavar_formatter(action, action.dest)(1)
            return metavar
        else:
            # print(action.required)
            parts = []
            if action.nargs == 0:
                parts.extend(action.option_strings)
            else:
                default = action.dest.upper()
                args_string = self._format_args(action, default)
                for option_string in action.option_strings:
                    parts.append('%s' % option_string)
                parts[-1] += ' %s' % args_string
            return ', '.join(parts)


class Cli(object):
    _cli: argparse.ArgumentParser = None

    def __init__(self, descriptor, prog=os.path.basename(sys.argv[0])):
        self._descriptor = descriptor
        self._parser = argparse.ArgumentParser(prog=prog, add_help=False, formatter_class=VolunorHelpFormatter)
        self._optional_args = self._parser.add_argument_group("optional arguments")
        self._optional_args.add_argument("-h", "--help", action="help", help="show this help message and exit")
        self._parser.add_argument('--_VOLUNOR_CURRENT_PARSER', required=False, default=self._parser,
                                  help=argparse.SUPPRESS)

        if isinstance(descriptor, typing.Dict):
            self._cli = self._from_dict(self._parser, descriptor)

    def _from_dict(self, parser: argparse.ArgumentParser, descriptor=None, level=0):
        if issubclass(type(descriptor), Command.__class__):
            parser.add_argument('--_VOLUNOR_CALLABLE_COMMAND', required=False, default=descriptor,
                                help=argparse.SUPPRESS)

            required_args = parser.add_argument_group("required arguments")
            optional_args = parser.add_argument_group("optional arguments")
            optional_args.add_argument("-h", "--help", action="help", help="show this help message and exit")
            descriptor.volunor_args(descriptor, required_args, optional_args)

        if isinstance(descriptor, typing.Dict) and descriptor.keys().__len__() > 0:
            sub_parser = parser.add_subparsers(title="commands", metavar="COMMAND")

            for key, item in descriptor.items():
                command_sub_parser = sub_parser.add_parser(name=key, help="", formatter_class=VolunorHelpFormatter, add_help=False)
                _optional_args = command_sub_parser.add_argument_group("optional arguments")
                _optional_args.add_argument("-h", "--help", action="help", help="show this help message and exit")
                command_sub_parser.add_argument('--_VOLUNOR_CURRENT_PARSER', required=False, default=command_sub_parser,
                                                help=argparse.SUPPRESS)
                self._from_dict(command_sub_parser, item, level+1)

        return parser

    def _filtered_args(self, p: argparse.Namespace):
        out = p.__dict__
        del out['_VOLUNOR_CALLABLE_COMMAND']
        return out

    def print_help(self, file=None):
        self._cli.print_help(file)

    def big_gang(self):
        r_code = 0
        args = self._cli.parse_args()
        if hasattr(args, "_VOLUNOR_CALLABLE_COMMAND"):
            return_value = args._VOLUNOR_CALLABLE_COMMAND()(**self._filtered_args(args))
            if return_value is None:
                r_code = 0
            elif type(return_value) is int:
                r_code = return_value
            else:
                r_code = 1
        else:
            args._VOLUNOR_CURRENT_PARSER.print_help()

        sys.exit(r_code)
