#!/usr/bin/env python3
"""TLFi command-line interface.

If Blessings is installed on your system, you will get pretty colors and
formatting almost like in the TLFi.
"""

import argparse
import difflib
import lzma
import os
import re
import sqlite3
import sys
from pathlib import Path
from typing import Generator

from blessings import Terminal
from bs4 import BeautifulSoup, NavigableString

T = Terminal()
TAG_STRIP_RE = re.compile(r"\s+")


def main():
    ap = argparse.ArgumentParser(description="TLFi CLI")
    ap.add_argument("query", help="mot(s) à chercher")
    ap.add_argument("-d", "--database", help="base de données")
    args = ap.parse_args()

    if args.database:
        db_path = Path(args.database)
    elif (env_db_path := os.environ.get("TLFI_DATABASE")):
        db_path = Path(env_db_path)
    else:
        sys.exit("Pas de base de données et TLFI_DATABASE n'est pas défini.")

    lexical_form = args.query
    connection = sqlite3.connect(db_path)
    printed = 0
    for definition_html in get_definitions(lexical_form, connection):
        pretty_print_definition(definition_html)
        printed += 1
    if printed == 0:
        print("Forme lexicale non trouvée. Suggestions :")
        for suggestion in get_suggestions(lexical_form, connection):
            print(f"* {suggestion}")


def get_definitions(
    lexical_form: str,
    connection: sqlite3.Connection
) -> Generator[str, None, None]:
    cursor = connection.cursor()
    result = cursor.execute(
        "SELECT definition FROM definitions WHERE lexical_form = ?",
        (lexical_form,)
    )
    for (blob,) in result.fetchall():
        yield lzma.decompress(blob).decode()


def pretty_print_definition(html: str):
    soup = BeautifulSoup(html, "html.parser")
    content = parse_tag(soup.div.div)
    print(content)


def parse_tag(tag) -> str:
    if isinstance(tag, NavigableString):
        return TAG_STRIP_RE.sub(" ", tag)
    content = ""
    for child in tag.children:
        content += parse_tag(child)
    if tag.name == "div":
        content += "\n"
    if tag.name == "span":
        classes = tag.get("class") or []
        if "tlf_cdefinition" in classes:
            content = f"{T.yellow}{content}{T.normal}"
        if "tlf_cdomaine" in classes:
            content = f"{T.red}{content}{T.normal}"
        if "tlf_csyntagme" in classes:
            content = f"{T.green}{content}{T.normal}"
        if "tlf_cmot" in classes:
            content = f"{T.reverse}{content}{T.normal}"
    if tag.name == "b":
        content = f"{T.bold}{content}{T.normal}"
    if tag.name == "i":
        content = f"{T.italic}{content}{T.no_italic}"
    return content


def get_suggestions(
    query: str,
    connection: sqlite3.Connection
) -> Generator[str, None, None]:
    """Return a form for which a definition might exist, else None.

    If we are sure the lexical form does not have definitions, suggest similar
    words to the user.
    """
    cursor = connection.cursor()
    result = cursor.execute("SELECT lexical_form FROM definitions")
    yielded = []
    for (form,) in result.fetchall():
        if difflib.SequenceMatcher(None, query, form).ratio() > 0.8:
            if form not in yielded:
                yield form
                yielded.append(form)


if __name__ == "__main__":
    main()
