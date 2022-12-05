"""
This module is part of the 'sitzungsdienst' package,
which is released under GPL-3.0-only license.
"""

from operator import itemgetter
import re
from typing import IO

import PyPDF2

from .models.court import CourtDates
from .models.express import ExpressDates
from .regex import ASSIGNMENT, EXPRESS, PERSON
from .utils import dedupe


class StA:
    """
    Handles weekly PDF assignments as issued by 'web.sta'
    """

    @staticmethod
    def run(
        pdf: list[IO[bytes] | str] | IO[bytes] | str,
    ) -> tuple[CourtDates, ExpressDates]:
        """
        ...

        :param pdf: list[IO[bytes] | str] | IO[bytes] | str PDF contents OR filepath(s)
        :return: tuple[CourtDates, ExpressDates]
        """

        # If not list ..
        if not isinstance(pdf, list):
            # .. convert it
            pdf = [pdf]

        # Create data arrays
        court_dates: list[dict[str, str]] = []
        express_dates: list[dict[str, str]] = []

        # Loop over input data
        for item in pdf:
            # Create data array
            pages: dict[int, list[str]] = {}

            # Browse pages
            for idx, page in enumerate(PyPDF2.PdfReader(item).pages):
                # Retrieve PDF pages
                page: list[str] = [
                    text.strip() for text in page.extract_text().splitlines() if text
                ]

                # If first page ..
                if idx == 0:
                    # .. retrieve express service dates
                    express_dates += StA.express(page)

                pages[idx] = page

            # Retrieve court dates
            court_dates += StA.process(StA.extract(pages))

        # Sort data
        court_dates.sort(key=itemgetter("date", "who", "when", "where", "what"))
        express_dates.sort(key=itemgetter("start", "who", "end"))

        # Remove duplicates
        return CourtDates(dedupe(court_dates)), ExpressDates(dedupe(express_dates))

    @staticmethod
    def extract(pages: dict[int, list[str]]) -> dict[str, dict[int, list[str]]]:
        """
        Extracts raw data from PDF pages

        :param pages: dict[int, list[str]] PDF pages
        :return: dict Raw source data
        """

        # Create data array
        raw: dict[str, list[str]] = {}

        # Reset weekday buffer
        date: str = ""

        # Extract assignment data
        for page in pages.values():
            # Reset mode
            is_live = False

            for index, text in enumerate(page):
                # Determine starting point ..
                if text == "Anfahrt":
                    is_live = True

                    # .. and proceed with next entry
                    continue

                # Determine terminal point ..
                if text == "Seite":
                    is_live = False

                    # .. and proceed with next entry
                    continue

                # Enforce entries between starting & terminal point
                if not is_live or "Ende der Auflistung" in text:
                    continue

                # Determine current date / weekday
                if text in ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]:
                    date = page[index + 1]

                    if date not in raw:
                        raw[date] = []

                    # Proceed with next entry
                    continue

                # Proceed with next entry if it indicates ..
                # (1) .. current date
                if text == date:
                    continue

                # (2) .. follow-up appointment for main trial
                if text in ["F", "+"]:
                    continue

                raw[date].append(text)

        return raw

    @staticmethod
    def process(raw: dict[str, list[str]]) -> list[dict[str, str]]:
        """
        Processes raw data

        :param raw: dict Raw data
        :return: list[dict[str, str]] Data representing court dates
        """

        # Create data array
        unprocessed: list[tuple[str, str, list[str]]] = []

        # Iterate over source data
        for date, item in raw.items():
            buffer: list[str] = []
            court: str = ""

            # Iterate over text blocks
            for index, text in enumerate(item):
                if is_court(text):
                    court = text

                else:
                    buffer.append(text)

                if index + 1 == len(item) or is_court(item[index + 1]):
                    unprocessed.append((date, court, buffer))

                    # Reset buffer
                    buffer = []

        # Reset global data array
        data: list[dict[str, str]] = []

        for item in unprocessed:
            # Unpack values
            date, court, buffer = item

            # Format data as string
            string = " ".join(buffer)

            # Find assignments
            matches = ASSIGNMENT.finditer(string)

            for match in matches:
                data.append(
                    {
                        "date": format_date(date),
                        "when": match.group("time"),
                        "who": format_people(match.group("assigned")),
                        "where": format_place(court, match.group("where")),
                        "what": match.group("docket"),
                    }
                )

        return data

    @staticmethod
    def express(page: list[str]) -> list[dict[str, str]]:
        """
        Extracts express service dates

        :param page: list[str] PDF page
        :return: list[dict[str, str]] Data representing express service dates
        """

        # Create data array
        express: list[str] = []

        # Detect 'express mode'
        # (1) Activation
        is_express = False

        for text in page:
            # Skip if no express service
            if text == "Keine Einteilung":
                break

            # Determine express service ..
            if text == "Eildienst":
                is_express = True

                # .. and proceed with next entry
                continue

            # Skip
            if text == "Tag":
                break

            if is_express:
                express.append(text)

        # Combine data to string for easier regEx matching
        string = " ".join(express)

        # Find matches
        matches = EXPRESS.finditer(string)

        # Create data buffer
        data: list[dict[str, str]] = []

        # Loop over matched time periods & their assignees ..
        for match in matches:
            # .. storing their data
            data.append(
                {
                    "start": format_date(match.group("from")),
                    "end": format_date(match.group("to")),
                    "who": format_people(match.group("assigned")),
                }
            )

        return data


def is_court(string: str) -> bool:
    """
    Checks whether string denotes district or regional court

    :param string: str String to be checked
    :return: bool Whether or not string denotes a court
    """

    if re.match(r"(?:AG|LG)\s", string.strip()):
        return True

    return False


def format_date(string: str, separator: str = "-") -> str:
    """
    Formats given date using specified separator

    :param string: str String representing date
    :param separator: str Separator
    :return: str Formatted date
    """

    return separator.join(reversed(string.split(".")))


def format_place(court: str, extra: str) -> str:
    """
    Formats court & additional information

    :param court: str String representing a court
    :param extra: str String holding additional information
    :return: str Formatted place
    """

    # Format string representing court
    string = court.replace(" ,", "").strip()

    return f"{string} {extra.strip()}" if extra else string


def format_people(string: str) -> str:
    """
    Formats assigned people

    :param string: str String representing assigned people
    :return: str Formatted people
    """

    # Find matches
    matches = PERSON.finditer(string)

    # Create data array
    people = []

    for match in matches:
        # Clean strings & combine them
        people.append(format_person(match))

    # If none found ..
    if not people:
        # .. return original string
        return string

    # Bring people together
    return "; ".join(people)


def format_person(match: re.Match) -> str:  # type: ignore
    """
    Formats single person

    :param match: re.Match Match representing single person
    :return: str Formatted person
    """

    return " ".join(
        [
            string.strip()
            for string in [
                match.group("title"),
                match.group("doc"),
                match.group("first"),
                match.group("last"),
                match.group("department"),
            ]
            if string
        ]
    )
