import re
from typing import List
from importlib import resources

from hidetext.textspan import TextSpan
from .filter import Filter


class Profanity(Filter):
    name: str = "PROFANITY"

    terms: List[str]

    def __init__(self, language_code: str = "en") -> None:
        super().__init__()
        self.terms = self._load_profanities(language_code)

    def search(self, text: str) -> List[TextSpan]:
        tokenized = self._tokens(text)
        return [
            token
            for token in tokenized
            if self._normalize_word(token.text) in self.terms
        ]

    def is_valid(self, text: str) -> bool:
        return self._normalize_word(text) in self.terms

    def _normalize_word(self, word: str) -> str:
        cleaned = word.lower().strip()
        normalized = ""
        for c in cleaned:
            if len(normalized) == 0:
                normalized += c
            elif (
                c != normalized[-1]
                or c in ["r", "l"]
                and (len(normalized) < 2 or normalized[-2] not in ["r", "l"])
            ):
                normalized += c
        return normalized

    def _tokens(self, text: str) -> List[TextSpan]:
        tokens = []
        last_end = 0
        for match in re.finditer(r"[\s+\!]", text):
            tokens.append(
                TextSpan(
                    last_end, match.start(), self.name, text[last_end : match.start()]
                )
            )
            last_end = match.end()
        if last_end < len(text):
            tokens.append(
                TextSpan(last_end, len(text), self.name, text[last_end : len(text)])
            )
        return tokens

    def _load_profanities(self, language_code: str) -> List[str]:
        lines: str = resources.read_text(
            f"hidetext.resources.{language_code}", "profanities.txt"
        )
        return [word.lower().strip() for word in lines.split("\n")]
