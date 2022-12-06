import abc
import typing as t
import warnings

import torch
from torch.distributions import constraints
from torch.distributions.utils import lazy_property

DistributionParamsT = t.TypeVar("DistributionParamsT", bound="DistributionParams")


class DistributionParams(abc.ABC):
    @property
    @abc.abstractmethod
    def batch_shape(self) -> torch.Size:
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def event_shape(self) -> torch.Size:
        raise NotImplementedError

    @property
    def support(self) -> constraints.Constraint:
        raise NotImplementedError

    @abc.abstractmethod
    def astuple(self) -> tuple[torch.Tensor, ...]:
        raise NotImplementedError

    @property
    def arg_constraints(self) -> t.Dict[str, constraints.Constraint]:
        return {}

    def validate_sample(self, value: torch.Tensor) -> None:
        """Argument validation for methods such as `log_prob`, `cdf`, `icdf` etc.

        The rightmost dimensions of `value` must agree with `self.event_shape` and
        `self.batch_shape`.

        Raises:
            ValueError: If `value` is not a valid sample.
        """
        event_dim_start = len(value.size()) - len(self.event_shape)
        if value.size()[event_dim_start:] != self.event_shape:
            raise ValueError(
                "The right-most size of value must match event_shape:"
                + f" {value.size()} vs {self.event_shape}."
            )

        actual_shape = value.size()
        expected_shape = self.batch_shape + self.event_shape
        for i, j in zip(reversed(actual_shape), reversed(expected_shape)):
            if i != 1 and j != 1 and i != j:
                raise ValueError(
                    "Value is not broadcastable with batch_shape+event_shape:"
                    + f" {actual_shape} vs {expected_shape}."
                )

        try:
            support = self.support
        except NotImplementedError:
            warnings.warn(
                f"{self.__class__} does not define `support` to enable "
                + "sample validation. Please initialize the distribution with "
                + "`validate_args=False` to turn off validation."
            )
            return
        assert support is not None
        valid: torch.ByteTensor = support.check(value)
        if not valid.all():
            raise ValueError(
                "Expected value argument "
                f"({type(value).__name__} of shape {tuple(value.shape)}) "
                f"to be within the support ({repr(support)}) "
                f"of the distribution {repr(self)}, "
                f"but found invalid values:\n{value}"
            )

    def _validate_args(self) -> None:
        """Validate the parameters of the distribution.

        NOTE: Taken from torch.distributions.distribution.Distribution.__init__

        Extracted into a separate method on parameters because Distribution is stateless
        """
        if not self.arg_constraints:
            warnings.warn(
                f"{self.__class__} does not define `arg_constraints`. Not validating."
            )
        for param, constraint in self.arg_constraints.items():
            if constraints.is_dependent(constraint):
                continue  # skip constraints that cannot be checked
            if param not in self.__dict__ and isinstance(
                getattr(type(self), param), lazy_property
            ):
                continue  # skip checking lazily-constructed args
            value = getattr(self, param)
            valid: torch.ByteTensor = constraint.check(value)
            if not valid.all():
                raise ValueError(
                    f"Expected parameter {param} "
                    f"({type(value).__name__} of shape {tuple(value.shape)}) "
                    f"of distribution {repr(self)} "
                    f"to satisfy the constraint {repr(constraint)}, "
                    f"but found invalid values:\n{value}"
                )


class Distribution(abc.ABC, t.Generic[DistributionParamsT]):
    @classmethod
    @abc.abstractmethod
    def sample(
        cls,
        params: DistributionParamsT,
        sample_shape: torch.Size | tuple[int, ...] = torch.Size(),
        generator: torch.Generator | None = None,
    ) -> torch.Tensor:
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def rsample(
        cls,
        params: DistributionParamsT,
        sample_shape: torch.Size | tuple[int, ...] = torch.Size(),
        generator: torch.Generator | None = None,
    ) -> torch.Tensor:
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def log_prob(cls, params: DistributionParamsT, value: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def entropy(cls, params: DistributionParamsT) -> torch.Tensor:
        raise NotImplementedError

    @classmethod
    def perplexity(cls, params: DistributionParamsT) -> torch.Tensor:
        return torch.exp(cls.entropy(params))

    @classmethod
    def _extended_shape(
        cls,
        params: DistributionParamsT,
        sample_shape: torch.Size | tuple[int, ...] = torch.Size(),
    ) -> torch.Size:
        if not isinstance(sample_shape, torch.Size):
            sample_shape = torch.Size(sample_shape)
        result = sample_shape + params.batch_shape + params.event_shape
        if not isinstance(result, torch.Size):
            result = torch.Size(result)
        return result
