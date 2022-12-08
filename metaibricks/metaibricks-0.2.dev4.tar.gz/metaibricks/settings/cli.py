import argparse

import metaibricks as mab
from metaibricks.settings.settings import Settings


class CLI:
    """Class for centralizing mataibricks's Command Line Interface"""

    def __init__(self) -> None:
        self.parser = self.get_parser()

    def get_parser(self):
        version_header = f"{mab.__name__} ({mab.__version__})"
        parser = argparse.ArgumentParser(prog=f"{version_header}")
        # version
        parser.add_argument("--version", action="version", version=version_header)
        # netrc file
        parser.add_argument(
            "--netrc-filename",
            help=(
                "Netrc file's name where to store the credentials."
                " Default is ~/.netrc."
            ),
        )
        # logging
        parser.add_argument(
            "--log-level",
            help="The logging level.",
            choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        )
        parser.add_argument(
            "--log-file-name",
            default=None,
            type=str,
            help="The logging file's name.",
        )
        parser.add_argument(
            "--log-file-level",
            help="The logging level of the given log file.",
            choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        )
        return parser

    def parse_args(
        self, args: list = None, namespace: argparse.Namespace = None
    ) -> argparse.Namespace:
        # retrieving args
        parsed_args = self.parser.parse_args(args=args, namespace=namespace)

        Settings.clean()
        Settings.set(**parsed_args.__dict__)

        return parsed_args
