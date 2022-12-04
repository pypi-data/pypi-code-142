from __future__ import annotations

from argparse import Namespace as _Namespace, ArgumentParser as _ArgumentParser, ArgumentDefaultsHelpFormatter, Action
from typing import Sequence

__all__ = ["ArgumentParser"]


class Namespace(_Namespace):

    def print_params(self, *, prtf=print):
        prtf("")
        prtf("Parameters:")
        for attr, value in sorted(vars(self).items()):
            prtf("{}={}".format(attr.upper(), value))
        prtf("")

    def as_markdown(self):
        """ Return configs as Markdown format """
        text = "|name|value|  \n|-|-|  \n"
        for attr, value in sorted(vars(self).items()):
            text += "|{}|{}|  \n".format(attr, value)
        return text

    @classmethod
    def from_namespace(cls, args: _Namespace) -> 'Namespace':
        return cls(**vars(args))


class ArgumentParser(_ArgumentParser):
    def __init__(self, *args, formatter_class=ArgumentDefaultsHelpFormatter, **kwargs) -> None:
        super().__init__(*args, **kwargs, formatter_class=formatter_class)

    def add_argument(
            self, *args, help="", **kwargs
    ) -> Action:
        return super(ArgumentParser, self).add_argument(*args, help=help, **kwargs)

    def parse_args(self, args: Sequence[str] | None = ...) -> Namespace:
        args = super(ArgumentParser, self).parse_args()
        return Namespace.from_namespace(args)

    def parse_known_args(
            self, args: Sequence[str] | None = ..., namespace: Namespace | None = ...
    ) -> tuple[Namespace, list[str]]:
        args, unknown_str_list = super(ArgumentParser, self).parse_known_args()
        return Namespace.from_namespace(args), unknown_str_list
