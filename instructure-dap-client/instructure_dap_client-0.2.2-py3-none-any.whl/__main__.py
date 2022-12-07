import argparse
import dataclasses
import logging
import os
from datetime import datetime
from pprint import pprint
from typing import Optional

from .api import DAPClient
from .arguments import EnumAction, environment_default, valid_utc_datetime, valid_base64
from .dap_error import OperationError
from .dap_types import Format, IncrementalQuery, SnapshotQuery


class Arguments(argparse.Namespace):
    base_url: str
    api_key: str
    loglevel: str

    namespace: str
    table: str
    format: Format
    output_directory: str

    since: datetime
    until: Optional[datetime]


# prints the main and the subparser help messages at the same time
class _HelpAction(argparse._HelpAction):
    def __call__(self, parser, namespace, values, option_string=None):
        parser.print_help()
        print()

        # get subparsers from parser
        subparsers_actions = [
            action
            for action in parser._actions
            if isinstance(action, argparse._SubParsersAction)
        ]

        for subparsers_action in subparsers_actions:
            # print subparsers' help
            for choice, subparser in subparsers_action.choices.items():
                print("Command '{}'".format(choice))
                print(subparser.format_help())

        parser.exit()


def log_level_name(level: int) -> str:
    name: str = logging.getLevelName(level)
    return name.lower()


# subcommand functions
def add_namespace_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--namespace",
        default="canvas",
        help="Identifies the data source.",
    )


def add_query_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--table",
        required=True,
        help="Table name whose data to fetch.",
    )
    parser.add_argument(
        "--format",
        type=Format,
        action=EnumAction,
        default=Format.JSONL,
        help="Data output format.",
    )
    parser.add_argument(
        "--output-directory",
        metavar="DIR",
        default="downloads",
        help="Directory where the query result will be downloaded to. Can be an absolute or relative path.",
    )


def parse_snapshot(args: Arguments) -> SnapshotQuery:
    return SnapshotQuery(format=args.format, filter=None)


def parse_incremental(args: Arguments) -> IncrementalQuery:
    return IncrementalQuery(
        format=args.format, filter=None, since=args.since, until=args.until
    )


def console_entry():
    parser = argparse.ArgumentParser(
        description="Invokes the DAP API to fetch table snapshots and incremental updates.",
        epilog="For more information, check out the OpenAPI specification for DAP API: https://data-access-platform-api.s3.amazonaws.com/index.html",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        add_help=False,
    )
    parser.prog = os.path.basename(os.path.dirname(__file__))

    parser.add_argument(
        "--base-url",
        metavar="URL",
        help="Base URL of the DAP API.",
        action=environment_default("DAP_API_URL"),
    )
    parser.add_argument(
        "--api-key",
        metavar="Key",
        help="API key.",
        action=environment_default("DAP_API_KEY"),
        type=valid_base64,
    )
    parser.add_argument(
        "--loglevel",
        choices=[
            log_level_name(level)
            for level in (
                logging.DEBUG,
                logging.INFO,
                logging.WARN,
                logging.ERROR,
                logging.CRITICAL,
            )
        ],
        default=log_level_name(logging.INFO),
        help="Sets log verbosity.",
    )

    # add custom help
    parser.add_argument(
        "--help", "-h", action=_HelpAction, help="show this help message and exit"
    )

    subparsers = parser.add_subparsers(
        help="Command to execute, e.g. initiate a snapshot or an incremental query, or get list of tables.",
        required=True,
        dest="command",
    )

    snapshot_parser = subparsers.add_parser(
        "snapshot",
        help="Performs a snapshot query.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    add_query_arguments(snapshot_parser)
    add_namespace_argument(snapshot_parser)
    snapshot_parser.set_defaults(parse_query=parse_snapshot)

    incremental_parser = subparsers.add_parser(
        "incremental",
        help="Performs an incremental query with a given start, and (optionally) end timestamp.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    add_query_arguments(incremental_parser)
    add_namespace_argument(incremental_parser)
    incremental_parser.add_argument(
        "--since",
        metavar="DATETIME",
        required=True,
        help="Start timestamp for an incremental query. Examples: 2022-06-13T09:30:00Z or 2022-06-13T09:30:00+02:00.",
        type=valid_utc_datetime,
    )
    incremental_parser.add_argument(
        "--until",
        metavar="DATETIME",
        required=False,
        help="End timestamp for an incremental query. Examples: 2022-06-13T09:30:00Z or 2022-06-13T09:30:00+02:00.",
        type=valid_utc_datetime,
    )
    incremental_parser.set_defaults(parse_query=parse_incremental)

    list_parser = subparsers.add_parser(
        "list",
        help="Lists the name of all tables available for querying in the specified namespace.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    add_namespace_argument(list_parser)

    schema_parser = subparsers.add_parser(
        "schema",
        help="Returns the JSON schema that records in the table conform to.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    add_namespace_argument(schema_parser)
    schema_parser.add_argument(
        "--table",
        required=True,
        help="Table name whose schema to return.",
    )
    schema_parser.add_argument(
        "--output-directory",
        metavar="DIR",
        default="downloads/schemas",
        help="Directory where the json schema will be downloaded to. Can be an absolute or relative path.",
    )

    args = Arguments()
    parser.parse_args(namespace=args)

    logging.basicConfig(
        level=getattr(logging, args.loglevel.upper(), logging.INFO),
        format="%(asctime)s - %(levelname)s - %(funcName)s [%(lineno)d] - %(message)s",
    )

    try:
        with DAPClient(
            base_url=args.base_url,
            api_key=args.api_key,
        ) as my_client:
            if args.command == "list":
                tables = my_client.get_tables(args.namespace)
                print(
                    f"The following tables are available in namespace '{args.namespace}':"
                )
                for t in tables:
                    print(t)
            elif args.command == "schema":
                my_client.download_table_schema(
                    args.namespace, args.table, args.output_directory
                )
            elif args.command in ("incremental", "snapshot"):
                query = args.parse_query(args)
                my_client.fetch_table_data(
                    args.namespace, args.table, query, args.output_directory
                )
            else:
                raise NotImplementedError(f"Unrecognized command '{args.command}'")

    except OperationError as e:
        print(f"An exception occurred while executing the command:")
        pprint(dataclasses.asdict(e), sort_dicts=False)


if __name__ == "__main__":
    console_entry()
