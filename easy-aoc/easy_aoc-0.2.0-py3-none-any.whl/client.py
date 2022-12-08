"""A client to communicate with the Advent of Code website."""
from __future__ import annotations

import enum
import http
import logging
import re
from typing import Protocol

import attrs
import bs4 as bs4
import requests
import yarl

from easy_aoc import domain, exceptions

_log = logging.getLogger(__name__)
_P_TIME = re.compile(r"(?:(?P<minutes>\d+)m )?(?P<seconds>\d+)s")


# pylint: disable-next=too-few-public-methods
class IAocClient(Protocol):
    """Protocol for an AocClient."""

    def get_puzzle_input(self, puzzle: domain.Puzzle) -> domain.PuzzleInput:
        """Get a puzzle input."""

    def submit_answer(self, answer: domain.Answer) -> domain.Submission | None:
        """Submit an answer."""


@attrs.define  # pylint: disable-next=too-few-public-methods
class AocClient:
    """A client class to query the Advent of Code website."""

    base_url: yarl.URL = attrs.field(converter=yarl.URL)
    session_key: str = attrs.field(repr=lambda key: "[hidden]")
    version: str = attrs.field(repr=False)

    def get_puzzle_input(self, puzzle: domain.Puzzle) -> domain.PuzzleInput:
        """Get a puzzle input from the Advent of Code website.

        :param puzzle: The puzzle to fetch the input of
        :return: The raw string puzzle input
        """
        input_url = self._get_puzzle_url(puzzle) / "input"
        response = self._request(method="GET", url=input_url)
        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            if exc.response.status_code == http.HTTPStatus.NOT_FOUND:
                raise exceptions.PuzzleInputUnavailable(puzzle=puzzle) from exc
            raise  # pragma: nocover
        else:
            return domain.PuzzleInput(puzzle=puzzle, text=response.text)

    def submit_answer(self, answer: domain.Answer) -> domain.Submission | None:
        """Submit an answer to the Advent of Code.

        :param answer: The answer to submit
        :return: An instance of Submission
        """
        submission_url = self._get_puzzle_url(answer.part.puzzle) / "answer"
        data = _serialize_answer_form_data(answer)

        response = self._request(method="POST", url=submission_url, data=data)
        response.raise_for_status()

        parsed_response = ParsedResponse.from_response(response)
        if parsed_response.raw_result == RawResult.TIMEOUT:
            _log.error("You can't submit yet!\n\n%s", parsed_response.message)
            return None

        result = parsed_response.raw_result.to_result()
        return domain.Submission(answer=answer, result=result)

    def _get_puzzle_url(self, puzzle: domain.Puzzle) -> yarl.URL:
        """Get the url for a specific puzzle.

        :param puzzle: The puzzle to get the url for
        :return: The URL for the puzzle
        """
        return self.base_url / str(puzzle.year) / "day" / str(puzzle.day)

    def _request(
        self, method: str, url: yarl.URL, data: dict[str, str] | None = None
    ) -> requests.Response:
        """Request a URL with the specified method.

        :param method: The request method to use
        :param url: The url to request
        :param data: The optional form data to send with the request
        :return: The response to the request
        """
        return requests.request(
            method=method,
            url=str(url),
            data=data,
            cookies={"session": self.session_key},
            timeout=(15.0, 15.0),
            headers={"User-Agent": f"easy-aoc/{self.version}"},
        )


def _serialize_answer_form_data(answer: domain.Answer) -> dict[str, str]:
    """Serialize the answer as form data.

    :param answer: The answer to serialize
    :return: A form data dict prepared for the request
    """
    return {"level": str(answer.part.part), "answer": answer.answer}


class RawResult(enum.Enum):
    """A raw submission result."""

    CORRECT = 1
    INCORRECT = 2
    TIMEOUT = 3

    def to_result(self) -> domain.Result:
        """Convert this RawResult to an actual Result.

        :return: An instance of Result
        """
        match self:
            case RawResult.CORRECT:
                return domain.Result.CORRECT
            case RawResult.INCORRECT:
                return domain.Result.INCORRECT
            case _:
                raise ValueError(f"Can't convert {self!r} to Result.")


@attrs.define(frozen=True)
class Timeout:
    """A submission timeout."""

    minutes: int
    seconds: int

    @classmethod
    def from_message(cls, message: str) -> "Timeout":
        """Parse a timeout from a message.

        :param message: The message to parse
        :return: An instance of Timeout
        """
        minutes, seconds = _P_TIME.search(message).groups(default="0")
        return cls(minutes=int(minutes), seconds=int(seconds))


@attrs.define(frozen=True)
class ParsedResponse:
    """The parsed response"""

    message: str
    raw_result: RawResult
    timeout: Timeout | None

    @classmethod
    def from_response(cls, response: requests.Response) -> ParsedResponse:
        """Create a ParsedResponse instance from a response.

        :param response: The response to parse
        :return: An instance of parsed response
        """
        contents = response.text
        soup = bs4.BeautifulSoup(contents, "html.parser")
        message = soup.main.article.text.strip()
        if message.startswith("That's the right answer!"):
            raw_result = RawResult.CORRECT
            timeout = None
        elif message.startswith("You gave an answer too recently;"):
            raw_result = RawResult.TIMEOUT
            timeout = Timeout.from_message(message)
        else:
            raw_result = RawResult.INCORRECT
            timeout = None

        return cls(message=message, raw_result=raw_result, timeout=timeout)
