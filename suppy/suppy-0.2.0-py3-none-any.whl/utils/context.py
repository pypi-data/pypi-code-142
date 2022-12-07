"""
This module contains the context variables used throughout the events

It's main purpose is event logging with context
"""
from contextlib import contextmanager
from contextvars import ContextVar
from typing import TYPE_CHECKING, Iterable, Iterator

if TYPE_CHECKING:
    from suppy import Node

period: ContextVar[int] = ContextVar("period", default=-1)
loop: ContextVar[int] = ContextVar("loop", default=-1)
node: ContextVar["Node"] = ContextVar("node")


@contextmanager
def node_ctx(node_: "Node") -> Iterator["Node"]:
    token = node.set(node_)
    try:
        yield node_
    finally:
        node.reset(token)


@contextmanager
def period_ctx(period_: int) -> Iterator[int]:
    token = period.set(period_)
    try:
        yield period_
    finally:
        period.reset(token)


def iter_nodes(nodes: Iterable["Node"]) -> Iterator["Node"]:
    """Wrap the nodes iterator with the node context"""
    for _node in nodes:
        with node_ctx(_node):
            yield _node
