import itertools
from typing import List, Optional
from .filters.filter import Filter
from .filters import Email, Phone, Profanity, IdCard
from .censor import Censor
from .textspan import TextSpan
from . import placeholders


class Hidetext:
    def __init__(
        self, language_code: str = "en", filters: Optional[List[Filter]] = None
    ) -> None:
        self._language_code = language_code
        self._filters = (
            filters
            if filters
            else [
                Email(),
                Phone(),
                Profanity(self._language_code),
                IdCard(),
            ]
        )

    def character(self, text: str) -> str:
        spans = self._get_text_spans(text)
        censor = Censor(placeholders.Character())
        return censor.censor(text, spans)

    def kind(
        self, text: str, start_character: str = "<", end_character: str = ">"
    ) -> str:
        spans = self._get_text_spans(text)
        censor = Censor(placeholders.Kind(start_character, end_character))
        return censor.censor(text, spans)

    def _get_text_spans(self, text: str) -> List[TextSpan]:
        return list(
            itertools.chain.from_iterable([f.search(text) for f in self._filters])
        )
