from abc import ABC, abstractmethod
from hidetext.textspan import TextSpan


class Placeholder(ABC):
    @abstractmethod
    def replace(self, span: TextSpan) -> str:
        """Generates a replacement for the provided text span

        :param span: Span to be replaced
        :type span: TextSpan
        :return: Replacement for the span
        :rtype: str
        """
