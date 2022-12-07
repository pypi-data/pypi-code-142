import math
import typing as t

import torch

from torchsilk.init.uniform import uniform


# These no_grad_* functions are necessary as wrappers around the parts of these
# functions that use `with torch.no_grad()`. The JIT doesn't support context
# managers, so these need to be implemented as builtins. Using these wrappers
# lets us keep those builtins small and re-usable.
def _func_no_grad_uniform(
    generator: torch.Generator,
    size: tuple[int, ...],
    a: float,
    b: float,
    dtype: torch.dtype = torch.float32,
) -> torch.Tensor:
    """Functional version of torch.nn.init._no_grad_uniform_."""
    with torch.no_grad():
        return uniform(generator=generator, size=size, a=a, b=b, dtype=dtype)


@t.overload
def _func_no_grad_normal(
    mean: float,
    std: float,
    generator: torch.Generator,
    size: tuple[int, ...] = (),
) -> torch.Tensor:
    ...


@t.overload
def _func_no_grad_normal(
    mean: torch.Tensor,
    std: torch.Tensor,
    generator: torch.Generator,
    size: tuple[int, ...] = (),
) -> torch.Tensor:
    ...


def _func_no_grad_normal(
    mean: float | torch.Tensor,
    std: float | torch.Tensor,
    generator: torch.Generator,
    size: tuple[int, ...] = (),
) -> torch.Tensor:
    with torch.no_grad():
        if not size:
            assert isinstance(mean, torch.Tensor)
            assert isinstance(std, torch.Tensor)
            return torch.normal(mean=mean, std=std, generator=generator)
        else:
            assert isinstance(mean, float)
            assert isinstance(std, float)
            return torch.normal(mean=mean, std=std, size=size, generator=generator)


def _func_calculate_fan_in_and_fan_out(
    dimensions: int, shape: tuple[int, ...]
) -> tuple[int, int]:
    if dimensions < 2:
        raise ValueError(
            "Fan in and fan out can not be computed for tensor with fewer than 2"
            + " dimensions"
        )

    num_input_fmaps = shape[1]
    num_output_fmaps = shape[0]
    receptive_field_size = 1
    if dimensions > 2:
        # math.prod is not always available, accumulate the product manually
        # we could use functools.reduce but that is not supported by TorchScript
        for s in shape[2:]:
            receptive_field_size *= s
    fan_in = num_input_fmaps * receptive_field_size
    fan_out = num_output_fmaps * receptive_field_size

    return fan_in, fan_out


def xavier_uniform(
    shape: tuple[int, ...],
    generator: torch.Generator,
    gain: float = 1.0,
) -> torch.Tensor:
    r"""Returns a new `Tensor` with given shape with values according to the method
    described in `Understanding the difficulty of training deep feedforward
    neural networks` - Glorot, X. & Bengio, Y. (2010), using a uniform
    distribution. The resulting tensor will have values sampled from
    :math:`\mathcal{U}(-a, a)` where

    .. math::
        a = \text{gain} \times \sqrt{\frac{6}{\text{fan\_in} + \text{fan\_out}}}

    Also known as Glorot initialization.

    This is the functional equivalent to calling
    `torch.nn.init.xavier_uniform_` with
    - shape=tensor.shape

    Args:
        shape: the shape of the resulting tensor
        generator: Generator used for random number generation
        gain: an optional scaling factor

    Examples:
        >>> import torch.nn as nn
        ... generator = torch.Generator(device='cpu')
        ... generator.manual_seed(0)
        ... res = xavier_uniform(
        ...     shape=(3, 5), generator=generator, gain=nn.init.calculate_gain('relu')
        ... )
        ... assert res.shape == (3, 5)
    """
    dimensions = len(shape)
    fan_in, fan_out = _func_calculate_fan_in_and_fan_out(
        dimensions=dimensions, shape=shape
    )
    std = gain * math.sqrt(2.0 / float(fan_in + fan_out))
    a = math.sqrt(3.0) * std  # Calculate uniform bounds from standard deviation

    return _func_no_grad_uniform(generator=generator, size=shape, a=-a, b=a)


