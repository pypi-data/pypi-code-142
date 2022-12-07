import typing as t

import numpy as np
import torch

from torchsilk.init.xavier import _func_no_grad_normal  # type: ignore


def orthogonal(
    shape: tuple[int, ...],
    generator: torch.Generator,
    gain: float = 1,
):
    r"""Returns a new `Tensor` with given shape with a (semi) orthogonal matrix, as
    described in `Exact solutions to the nonlinear dynamics of learning in deep
    linear neural networks` - Saxe, A. et al. (2013). The input tensor must have
    at least 2 dimensions, and for tensors with more than 2 dimensions the
    trailing dimensions are flattened.

    Args:
        shape: Shape of output tensor
        generator: Generator used for random number generation
        gain: optional scaling factor

    Examples:
        >>> generator = torch.Generator(device='cpu')
        ... w = torch.empty(3, 5)
        ... res = orthogonal(w.shape, generator=generator)
    """
    ndimensions = len(shape)
    numel = int(np.prod(shape))
    if ndimensions < 2:
        print(shape)
        raise ValueError(
            f"Only tensors with 2 or more dimensions are supported, not {ndimensions}"
        )

    if numel == 0:
        # no-op
        return torch.as_tensor([])
    rows = shape[0]
    cols = numel // rows
    flattened = _func_no_grad_normal(
        mean=0.0, std=1.0, size=(rows, cols), generator=generator
    )

    if rows < cols:
        flattened.t_()

    # Compute the qr factorization
    q, r = t.cast(tuple[torch.Tensor, torch.Tensor], torch.linalg.qr(flattened))
    # Make Q uniform according to https://arxiv.org/pdf/math-ph/0609050.pdf
    d = torch.diag(r, 0)
    ph = d.sign()
    q *= ph

    if rows < cols:
        q.t_()
    with torch.no_grad():
        result = q.view(shape).mul_(gain)
    return result


def orthogonal_like(
    tensor: torch.Tensor, generator: torch.Generator, gain: float = 1
) -> torch.Tensor:
    r"""Returns a new `Tensor` with given shape with a (semi) orthogonal matrix, as
    described in `Exact solutions to the nonlinear dynamics of learning in deep
    linear neural networks` - Saxe, A. et al. (2013). The input tensor must have
    at least 2 dimensions, and for tensors with more than 2 dimensions the
    trailing dimensions are flattened.

    Args:
        shape: Shape of output tensor
        generator: Generator used for random number generation
        gain: optional scaling factor

    Examples:
        >>> generator = torch.Generator(device='cpu')
        ... w = torch.empty(3, 5)
        ... res = orthogonal_like(w, generator=generator)
    """
    return orthogonal(shape=tensor.shape, generator=generator, gain=gain)
