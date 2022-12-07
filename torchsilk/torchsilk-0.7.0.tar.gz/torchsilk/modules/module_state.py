"""ModuleState is a container for a functional module along with its parameters and
buffers (if any)."""
import typing as t

import functorch as ft
import torch
import typing_extensions as te

from torchsilk import type_defs as tdf
from torchsilk.modules.buffers import NamedBuffers
from torchsilk.modules.type_defs import FunctionalModule, FunctionalModuleWithBuffers


class _ModuleStateWithoutBuffers(t.Generic[tdf.P, tdf.R_co]):
    """A container for a stateless module and its parameters.

    Example:

    .. code-block:: python

    >>> import torch
    ... import functorch as ft
    ... module = torch.nn.Sequential(
    ...     torch.nn.Linear(3, 3),
    ...     torch.nn.ReLU(),
    ...     torch.nn.Linear(3, 3),
    ... )
    ... x = torch.randn(4, 3)
    ... m = _ModuleStateWithoutBuffers.from_torch_module(module)
    ... exp_res = m(x)
    ... func_module, params = ft.make_functional(module)
    ... act_res = func_module(params, x)
    ... assert torch.allclose(exp_res, act_res)
    """

    def __init__(
        self,
        module: FunctionalModule[tdf.P, tdf.R_co],
        parameters: tuple[torch.nn.Parameter, ...],
    ) -> None:
        """NOTE: Not intended to be called directly. Use `from_torch_module` instead."""
        self._module = module
        self._parameters = parameters

    @classmethod
    def from_torch_module(cls: type[te.Self], torch_module: torch.nn.Module) -> te.Self:
        """Create a `_ModuleStateWithoutBuffers` from a torch module.

        This is the main way to create a `_ModuleStateWithoutBuffers` instance.

        Example:

        .. code-block:: python

        >>> import torch
        ... import functorch as ft
        ... class MyModule(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         self.linear = torch.nn.Linear(3, 3)
        ...         self.relu = torch.nn.ReLU()
        ...     def forward(self, x):
        ...         return self.relu(self.linear(x))
        ... module = MyModule()
        ... x = torch.randn(4, 3)
        ... m = _ModuleStateWithoutBuffers.from_torch_module(module)
        ... act_res = m(x)
        ... func_module, params = ft.make_functional(module)
        ... exp_res = func_module(params, x)
        ... assert torch.allclose(exp_res, act_res)

        >>> import torch
        ... import functorch as ft
        ... import pytest
        ... class MyModule(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         self.linear = torch.nn.Linear(3, 2)
        ...         self.relu = torch.nn.ReLU()
        ...     def forward(self, x, y, *, z=0):
        ...         return self.relu(self.linear(x) + y) + z
        ... module = MyModule()
        ... x = torch.randn(4, 3)
        ... y = torch.randn(4, 2)
        ... z = torch.randn(4, 2)
        ... m = _ModuleStateWithoutBuffers.from_torch_module(module)
        ... act_res = m(x, y, z=z)
        ... func_module, params = ft.make_functional(module)
        ... exp_res = func_module(params, x, y, z=z)
        ... assert torch.allclose(exp_res, act_res)
        ... act_res = m(x, y)
        ... exp_res = func_module(params, x, y)
        ... assert torch.allclose(exp_res, act_res)
        ... also_act_res = m(x, y, z=1)
        ... also_exp_res = func_module(params, x, y, z=1)
        ... assert torch.allclose(also_exp_res, also_act_res)
        ... with pytest.raises(TypeError):
        ...     m(x, y, z=z, w=1)
        """
        func, parameters = ft.make_functional(
            torch_module, disable_autograd_tracking=True
        )
        return cls(t.cast(FunctionalModule[tdf.P, tdf.R_co], func), parameters)

    @property
    def module(self) -> FunctionalModule[tdf.P, tdf.R_co]:
        """Return the underlying stateless module."""
        return self._module

    @property
    def parameters(self) -> tuple[torch.nn.Parameter, ...]:
        """Return the parameters of the underlying stateless module."""
        return self._parameters

    def apply(
        self,
        params: tuple[torch.nn.Parameter, ...],
        *args: tdf.P.args,
        **kwargs: tdf.P.kwargs,
    ) -> tdf.R_co:
        """Apply the module to the given parameters and buffers.

        Example:

        >>> import torch
        ... import functorch as ft
        ... module = torch.nn.Sequential(
        ...     torch.nn.Linear(3, 3),
        ...     torch.nn.ReLU(),
        ...     torch.nn.Linear(3, 3),
        ... )
        ... x = torch.randn(4, 3)
        ... m = _ModuleStateWithoutBuffers.from_torch_module(module)
        ... exp_res = m(x)
        ... func_module, params = ft.make_functional(module)
        ... act_res = func_module(params, x)
        ... assert torch.allclose(exp_res, act_res)
        ... new_params = tuple(p + 1 for p in params)
        ... new_act_res = m.apply(new_params, x)
        ... new_exp_res = func_module(new_params, x)
        ... assert torch.allclose(new_exp_res, new_act_res)
        """
        return self._module(params, *args, **kwargs)

    def evolve(
        self,
        parameters: tuple[torch.nn.Parameter, ...],
    ) -> te.Self:
        """Return a new `_ModuleStateWithoutBuffers` with the given changes.

        Example:

        >>> import torch
        ... import functorch as ft
        ... class MyModule(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         self.linear = torch.nn.Linear(3, 3)
        ...         self.relu = torch.nn.ReLU()
        ...     def forward(self, x):
        ...         return self.relu(self.linear(x))
        ... module = MyModule()
        ... x = torch.randn(4, 3)
        ... m = _ModuleStateWithoutBuffers.from_torch_module(module)
        ... func_module, params = ft.make_functional(module)
        ... exp_res = func_module(params, x)
        ... act_res = m(x)
        ... assert torch.allclose(exp_res, act_res)
        ... new_params = tuple(p + 1 for p in params)
        ... m = m.evolve(new_params)
        ... new_res = m(x)
        ... assert not torch.allclose(exp_res, new_res)
        """
        if parameters is None:
            parameters = self._parameters
        return self.__class__(self.module, parameters)

    def __call__(self, *args: tdf.P.args, **kwargs: tdf.P.kwargs) -> tdf.R_co:
        return self.module(self.parameters, *args, **kwargs)


