from abc import ABCMeta, abstractmethod


class IDirector(metaclass=ABCMeta):
    """Director interface."""

    @staticmethod
    @abstractmethod
    def construct(username: str, token: str = ''):
        """Construct an object."""
