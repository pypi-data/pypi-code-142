from abc import ABC, abstractmethod
import re
from typing import List, Dict

from hidetext.textspan import TextSpan
from .filter import Filter


class PatternFilter(Filter, ABC):
    @property
    @abstractmethod
    def patterns(self) -> Dict[str, str]:
        """Dictionary of patterns to be used in the filter. Keys are the name of the pattern and
        the value is a valid regex

        :return: Patterns of the filter
        :rtype: Dict[str, str]
        """

    def search(self, text: str) -> List[TextSpan]:
        results = []
        for pattern in self.patterns:
            for match in re.finditer(r"\b" + self.patterns[pattern] + r"\b", text):
                results.append(
                    TextSpan(match.start(), match.end(), self.name, match.group(0))
                )
        return results

    def is_valid(self, text: str) -> bool:
        for pattern in self.patterns:
            matched = re.match(self.patterns[pattern], text)
            if matched:
                return matched.start() == 0 and matched.end() == len(text)
        return False
