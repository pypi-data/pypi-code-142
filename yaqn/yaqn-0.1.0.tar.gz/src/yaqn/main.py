from . import config
from pathlib import Path
from argparse import ArgumentParser, Namespace
from .gui import Gui
import typing
import sys

def main() -> None:
    parser: ArgumentParser = ArgumentParser(
        prog='yaqn',
        description='A markdown quicknote app made in python and gtk.'
    )

    parser.add_argument(
        '--config',
        default=None,
        required=False,
        dest='custom_config_path',
        help='Set a custom path (absolute) to the config file.',
        type=str,
    )

    parser.add_argument(
        '--check',
        default=False,
        required=False,
        dest='check_mode',
        help='Only run the config file checks and restore it if is necessary.',
        action='store_true',
    )

    args: Namespace = parser.parse_args()

    # Check if the custom config path selected by the user is a dir
    custom_config_path: Path | None
    if args.custom_config_path is not None and Path(args.custom_config_path).is_dir():
        custom_config_path = Path(args.custom_config_path)
    else:
        custom_config_path = None

    config_data: dict[str, typing.Any] = config.read_config(custom_config_path)

    # If check mode is activated not start the gui
    if args.check_mode:
        print('[ INFO ] Check mode -> Config checked and operative')
        sys.exit(0)

    gui: Gui = Gui(config_data['notes_path'], config_data['extension'])
