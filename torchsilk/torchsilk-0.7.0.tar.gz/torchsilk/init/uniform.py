import torch


def uniform(
    generator: torch.Generator,
    size: tuple[int, ...],
    a: float,
    b: float,
    dtype: torch.dtype = torch.float32,
) -> torch.Tensor:
    r"""Returns a random floating point number from the uniform distribution
    :math:`\mathcal{U}(a, b)` on the interval :math:`[a, b)`

    Args:
        generator: a `torch.Generator` object
        size: a tuple defining the shape of the output tensor
        a: the lower bound of the range to sample from
        b: the upper bound of the range to sample from
        dtype: the desired data type of returned tensor
        device: the desired device of returned tensor

    Examples:
        >>> generator = torch.Generator(device='cpu')
        ... generator.manual_seed(0)
        ... size = (3, 5)
        ... dtype = torch.float16
        ... device = 'cpu'
        ... tensor = torch.empty(size, dtype=dtype, device=device)
        ... res = uniform_like(tensor, generator, a=-0.1, b=0.1)
        ... assert res.shape == tensor.shape
        ... assert res.dtype == tensor.dtype
        ... assert res.device == tensor.device
        ... assert res.min() >= -0.1, res.min()
        ... assert res.max() <= 0.1, res.max()
    """
    if a >= b:
        raise ValueError(f"uniform_ expects a < b, but got a={a} and b={b}")
    return (b - a) * torch.rand(
        *size, generator=generator, dtype=dtype, device=generator.device
    ) + a


def uniform_like(
    tensor: torch.Tensor,
    generator: torch.Generator,
    a: float,
    b: float,
) -> torch.Tensor:
    r"""Returns a tensor with the same characteristics as :attr:`tensor` filled with
    numbers from the uniform distribution :math:`\mathcal{U}(a, b)` on the interval
    :math:`[a, b)`.

    Args:
        tensor: a tensor defining the shape of the output tensor
        generator: a `torch.Generator` object
        a: the lower bound of the range to sample from
        b: the upper bound of the range to sample from

    Examples:
        >>> generator = torch.Generator(device='cpu')
        ... generator.manual_seed(0)
        ... size = (3, 5)
        ... dtype = torch.float16
        ... device = 'cpu'
        ... tensor = torch.empty(size, dtype=dtype, device=device)
        ... res = uniform_like(tensor, generator, a=-0.1, b=0.1)
        ... assert res.shape == tensor.shape
        ... assert res.dtype == tensor.dtype
        ... assert res.device == tensor.device
        ... assert res.min() >= -0.1, res.min()
        ... assert res.max() <= 0.1
    """
    if generator.device != tensor.device:
        # Raising RuntimeError because PyTorch does the same thing if you pass a gpu
        # generator and ask for a cpu tensor or vice-versa.
        raise RuntimeError(
            f"Generator device {generator.device} must match tensor device"
            + f" {tensor.device}"
        )
    return uniform(
        generator=generator,
        size=tensor.shape,
        a=a,
        b=b,
        dtype=tensor.dtype,
    )
