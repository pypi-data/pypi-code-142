from mybar.base import Bar, Config
from mybar import cli

from typing import NoReturn


def main() -> NoReturn:
    '''A command line utility...'''
    parser = cli.Parser()
    # print([a.dest for a in parser._actions])
    try:
        params = parser.parse_from_stdin()
    except cli.UnrecoverableError as e:
        parser.error(e.msg)
        # parser.error(e.args[0])
    bar = Bar.from_dict(params)
    bar.run()

    # argnames = [(a.option_strings[0], a.metavar or a.dest.upper()) for a in parser._actions]
    # print(argnames)

main()