class _ModuleStateWithBuffers(t.Generic[tdf.P, tdf.R_co]):
    """A container for a stateless module, its parameters and its buffers.

    Example:

    .. code-block:: python

    >>> import torch
    ... import functorch as ft
    ... class ModuleWithBuffers(torch.nn.Module):
    ...     def __init__(self):
    ...         super().__init__()
    ...         self.register_buffer("x", torch.randn(3))
    ...     def forward(self, x):
    ...         return x + self.x
    ... module = ModuleWithBuffers()
    ... x = torch.randn(4, 3)
    ... m = _ModuleStateWithBuffers.from_torch_module(module)
    ... act_res = m(x)
    ... func_module, params, buffers = ft.make_functional_with_buffers(module)
    ... exp_res = func_module(params, buffers, x)
    ... assert torch.allclose(exp_res, act_res)
    ... assert torch.allclose(m.named_buffers.x, buffers[0])
    """

    def __init__(
        self,
        module: FunctionalModuleWithBuffers[tdf.P, tdf.R_co],
        parameters: tuple[torch.nn.Parameter, ...],
        buffers: tuple[torch.Tensor, ...],
        named_buffers: NamedBuffers,
    ) -> None:
        self._module = module
        self._parameters = parameters
        self._buffers = buffers
        self._named_buffers = named_buffers

    @classmethod
    def from_torch_module(cls: type[te.Self], torch_module: torch.nn.Module) -> te.Self:
        """Create a `_ModuleStateWithBuffers` from a torch module.

        This is the main way to create a `_ModuleStateWithBuffers` instance.

        Examples:

        .. code-block:: python

        >>> import torch
        ... import functorch as ft
        ... class ModuleWithBuffers(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         self.register_buffer("x", torch.randn(3))
        ...     def forward(self, x):
        ...         return x + self.x
        ... module = ModuleWithBuffers()
        ... x = torch.randn(4, 3)
        ... m = _ModuleStateWithBuffers.from_torch_module(module)
        ... act_res = m(x)
        ... func_module, params, buffers = ft.make_functional_with_buffers(module)
        ... exp_res = func_module(params, buffers, x)
        ... assert torch.allclose(exp_res, act_res)
        ... assert torch.allclose(m.named_buffers.x, buffers[0])
        """
        named_buffers = NamedBuffers.from_module(torch_module)
        func, parameters, buffers = ft.make_functional_with_buffers(
            torch_module, disable_autograd_tracking=True
        )
        return cls(
            module=t.cast(FunctionalModuleWithBuffers[tdf.P, tdf.R_co], func),
            parameters=parameters,
            buffers=buffers,
            named_buffers=named_buffers.evolve_from_values(buffers),
        )

    @property
    def module(self) -> FunctionalModuleWithBuffers[tdf.P, tdf.R_co]:
        return self._module

    @property
    def parameters(self) -> tuple[torch.nn.Parameter, ...]:
        return self._parameters

    @property
    def buffers(self) -> tuple[torch.Tensor, ...]:
        return self._buffers

    @property
    def named_buffers(self) -> NamedBuffers:
        return self._named_buffers

    def apply(
        self,
        params: tuple[torch.nn.Parameter, ...],
        buffers: tuple[torch.Tensor, ...],
        *args: tdf.P.args,
        **kwargs: tdf.P.kwargs,
    ) -> tdf.R_co:
        """Apply the module to the given parameters and buffers.

        Example:

        >>> import torch
        ... import functorch as ft
        ... class ModuleWithBuffers(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         self.linear = torch.nn.Linear(3, 3)
        ...         self.register_buffer("x", torch.randn(3))
        ...     def forward(self, x):
        ...         return self.linear(x) + self.x
        ... module = ModuleWithBuffers()
        ... x = torch.randn(4, 3)
        ... m = _ModuleStateWithBuffers.from_torch_module(module)
        ... exp_res = m(x)
        ... func_module, params, buffers = ft.make_functional_with_buffers(module)
        ... act_res = func_module(params, buffers, x)
        ... assert torch.allclose(exp_res, act_res)
        ... new_params = tuple(p + 1 for p in params)
        ... new_act_res = m.apply(new_params, buffers, x)
        ... new_exp_res = func_module(new_params, buffers, x)
        ... assert torch.allclose(new_exp_res, new_act_res)
        """
        return self._module(params, buffers, *args, **kwargs)

    def evolve(
        self: te.Self,
        parameters: tuple[torch.nn.Parameter, ...] | None = None,
        buffers: tuple[torch.Tensor, ...] | None = None,
        named_buffers: NamedBuffers | None = None,
    ) -> te.Self:
        """Return a new `_ModuleStateWithBuffers` with the given changes.

        Args:
        -----
            parameters: tuple[torch.nn.Parameter, ...] | None
                The new parameters of the module. If None, parameters are not changed.
            buffers: tuple[torch.Tensor, ...] | None
                The new buffers of the module. If None, buffers are not changed.
                Cannot be used together with named_buffers.
            named_buffers: NamedBuffers | None
                The new named buffers of the module. If None, named_buffers are not
                changed.
                Cannot be used together with buffers.
        Returns:
        --------
            A new `_ModuleStateWithBuffers` with the given changes.

        Examples:

        >>> import torch
        ... import functorch as ft
        ... class ModuleWithBuffers(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         self.register_buffer("x", torch.randn(3))
        ...     def forward(self, x):
        ...         return x + self.x
        ... module = ModuleWithBuffers()
        ... x = torch.randn(4, 3)
        ... m = _ModuleStateWithBuffers.from_torch_module(module)
        ... act_res = m(x)
        ... func_module, params, buffers = ft.make_functional_with_buffers(module)
        ... exp_res = func_module(params, buffers, x)
        ... assert torch.allclose(exp_res, act_res)
        ... assert torch.allclose(m.named_buffers.x, buffers[0])
        ... m = m.evolve(buffers=(torch.randn(3),))
        ... new_res = m(x)
        ... assert not torch.allclose(new_res, act_res)

        # Cannot use both buffers and named_buffers
        >>> m = m.evolve(
        ...     buffers=(torch.randn(3),), named_buffers=m.named_buffers
        ... )  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: Cannot specify both buffers and named_buffers
        """
        if parameters is None:
            parameters = self.parameters
        if buffers and named_buffers:
            raise ValueError("Cannot specify both buffers and named_buffers")
        elif buffers:
            named_buffers = self.named_buffers.evolve_from_values(buffers)
        elif named_buffers:
            buffers = tuple(named_buffers.values())
        else:
            buffers = self.buffers
            named_buffers = self.named_buffers
        assert parameters is not None
        assert buffers is not None
        assert named_buffers is not None
        return self.__class__(
            module=self._module,
            parameters=parameters,
            buffers=buffers,
            named_buffers=named_buffers,
        )

    def __call__(self, *args: tdf.P.args, **kwargs: tdf.P.kwargs) -> tdf.R_co:
        return self.module(self.parameters, self.buffers, *args, **kwargs)


