# parse_intermixed_args is available only on python >= 3.7
import argparse


class IntermixedParser:
    """
    Implement a "smart" parser, or at least a more tolerant one.
    To be more specific, argument order matters with subparsers, and because of recusivity in
    the argparser namespace variable used by parse_args, they will be overwritten and set
    to none in case of order mismatch.

    In order to achieve tolerance, and allow
      foobar one two --id 42
    to be the same as
      foobar one --id 42 two
    we'll create a two stage parser.

    The second stage parser does not use subparsers, but adds positional arguments to eat up
    the argument.

    This effectively allows an argument to be valid from the subparser, up until end of the line.

    Why all this mess?
    So that the public API does not change if we can move a parameter up or down the chain.
    """

    def __init__(self, parent=None, name=None, description=None, arguments_fn=None, reparse=False, func_fn=None):
        """
        :params parent: Parent Parser if any
        :params name: Name of the parser, required when it's a subparser.
        :params description:
        :params arguments_fn: Function to call to add arguments to this parser
        :params reparse: If true, then reparse with the second stage parser
        :params func_fn: Set default 'action' to this function
        """

        self._parent = parent
        self._name = name
        self._description = description
        self._parser = None
        self._subparsers = None
        self._func_fn = func_fn

        # Add the arguments by calling the optional callback
        self._arguments = argparse.ArgumentParser(
            add_help=False,
            description=self._description,
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )
        if arguments_fn:
            arguments_fn(self._arguments)

        # If we don't have a parent, then we're at the top
        if not self._parent:
            self._parser = argparse.ArgumentParser(description=self._description, parents=self._arguments_r)
        else:
            # Get parent subparser, creating it if necessary
            parent_subparsers = self._parent.subparsers
            self._parser = parent_subparsers.add_parser(
                self._name,
                description=self._description,
                parents=self._arguments_r,
                formatter_class=argparse.RawDescriptionHelpFormatter,
            )

        # Set some magic on this parser
        if func_fn:
            self._parser.set_defaults(func=func_fn)

        if reparse:
            self._parser.set_defaults(parser=self)

    def recreate(self):
        arg_list = self._arguments_r

        # add dummy positional argument to eat up previous subparsers
        count = max(0, len(arg_list) - 1)
        dummies = argparse.ArgumentParser(add_help=False)
        dummies.add_argument("action", nargs=count)

        parents = [dummies]
        parents.extend(arg_list)

        parser = argparse.ArgumentParser(parents=parents)
        parser.set_defaults(func=self._func_fn)
        return parser

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
        if not self._parent:
            return [self._arguments]

        rv = []
        rv.extend(self._parent._arguments_r)
        rv.append(self._arguments)
        return rv

    @property
    def parser(self):
        return self._parser

    @property
    def subparsers(self):
        if not self._subparsers:
            self._subparsers = self.parser.add_subparsers()
        return self._subparsers

    def set_defaults(self, *args, **kwargs):
        return self._parser.set_defaults(*args, **kwargs)

    def parse_args(self, *args):
        # first pass handles help and invalid command lines
        rv = self._parser.parse_args(*args)
        if "parser" not in rv:
            return rv

        parser = rv.parser.recreate()
        rv = parser.parse_intermixed_args(*args)
        return rv

    def add_subparser(self, func):
        return func(self, IntermixedParser)
