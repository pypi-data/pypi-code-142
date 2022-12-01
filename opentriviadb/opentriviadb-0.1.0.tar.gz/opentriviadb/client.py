# Copyright (c) 2022-present, Ethan Henderson
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Client interfaces for the OpenTriviaDB wrapper."""

from __future__ import annotations

import asyncio
import enum
import sys
import typing as t
from base64 import b64decode
from types import TracebackType

from aiohttp import ClientSession

from opentriviadb import BASE_URL, TOKEN_URL
from opentriviadb.errors import InvalidParameter, NoResults, TokenEmpty, TokenNotFound
from opentriviadb.questions import Question

EXCEPTIONS: t.Final = [None, NoResults, InvalidParameter, TokenNotFound, TokenEmpty]


class Category(enum.Enum):
    GENERAL_KNOWLEDGE = 9
    ENTERTAINMENT_BOOKS = 10
    ENTERTAINMENT_FILM = 11
    ENTERTAINMENT_MUSIC = 12
    ENTERTAINMENT_MUSICALS_AND_THEATRES = 13
    ENTERTAINMENT_TELEVISION = 14
    ENTERTAINMENT_VIDEO_GAMES = 15
    ENTERTAINMENT_BOARD_GAMES = 16
    SCIENCE_AND_NATURE = 17
    SCIENCE_COMPUTERS = 18
    SCIENCE_MATHEMATICS = 19
    MYTHOLOGY = 20
    SPORTS = 21
    GEOGRAPHY = 22
    HISTORY = 23
    POLITICS = 24
    ART = 25
    CELEBRITIES = 26
    ANIMALS = 27
    VEHICLES = 28
    ENTERTAINMENT_COMICS = 29
    SCIENCE_GADGETS = 30
    ENTERTAINMENT_JAPANESE_ANIME_AND_MANGA = 31
    ENTERTAINMENT_CARTOON_AND_ANIMATIONS = 32


class Client:
    """A client for the Open Trivia API.

    Parameters
    ----------
    token : str, optional
        Your session token. This is not an access token in the
        traditional sense (and is thus optional), but a token generated
        by the API in order to track which questions you have received.
        This is done to prevent duplicate questions.

    Other Parameters
    ----------------
    loop : AbstractEventLoop, optional
        The event loop the client should use. If you don't provide one,
        the client will create one.
    session : ClientSession, optional
        The AIOHTTP session the client should use. If you don't provide
        one, the client will create one.

    ??? example "Basic example"
        ```py
        client = Client()
        ```

    ??? example "Context manager example"
        ```py
        async with Client() as client:
            ...
        ```
    """

    def __init__(
        self,
        token: str | None = None,
        *,
        loop: asyncio.AbstractEventLoop | None = None,
        session: ClientSession | None = None,
        **kwargs: t.Any,
    ) -> None:
        try:
            self._loop = loop or asyncio.get_running_loop()
        except RuntimeError:
            self._loop = (
                asyncio.new_event_loop()
                if sys.version_info >= (3, 10)
                else asyncio.get_event_loop()
            )

        self._session = session or ClientSession(loop=self._loop, **kwargs)
        self.token = token

    async def __aenter__(self) -> Client:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.teardown()

    async def round(
        self,
        amount: int = 10,
        category: Category | None = None,
        difficulty: t.Literal["easy", "medium", "hard"] | None = None,
        type: t.Literal["multiple", "boolean"] | None = None,
    ) -> t.AsyncIterator[Question]:
        """Run a round of trivia.

        Parameters
        ----------
        amount : int, optional
            The number of questions the round should contain. This
            cannot be higher than 50, and defaults to 10.
        category : Category, optional
            The category of the questions that should be in the round.
            This should be passed as a `Category` enum, which can be
            imported using `from opentriviadb import Category`. If this
            is not provided, the questions will be in a mix of
            categories.
        difficulty : "easy" or "medium" or "hard", optional
            The difficulty of questions that should be in the round. If
            this is not provided, the questions can be of any
            difficulty.
        type : "multiple" or "boolean", optional
            The type of questions that should be in the round. This can
            either be multiple choice ("multiple") or true-false
            ("boolean"). If this is not provided, the questions can be
            either.

        Yields
        ------
        Question
            Asynchronously yield questions one by one.

        Raises
        ------
        NoResults
            The API does not have enough questions to satisfy your
            query.
        InvalidParameter
            An invalid parameter has been passed.
        TokenNotFound
            Session token does not exist (session tokens are not
            required to make requests).
        TokenEmpty
            The session token needs to be reset (use
            `client.reset_token` to do this).

        ??? example "Basic example"
            ```py
            async for q in client.round():
                print(q.question)
            ```

        ??? example "Example with parameters"
            ```py
            from opentriviadb import Category

            async for q in client.round(
                amount=25,
                category=Category.GENERAL_KNOWLEDGE,
                difficulty="easy",
                type="multiple",
            ):
                print(q.question)
            ```
        """

        url = (
            BASE_URL
            + f"?amount={amount}"
            + (f"&category={category.value}" if category else "")
            + (f"&difficulty={difficulty}" if difficulty else "")
            + (f"&type={type}" if type else "")
            + "&encode=base64"
            + (f"&token={self.token}" if self.token else "")
        )

        async with self._session.get(url) as resp:
            resp.raise_for_status()
            data = await resp.json()

        code = data["response_code"]
        results = data["results"]

        if code != 0:
            raise EXCEPTIONS[code]()

        for result in results:
            yield Question(
                b64decode(result["category"]).decode("utf-8"),
                b64decode(result["type"]).decode("utf-8"),
                b64decode(result["difficulty"]).decode("utf-8"),
                b64decode(result["question"]).decode("utf-8"),
                b64decode(result["correct_answer"]).decode("utf-8"),
                [b64decode(i).decode("utf-8") for i in result["incorrect_answers"]],
            )

    async def request_token(self) -> str:
        """Request a session token from the API.

        While the token is returned from this method, you don't need to
        do anything extra to allow the client to use the token.

        Returns
        -------
        str
            The session token. This is automatically applied to the
            client, but is returned to allow you to store it for future
            use.
        """

        async with self._session.get(TOKEN_URL + "?command=request") as resp:
            resp.raise_for_status()
            data = await resp.json()

        self.token = data["token"]
        return t.cast(str, self.token)

    async def reset_token(self) -> None:
        """Reset a session token.

        This resets the token currently applied to the client. This does
        not error if no token currently exists, but instead silently
        does nothing.

        Returns
        -------
        None
        """

        async with self._session.get(
            TOKEN_URL + f"?command=reset&token={self.token}"
        ) as resp:
            resp.raise_for_status()

    async def teardown(self) -> None:
        """Close the AIOHTTP session.

        This should be called before closing your program. If you use
        the client via the context manager, this is called
        automatically.

        Returns
        -------
        None
        """

        await self._session.close()
