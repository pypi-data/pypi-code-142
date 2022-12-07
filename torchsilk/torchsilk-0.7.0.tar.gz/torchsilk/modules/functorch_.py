"""Typed versions of some functorch functions."""
import functorch as ft
import torch

from torchsilk import type_defs as tdf
from torchsilk.modules.type_defs import (
    FunctionalModule,
    FunctionalModuleWithBuffers,
    TorchModule,
)


def make_functional(
    module: TorchModule[tdf.P, tdf.R],
) -> tuple[FunctionalModule[tdf.P, tdf.R], tuple[torch.nn.Parameter, ...]]:
    """A type-safe version of functorch.make_functional."""
    return ft.make_functional(module)  # type: ignore


def make_functional_with_buffers(
    module: TorchModule[tdf.P, tdf.R],
) -> tuple[
    FunctionalModuleWithBuffers[tdf.P, tdf.R],
    tuple[torch.nn.Parameter, ...],
    tuple[torch.Tensor, ...],
]:
    """A type-safe version of functorch.make_functional_with_buffers."""
    return ft.make_functional_with_buffers(module)  # type: ignore
