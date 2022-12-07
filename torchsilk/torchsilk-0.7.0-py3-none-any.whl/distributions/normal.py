import math

import attrs
import torch
from torch.distributions import constraints
from torch.distributions.utils import (
    broadcast_all,  # pyright: ignore[reportUnknownVariableType]
)

from torchsilk.distributions.base import Distribution, DistributionParams
from torchsilk.distributions.utils import (
    _standard_normal,  # pyright: ignore[reportPrivateUsage]
)


@attrs.define(frozen=True)
class NormalDistParams(DistributionParams):
    loc: torch.Tensor
    scale: torch.Tensor

    validate_args: bool = False

    _arg_constraints: dict[str, constraints.Constraint] = attrs.field(
        init=False,
        factory=lambda: {
            "loc": constraints.real,
            "scale": constraints.positive,
        },
    )
    _batch_shape: torch.Size = attrs.field(init=False)
    _event_shape: torch.Size = attrs.field(init=False)

    def __attrs_post_init__(self):
        if self.loc.shape != self.scale.shape:
            raise ValueError(
                "loc and scale must have the same shape."
                + f" Got {self.loc.shape} and {self.scale.shape}."
            )
        if self.validate_args:
            self._validate_args()

    @classmethod
    def from_numbers(
        cls, loc: float | torch.Tensor, scale: float | torch.Tensor
    ) -> "NormalDistParams":
        return cls(*broadcast_all(loc, scale))

    def astuple(self) -> tuple[torch.Tensor, torch.Tensor]:
        return self.loc, self.scale

    @property
    def arg_constraints(self) -> dict[str, constraints.Constraint]:
        return self._arg_constraints

    @property
    def batch_shape(self) -> torch.Size:
        return self.loc.size()

    @property
    def event_shape(self) -> torch.Size:
        return torch.Size()

    @property
    def mean(self) -> torch.Tensor:
        return self.loc

    @property
    def mode(self) -> torch.Tensor:
        return self.loc

    @property
    def stddev(self) -> torch.Tensor:
        return self.scale

    @property
    def support(self) -> constraints.Constraint:
        return constraints.real

    @property
    def variance(self) -> torch.Tensor:
        return self.stddev.pow(2)


class Normal(Distribution[NormalDistParams]):
    @classmethod
    def sample(
        cls,
        params: NormalDistParams,
        sample_shape: torch.Size | tuple[int, ...] = torch.Size(),
        generator: torch.Generator | None = None,
    ) -> torch.Tensor:
        sample_shape = cls._extended_shape(params, sample_shape)
        with torch.no_grad():
            return torch.normal(
                params.loc.expand(sample_shape),
                params.scale.expand(sample_shape),
                generator=generator,
            )

    @classmethod
    def rsample(
        cls,
        params: NormalDistParams,
        sample_shape: torch.Size | tuple[int, ...] = torch.Size(),
        generator: torch.Generator | None = None,
    ) -> torch.Tensor:
        shape = cls._extended_shape(params, sample_shape)
        eps = _standard_normal(
            shape, dtype=params.loc.dtype, device=params.loc.device, generator=generator
        )
        return params.loc + eps * params.scale

    @classmethod
    def log_prob(
        cls,
        params: NormalDistParams,
        value: torch.Tensor,
    ) -> torch.Tensor:
        if params.validate_args:
            params.validate_sample(value)
        # compute the variance
        var = params.scale**2
        return -((value - params.loc) ** 2) / (2 * var) - 0.5 * torch.log(
            2 * var * math.pi
        )

    @classmethod
    def entropy(cls, params: NormalDistParams) -> torch.Tensor:
        return 0.5 + 0.5 * math.log(2 * math.pi) + torch.log(params.scale)
