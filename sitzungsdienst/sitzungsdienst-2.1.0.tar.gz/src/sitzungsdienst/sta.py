"""
This module is part of the 'sitzungsdienst' package,
which is released under GPL-3.0-only license.
"""

from __future__ import annotations

import operator
import re
from typing import IO

import PyPDF2

from .models.court import CourtDate, CourtDates
from .models.express import ExpressDate, ExpressDates
from .regex import ASSIGNMENT, EXPRESS, PERSON
from .utils import dedupe, flatten, sort_din5007


class Sitzungsdienst:
    """
    Handles weekly PDF assignments as issued by 'web.sta'
    """

    # PDF data
    contents: dict[int, list[str]] | None = None

    def __init__(self, pdf_file: IO[bytes] | str | None = None) -> None:
        """
        Creates 'Sitzungsdienst' instance

        :param pdf_file: IO[bytes] | str Binary stream OR filepath representing PDF
        :return: None
        """

        # If provided ..
        if pdf_file:
            # .. load PDF file
            self.load_pdf(pdf_file)

    def load_pdf(self, pdf) -> Sitzungsdienst:  # type: ignore
        """
        Loads PDF contents for further processing

        :param pdf: BinaryIO | str PDF file (either binary stream OR filepath)
        :return: sitzungsdienst.sta.Sitzungsdienst
        """

        # Create data array
        self.contents: dict[int, list[str]] = {}

        # Fetch content from PDF file
        for i, page in enumerate(PyPDF2.PdfReader(pdf).pages):
            self.contents[i + 1] = [
                text.strip() for text in page.extract_text().splitlines() if text
            ]

        return self

    def _extract_source(self) -> dict[str, list[str]]:
        """
        Extracts raw data from PDF source

        :return: dict Raw source data
        :raises: ValueError Missing PDF contents
        """

        # If PDF contents not present ..
        if self.contents is None:
            # .. fail early
            raise ValueError("Missing PDF contents!")

        # Create data array
        source: dict[str, list[str]] = {}

        # Reset weekday buffer
        date: str = ""

        # Extract assignment data
        for page in self.contents.values():
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

                    if date not in source:
                        source[date] = []

                    # Proceed with next entry
                    continue

                # Proceed with next entry if it indicates ..
                # (1) .. current date
                if text == date:
                    continue

                # (2) .. follow-up appointment for main trial
                if text in ["F", "+"]:
                    continue

                source[date].append(text)

        return source

    def _process_source(self, source: dict[str, list[str]]) -> CourtDates:
        """
        Processes raw source data

        :param source: dict Raw source data
        :return: sitzungsdienst.models.court.CourtDates Court dates
        """

        # Create data array
        unprocessed: list[tuple[str, str, list[str]]] = []

        # Iterate over source data
        for date, raw in source.items():
            buffer: list[str] = []
            court: str = ""

            # Iterate over text blocks
            for index, text in enumerate(raw):
                if is_court(text):
                    court = text

                else:
                    buffer.append(text)

                if index + 1 == len(raw) or is_court(raw[index + 1]):
                    unprocessed.append((date, court, buffer))

                    # Reset buffer
                    buffer = []

        # Reset global data array
        data: list[CourtDate] = []

        for item in unprocessed:
            # Unpack values
            date, court, buffer = item

            # Format data as string
            string = " ".join(buffer)

            # Find assignments
            matches = ASSIGNMENT.finditer(string)

            for match in matches:
                data.append(
                    CourtDate(
                        **{
                            "date": format_date(date),
                            "when": match.group("time"),
                            "who": format_people(match.group("assigned")),
                            "where": format_place(court, match.group("where")),
                            "what": match.group("docket"),
                        }
                    )
                )

        # Sort data
        data.sort(key=operator.attrgetter("date", "who", "when", "where", "what"))

        return CourtDates(data)

    def court_dates(self) -> CourtDates:
        """
        Retrieves court dates

        :return: sitzungsdienst.models.court.CourtDates Court dates
        """

        # Extract source data from PDF
        source = self._extract_source()

        # Process it
        return self._process_source(source)

    def express_dates(self) -> ExpressDates:
        """
        Extracts express service dates

        :return: sitzungsdienst.models.express.ExpressDates Express service dates
        :raises: ValueError Missing PDF contents
        """

        # If PDF contents not present ..
        if self.contents is None:
            # .. fail early
            raise ValueError("Missing PDF contents!")

        # Create data array
        express: list[str] = []

        # Detect 'express mode'
        # (1) Activation
        is_express = False

        for text in self.contents[1]:
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
        data: list[ExpressDate] = []

        # Loop over matched time periods & their assignees ..
        for match in matches:
            # .. storing their data
            data.append(
                ExpressDate(
                    **{
                        "start": format_date(match.group("from")),
                        "end": format_date(match.group("to")),
                        "who": format_people(match.group("assigned")),
                    }
                )
            )

        return ExpressDates(data)

    def sort_people(self, string: re.Match | str) -> tuple[str, str]:  # type: ignore
        """
        Sorts strings & match objects representing people ('sorted' helper)

        :param string: re.Match | str (Matched) input string
        :return: tuple Strings for comparison
        """

        # Determine input string
        string = (
            string.split()[-1]
            if isinstance(string, str)
            else string.group("last") + " " + string.group("first")
        )

        # Respect german umlauts
        return sort_din5007(string)

    def extract_people(self, as_string: bool = True) -> list[str]:
        """
        Extracts assigned people from PDF contents

        :param as_string: bool Whether to export strings OR match objects
        :return: List[str] Assigned people
        :raises: ValueError Missing PDF contents
        """

        # If PDF contents not present ..
        if self.contents is None:
            # .. fail early
            raise ValueError("Missing PDF contents!")

        # Determine whether texts contains people
        matches = PERSON.finditer(" ".join(flatten(self.contents.values())))

        # Extract people while ..
        # (1) .. removing duplicate entries
        # (2) .. sorting by last & first name
        people = sorted(dedupe(list(matches)), key=self.sort_people)

        # If specified, return them ..
        if as_string:
            # .. as strings
            return [format_person(match) for match in people]

        # .. otherwise as match objects
        return people


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
