"""
The IntermixedParser is based on `argparse`, and just like argparse, makes it easy to write user-friendly command-line
interfaces.

The IntermixedParser is tolerant for the location of the arguments, optional or positional.
"""
import argparse


class ParserBase:
    """
    Lorem ipsum
    """

    def __init__(self, *args, add_help=True, **kwargs):
        """
        Lorem ipsum
        """
        # Our self parser
        self._parser = None

        # Both the top and subparsers can have other parsers
        self._subparsers = None

        self._add_help = add_help
        self._args = args
        self._kwargs = kwargs

        # A parser that only holds arguments, and no help
        self._arguments = argparse.ArgumentParser(*args, add_help=False, **kwargs)

    def add_argument(self, *args, **kwargs):
        """
        Lorem ipsum
        """
        self._arguments.add_argument(*args, **kwargs)

    @property
    def subparsers(self):
        """
        Lorem ipsum
        """
        if not self._subparsers:
            self._subparsers = self._parser.add_subparsers()
        return self._subparsers

    @property
    def parser(self):
        """
        Lorem ipsum
        """
        if self._parser is None:
            # We don't have a parent, we're at the top
            self._parser = argparse.ArgumentParser(
                parents=self._arguments_r,
                *self._args,
                add_help=self._add_help,
                **self._kwargs,
            )
        return self._parser

    def set_defaults(self, **kwargs):
        """
        Lorem ipsum
        """
        self.parser.set_defaults(**kwargs)


class MainParser(ParserBase):
    """
    Lorem ipsum
    """

    def __init__(self, add_help=True, **kwargs):
        """
        Lorem ipsum
        """
        super().__init__(add_help=add_help, **kwargs)

    def _recreate(self):
        """
        Lorem ipsum
        """
        arg_list = self._arguments_r

        # add dummy positional argument to eat up previous subparsers
        count = max(0, len(arg_list) - 1)
        dummies = argparse.ArgumentParser(add_help=False)
        dummies.add_argument("action", nargs=count)

        parents = [dummies]
        parents.extend(arg_list)

        parser = argparse.ArgumentParser(parents=parents)
        return parser

    @property
    def _arguments_r(self):
        """
        Get recursive arguments as a list
        """
        return [self._arguments]

    def parse_args(self, *args):
        """
        Lorem ipsum
        """
        # first pass handles help and invalid command lines
        rv = self.parser.parse_args(*args)
        if "parser" not in rv:
            return rv

        parser = rv.parser._recreate()
        rv = parser.parse_intermixed_args(*args)
        return rv


class SubParser(ParserBase):
    """
    Lorem ipsum
    """

    def __init__(
        self,
        parent,
        prog,  # = name
        argument_default=None,
        add_help=True,
        **kwargs,
    ):
        """
        Lorem ipsum

        :params parent: Parent Parser if any

        Keyword Arguments:
            - prog -- The name of the program (default: sys.argv[0])
            - usage -- A usage message (default: auto-generated from arguments)
            - description -- A description of what the program does
            - epilog -- Text following the argument descriptions
            - parents -- Parsers whose arguments should be copied into this one
            - formatter_class -- HelpFormatter class for printing help messages
            - prefix_chars -- Characters that prefix optional arguments
            - fromfile_prefix_chars -- Characters that prefix files containing
                additional arguments
            - argument_default -- The default value for all arguments
            - conflict_handler -- String indicating how to handle conflicts
            - add_help -- Add a -h/-help option
            - allow_abbrev -- Allow long options to be abbreviated unambiguously
            - exit_on_error -- Determines whether or not ArgumentParser exits with
                error info when an error occurs
        """
        self._parent = parent

        super().__init__(add_help=add_help, **kwargs)

        # Get parent subparser, and add our arguments parser to it
        self._parser = self._parent.subparsers.add_parser(prog, parents=self._arguments_r, **kwargs)

    @property
    def arguments(self):
        """
        Get local arguments
        """
        return self._arguments

    @property
    def _arguments_r(self):
        """
        Get recursive arguments as a list
        """
        rv = []
        rv.extend(self._parent._arguments_r)
        rv.append(self._arguments)
        return rv

    def set_defaults(self, *args, **kwargs):
        """
        Lorem ipsum
        """
        return self._parser.set_defaults(*args, **kwargs)
