import abc
from typing import Union, List

from numpy import iterable

from .._ipa_content_provider import IPAContentProviderLayer
from ...._content_type import ContentType
from ...._tools import try_copy_to_list


class BaseSurfaceDefinition(IPAContentProviderLayer, abc.ABC):
    pass


DefnDefns = Union[BaseSurfaceDefinition, List[BaseSurfaceDefinition]]


class Definitions(IPAContentProviderLayer):
    def __init__(
        self,
        universe: "DefnDefns",
    ):
        universe = try_copy_to_list(universe)
        if not iterable(universe):
            universe = [universe]

        super().__init__(
            content_type=ContentType.SURFACES,
            universe=universe,
            __plural__=True,
        )
