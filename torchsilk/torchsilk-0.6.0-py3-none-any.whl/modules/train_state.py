"""TrainState class for torchsilk."""
import typing as t

import attrs
import functorch as ft
import torch
import torchopt as tpt
import typing_extensions as tx
from optree import PyTreeTypeVar

from torchsilk.type_defs import P

R = t.TypeVar("R", torch.Tensor, tuple[torch.Tensor, ...])
R_co = t.TypeVar("R_co", torch.Tensor, tuple[torch.Tensor, ...], covariant=True)
ParamsTree: t.TypeAlias = PyTreeTypeVar("ParamsTree", torch.nn.Parameter)  # type: ignore  # noqa: E501
ParamsT_contra = t.TypeVar("ParamsT_contra", bound=ParamsTree, contravariant=True)
ParamsT = t.TypeVar("ParamsT", bound=ParamsTree)
OptStateT = t.TypeVar("OptStateT")
OptStateT_co = t.TypeVar("OptStateT_co", covariant=True)


class TransformInitFn(t.Protocol[ParamsT_contra, OptStateT_co]):
    """Typed version of `torchopt.<opt_func>.init`.

    <opt_func> is the name of the optimizer function, e.g. `adam`.

    See FunctionalOptimizer for more details.
    """

    def __call__(self, params: ParamsT_contra) -> OptStateT_co:
        raise NotImplementedError


class TransformUpdateFn(t.Protocol[ParamsT, OptStateT]):
    """Typed version of `torchopt.<opt_func>.update`.

    <opt_func> is the name of the optimizer function, e.g. `adam`.

    See FunctionalOptimizer for more details.
    """

    def __call__(
        self,
        updates: ParamsT,
        state: OptStateT,
        *,
        params: ParamsT | None = ...,
        inplace: bool = ...,
    ) -> t.Tuple[ParamsT, OptStateT]:
        """Update the parameters with updates."""
        raise NotImplementedError


class FunctionalOptimizer(t.Protocol[ParamsT, OptStateT]):
    """Typed version of `torchopt.<opt_func>`.

    <opt_func> is the name of the optimizer function, e.g. `adam`. Calling an optimizer
    function in torchopt returns an object that follows this protocol.

    Attributes:
    -----------
        init: The init function of the optimizer. Used to initialize the optimizer state
            from the parameters.
        update: The update function of the optimizer. Used to update the parameters with
            the updates for a given optimizer state.

    Example:
    --------
    >>> import torchopt as tpt
    ... import torchsilk as ts
    ... params = torch.nn.Parameter(torch.randn(3, 3))
    ... opt_func = tpt.adam(1e-3)
    ... opt_state = opt_func.init(params)
    ... gradients = torch.randn(3, 3)
    ... updates, opt_state = opt_func.update(gradients, opt_state)
    ... new_params = tpt.apply_updates(params, updates, inplace=False)
    ... assert not torch.allclose(params, new_params)
    """

    @property
    def init(self) -> TransformInitFn[ParamsT, OptStateT]:
        raise NotImplementedError

    @property
    def update(self) -> TransformUpdateFn[ParamsT, OptStateT]:
        raise NotImplementedError


class LossFunction(t.Protocol[ParamsT_contra, P, R_co]):
    """Protocol for loss funcrtions that can be used with TrainState.

    Attributes:
    -----------
        params: The parameters to be optimized.
        args: The positional arguments to the loss function.
        kwargs: The keyword arguments to the loss function.

    Returns:
    --------
        The loss value.
    """

    def __call__(
        self, params: ParamsT_contra, *args: P.args, **kwargs: P.kwargs
    ) -> R_co:
        raise NotImplementedError


