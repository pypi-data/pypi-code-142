# parse_intermixed_args is available only on python >= 3.7
import argparse
import sys


class BaseParser:
    def __init__(self):
        self._parser = None
        self._parent = None
        self._finalized = False
        self._subparsers = None
        self._bg_parser = argparse.ArgumentParser(add_help=False)

    def add_argument(self, *args, **kwargs):
        """
        The add_argument() method attaches individual argument specifications to the parser. It supports positional
        arguments, options that accept values, and on/off flags.
        """
        if self._finalized:
            raise RuntimeError("Cannot add arguments to a parser that has been finalized")
        self._bg_parser.add_argument(*args, **kwargs)

    @property
    def subparsers(self):
        if not self._subparsers:
            self._subparsers = self._parser.add_subparsers()
        return self._subparsers

    def _rebuild(self):
        arg_list = self._get_arguments()

        # add dummy positional argument to eat up previous subparsers
        count = max(0, len(arg_list) - 1)
        dummies = argparse.ArgumentParser(add_help=False)
        dummies.add_argument("_imxd_action", nargs=count)

        parents = [dummies]
        parents.extend(arg_list)

        parser = argparse.ArgumentParser(parents=parents)
        parser.set_defaults(func=self._func_fn)
        return parser


class TopParser(BaseParser):
    def __init__(
        self,
        prog: str = None,
        usage: str = None,
        description: str = None,
        epilog: str = None,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prefix_chars: str = "-",
        fromfile_prefix_chars: str = None,
        argument_default=None,
        conflict_handler: str = "error",
        add_help: bool = True,
        allow_abbrev: bool = True,
        exit_on_error: bool = True,
    ):
        super().__init__()
        self._kwargs = {
            "prog": prog,
            "usage": usage,
            "description": description,
            "epilog": epilog,
            "formatter_class": formatter_class,
            "prefix_chars": prefix_chars,
            "fromfile_prefix_chars": fromfile_prefix_chars,
            "argument_default": argument_default,
            "conflict_handler": conflict_handler,
            "add_help": add_help,
            "allow_abbrev": allow_abbrev,
            "exit_on_error": exit_on_error,
        }
        if sys.version_info[0] == 3 and sys.version_info[1] <= 8:
            self._kwargs.pop("exit_on_error")
        #

    def _get_arguments(self):
        """
        Get recursive arguments as a list
        """
        return [self._bg_parser]

    def attach(
        self,
        final=False,
        func_fn=None,
    ):
        # top parser
        if self._finalized:
            raise RuntimeError("Cannot attach an already finalized parser")
        self.finalized = True
        self._func_fn = func_fn

        # If we don't have a parent, then we're at the top
        self._parser = argparse.ArgumentParser(parents=self._get_arguments())

        # Set some magic on this parser
        if func_fn:
            self._parser.set_defaults(func=func_fn)

        if final:
            self._parser.set_defaults(parser=self)

    def parse_args(self, *args):
        """
        Lorem ipsum
        """
        # first pass handles help and invalid command lines
        rv = self._parser.parse_args(*args)
        if "parser" not in rv:
            return rv

        parser = rv.parser._rebuild()
        rv = parser.parse_intermixed_args(*args)
        del rv._imxd_action
        return rv


class ChildParser(BaseParser):
    def __init__(
        self,
        parent=None,
        prog: str = None,
        usage: str = None,
        description: str = None,
        epilog: str = None,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prefix_chars: str = "-",
        fromfile_prefix_chars: str = None,
        argument_default=None,
        conflict_handler: str = "error",
        add_help: bool = True,
        allow_abbrev: bool = True,
        exit_on_error: bool = True,
    ):
        super().__init__()
        self._kwargs = {
            "prog": prog,
            "usage": usage,
            "description": description,
            "epilog": epilog,
            "formatter_class": formatter_class,
            "prefix_chars": prefix_chars,
            "fromfile_prefix_chars": fromfile_prefix_chars,
            "argument_default": argument_default,
            "conflict_handler": conflict_handler,
            "add_help": add_help,
            "allow_abbrev": allow_abbrev,
            "exit_on_error": exit_on_error,
        }
        if sys.version_info[0] == 3 and sys.version_info[1] <= 8:
            self._kwargs.pop("exit_on_error")

        self._parent = parent
        #

    def _get_arguments(self):
        """
        Get recursive arguments as a list
        """
        rv = []
        rv.extend(self._parent._get_arguments())
        rv.append(self._bg_parser)
        return rv

    def attach(
        self,
        final=False,
        func_fn=None,
    ):
        # child parser
        if self._finalized:
            raise RuntimeError("Cannot attach an already finalized parser")
        self.finalized = True
        self._func_fn = func_fn

        # Get parent subparser, creating it if necessary
        parent_subparsers = self._parent.subparsers

        name = self._kwargs.get("prog", "")
        self._parser = parent_subparsers.add_parser(name, parents=self._get_arguments())

        # Set some magic on this parser
        if func_fn:
            self._parser.set_defaults(func=func_fn)

        if final:
            self._parser.set_defaults(parser=self)