def xavier_uniform_like(
    tensor: torch.Tensor,
    generator: torch.Generator,
    gain: float = 1.0,
) -> torch.Tensor:
    r"""Returns a `Tensor` with same shape as with values according to the method
    described in `Understanding the difficulty of training deep feedforward
    neural networks` - Glorot, X. & Bengio, Y. (2010), using a uniform
    distribution. The resulting tensor will have values sampled from
    :math:`\mathcal{U}(-a, a)` where

    .. math::
        a = \text{gain} \times \sqrt{\frac{6}{\text{fan\_in} + \text{fan\_out}}}

    Also known as Glorot initialization.

    Args:
        tensor: an n-dimensional `torch.Tensor`
        generator: Generator used for random number generation
        gain: an optional scaling factor

    Examples:
        >>> import torch.nn as nn
        ... generator = torch.Generator(device='cpu')
        ... w = torch.empty(3, 5)
        ... res = xavier_uniform_like(
        ...     w, gain=nn.init.calculate_gain('relu'), generator=generator
        ... )
        ... assert res.shape == (3, 5)

    """
    return xavier_uniform(shape=tensor.shape, generator=generator, gain=gain)


def xavier_normal(
    shape: tuple[int, ...],
    generator: torch.Generator,
    gain: float = 1.0,
) -> torch.Tensor:
    r"""Returns a new `Tensor` with given shape with values according to the method
    described in `Understanding the difficulty of training deep feedforward
    neural networks` - Glorot, X. & Bengio, Y. (2010), using a normal
    distribution. The resulting tensor will have values sampled from
    :math:`\mathcal{N}(0, \text{std}^2)` where

    .. math::
        \text{std} = \text{gain} \times \sqrt{\frac{2}{\text{fan\_in} + \text{fan\_out}}}  # noqa: E501

    Also known as Glorot initialization.

    Args:
        shape: shape of output tensor
        generator: Generator used for random number generation
        gain: an optional scaling factor

    Examples:
        >>> import torch.nn as nn
        ... generator = torch.Generator(device='cpu')
        ... generator.manual_seed(0)
        ... res = xavier_normal(
        ...     (3, 5), generator=generator, gain=nn.init.calculate_gain('relu')
        ... )
    """
    fan_in, fan_out = _func_calculate_fan_in_and_fan_out(
        dimensions=len(shape), shape=shape
    )
    std = gain * math.sqrt(2.0 / float(fan_in + fan_out))

    return _func_no_grad_normal(size=shape, generator=generator, mean=0.0, std=std)


def xavier_normal_like(
    tensor: torch.Tensor, generator: torch.Generator, gain: float = 1.0
) -> torch.Tensor:
    r"""Returns a new `Tensor` with shape = tensor.shape with values according to the
    method described in `Understanding the difficulty of training deep feedforward
    neural networks` - Glorot, X. & Bengio, Y. (2010), using a normal
    distribution. The resulting tensor will have values sampled from
    :math:`\mathcal{N}(0, \text{std}^2)` where

    .. math::
        \text{std} = \text{gain} \times \sqrt{\frac{2}{\text{fan\_in} + \text{fan\_out}}}  # noqa: E501

    Also known as Glorot initialization.

    Args:
        tensor: an n-dimensional `torch.Tensor`
        generator: Generator used for random number generation
        gain: an optional scaling factor

    Examples:
        >>> from torch import nn
        ... generator = torch.Generator(device='cpu')
        ... w = torch.empty(3, 5)
        ... res = xavier_normal_like(
        ...     w, gain=nn.init.calculate_gain('relu'), generator=generator
        ... )
        ... assert res.shape == (3, 5)
    """
    return xavier_normal(shape=tensor.shape, generator=generator, gain=gain)
