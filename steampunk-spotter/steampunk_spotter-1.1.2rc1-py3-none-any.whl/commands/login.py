"""Provide login CLI command."""

import argparse
import os
from getpass import getpass
from pathlib import Path

from spotter.api import ApiClient
from spotter.storage import Storage


def add_parser(subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
    """
    Add a new parser for login command to subparsers.

    :param subparsers: Subparsers action
    """
    parser = subparsers.add_parser(
        "login", help="Log in to Steampunk Spotter user account"
    )
    parser.add_argument(
        "--username", "-u", type=str, help="Steampunk Spotter username"
    )
    parser.add_argument(
        "--password", "-p", type=str, help="Steampunk Spotter password"
    )
    parser.set_defaults(func=_parser_callback)


def _parser_callback(args: argparse.Namespace) -> None:
    """
    Execute callback for login command.

    :param args: Argparse arguments
    """
    username = args.username or os.environ.get("SPOTTER_USERNAME") or input("Username: ")
    password = args.password or os.environ.get("SPOTTER_PASSWORD") or getpass()

    login(username, password, args.storage_path)
    print("Login successful!")


def login(username: str, password: str, storage_path: Path) -> None:
    """
    Do user login.

    :param username: Steampunk Spotter username
    :param password: Steampunk Spotter password
    :param storage_path: Path to storage
    """
    storage = Storage.create(storage_path)
    api_client = ApiClient(ApiClient.ENDPOINT, storage, username, password)
    api_client.login()
