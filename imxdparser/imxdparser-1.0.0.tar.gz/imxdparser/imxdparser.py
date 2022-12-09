# parse_intermixed_args is available only on python >= 3.7
import argparse
import sys


class BaseParser:
    """
    Lorem ipsum sit dolor amet
    """

    def __init__(self, **kwargs):
        """
        Lorem ipsum sit dolor amet
        """
        self._kwargs = kwargs
        if sys.version_info[0] == 3 and sys.version_info[1] <= 8:
            self._kwargs.pop("exit_on_error", None)

        self._fg_parser = None
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

    def set_defaults(self, **kwargs):
        """
        set_defaults() allows some additional attributes that are determined without any inspection of the command line
        to be added
        """
        self._not_finalized_fence()
        self._fg_parser.set_defaults(**kwargs)
        self._bg_parser.set_defaults(**kwargs)

    def _finalized_fence(self):
        """
        Lorem ipsum sit dolor amet
        """
        # top parser
        if self._finalized:
            raise RuntimeError("Cannot attach an already finalized parser")
        self._finalized = True

    def _not_finalized_fence(self):
        """
        Lorem ipsum sit dolor amet
        """
        # top parser
        if not self._finalized:
            raise RuntimeError("Parser must be finalized for that action")

    def _get_subparsers(self):
        """
        Lorem ipsum
        """
        # Called by the child on the parent parser
        self._finalized = True
        if not self._subparsers:
            self._subparsers = self._fg_parser.add_subparsers()
        return self._subparsers

    def _rebuild(self):
        """
        Lorem ipsum
        """
        arg_list = self._get_arguments()

        # add dummy positional argument to eat up previous subparsers
        count = max(0, len(arg_list) - 1)
        dummies = argparse.ArgumentParser(add_help=False)
        dummies.add_argument("_imxd_action", nargs=count)

        parents = [dummies]
        parents.extend(arg_list)

        parser = argparse.ArgumentParser(parents=parents)
        return parser


class MainParser(BaseParser):
    """
    Lorem ipsum sit dolor amet
    """

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
        """
        Create a base parser that holds an extra internal argument parser.

        Parameters
        ----------

        prog: dict[str]
            The name of the program (default: sys.argv[0])

        usage:
            A usage message (default: auto-generated from arguments)

        description:
            A description of what the program does

        epilog:
            Text following the argument descriptions

        formatter_class:
            HelpFormatter class for printing help messages. Note: changed from default argparse.HelpFormatter

        prefix_chars:
            Characters that prefix optional arguments

        fromfile_prefix_chars:
            Characters that prefix files containing additional arguments

        argument_default:
            The default value for all arguments

        conflict_handler:
            String indicating how to handle conflicts

        add_help:
            Add a -h/-help option

        allow_abbrev:
            Allow long options to be abbreviated unambiguously

        exit_on_error:
            Determines whether or not ArgumentParser exits with error info when an error occurs
        """
        super().__init__(
            prog=prog,
            usage=usage,
            description=description,
            epilog=epilog,
            formatter_class=formatter_class,
            prefix_chars=prefix_chars,
            fromfile_prefix_chars=fromfile_prefix_chars,
            argument_default=argument_default,
            conflict_handler=conflict_handler,
            add_help=add_help,
            allow_abbrev=allow_abbrev,
            exit_on_error=exit_on_error,
        )
        #

    def _get_arguments(self):
        """
        Get background parser as a list
        """
        return [self._bg_parser]

    def attach(self):
        """
        Lorem ipsum sit dolor amet
        """
        self._finalized_fence()
        self._fg_parser = argparse.ArgumentParser(parents=self._get_arguments(), **self._kwargs)

    def parse_args(self, *args):
        """
        Lorem ipsum sit dolor amet
        """
        # first pass handles help and invalid command lines
        rv = self._fg_parser.parse_args(*args)
        if "_imxd_parser" not in rv:
            return rv

        # pylint: disable=protected-access
        parser = rv._imxd_parser._rebuild()
        rv = parser.parse_intermixed_args(*args)
        del rv._imxd_action
        return rv


class ChildParser(BaseParser):
    """
    Lorem ipsum sit dolor amet
    """

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
            self._kwargs.pop("exit_on_error", None)

        self._parent = parent
        #

    def _get_arguments(self):
        """
        Get recursive arguments as a list
        """
        rv = []
        # pylint: disable=protected-access
        rv.extend(self._parent._get_arguments())
        rv.append(self._bg_parser)
        return rv

    def attach(self):
        """
        Lorem ipsum sit dolor amet
        """
        self._finalized_fence()

        # Get parent subparser, creating it if necessary
        # pylint: disable=protected-access
        parent_subparsers = self._parent._get_subparsers()

        name = self._kwargs.get("prog", "")
        self._fg_parser = parent_subparsers.add_parser(name, parents=self._get_arguments(), **self._kwargs)

        # Set some magic on this parser
        self._fg_parser.set_defaults(_imxd_parser=self)
