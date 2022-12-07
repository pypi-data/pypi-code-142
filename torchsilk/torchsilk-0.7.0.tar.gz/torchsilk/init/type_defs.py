import typing as t

import torch

P = t.ParamSpec("P")
TensorT = t.TypeVar("TensorT", torch.Tensor, torch.nn.Parameter)


class FunctionalInitializer(t.Protocol[P, TensorT]):
    def __call__(
        self,
        tensor: TensorT,
        generator: torch.Generator,
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> TensorT:
        raise NotImplementedError()
