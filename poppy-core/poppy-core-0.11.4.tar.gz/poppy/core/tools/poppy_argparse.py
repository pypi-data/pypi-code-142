#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

__all__ = ["argparse"]

# make a monkeypatch (I know it is horrible) of the argparse, because of the
# incompatibility of the module from 3.4.2 to 3.4.3, where the defaults
# argument set on a child subparser are not applied if already present in the
# parent subparser, making impossible the definition of a hierarchy in the
# subcommands. This bug is corrected in 3.4.3 and thus we monkeypatch the
# module to make it behaving the same way.


# monkey patch !
def monkeypatch(self, parser, namespace, values, option_string=None):
    parser_name = values[0]
    arg_strings = values[1:]

    # set the parser name if requested
    if self.dest is not argparse.SUPPRESS:
        setattr(namespace, self.dest, parser_name)

    # select the parser
    try:
        parser = self._name_parser_map[parser_name]
    except KeyError:
        args = {'parser_name': parser_name,
                'choices': ', '.join(self._name_parser_map)}
        msg = _('unknown parser %(parser_name)r (choices: %(choices)s)') % args
        raise argparse.ArgumentError(self, msg)

    # parse all the remaining options into the namespace
    # store any unrecognized options on the object, so that the top
    # level parser can decide what to do with them

    # In case this subparser defines new defaults, we parse them
    # in a new namespace object and then update the original
    # namespace for the relevant parts.
    subnamespace, arg_strings = parser.parse_known_args(arg_strings, None)
    for key, value in vars(subnamespace).items():
        setattr(namespace, key, value)

    if arg_strings:
        vars(namespace).setdefault(argparse._UNRECOGNIZED_ARGS_ATTR, [])
        getattr(namespace, argparse._UNRECOGNIZED_ARGS_ATTR).extend(
            arg_strings
        )

argparse._SubParsersAction.__call__ = monkeypatch

