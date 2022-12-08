import argparse
import io
import os
import re
import sys
import subprocess
import tempfile

import git
from git import Repo
from pyrogram import Client


def main():
    parser = argparse.ArgumentParser(
        epilog="All other arguments are passed through to git format-patch."
    )
    parser.add_argument(
        "--to", help="Correspondent @handle", action="append", required=True
    )
    args, args_passthrough = parser.parse_known_args()

    repo = Repo(".")

    cfg = repo.config_reader()
    try:
        api_id = cfg.get_value("sendtelegram", "apiid")
        api_hash = cfg.get_value("sendtelegram", "apihash")
        session_string = cfg.get_value("sendtelegram", "sessionstring")
    except git.config.cp.NoSectionError:
        print("git config sendtelegram not found, see --help", file=sys.stderr)
        sys.exit(1)

    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            [
                "git",
                "format-patch",
                "--output-directory",
                tmp,
                "--quiet",
                *args_passthrough,
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        patches = [f"{tmp}/{f}" for f in os.listdir(tmp)[::-1]]

        with Client(
            "my_account", api_id, api_hash, session_string=session_string
        ) as tg:
            for addressee in args.to:
                for patch in patches:
                    tg.send_document(addressee, patch)