class ModuleState(t.Generic[tdf.P, tdf.R_co]):
    """A container for a stateless module, its parameters and its buffers if it has any.

    NOTE: Do not initialize this directly. Use ModuleState.from_torch_module.

    Example:
    1. A module without buffers
    >>> import torch
    ... import functorch as ft
    ... class ModuleWithoutBuffers(torch.nn.Module):
    ...     def __init__(self):
    ...         super().__init__()
    ...         self.linear = torch.nn.Linear(3, 4)
    ...     def forward(self, x, y):
    ...         return self.linear(x) + y
    ... torch_module = ModuleWithoutBuffers()
    ... module_state = ModuleState.from_torch_module(torch_module)
    ... x = torch.randn(4, 3)
    ... y = torch.randn(4, 4)
    ... act_res = module_state(x, y)
    ... func_module, params = ft.make_functional(torch_module)
    ... exp_res = func_module(params, x, y)
    ... assert torch.allclose(exp_res, act_res)

    2. A module with buffers
    >>> import torch
    ... import functorch as ft
    ... class ModuleWithBuffers(torch.nn.Module):
    ...     def __init__(self):
    ...         super().__init__()
    ...         self.register_buffer("x", torch.randn(3))
    ...     def forward(self, x):
    ...         return x + self.x
    ... torch_module = ModuleWithBuffers()
    ... module_state = ModuleState.from_torch_module(torch_module)
    ... x = torch.randn(4, 3)
    ... act_res = module_state(x)
    ... func_module, params, buffers = ft.make_functional_with_buffers(torch_module)
    ... exp_res = func_module(params, buffers, x)
    ... assert torch.allclose(exp_res, act_res)
    ... assert torch.allclose(module_state.named_buffers.x, buffers[0])
    """

    def __init__(
        self,
        module_state: _ModuleStateWithoutBuffers[tdf.P, tdf.R_co]
        | _ModuleStateWithBuffers[tdf.P, tdf.R_co],
    ) -> None:
        self._module_state = module_state
        self._has_buffers = isinstance(module_state, _ModuleStateWithBuffers)
        self._buffers = (
            module_state.buffers
            if isinstance(module_state, _ModuleStateWithBuffers)
            else t.cast(tuple[torch.Tensor, ...], tuple())
        )
        self._named_buffers = (
            module_state.named_buffers
            if isinstance(module_state, _ModuleStateWithBuffers)
            else NamedBuffers({})
        )

    @classmethod
    def from_torch_module(cls: type[te.Self], torch_module: torch.nn.Module) -> te.Self:
        if next(torch_module.buffers(recurse=True), None) is not None:
            # If the module has buffers, use _ModuleStateWithBuffers.
            return cls(
                _ModuleStateWithBuffers[tdf.P, tdf.R_co].from_torch_module(torch_module)
            )
        else:
            # Otherwise, use _ModuleStateWithoutBuffers.
            return cls(
                _ModuleStateWithoutBuffers[tdf.P, tdf.R_co].from_torch_module(
                    torch_module
                )
            )

    @property
    def module(
        self,
    ) -> FunctionalModule[tdf.P, tdf.R_co] | FunctionalModuleWithBuffers[
        tdf.P, tdf.R_co
    ]:
        return self._module_state.module

    @property
    def parameters(self) -> tuple[torch.nn.Parameter, ...]:
        return self._module_state.parameters

    @property
    def buffers(self) -> tuple[torch.Tensor, ...]:
        return self._buffers

    @property
    def named_buffers(self) -> NamedBuffers:
        return self._named_buffers

    @property
    def has_buffers(self) -> bool:
        return self._has_buffers

    def apply(
        self,
        params: tuple[torch.nn.Parameter, ...],
        *args: tdf.P.args,
        **kwargs: tdf.P.kwargs,
    ) -> tdf.R_co:
        """Applies the module with the given parameters and buffers.

        NOTE: This is equivalent to calling the module state directly.

        Example:
        1. A module without buffers
        >>> import torch
        ... import functorch as ft
        ... class ModuleWithoutBuffers(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         self.linear = torch.nn.Linear(3, 4)
        ...     def forward(self, x, y):
        ...         return self.linear(x) + y
        ... torch_module = ModuleWithoutBuffers()
        ... module_state = ModuleState.from_torch_module(torch_module)
        ... x = torch.randn(4, 3)
        ... y = torch.randn(4, 4)
        ... act_res = module_state.apply(module_state.parameters, x, y)
        ... func_module, params = ft.make_functional(torch_module)
        ... exp_res = func_module(params, x, y)
        ... assert torch.allclose(exp_res, act_res)

        2. A module with buffers
        >>> import torch
        ... import functorch as ft
        ... class ModuleWithBuffers(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         self.linear = torch.nn.Linear(3, 3)
        ...         self.register_buffer("x", torch.randn(3))
        ...     def forward(self, x):
        ...         return self.linear(x) + self.x
        ... torch_module = ModuleWithBuffers()
        ... module_state = ModuleState.from_torch_module(torch_module)
        ... func_module, *_ = ft.make_functional_with_buffers(torch_module)
        ... x = torch.randn(4, 3)
        ... act_res = module_state.apply(
        ...     module_state.parameters, x
        ... )
        ... exp_res = func_module(module_state.parameters, module_state.buffers, x)
        ... assert torch.allclose(exp_res, act_res)
        ... new_params = tuple(p + 1 for p in module_state.parameters)
        ... new_act_res = module_state.apply(new_params, x)
        ... assert not torch.allclose(new_act_res, act_res)
        ... new_exp_res = func_module(new_params, module_state.buffers, x)
        ... assert torch.allclose(new_exp_res, new_act_res)
        """
        if self.has_buffers:
            assert isinstance(self._module_state, _ModuleStateWithBuffers)
            return self._module_state.apply(params, self.buffers, *args, **kwargs)
        assert isinstance(self._module_state, _ModuleStateWithoutBuffers)
        return self._module_state.apply(params, *args, **kwargs)

    def apply_with_buffers(
        self,
        params: tuple[torch.nn.Parameter, ...],
        buffers: tuple[torch.Tensor, ...],
        *args: tdf.P.args,
        **kwargs: tdf.P.kwargs,
    ) -> tdf.R_co:
        """Applies the module with the given parameters and buffers.

        NOTE: This is equivalent to calling the module state directly.

        Example:
        1. A module without buffers
        >>> import torch
        ... import functorch as ft
        ... import pytest
        ... class ModuleWithoutBuffers(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         self.linear = torch.nn.Linear(3, 4)
        ...     def forward(self, x, y):
        ...         return self.linear(x) + y
        ... torch_module = ModuleWithoutBuffers()
        ... module_state = ModuleState.from_torch_module(torch_module)
        ... func_module, *_ = ft.make_functional(torch_module)
        ... x = torch.randn(4, 3)
        ... y = torch.randn(4, 4)
        ... act_res = module_state.apply(module_state.parameters, x, y)
        ... exp_res = func_module(module_state.parameters, x, y)
        ... assert torch.allclose(exp_res, act_res)

        2. A module with buffers
        >>> import torch
        ... import functorch as ft
        ... class ModuleWithBuffers(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         self.linear = torch.nn.Linear(3, 3)
        ...         self.register_buffer("x", torch.randn(3))
        ...     def forward(self, x):
        ...         return self.linear(x) + self.x
        ... torch_module = ModuleWithBuffers()
        ... module_state = ModuleState.from_torch_module(torch_module)
        ... func_module, *_ = ft.make_functional_with_buffers(torch_module)
        ... x = torch.randn(4, 3)
        ... act_res = module_state.apply_with_buffers(
        ...     module_state.parameters, module_state.buffers, x
        ... )
        ... exp_res = func_module(module_state.parameters, module_state.buffers, x)
        ... assert torch.allclose(exp_res, act_res)
        ... new_params = tuple(p + 1 for p in module_state.parameters)
        ... new_buffers = tuple(b + 1 for b in module_state.buffers)
        ... new_act_res = module_state.apply_with_buffers(new_params, new_buffers, x)
        ... assert not torch.allclose(new_act_res, act_res)
        ... new_exp_res = func_module(new_params, new_buffers, x)
        ... assert torch.allclose(new_exp_res, new_act_res)
        """
        if not self.has_buffers:
            raise ValueError("This module state does not have buffers.")
        assert isinstance(self._module_state, _ModuleStateWithBuffers)
        return self._module_state.apply(params, buffers, *args, **kwargs)

    def evolve(
        self,
        parameters: tuple[torch.nn.Parameter, ...] | None = None,
        buffers: tuple[torch.Tensor, ...] | None = None,
        named_buffers: NamedBuffers | None = None,
    ) -> "ModuleState[tdf.P, tdf.R_co]":
        """Return a new ModuleState with the specified changes.

        Args:
        -----
            parameters: tuple[torch.nn.Parameter, ...] | None
                If not None, update the parameters.
            buffers: tuple[torch.Tensor, ...] | None
                If not None, update the buffers.
            named_buffers: NamedBuffers | None
                If not None, update the named_buffers.
        Returns:
        --------
            A new ModuleState with the specified changes.
        Raises:
        -------
            ValueError: If both buffers and named_buffers are specified.
            ValueError: If module has no buffers and no parameters are specified.

        Example:
        1. Update parameters
        >>> import torch
        ... import functorch as ft
        ... class ModuleWithoutBuffers(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         self.linear = torch.nn.Linear(3, 4)
        ...     def forward(self, x, y):
        ...         return self.linear(x) + y
        ... torch_module = ModuleWithoutBuffers()
        ... module_state = ModuleState.from_torch_module(torch_module)
        ... x = torch.randn(4, 3)
        ... y = torch.randn(4, 4)
        ... act_res = module_state(x, y)
        ... func_module, params = ft.make_functional(torch_module)
        ... exp_res = func_module(params, x, y)
        ... assert torch.allclose(exp_res, act_res)
        ... new_params = tuple(p + 1 for p in params)
        ... new_module_state = module_state.evolve(parameters=new_params)
        ... new_res = new_module_state(x, y)
        ... assert not torch.allclose(exp_res, new_res)

        2. Update buffers
        >>> import torch
        ... import functorch as ft
        ... class ModuleWithBuffers(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         self.register_buffer("x", torch.randn(3))
        ...     def forward(self, x):
        ...         return x + self.x
        ... torch_module = ModuleWithBuffers()
        ... module_state = ModuleState.from_torch_module(torch_module)
        ... x = torch.randn(4, 3)
        ... act_res = module_state(x)
        ... func_module, params, buffers = ft.make_functional_with_buffers(torch_module)
        ... exp_res = func_module(params, buffers, x)
        ... assert torch.allclose(exp_res, act_res)
        ... new_buffers = tuple(b + 1 for b in buffers)
        ... new_module_state = module_state.evolve(buffers=new_buffers)
        ... new_res = new_module_state(x)
        ... assert not torch.allclose(exp_res, new_res)

        3. Passing both buffers and named_buffers raises ValueError
        >>> import torch
        ... import functorch as ft
        ... import pytest
        ... class ModuleWithBuffers(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         self.register_buffer("x", torch.randn(3))
        ...     def forward(self, x):
        ...         return x + self.x
        ... torch_module = ModuleWithBuffers()
        ... module_state = ModuleState.from_torch_module(torch_module)
        ... x = torch.randn(4, 3)
        ... act_res = module_state(x)
        ... func_module, params, buffers = ft.make_functional_with_buffers(torch_module)
        ... exp_res = func_module(params, buffers, x)
        ... assert torch.allclose(exp_res, act_res)
        ... new_buffers = tuple(b + 1 for b in buffers)
        ... new_named_buffers = module_state.named_buffers.evolve_from_values(
        ...     new_buffers
        ... )
        ... with pytest.raises(ValueError):
        ...     module_state.evolve(
        ...         buffers=new_buffers, named_buffers=new_named_buffers
        ...     )
        """
        if not self.has_buffers:
            if not parameters:
                raise ValueError(
                    "parameters must be specified when the module has no buffers."
                )
            return self.__class__(self._module_state.evolve(parameters=parameters))
        assert isinstance(self._module_state, _ModuleStateWithBuffers)
        if buffers and named_buffers:
            raise ValueError("Cannot specify both buffers and named_buffers")
        return self.__class__(
            self._module_state.evolve(
                parameters=parameters, buffers=buffers, named_buffers=named_buffers
            )
        )

    def to(self, *args: t.Any, **kwargs: t.Any) -> "ModuleState[tdf.P, tdf.R_co]":
        """Move the buffers to the specified device.

        Args:
        -----
            *args: Any
            **kwargs: Any
            Any arguments accepted by torch.Tensor.to(...).
        Returns:
        --------
            A new ModuleState with the buffers moved to the specified device and/or
            dtype and/or memory format.

        Examples:
        ---------

        >>> import torch
        ... import functorch as ft
        ... import torchsilk as tsk
        ... class ModuleWithBuffers(torch.nn.Module):
        ...     def __init__(self):
        ...         super().__init__()
        ...         self.register_buffer("x", torch.randn(3))
        ...     def forward(self, x):
        ...         return x + self.x
        ... torch_module = ModuleWithBuffers()
        ... module_state = ModuleState.from_torch_module(torch_module)
        ... float64_module_state = module_state.to(dtype=torch.float64)
        ... assert float64_module_state.named_buffers.x.dtype == torch.float64
        """
        new_params = t.cast(
            tuple[torch.nn.Parameter, ...],
            tuple(x.to(*args, **kwargs) for x in self.parameters),
        )
        new_named_buffers = {
            k: v.to(*args, **kwargs) for k, v in self.named_buffers.items()
        }
        new_buffers = tuple(new_named_buffers.values())
        return self.__class__(
            module_state=_ModuleStateWithBuffers(
                module=self.module,  # type: ignore
                parameters=new_params,
                buffers=new_buffers,
                named_buffers=NamedBuffers(new_named_buffers),
            )
            if new_buffers
            else _ModuleStateWithoutBuffers(
                module=self.module, parameters=new_params  # type: ignore
            )
        )

    def __call__(self, *args: tdf.P.args, **kwargs: tdf.P.kwargs) -> tdf.R_co:
        return self._module_state(*args, **kwargs)

    def __str__(self) -> str:
        return str(self._module_state)
