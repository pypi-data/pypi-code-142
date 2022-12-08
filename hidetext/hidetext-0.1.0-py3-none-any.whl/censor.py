from typing import List

from .textspan import TextSpan
from .placeholders import Placeholder


class Censor:
    def __init__(self, placeholder: Placeholder):
        self._placeholder = placeholder

    def censor(self, text: str, spans: List[TextSpan]) -> str:
        spans.sort()
        censored_text = []
        last_end = 0
        for span in spans:
            censored_text.append(text[last_end : span.start])
            replacement = self._placeholder.replace(span)
            censored_text.append(replacement)
            last_end = span.end
        censored_text.append(text[last_end:])
        return "".join(censored_text)
