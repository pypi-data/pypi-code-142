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

"""OpenTriviaDB errors."""

from __future__ import annotations


class OpenTriviaError(Exception):
    """The base error for OpenTriviaDB errors."""


class NoResults(OpenTriviaError):
    """Exception thrown when no results can be returned from the API."""

    def __init__(self) -> None:
        super().__init__("the API does not have enough questions for your query")


class InvalidParameter(OpenTriviaError):
    """An invalid parameter was passed to the API."""

    def __init__(self) -> None:
        super().__init__(
            "an invalid parameter has been passed -- refer to the docs to "
            "check valid values"
        )


class TokenNotFound(OpenTriviaError):
    """A session token is required for the request, but does not
    exist."""

    def __init__(self) -> None:
        super().__init__(
            "session token does not exist -- use `client.retrieve_token` to "
            "create a new one"
        )


class TokenEmpty(OpenTriviaError):
    """All possible questions have been returned while the active
    session token is in use, and the token should be reset."""

    def __init__(self) -> None:
        super().__init__(
            "all possible questions returned using current token -- use "
            "`client.reset_token` to reset it"
        )
