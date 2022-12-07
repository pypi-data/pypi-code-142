import torch
import torch._C


def _standard_normal(  # pyright: ignore[reportUnusedFunction]
    shape: torch.Size | tuple[int, ...],
    dtype: torch.dtype,
    device: torch.device,
    generator: torch.Generator | None = None,
) -> torch.Tensor:
    """This function meant to be only used internally in torchsilk.

    Args:
    -----
    shape: torch.Size | tuple[int, ...]
        The shape of the output tensor.
    dtype: torch.dtype
        The dtype of the output tensor.
    device: torch.device
        The device of the output tensor.
    generator: torch.Generator | None
        The generator to use for the random number generation.

    Returns:
    --------
    torch.Tensor
        A tensor of shape `shape` with standard normal distribution.

    I needed to copy this function from torch.distributions.utils because the original
    does not support the generator argument.

    Taken from [PyTorch Repo](https://github.com/pytorch/pytorch/blob/1da633f98a5da000083c0c47d9e192b2689f867b/torch/distributions/utils.py#L45)  # noqa: E501
    """
    if torch._C._get_tracing_state():  # type: ignore
        # [JIT WORKAROUND] lack of support for .normal_()
        return torch.normal(
            torch.zeros(shape, dtype=dtype, device=device),
            torch.ones(shape, dtype=dtype, device=device),
            generator=generator,
        )
    return torch.empty(shape, dtype=dtype, device=device).normal_(generator=generator)
