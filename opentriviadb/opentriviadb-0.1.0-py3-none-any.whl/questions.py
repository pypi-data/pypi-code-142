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

"""Questions interfaces for the OpenTriviaDB wrapper."""

from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass()
class Question:
    """A question.

    Attributes
    ----------
    category : str
        The question category.
    type : str
        The question type.
    difficulty : str
        The question difficulty.
    question : str
        The question body.
    correct_answer : str
        The question's correct answer.
    incorrect_answers : list of str
        A list of the question's incorrect answers.
    """

    category: str
    type: str
    difficulty: str
    question: str
    correct_answer: str
    incorrect_answers: list[str]

    @property
    def options(self) -> list[str]:
        """All the question options shuffled in a random order.

        Returns
        -------
        list of str
        """

        if self.type == "boolean":
            return ["True", "False"]

        return random.sample([self.correct_answer, *self.incorrect_answers], 4)

    def answer(self, option: str) -> bool:
        """Answer the question, and check if it is correct.

        Parameters
        ----------
        option : str
            The option with which you wish to answer the question.

        Returns
        -------
        bool
            Whether you answered the question correctly.
        """

        return option != self.correct_answer
