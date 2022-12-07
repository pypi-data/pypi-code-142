"""Type definitions / aliases for the sbft API."""
import typing as t

import torch

from torchsilk import type_defs as tdf


class TorchModule(t.Protocol[tdf.P, tdf.R_co]):
    """A typed version of torch.nn.Module."""

    def forward(self, *args: tdf.P.args, **kwargs: tdf.P.kwargs) -> tdf.R_co:
        raise NotImplementedError


class FunctionalModule(t.Protocol[tdf.P, tdf.R]):
    """A module that can be called like a function.

    A type-safe version of functorch's FunctionalModule which is obtained from the
    result of calling functorch.make_functional(...).
    """

    @classmethod
    def from_module(
        cls, module: TorchModule[tdf.P, tdf.R]
    ) -> "FunctionalModule[tdf.P, tdf.R]":
        raise NotImplementedError

    def __call__(
        self,
        parameters: tuple[torch.nn.Parameter, ...],
        *args: tdf.P.args,
        **kwargs: tdf.P.kwargs,
    ) -> tdf.R:
        ...


class FunctionalModuleWithBuffers(t.Protocol[tdf.P, tdf.R_co]):
    """A module that can be called like a function.

    A type-safe version of functorch's FunctionalModuleWithBuffers which is obtained
    from the result of calling functorch.make_functional_with_buffers(...).
    """

    @classmethod
    def from_module(
        cls, module: TorchModule[tdf.P, tdf.R]
    ) -> "FunctionalModule[tdf.P, tdf.R]":
        raise NotImplementedError

    def __call__(
        self,
        parameters: tuple[torch.nn.Parameter, ...],
        buffers: tuple[torch.Tensor, ...],
        *args: tdf.P.args,
        **kwargs: tdf.P.kwargs,
    ) -> tdf.R_co:
        ...
