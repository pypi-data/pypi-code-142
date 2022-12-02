from graphql import OperationType
from pydantic import Field
from rath import rath
import contextvars
import logging

from rath.links.base import TerminatingLink
from rath.contrib.fakts.links.aiohttp import FaktsAIOHttpLink
from rath.contrib.fakts.links.websocket import FaktsWebsocketLink
from rath.contrib.herre.links.auth import HerreAuthLink
from rath.links.aiohttp import AIOHttpLink
from rath.links.auth import AuthTokenLink

from rath.links.base import TerminatingLink
from rath.links.compose import TypedComposedLink, compose
from rath.links.dictinglink import DictingLink
from rath.links.shrink import ShrinkingLink
from rath.links.split import SplitLink
from rath.links.websockets import WebSocketLink

current_fluss_rath = contextvars.ContextVar("current_fluss_rath")


class FlussLinkComposition(TypedComposedLink):
    shrinking: ShrinkingLink = Field(default_factory=ShrinkingLink)
    dicting: DictingLink = Field(default_factory=DictingLink)
    auth: AuthTokenLink
    split: SplitLink


class FlussRath(rath.Rath):
    """_summary_

    Args:
        rath (_type_): _description_
    """

    link: FlussLinkComposition = Field(default_factory=FlussLinkComposition)

    async def __aenter__(self):
        await super().__aenter__()
        current_fluss_rath.set(self)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await super().__aexit__(exc_type, exc_val, exc_tb)
        current_fluss_rath.set(None)
