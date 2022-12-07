"""The main Module class."""
import json
import typing as t

import lovely_tensors as lt  # type: ignore
import torch
import yaml
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table

from torchsilk import type_defs as tdf
from torchsilk.modules.buffers import NamedBuffers
from torchsilk.modules.module_state import ModuleState
from torchsilk.modules.type_defs import FunctionalModule, FunctionalModuleWithBuffers


def json_to_yaml(x: str) -> str:
    """Convert a json string to yaml."""
    return yaml.safe_dump(json.loads(x))


class ModuleSetupNotImplemented(NotImplementedError):
    """Raised when Module.__setup_... functions are not implemented."""


class Module(t.Generic[tdf.PydanticModel, tdf.P, tdf.R_co]):
    """Opinionated wrapper around torch.nn.Module that acts like a stateless model.

    To construct a stateless model, you must implement either subclass either
    __setup_module_state__ or __setup_torch_module__. If you implement both, then
    __setup_module_state__ will be used.

    Examples:

    1. Model that doesn't have any parametrizable layers.

    >>> import torch
    ... import functorch as ft
    ... import torchsilk as tsk
    ... class MyModule(Module[tdf.EmptyModel, torch.Tensor, torch.Tensor]):
    ...     @classmethod
    ...     def __setup_torch_module__(cls, config) -> torch.nn.Module:
    ...         return torch.nn.Linear(1, 1)
    ... tsk_module = MyModule()
    ... torch_module = MyModule.__setup_torch_module__(tsk.BaseConfig())
    ... func_module, _ = ft.make_functional(torch_module)
    ... x = torch.randn(4, 1)
    ... assert torch.allclose(func_module(tsk_module.parameters(), x), tsk_module(x))

    2. Model that has parametrizable layers.

    >>> import torch
    ... import torchsilk as tsk
    ... from pydantic import validator
    ... class MyFeedForwardConfig(tsk.BaseConfig):
    ...     in_features: int
    ...     out_features: int
    ...     hidden_features: list[int]
    ...     hidden_activations: list[str | torch.nn.Module]
    ...     @validator('hidden_activations')
    ...     def check_activations(cls, v: t.Any) -> list[torch.nn.Module]:
    ...         return [getattr(torch.nn, a) for a in v]
    ... class MyFeedForward(Module[MyFeedForwardConfig, torch.Tensor, torch.Tensor]):
    ...     @classmethod
    ...     def __setup_torch_module__(self, config) -> torch.nn.Module:
    ...         layers = []
    ...         for i, (in_features, out_features, activation) in enumerate(
    ...             zip(
    ...                 [config.in_features, *config.hidden_features],
    ...                 [*config.hidden_features, config.out_features],
    ...                 [*config.hidden_activations, torch.nn.Identity],
    ...             )
    ...         ):
    ...             layers.append(torch.nn.Linear(in_features, out_features))
    ...             if activation != "linear":
    ...                 layers.append(activation())
    ...         return torch.nn.Sequential(*layers)
    ... config = MyFeedForwardConfig(
    ...     in_features=1,
    ...     out_features=1,
    ...     hidden_features=[2, 3],
    ...     hidden_activations=["ReLU", "ReLU"]
    ... )
    ... tsk_module = MyFeedForward(config)
    ... torch_module = MyFeedForward.__setup_torch_module__(config)
    ... func_module, _ = ft.make_functional(torch_module)
    ... x = torch.randn(4, config.in_features)
    ... assert torch.allclose(func_module(tsk_module.parameters(), x), tsk_module(x))

    3. Model that has buffers.

    >>> import torch
    ... import torchsilk as tsk
    ... class MyModule(Module[tdf.EmptyModel, [torch.Tensor], torch.Tensor]):
    ...     @classmethod
    ...     def __setup_torch_module__(cls, config) -> torch.nn.Module:
    ...         class _MyModule(torch.nn.Module):
    ...             def __init__(self):
    ...                 super().__init__()
    ...                 self.register_buffer("bias", torch.ones(1))
    ...             def forward(self, x):
    ...                 return x + self.bias
    ...         return _MyModule()
    ... tsk_module = MyModule(tdf.EmptyModel())
    ... torch_module = MyModule.__setup_torch_module__(tdf.EmptyModel())
    ... func_module, *_ = ft.make_functional_with_buffers(torch_module)
    ... x = torch.randn(4, 1)
    ... assert torch.allclose(
    ...     func_module(tsk_module.parameters(), tsk_module.buffers(), x),
    ...     tsk_module(x)
    ... )
    ... assert torch.allclose(tsk_module.buffers()[0], torch_module.bias)
    ... assert torch.allclose(tsk_module.named_buffers().bias, torch_module.bias)
    """

    def __init__(
        self,
        config: tdf.BaseConfig = tdf.BaseConfig(),
        module_state: ModuleState[tdf.P, tdf.R_co] | None = None,
    ) -> None:
        self.config = config
        if module_state:
            self._module_state = module_state
        else:
            self._init_module_state()

    def _init_module_state(self) -> None:
        try:
            self._module_state = self.__setup_module_state__(self.config)
        except ModuleSetupNotImplemented:
            try:
                torch_module = self.__setup_torch_module__(self.config)
            except ModuleSetupNotImplemented:
                raise ModuleSetupNotImplemented(
                    "Both __setup_module_state__ and __setup_torch_module__ are not"
                    + " implemented."
                ) from None
            else:
                self._module_state = ModuleState[tdf.P, tdf.R_co].from_torch_module(
                    torch_module
                )

    @classmethod
    def __setup_module_state__(
        cls, config: tdf.PydanticModel
    ) -> ModuleState[tdf.P, tdf.R_co]:
        raise ModuleSetupNotImplemented(
            f"{cls}.__setup_module_state__ not implemented."
        )

    @classmethod
    def __setup_torch_module__(cls, config: tdf.PydanticModel) -> torch.nn.Module:
        raise ModuleSetupNotImplemented(
            f"{cls}.__setup_torch_module__ not implemented."
        )

    @property
    def module(
        self,
    ) -> FunctionalModule[tdf.P, tdf.R_co] | FunctionalModuleWithBuffers[
        tdf.P, tdf.R_co
    ]:
        return self._module_state.module

    def apply(
        self,
        params: tuple[torch.nn.Parameter, ...],
        *args: tdf.P.args,
        **kwargs: tdf.P.kwargs,
    ) -> tdf.R_co:
        """Apply the module to the given arguments.

        Args:
        -----
            params: Parameters of the module.
            buffers: Buffers of the module.
            *args: Arguments to the module.
            **kwargs: Keyword arguments to the module.
        Returns:
        --------
            The result of applying the module to the given arguments.

        Examples:

        1. Module without buffers.
        >>> import torch
        ... import functorch as ft
        ... import torchsilk as tsk
        ... class MyModule(tsk.Module[tdf.EmptyModel, [torch.Tensor], torch.Tensor]):
        ...     @classmethod
        ...     def __setup_torch_module__(cls, config) -> torch.nn.Module:
        ...         return torch.nn.Linear(1, 1)
        ... tsk_module = MyModule(tdf.EmptyModel())
        ... torch_module = MyModule.__setup_torch_module__(tdf.EmptyModel())
        ... func_module, *_ = ft.make_functional(torch_module)
        ... x = torch.randn(4, 1)
        ... assert torch.allclose(
        ...     func_module(tsk_module.parameters(), x),
        ...     tsk_module(x)
        ... )
        ... new_params = tuple(torch.nn.Parameter(torch.randn(1, 1)) for _ in range(2))
        ... assert torch.allclose(
        ...     func_module(new_params, x),
        ...     tsk_module.apply(new_params, x)
        ... )

        2. Module with buffers.
        >>> import torch
        ... import functorch as ft
        ... import torchsilk as tsk
        ... class MyModule(tsk.Module[tdf.EmptyModel, [torch.Tensor], torch.Tensor]):
        ...     @classmethod
        ...     def __setup_torch_module__(cls, config) -> torch.nn.Module:
        ...         class _MyModule(torch.nn.Module):
        ...             def __init__(self):
        ...                 super().__init__()
        ...                 self.linear = torch.nn.Linear(1, 1)
        ...                 self.register_buffer("bias", torch.ones(1))
        ...             def forward(self, x):
        ...                 return self.linear(x) + self.bias
        ...         return _MyModule()
        ... tsk_module = MyModule(tdf.EmptyModel())
        ... torch_module = MyModule.__setup_torch_module__(tdf.EmptyModel())
        ... func_module, *_ = ft.make_functional_with_buffers(torch_module)
        ... x = torch.randn(4, 1)
        ... assert torch.allclose(
        ...     func_module(tsk_module.parameters(), tsk_module.buffers(), x),
        ...     tsk_module(x)
        ... )
        ... new_params = tuple(torch.nn.Parameter(torch.randn(1, 1)) for _ in range(2))
        ... assert torch.allclose(
        ...     func_module(new_params, tsk_module.buffers(), x),
        ...     tsk_module.apply(new_params, x)
        ... )
        """
        return self._module_state.apply(params, *args, **kwargs)

    def apply_with_buffers(
        self,
        params: tuple[torch.nn.Parameter, ...],
        buffers: tuple[torch.Tensor, ...],
        *args: tdf.P.args,
        **kwargs: tdf.P.kwargs,
    ) -> tdf.R_co:
        """Apply the module to the given arguments.

        Args:
        -----
            params: Parameters of the module.
            buffers: Buffers of the module.
            *args: Arguments to the module.
            **kwargs: Keyword arguments to the module.
        Returns:
        --------
            The result of applying the module to the given arguments.

        Examples:
        ---------

        1. Module without buffers.
        >>> import torch
        ... import functorch as ft
        ... import pytest
        ... import torchsilk as tsk
        ... class MyModule(tsk.Module[tdf.EmptyModel, [torch.Tensor], torch.Tensor]):
        ...     @classmethod
        ...     def __setup_torch_module__(cls, config) -> torch.nn.Module:
        ...         return torch.nn.Linear(1, 1)
        ... tsk_module = MyModule(tdf.EmptyModel())
        ... torch_module = MyModule.__setup_torch_module__(tdf.EmptyModel())
        ... func_module, *_ = ft.make_functional(torch_module)
        ... x = torch.randn(4, 1)
        ... buffers = tuple()
        ... with pytest.raises(ValueError):
        ...     tsk_module.apply_with_buffers(tsk_module.parameters(), buffers, x)

        2. Module with buffers.
        >>> import torch
        ... import functorch as ft
        ... import torchsilk as tsk
        ... class MyModule(tsk.Module[tdf.EmptyModel, [torch.Tensor], torch.Tensor]):
        ...     @classmethod
        ...     def __setup_torch_module__(cls, config) -> torch.nn.Module:
        ...         class _MyModule(torch.nn.Module):
        ...             def __init__(self):
        ...                 super().__init__()
        ...                 self.linear = torch.nn.Linear(1, 1)
        ...                 self.register_buffer("bias", torch.ones(1))
        ...             def forward(self, x):
        ...                 return self.linear(x) + self.bias
        ...         return _MyModule()
        ... tsk_module = MyModule(tdf.EmptyModel())
        ... torch_module = MyModule.__setup_torch_module__(tdf.EmptyModel())
        ... func_module, *_ = ft.make_functional_with_buffers(torch_module)
        ... x = torch.randn(4, 1)
        ... assert torch.allclose(
        ...     func_module(tsk_module.parameters(), tsk_module.buffers(), x),
        ...     tsk_module(x)
        ... )
        ... new_params = tuple(torch.nn.Parameter(torch.randn(1, 1)) for _ in range(2))
        ... assert torch.allclose(
        ...     func_module(new_params, tsk_module.buffers(), x),
        ...     tsk_module.apply(new_params, x)
        ... )
        """
        return self._module_state.apply_with_buffers(params, buffers, *args, **kwargs)

    def parameters(self) -> tuple[torch.nn.Parameter, ...]:
        return self._module_state.parameters

    def buffers(self) -> tuple[torch.Tensor, ...]:
        return self._module_state.buffers

    def named_buffers(self) -> NamedBuffers:
        return self._module_state.named_buffers

    def to(
        self, *args: t.Any, **kwargs: t.Any
    ) -> "Module[tdf.PydanticModel, tdf.P, tdf.R_co]":
        """Move the module to the specified device, dtype and/or memory format.

        Args:
        -----
            *args: t.Any
            **kwargs: t.Any
            Any arguments accepted by torch.Tensor.to(...).

        Returns:
        --------
            Module[tdf.PydanticModel, tdf.P, tdf.R]
            A copy of the module with the specified device, dtype and/or memory format.

        Examples:
        ---------

        >>> import torch
        ... import functorch as ft
        ... import torchsilk as tsk
        ... class MyModule(tsk.Module[tdf.EmptyModel, [torch.Tensor], torch.Tensor]):
        ...     @classmethod
        ...     def __setup_torch_module__(cls, config) -> torch.nn.Module:
        ...         return torch.nn.Linear(1, 1)
        ... tsk_module = MyModule(tdf.EmptyModel())
        ... torch_module = MyModule.__setup_torch_module__(tdf.EmptyModel())
        ... float64_module = tsk_module.to(torch.float64)
        ... float64_torch_module = torch_module.to(torch.float64)
        ... func_module, _ = ft.make_functional(float64_torch_module)
        ... x = torch.randn(4, 1).to(torch.float64)
        ... assert torch.allclose(
        ...     float64_module(x), func_module(float64_module.parameters(), x)
        ... )
        """
        return self.__class__(
            config=self.config, module_state=self._module_state.to(*args, **kwargs)
        )

    def evolve(
        self,
        parameters: tuple[torch.nn.Parameter, ...] | None = None,
        buffers: tuple[torch.Tensor, ...] | None = None,
        named_buffers: NamedBuffers | None = None,
    ) -> "Module[tdf.PydanticModel, tdf.P, tdf.R_co]":
        """Return new Module with same config but with new module_state from updates.

        Args:
        -----
            parameters: tuple[torch.nn.Parameter, ...]
                New parameters.
            buffers: tuple[torch.Tensor, ...]
                New buffers. Cannot be provided together with named_buffers.
            named_buffers: NamedBuffers
                New named_buffers. Cannot be provided together with buffers.
        Returns:
        --------
            Module[tdf.PydanticModel, tdf.P, tdf.R]
                New Module with updated parameters and/or buffers and/or named_buffers.

        Examples:
        ---------

        1. Update parameters.
        >>> import torch
        ... import functorch as ft
        ... import torchsilk as tsk
        ... class MyModule(Module[tdf.EmptyModel, [torch.Tensor], torch.Tensor]):
        ...     @classmethod
        ...     def __setup_torch_module__(cls, config) -> torch.nn.Module:
        ...         class _MyModule(torch.nn.Module):
        ...             def __init__(self):
        ...                 super().__init__()
        ...                 self.linear = torch.nn.Linear(1, 1)
        ...             def forward(self, x):
        ...                 return self.linear(x)
        ...         return _MyModule()
        ... tsk_module = MyModule(tdf.EmptyModel())
        ... torch_module = MyModule.__setup_torch_module__(tdf.EmptyModel())
        ... func_module, *_ = ft.make_functional(torch_module)
        ... x = torch.randn(4, 1)
        ... assert torch.allclose(
        ...     func_module(tsk_module.parameters(), x),
        ...     tsk_module(x)
        ... )
        ... new_params = (torch.nn.Parameter(torch.zeros(1)),)
        ... new_tsk_module = tsk_module.evolve(parameters=new_params)
        ... assert not torch.allclose(
        ...    func_module(tsk_module.parameters(), x),
        ...    new_tsk_module(x)
        ... )

        2. Update buffers.
        >>> import torch
        ... import torchsilk as tsk
        ... class MyModule(Module[tdf.EmptyModel, [torch.Tensor], torch.Tensor]):
        ...     @classmethod
        ...     def __setup_torch_module__(cls, config) -> torch.nn.Module:
        ...         class _MyModule(torch.nn.Module):
        ...             def __init__(self):
        ...                 super().__init__()
        ...                 self.register_buffer("bias", torch.ones(1))
        ...             def forward(self, x):
        ...                 return x + self.bias
        ...         return _MyModule()
        ... tsk_module = MyModule(tdf.EmptyModel())
        ... torch_module = MyModule.__setup_torch_module__(tdf.EmptyModel())
        ... func_module, *_ = ft.make_functional_with_buffers(torch_module)
        ... x = torch.randn(4, 1)
        ... assert torch.allclose(
        ...     func_module(tsk_module.parameters(), tsk_module.buffers(), x),
        ...     tsk_module(x)
        ... )
        ... new_buffers = (torch.zeros(1),)
        ... new_tsk_module = tsk_module.evolve(buffers=new_buffers)
        ... assert not torch.allclose(
        ...    func_module(tsk_module.parameters(), tsk_module.buffers(), x),
        ...    new_tsk_module(x)
        ... )

        3. Updating both parameters and buffers raises a ValueError.
        >>> import torch
        ... import torchsilk as tsk
        ... import pytest
        ... class MyModule(Module[tdf.EmptyModel, [torch.Tensor], torch.Tensor]):
        ...     @classmethod
        ...     def __setup_torch_module__(cls, config) -> torch.nn.Module:
        ...         class _MyModule(torch.nn.Module):
        ...             def __init__(self):
        ...                 super().__init__()
        ...                 self.linear = torch.nn.Linear(1, 1)
        ...                 self.register_buffer("bias", torch.ones(1))
        ...             def forward(self, x):
        ...                 return self.linear(x) + self.bias
        ...         return _MyModule()
        ... tsk_module = MyModule(tdf.EmptyModel())
        ... new_params = (torch.nn.Parameter(torch.zeros(1)),)
        ... new_buffers = (torch.zeros(1),)
        ... new_named_buffers = tsk_module.named_buffers().evolve_from_values(
        ...     new_buffers
        ... )
        ... with pytest.raises(ValueError):
        ...     tsk_module.evolve(
        ...         parameters=new_params,
        ...         buffers=new_buffers,
        ...         named_buffers=new_named_buffers,
        ...     )
        """
        return self.__class__(
            config=self.config,
            module_state=self._module_state.evolve(
                parameters=parameters, buffers=buffers, named_buffers=named_buffers
            ),
        )

    def show(self, max_n_params: int = 2) -> None:
        """Show a pretty representation of self.

        Args:
        -----
            max_n_params: int
                Maximum number of parameters to show.

        Example representation:
        -----------------------

        >>> import torch
        ... class MyModule(Module[tdf.EmptyModel, [torch.Tensor], torch.Tensor]):
        ...     @classmethod
        ...     def __setup_torch_module__(cls, config) -> torch.nn.Module:
        ...         class _MyModule(torch.nn.Module):
        ...             def __init__(self):
        ...                 super().__init__()
        ...                 self.linear = torch.nn.Linear(2, 4)
        ...                 self.register_buffer("bias", torch.randn(5, 5))
        ...             def forward(self, x):
        ...                 return self.linear(x) + self.bias
        ...         return _MyModule()
        ... tsk_module = MyModule(tdf.EmptyModel())
        ... tsk_module.show()

        ──────────────────────── MyModule ────────────────────────
        ╭────────────────── Config: EmptyModel ──────────────────╮
        │ {}                                                     │
        │                                                        │
        ╰────────────────────────────────────────────────────────╯
        ╭──────────────────────── Module ────────────────────────╮
        │ FunctionalModuleWithBuffers(                           │
        │   (stateless_model): _MyModule(                        │
        │     (linear): Linear(in_features=2, out_features=4,    │
        │ bias=True)                                             │
        │   )                                                    │
        │ )                                                      │
        ╰────────────────────────────────────────────────────────╯
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃                       Parameters                       ┃
        ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
        │ Parameter[4, 2] n=8 x∈[-0.571, 0.663] μ=0.068 σ=0.412  │
        │  [[0.346, -0.571], [0.502, 0.071], [-0.143, -0.233],   │
        │                    [0.663, -0.090]]                    │
        │ Parameter[4] x∈[-0.681, 0.514] μ=0.081 σ=0.560 [0.490, │
        │                 0.514, -0.681, 0.001]                  │
        └────────────────────────────────────────────────────────┘
        ┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ Name                 ┃             Buffers             ┃
        ┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
        │ bias                 │  tensor[5, 5] n=25 x∈[-3.056,   │
        │                      │     2.311] μ=-0.062 σ=1.044     │
        └──────────────────────┴─────────────────────────────────┘
        """
        console = Console()
        console.rule(f"{self.__class__.__name__}")
        console.print(
            Panel(
                Syntax(json_to_yaml(self.config.json()), lexer="yaml"),
                title=f"Config: {self.config.__class__.__name__}",
                border_style="blue",
            )
        )
        console.print(
            Panel(str(self._module_state.module), title="Module", border_style="yellow")
        )
        if max_n_params > 0:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Parameters", width=console.width, justify="center")
            for param in self._module_state.parameters[:max_n_params]:
                table.add_row(str(lt.lovely(param)))
            console.print(table)
        if self._module_state.has_buffers:
            console.print(
                self.named_buffers().as_table(
                    name_column_width=24, buffers_column_width=console.width - 24
                )
            )

    def __call__(self, *args: tdf.P.args, **kwargs: tdf.P.kwargs) -> tdf.R_co:
        return self._module_state(*args, **kwargs)