@attrs.define()
class TrainState(t.Generic[ParamsT, P, R, OptStateT]):
    """The TrainState is an abstraction for the training state of a model.

    It contains the parameters to be optimized, the loss function, the optimizer, and
    the optimizer state.

    Attributes:
    -----------
        params: ParamsT
            The parameters to be optimized.
        has_aux: bool
            Whether the loss function returns additional values besides the loss.
        loss_fn: LossFunction[ParamsT, P, R]
            The loss function.
        opt_func: torchopt.<opt_func>, like torchopt.adam. FunctionalOptimizer
            The optimizer function.
        arg_nums: tuple[int, ...]
            The positional indices of the arguments wrt the loss function for which the
            gradients are to be computed.
        opt_state: OptStateT
            The optimizer state.
    """

    params: ParamsT
    loss_fn: LossFunction[ParamsT, P, R]
    opt_func: FunctionalOptimizer[ParamsT, OptStateT]

    has_aux: bool = False
    arg_nums: tuple[int, ...] = (0,)
    opt_state: OptStateT = attrs.field(default=None)

    def __attrs_post_init__(self) -> None:
        if self.opt_state is None:
            self.opt_state = self.opt_func.init(self.params)

    @property
    def grad_fn(
        self,
    ) -> t.Callable[t.Concatenate[ParamsT, P], ParamsT]:
        """The gradient function for the loss function.

        Returns:
        --------
            A function that takes the parameters, and the positional and keyword
            arguments to the loss function, and returns the gradients of the loss wrt
            the parameters.

        Example:
        --------

        >>> import torchsilk as ts
        ... import torchopt as tpt
        ... params = torch.nn.Parameter(torch.randn(3, 3))
        ... loss_fn = lambda params, x: torch.sum(params * x)
        ... opt_func = tpt.adam(1e-3)
        ... train_state = ts.TrainState(params, loss_fn, opt_func)
        ... x = torch.randn(3, 3)
        ... gradients = train_state.grad_fn(params, x)
        ... assert torch.allclose(gradients[0], x)
        """
        return t.cast(
            t.Callable[t.Concatenate[ParamsT, P], ParamsT],
            ft.grad(
                self.loss_fn,
                argnums=self.arg_nums,
                has_aux=self.has_aux,
            ),
        )

    @property
    def grad_and_value_fn(
        self,
    ) -> t.Callable[t.Concatenate[ParamsT, P], t.Tuple[ParamsT, R]]:
        """The gradient and value function for the loss function.

        Returns:
        --------
            A function that takes the parameters, and the positional and keyword
            arguments to the loss function, and returns the gradients of the loss wrt
            the parameters, and the loss value.

        Example:
        --------
        >>> import torchsilk as ts
        ... import torchopt as tpt
        ... params = torch.nn.Parameter(torch.randn(3, 3))
        ... loss_fn = lambda params, x: torch.sum(params * x)
        ... opt_func = tpt.adam(1e-3)
        ... train_state = ts.TrainState(params, loss_fn, opt_func)
        ... x = torch.randn(3, 3)
        ... gradients, value = train_state.grad_and_value_fn(params, x)
        ... assert torch.allclose(gradients[0], x)
        ... assert torch.allclose(value, torch.sum(params * x))
        """
        return t.cast(
            t.Callable[t.Concatenate[ParamsT, P], ParamsT],
            ft.grad_and_value(
                self.loss_fn,
                argnums=self.arg_nums,
                has_aux=self.has_aux,
            ),
        )

    def step(self: tx.Self, *args: P.args, **kwargs: P.kwargs) -> tx.Self:
        """Perform a single step of optimization.

        Args:
        -----
            args: The positional arguments to the loss function.
            kwargs: The keyword arguments to the loss function.

        Returns:
        --------
            The updated TrainState.

        Example:
        --------
        >>> import pytest
        ... import torchsilk as ts
        ... import torchopt as tpt
        ... params = torch.nn.Parameter(torch.randn(3, 3))
        ... loss_fn = lambda params, x: torch.sum(params * x)
        ... opt_func = tpt.adam(1e-3)
        ... train_state = ts.TrainState(params, loss_fn, opt_func)
        ... orig_opt_state = train_state.opt_state
        ... x = torch.randn(3, 3)
        ... train_state = train_state.step(x)
        ... assert not torch.allclose(params, train_state.params)
        ... assert orig_opt_state is not train_state.opt_state
        """
        grad = self.grad_fn(self.params, *args, **kwargs)
        updates, new_opt_state = self.opt_func.update(
            grad, self.opt_state, params=self.params
        )
        new_params = tpt.apply_updates(self.params, updates[0], inplace=False)
        return self.__class__(
            params=new_params,
            has_aux=self.has_aux,
            loss_fn=self.loss_fn,
            opt_func=self.opt_func,
            arg_nums=self.arg_nums,
            opt_state=new_opt_state,
        )

    def step_and_value(
        self: tx.Self, *args: P.args, **kwargs: P.kwargs
    ) -> t.Tuple[tx.Self, R]:
        """Perform a single step of optimization, and return the loss value.

        Args:
        -----
            args: The positional arguments to the loss function.
            kwargs: The keyword arguments to the loss function.

        Returns:
        --------
            The updated TrainState, and the loss value.

        Example:
        --------
        >>> import pytest
        ... import torchsilk as ts
        ... import torchopt as tpt
        ... params = torch.nn.Parameter(torch.randn(3, 3))
        ... loss_fn = lambda params, x: torch.sum(params * x)
        ... opt_func = tpt.adam(1e-3)
        ... train_state = ts.TrainState(params, loss_fn, opt_func)
        ... orig_opt_state = train_state.opt_state
        ... x = torch.randn(3, 3)
        ... train_state, value = train_state.step_and_value(x)
        ... assert not torch.allclose(params, train_state.params)
        ... assert orig_opt_state is not train_state.opt_state
        ... assert torch.allclose(value, torch.sum(params * x))
        """
        grad, value = self.grad_and_value_fn(self.params, *args, **kwargs)
        updates, new_opt_state = self.opt_func.update(
            grad, self.opt_state, params=self.params
        )
        new_params = tpt.apply_updates(self.params, updates[0], inplace=False)
        return (
            self.__class__(
                params=new_params,
                has_aux=self.has_aux,
                loss_fn=self.loss_fn,
                opt_func=self.opt_func,
                arg_nums=self.arg_nums,
                opt_state=new_opt_state,
            ),
            value,
        )

    def evolve(
        self: tx.Self,
        *,
        params: ParamsT | None = None,
        has_aux: bool | None = None,
        loss_fn: LossFunction[ParamsT, P, R] | None = None,
        opt_func: FunctionalOptimizer[ParamsT, OptStateT] | None = None,
        arg_nums: tuple[int, ...] | None = None,
        opt_state: OptStateT | None = None,
    ) -> tx.Self:
        """Return a new TrainState with the given attributes replaced.

        Args:
        -----
            params: The new params.
            has_aux: The new has_aux.
            loss_fn: The new loss_fn.
            opt_func: The new opt_func.
            arg_nums: The new arg_nums.
            opt_state: The new opt_state.

        Returns:
        --------
            A new TrainState with the given attributes replaced.
        """
        return self.__class__(
            params=self.params if params is None else params,
            has_aux=self.has_aux if has_aux is None else has_aux,
            loss_fn=self.loss_fn if loss_fn is None else loss_fn,
            opt_func=self.opt_func if opt_func is None else opt_func,
            arg_nums=self.arg_nums if arg_nums is None else arg_nums,
            opt_state=self.opt_state if opt_state is None else opt_state,
        )
