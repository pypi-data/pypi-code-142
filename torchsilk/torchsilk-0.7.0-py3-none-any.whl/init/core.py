import typing as t

import torch

from torchsilk.init.type_defs import FunctionalInitializer, P, TensorT


def init_like_params(
    params: tuple[TensorT, ...],
    generator: torch.Generator,
    initializer: FunctionalInitializer[P, TensorT],
    *args: P.args,
    **kwargs: P.kwargs,
) -> t.Iterator[TensorT]:
    """Initializes a sequence of parameters like the parameters in `params`.

    Args:
        params: a sequence of tensors defining the shape of the output tensors
        generator: a `torch.Generator` object
        initializer: a function that takes in a tensor and returns a tensor of the
            same shape and dtype as the input tensor
        **kwargs: additional keyword arguments to pass to `initializer`

    Examples:
        >>> import torchsilk.init as tsi
        ... generator = torch.Generator(device='cpu')
        ... generator.manual_seed(0)
        ... params = [torch.empty(3, 5).to(device='cpu', dtype=torch.float16)]
        ... res = init_like_params(params, generator, tsi.uniform_like, a=-0.1, b=0.1)
        ... assert all(r.shape == p.shape for r, p in zip(res, params))
        ... assert all(r.dtype == p.dtype for r, p in zip(res, params))
        ... assert all(r.device == p.device for r, p in zip(res, params))
    """
    for param in params:
        yield initializer(tensor=param, generator=generator, *args, **kwargs).to(
            param.device
        )


def zeros_init_like(
    tensor: TensorT,
    generator: torch.Generator,
) -> TensorT:
    result = torch.zeros_like(tensor)
    if isinstance(tensor, torch.Tensor):
        return result
    return torch.nn.Parameter(result)


def constant_init_like(
    tensor: TensorT,
    generator: torch.Generator,
    value: float,
) -> TensorT:
    result = torch.full_like(tensor, value)
    if isinstance(tensor, torch.Tensor):
        return result
    return torch.nn.Parameter(result)


def init_feed_forward_like(
    weights_init: FunctionalInitializer[[], TensorT],
    bias_init: FunctionalInitializer[[], TensorT] = zeros_init_like,
) -> FunctionalInitializer[[], TensorT]:
    """Initialize either the weights or biases of a feed-forward layer.

    Args:
    -----
        weights_init: a function that takes in a tensor and returns a tensor of the
            same shape and dtype as the input tensor
        bias_init: a function that takes in a tensor and returns a tensor of the
            same shape and dtype as the input tensor
    Returns:
    --------
        A function that can initialize either the weights or the bias of a feed-forward
        layer.
        Signature of the returned function:
            (tensor: TensorT, generator: torch.Generator) -> TensorT
        where:
            tensor: a tensor defining the shape of the output tensor
            generator: a `torch.Generator` object for seeding the random number
                generator

    Examples:
    ---------

    >>> import torch
    ... import functorch as ft
    ... from functools import partial
    ... generator = torch.Generator(device='cpu').manual_seed(0)
    ... linear = torch.nn.Linear(3, 5)
    ... linear_func, params = ft.make_functional(linear)
    ... weights, bias = params
    ... initializer = init_feed_forward_like(
    ...     partial(constant_init_like, value=2)
    ... )
    ... new_weights, new_bias = init_like_params(params, generator, initializer)
    ... assert torch.allclose(new_weights, torch.full_like(weights, 2))
    ... assert torch.allclose(new_bias, torch.zeros_like(bias))
    """

    def init(tensor: TensorT, generator: torch.Generator) -> TensorT:
        if tensor.ndim == 2:
            return weights_init(tensor=tensor, generator=generator)
        if tensor.ndim == 1:
            return bias_init(tensor=tensor, generator=generator)
        raise ValueError(
            f"Expected tensor to have 1 or 2 dimensions, got {tensor.ndim}"
        )

    return init
