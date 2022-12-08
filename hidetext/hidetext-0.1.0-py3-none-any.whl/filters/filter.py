from abc import ABC, abstractmethod
from typing import List

from hidetext.textspan import TextSpan


class Filter(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Name of the filter

        :return: Name of the filter
        :rtype: str
        """

    @abstractmethod
    def search(self, text: str) -> List[TextSpan]:
        """Returns the spans of text matched by the filter

        :param text: Text to search terms to filter
        :type text: str
        :return: Spans of text matched
        :rtype: List[TextSpan]
        """

    @abstractmethod
    def is_valid(self, text: str) -> bool:
        """Returns True iff the text exactly matched with a term for be filtered

        :param text: Text to be matched
        :type text: str
        :return: True iff the text exactly matched
        :rtype: bool
        """
