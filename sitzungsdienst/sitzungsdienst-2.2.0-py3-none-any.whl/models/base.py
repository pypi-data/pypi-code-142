"""
This module is part of the 'sitzungsdienst' package,
which is released under GPL-3.0-only license.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
import datetime
from typing import Any, Sequence

import ics  # type: ignore


@dataclass
class Date:
    """
    Base class for single assignment
    """

    who: str

    def to_dict(self) -> dict[str, Any]:
        """
        Exports data

        :return: dict
        """

        return asdict(self)


class Dates(ABC):
    """
    Base class for multiple assignments
    """

    # Assignment data
    data: Sequence[Date]

    # Event host (ICS only)
    creator: str = "S1SYPHOS"

    # Preferred timezone (ICS only)
    timezone: str = "Europe/Berlin"

    def __iter__(self):  # type: ignore
        yield from self.data

    def __len__(self) -> int:
        return len(self.data)

    def to_dict(self) -> list[dict[str, Any]]:
        """
        Exports assignment data

        :return: list[dict[str, Any]]
        """

        return [item.to_dict() for item in self.data]

    def _filter(self, query: list[str] | str) -> list[Date]:
        """
        Filters assignments by search term(s)

        :param query: List[str] | str Search terms
        :return: list[Date] Filtered assignments
        """

        # If query represents string ..
        if isinstance(query, str):
            # .. make it a list
            query = [query]

        # Create data buffer
        results: list[Date] = []

        # Loop over search terms in order to ..
        for term in query:
            # .. filter out relevant items
            results.extend(
                [item for item in self.data if term.lower() in item.who.lower()]
            )

        return results

    @abstractmethod
    def filter(self, query: list[str] | str) -> Dates:
        """
        Filters assignments by search term(s)

        :param query: List[str] | str Search terms
        :return: Dates Filtered assignments
        """

    @abstractmethod
    def data2ics(self) -> ics.Calendar:
        """
        Exports assignments as ICS calendar object

        :return: ics.Calendar
        """

    # HELPERS

    def to_time(self, date_time: str, fmt: str = "%Y-%m-%d") -> datetime.datetime:
        """
        Datetime object helper

        :param date_time: str Date and/or time
        :param fmt: str Datetime pattern
        :return: datetime.datetime
        """

        return datetime.datetime.strptime(date_time, fmt)

    def add_attendees(self, people: str, event: ics.Event) -> None:
        """
        Adds people as attendees to event

        :param people: str Attendees
        :param event: ics.Event Attended event
        :return: None
        """

        for person in people.split(";"):
            # Build attendee
            attendee = ics.Attendee("")

            # Edit name (= title, full name & department)
            attendee.common_name = person

            # Add to assignment
            event.add_attendee(attendee)
