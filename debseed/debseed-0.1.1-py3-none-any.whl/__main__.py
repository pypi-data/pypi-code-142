from __future__ import annotations
import argparse, sys, logging, logging.config, os, atexit
from types import FunctionType
from .listiso import listiso
from .check import check
from .update import update
from .download import download
from .generate import generate
from .publish import publish
from .utils import RED, GREEN, YELLOW, CYAN, GRAY, BOLD_RED, RESET
from . import __version__


def main():
    configure_logging()

    parser = argparse.ArgumentParser(prog="debseed", description="Create ISO images to automate Debian installations, by appending a preseed file to Debian official images.")
    parser.add_argument('--version', action='version', version=f"%(prog)s {__version__}")
    
    add_func_command(parser, listiso)
    add_func_command(parser, check)
    add_func_command(parser, update)
    add_func_command(parser, download)
    add_func_command(parser, generate)
    add_func_command(parser, publish)

    exec_command(parser)


def add_func_command(parser: argparse.ArgumentParser, func: FunctionType, add_arguments: FunctionType = None, name: str = None, doc: str = None):
    """
    Add the given function as a subcommand of the parser.
    """
    # Determine help strings (from function docstring)
    if doc is None:
        doc = func.__doc__
    description = get_description_text(doc)
    help = get_help_text(doc)

    # Determine command options
    if name is None:
        name = getattr(func, 'command_name', func.__name__)  # may be defined using @command decorator

    if add_arguments is None:
        add_arguments = getattr(func, 'add_arguments', None)  # may be defined using @command decorator

    # Determine command parser object
    subparsers = get_subparsers(parser)
    cmdparser = subparsers.add_parser(name, help=help, description=description, formatter_class=argparse.RawTextHelpFormatter)

    # Add command
    if add_arguments:
        add_arguments(cmdparser)

    if 'func' in cmdparser._defaults:
        raise ValueError(f"{name} command already has a registered func")
    cmdparser.set_defaults(func=func)
    
    return cmdparser


def get_subparsers(parser: argparse.ArgumentParser) -> argparse._SubParsersAction:
    """
    Get or create the subparsers object associated with the given parser.
    """
    if parser._subparsers is not None:
        return next(filter(lambda action: isinstance(action, argparse._SubParsersAction), parser._subparsers._actions))
    else:
        return parser.add_subparsers()


def get_help_text(docstring: str):
    if docstring is None:
        return None
    
    docstring = docstring.strip()
    try:
        return docstring[0:docstring.index('\n')].strip()
    except:
        return docstring


def get_description_text(docstring: str):
    if docstring is None:
        return None
    
    description = None
    indent_size = 0
    
    for line in docstring.splitlines(keepends=False):
        if description:
            description += '\n' + line[indent_size:]
        else:
            indent_size = 0
            for char in line:
                if char not in [' ', '\t']:
                    description = line[indent_size:]
                    break
                else:
                    indent_size += 1

    return description


def run_command(parser: argparse.ArgumentParser, *args, default_func: FunctionType = None, default_add_arguments: FunctionType = None):
    """
    Run the command-line application, returning command result.
    """    
    args, unknown = parser.parse_known_args(*args)
    args = vars(args)
    func = args.pop('func', None)

    if func:
        if unknown:
            parser.print_usage(file=sys.stderr)
            print(f"{parser.prog}: error: unrecognized arguments: {' '.join(unknown)}", file=sys.stderr)
            return 2

    elif default_func:
        default_parser = argparse.ArgumentParser(prog=f"{parser.prog} (default)")

        if default_add_arguments:
            default_add_arguments(default_parser)

        args = vars(default_parser.parse_args(*args))
        func = default_func

    else:
        print(f"{RED}missing command name{RESET}", file=sys.stderr)
        return 2

    return func(**args)


def exec_command(parser: argparse.ArgumentParser, *args, default_func: FunctionType = None, default_add_arguments: FunctionType = None):
    """
    Run the command-line application and exit with appropriate return code.
    """
    r = run_command(*args, parser=parser, default_func=default_func, default_add_arguments=default_add_arguments)
    if not isinstance(r, int):
        r = 0 if r is None or r is True else 1
    sys.exit(r)


class ColoredRecord:
    LEVELCOLORS = {
        logging.DEBUG:     GRAY,
        logging.INFO:      '',
        logging.WARNING:   YELLOW,
        logging.ERROR:     RED,
        logging.CRITICAL:  BOLD_RED,
    }

    def __init__(self, record: logging.LogRecord):
        # The internal dict is used by Python logging library when formatting the message.
        # (inspired from library "colorlog").
        self.__dict__.update(record.__dict__)
        self.__dict__.update({
            'levelcolor': self.LEVELCOLORS.get(record.levelno, ''),
            'red': RED,
            'green': GREEN,
            'yellow': YELLOW,
            'cyan': CYAN,
            'gray': GRAY,
            'bold_red': BOLD_RED,
            'reset': RESET,
        })


class ColoredFormatter(logging.Formatter):
    def formatMessage(self, record: logging.LogRecord) -> str:
        """Format a message from a record object."""
        wrapper = ColoredRecord(record)
        message = super().formatMessage(wrapper)
        return message


class CountHandler(logging.Handler):
    def __init__(self, level=logging.WARNING):
        self.counts: dict[int, int] = {}
        atexit.register(self.print_counts)
        super().__init__(level=level)

    def print_counts(self):
        msg = ""

        levelnos = sorted(self.counts.keys(), reverse=True)
        for levelno in levelnos:
            levelname = logging.getLevelName(levelno)
            levelcolor = ColoredRecord.LEVELCOLORS.get(levelno, '')
            msg += (", " if msg else "") + f"{levelcolor}%s{RESET}" % levelname + ": %d" % self.counts[levelno]

        if msg:
            print("Logged " + msg)

    def emit(self, record: logging.LogRecord):
        if record.levelno >= self.level:
            if not record.levelno in self.counts:
                self.counts[record.levelno] = 1
            else:
                self.counts[record.levelno] += 1


def configure_logging():
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'color': {
                '()': ColoredFormatter.__module__ + '.' + ColoredFormatter.__qualname__,
                'format': '%(levelcolor)s%(levelname)-8s%(reset)s %(gray)s[%(name)s]%(reset)s %(levelcolor)s%(message)s%(reset)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'color',
            },
            'count': {
                'class': CountHandler.__module__ + '.' + CountHandler.__qualname__,
                'level': 'WARNING',
            },
        },
        'root': {
            'level': os.environ.get('LOG_LEVEL', 'INFO').upper(),
            'handlers': ['console', 'count'],
        },
    })


if __name__ == '__main__':
    main()
