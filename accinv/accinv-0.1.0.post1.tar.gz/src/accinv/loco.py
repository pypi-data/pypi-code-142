# SPDX-FileCopyrightText: 2022 Dominik Vilsmeier
#
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from dataclasses import dataclass
from functools import partial
import inspect
import math
from typing import (
    Any, Collection, Mapping, Optional, Protocol, Union, Type,
    cast,
)
from typing_extensions import TypeAlias

import numpy as np
from numpy.typing import NDArray

from .jacobian import (
    ComputeOrmFunction,
    ComputeJacobianFunction,
    AnalyticalJacobianMethod, NumericalJacobianMethod,
)
from .model import (
    Jacobian, Model, OpticsModel, ORM, OrmShape,
    ParameterUpdate,
)
from .optim import Optimizer, LeastSquares, Result
from .parameters import (
    ParameterGroup, AnalyticalParameterGroup, NumericalParameterGroup,
    HBpmGainErrors, HSteererGainErrors, VBpmGainErrors, VSteererGainErrors,
    Multipoles, Quadrupoles,
)
from .utils import chain_function_calls, is_iterator_exhausted, lowercase


__all__ = [
    'Loco', 'OrmMeasurement',
    'MissingElementsError',
]


array = np.ndarray


ModelAndJacobianMethod: TypeAlias = Union[
    tuple[Model, Type[NumericalJacobianMethod]],
    tuple[OpticsModel, Type[AnalyticalJacobianMethod]],
    tuple[Model, ComputeJacobianFunction],
]


@dataclass(frozen=True)
class OrmMeasurement:
    """This class represents the data for an ORM measurement."""
    orm: ORM
    uncertainty: ORM


class CustomizeResiduals(Protocol):
    def __call__(self, x: array, residuals: array) -> array:
        """Given the current parameter estimate `x` and the `residuals`,
           compute and return a customized version of the residuals.
        """
        ...


class CustomizeJacobian(Protocol):
    def __call__(self, x: array, jacobian: array) -> array:
        """Given the current parameter estimate `x` and `jacobian`,
           compute and return a customized version of the Jacobian.
        """
        ...


class SelectMainDiagonalBlocks:
    """Helper class for selecting main diagonal blocks from the ORM and Jacobian.

    Args:
        n_hbpms: Number of horizontal BPMs.
        n_hsteerers: Number of horizontal steerers.
        n_vbpms: Number of vertical BPMs.
        n_vsteerers: Number of vertical steerers.
    """

    def __init__(self, n_hbpms: int, n_hsteerers: int, n_vbpms: int, n_vsteerers: int):
        self.n_hbpms = n_hbpms
        self.n_hsteerers = n_hsteerers
        self.n_vbpms = n_vbpms
        self.n_vsteerers = n_vsteerers

    @property
    def orm_shape(self) -> OrmShape:
        return (self.n_hbpms + self.n_vbpms, self.n_hsteerers + self.n_vsteerers)

    def build_main_diagonal_block_indices(self) -> NDArray[np.int64]:
        """Return an index array which selects the main diagonal blocks from a flattened ORM."""
        indices = np.arange(math.prod(self.orm_shape)).reshape(self.orm_shape)
        hh = indices[:self.n_hbpms, :self.n_hsteerers]
        vv = indices[self.n_hbpms:, self.n_hsteerers:]
        return np.concatenate([hh.ravel(), vv.ravel()])

    def select_diagonal_blocks_from_residuals(self, _: array, residuals: array) -> array:
        """Select the main diagonal ORM blocks from the given `residuals`."""
        return residuals[self.build_main_diagonal_block_indices()]

    def select_diagonal_blocks_from_jacobian(self, _: array, jacobian: array) -> array:
        """Select the main diagonal ORM blocks from the given `jacobian`."""
        return jacobian[self.build_main_diagonal_block_indices(), :]


def _leave_as_is(x: array, quantity: array) -> array:
    return quantity


class Loco:
    """Main class for inverse modeling of linear optics from closed orbits.

    .. note::
       The order in which fitting parameters are appended from shorthand arguments is the
       same in which they appear in the function signature, i.e. `quadrupoles` followed by
       `multipoles` and gain errors. This is the same order in which the resulting parameter
       estimates are reported.

    .. note::
       Any element or parameter names should be given in lowercase. This is the convention
       used by the :class:`Model` backends. While lowercase conversion is ensured for the
       shorthand arguments (e.g. `quadrupoles`) this is not done for the parameters specified
       via `parameters`.

    Args:
        model_and_jacobian_method: The accelerator model and the Jacobian method to be used
                                   for computations.
        hbpms: Names of horizontal BPMs.
        hsteerers: Names of horizontal steerers.
        vbpms: Names of vertical BPMs.
        vsteerers: Names of vertical steerers.
        orm_measurement: The measured ORM and uncertainty to be fitted against the `model`.
        quadrupoles: Names of thick quadrupoles which are added as parameters to the fitting.
            This is a shorthand argument. Internally, the given names are converted to
            :class:`Quadrupoles`.
        multipoles: Names of thin multipoles which are then added as parameters to the fitting.
            This is a shorthand argument. Internally, the given names are converted to
            :class:`Multipoles`.
        fit_gain_errors: Flag to indicate whether BPM and steerer gain errors should be fitted.
            If true (the default), then those gain error parameters are appended to the specified
            `parameters` which are not present there yet.
        parameters: The parameters to be fitted. If `fit_gain_errors` is true, then the corresponding
            parameters will be added automatically, i.e. they should not appear here.
        remove_coupling_blocks_from_orm: (optional, default: False) If true, only the main diagonal
            blocks of the ORM will be used for fitting. This realized by modifying the residuals and
            Jacobian similar to `customize_residuals` and `customize_jacobian`. The selection of main
            diagonal blocks is inserted *before* these custom functions which will only receive the
            main diagonal blocks as arguments.
        optimizer: The choice of optimizer for the fitting procedure (defaults to
            :class:`LeastSquares`).
        compute_orm_kwargs: Additional keyword arguments for the ORM computation via
            :meth:`Model.compute_orm`. This includes the ``kicks`` keyword argument which will default
            to :attr:`Loco.DEFAULT_STEERER_KICKS` if not specified.
        customize_residuals: Callable which receives the current parameter guess and the corresponding
            residuals to return a customized version of the residuals.
        customize_jacobian: Callable which receives the current parameter guess and the corresponding
            Jacobian to return a customized version of the Jacobian.
    """

    DEFAULT_STEERER_KICKS = [1e-4]

    def __init__(
        self,
        model_and_jacobian_method: ModelAndJacobianMethod,
        *,
        hbpms: Collection[str],
        hsteerers: Collection[str],
        vbpms: Collection[str],
        vsteerers: Collection[str],
        orm_measurement: OrmMeasurement,
        quadrupoles: Optional[Collection[str]] = None,
        multipoles: Optional[Collection[str]] = None,
        fit_gain_errors: bool = True,
        parameters: Optional[Collection[ParameterGroup]] = None,
        remove_coupling_blocks_from_orm: bool = False,
        optimizer: Optional[Optimizer] = None,
        compute_orm_kwargs: Optional[dict[str, Any]] = None,
        customize_residuals: Optional[CustomizeResiduals] = None,
        customize_jacobian: Optional[CustomizeJacobian] = None,
    ):
        self.model_and_jacobian_method = model_and_jacobian_method
        self.parameters = list(parameters or [])
        self.hbpms = lowercase(hbpms)
        self.hsteerers = lowercase(hsteerers)
        self.vbpms = lowercase(vbpms)
        self.vsteerers = lowercase(vsteerers)
        self.orm_measurement = orm_measurement
        self.optimizer = optimizer or LeastSquares()
        self.compute_orm_kwargs = compute_orm_kwargs or {}
        self.compute_orm_kwargs.setdefault('kicks', self.DEFAULT_STEERER_KICKS)
        self.customize_residuals = customize_residuals or _leave_as_is
        self.customize_jacobian = customize_jacobian or _leave_as_is
        if remove_coupling_blocks_from_orm:
            helper = SelectMainDiagonalBlocks(
                n_hbpms=len(self.hbpms),
                n_hsteerers=len(self.hsteerers),
                n_vbpms=len(self.vbpms),
                n_vsteerers=len(self.vsteerers),
            )
            self.customize_residuals = chain_function_calls(
                [
                    self.customize_residuals,
                    lambda x, r, h=helper: (x, h.select_diagonal_blocks_from_residuals(x, r)),
                ],
                unpack=True,
            )
            self.customize_jacobian = chain_function_calls(
                [
                    self.customize_jacobian,
                    lambda x, j, h=helper: (x, h.select_diagonal_blocks_from_jacobian(x, j)),
                ],
                unpack=True,
            )
            del helper
        if quadrupoles:
            self.parameters.append(Quadrupoles.from_model(
                model_and_jacobian_method[0],
                names=lowercase(quadrupoles),
            ))
        if multipoles:
            self.parameters.append(Multipoles(names=lowercase(multipoles)))
        if fit_gain_errors:
            for names, type_ in zip(
                [hbpms, hsteerers, vbpms, vsteerers],
                [HBpmGainErrors, HSteererGainErrors, VBpmGainErrors, VSteererGainErrors]
            ):
                if not any(isinstance(p, type_) for p in self.parameters):
                    orm_shape = cast(OrmShape, orm_measurement.orm.shape)
                    self.parameters.append(type_(n=len(names), orm_shape=orm_shape))

        self.check_missing_elements(dict(
            hbpm=self.hbpms,
            hsteerer=self.hsteerers,
            vbpm=self.vbpms,
            vsteerer=self.vsteerers,
        ))

    def run(self, *, guess: Optional[array] = None, maxiter: Optional[int] = None) -> Result:
        """Start the inverse modeling and return the result.

        Args:
            guess: Optional initial guess for the parameter values (defaults to zero).
            maxiter: Maximum number of iterations in terms of the Jacobian evaluation.

        Returns:
            :class:`Result` object which contains various information about the fitting result;
            ``result.x`` are the final parameter values.
        """
        wrapper = self.build_wrapper()
        wrapper.maxiter = maxiter
        if guess is None:
            guess = np.zeros(wrapper.n_parameters)
        try:
            result = self.optimizer.run(
                f=lambda x: self.customize_residuals(x, wrapper.f(x)),
                j=lambda x: self.customize_jacobian(x, wrapper.j(x)),
                x0=guess,
            )
        except MaxIterDone as r:
            result = Result(
                x=r.x,
                fun=self.customize_residuals(r.x, r.fun),
                jac=self.customize_jacobian(r.x, r.jac),
                nfev=r.nfev,
                njev=r.njev,
                status=r.status,
                message=r.message,
            )
        return result

    def build_wrapper(self) -> Wrapper:
        """Build the :class:`Wrapper` instance for this instance."""
        model, jacobian_method = self.model_and_jacobian_method
        compute_orm = partial(
            model.compute_orm,
            hbpms=self.hbpms,
            hsteerers=self.hsteerers,
            vbpms=self.vbpms,
            vsteerers=self.vsteerers,
            **self.compute_orm_kwargs,
        )
        compute_jacobian: ComputeJacobianFunction  # be explicit for the type checker
        if inspect.isclass(jacobian_method) and issubclass(jacobian_method, AnalyticalJacobianMethod):
            if not isinstance(model, OpticsModel):
                raise TypeError(
                    f'AnalyticalJacobianMethod only works with an instance of OpticsModel '
                    f'(got {type(model)} instead)'
                )
            compute_jacobian = AnalyticalJacobianMethod(
                model=model,
                hbpms=self.hbpms,
                hsteerers=self.hsteerers,
                vbpms=self.vbpms,
                vsteerers=self.vsteerers,
            ).compute
        elif inspect.isclass(jacobian_method) and issubclass(jacobian_method, NumericalJacobianMethod):
            compute_jacobian = NumericalJacobianMethod(
                model=model,
                hbpms=self.hbpms,
                hsteerers=self.hsteerers,
                vbpms=self.vbpms,
                vsteerers=self.vsteerers,
                compute_orm_kwargs=self.compute_orm_kwargs,
            ).compute
        elif callable(jacobian_method):
            compute_jacobian = cast(ComputeJacobianFunction, jacobian_method)
        else:
            raise TypeError(
                f'Invalid type for jacobian_method: {type(jacobian_method)}. '
                f'Must be one of {AnalyticalJacobianMethod}, {NumericalJacobianMethod} '
                f'or a custom callable object with signature according to {ComputeJacobianFunction}.'
            )
        return Wrapper(
            compute_orm=compute_orm,
            compute_jacobian=compute_jacobian,
            parameters=self.parameters,
            hbpms=self.hbpms,
            hsteerers=self.hsteerers,
            vbpms=self.vbpms,
            vsteerers=self.vsteerers,
            target=self.orm_measurement.orm,
            uncertainty=self.orm_measurement.uncertainty,
            compute_orm_kwargs=self.compute_orm_kwargs,
        )

    def check_missing_elements(self, elements: Mapping[str, Collection[str]]) -> None:
        """Check if any of the specified elements are missing in the model.

        Args:
            elements: Maps arbitrary labels to names of elements.

        Raises:
            MissingElementsError: If any of the specified elements are missing.
        """
        model = self.model_and_jacobian_method[0]
        for label, specified in elements.items():
            found, = model.get_element_names(specified)
            if (missing := set(specified) - set(found)):
                raise MissingElementsError(label, sorted(missing))


class Wrapper:
    """Internal class which handles the computation logic during the fitting."""

    def __init__(
        self,
        compute_orm: ComputeOrmFunction,
        compute_jacobian: ComputeJacobianFunction,
        *,
        parameters: Collection[ParameterGroup],
        hbpms: Collection[str],
        hsteerers: Collection[str],
        vbpms: Collection[str],
        vsteerers: Collection[str],
        target: array,
        uncertainty: array,
        compute_orm_kwargs: Optional[dict[str, Any]] = None,
        maxiter: Optional[int] = None,
    ):
        self.compute_orm = compute_orm
        self.compute_jacobian = compute_jacobian
        self.parameters = list(parameters)
        self.hbpms = hbpms
        self.hsteerers = hsteerers
        self.vbpms = vbpms
        self.vsteerers = vsteerers
        self.target = target
        self.uncertainty = uncertainty
        self.compute_orm_kwargs = compute_orm_kwargs or {}
        self.maxiter = maxiter
        self.itercount = 0
        self.f_history: list[tuple[array, array]] = []
        self.j_history: list[tuple[array, array]] = []

    @property
    def n_hbpms(self):
        return len(self.hbpms)

    @property
    def n_hsteerers(self):
        return len(self.hsteerers)

    @property
    def n_vbpms(self):
        return len(self.vbpms)

    @property
    def n_vsteerers(self):
        return len(self.vsteerers)

    @property
    def n_parameters(self):
        return sum(p.count for p in self.parameters)

    def f(self, x: array) -> array:
        """Wrapper around the function which computes the ORM.

        Args:
            x: The current estimate of parameter values.

        Returns:
            The residuals emerging from the estimate `x`, scaled according to
            the measurement uncertainty.
        """
        pv_numerical, pv_analytical = self.collect_numerical_and_analytical_parameters(x)
        simulated = self.compute_orm(
            configuration=self.build_configuration_from_parameter_values(pv_numerical),
        )
        for group, values in pv_analytical:
            simulated = group.update_orm(simulated, values)
        residuals = np.ravel(simulated - self.target)
        self.f_history.append((x.copy(), residuals))
        return residuals / self.uncertainty.ravel()

    def j(self, x: array) -> array:
        """Wrapper around the function which computes the Jacobian.

        Args:
            x: The current estimate of parameter values.

        Returns:
            The Jacobian emerging from the estimate `x`, scaled according to
            the measurement uncertainty.
        """
        pv_numerical, pv_analytical = self.collect_numerical_and_analytical_parameters(x)
        configuration = self.build_configuration_from_parameter_values(pv_numerical)
        if pv_analytical:
            orm = self.compute_orm(configuration=configuration)
        else:
            orm = np.empty(0)  # not used, but satisfies the type checker
        J_parts: list[Jacobian] = []
        p_analytical_column_offsets: list[int] = []
        column_offset = 0
        for group in self.parameters:
            if isinstance(group, NumericalParameterGroup):
                part, __ = self.compute_jacobian([group], configuration)
            elif isinstance(group, AnalyticalParameterGroup):
                assert orm.size > 0
                part = group.build_jacobian(orm)
                p_analytical_column_offsets.append(column_offset)
            else:
                raise TypeError(f'Unknown type for parameter group: {type(group)}')
            J_parts.append(part)
            column_offset += group.count
        J = np.concatenate(J_parts, axis=1)
        assert len(p_analytical_column_offsets) == len(pv_analytical)
        for (group, values), offset in zip(pv_analytical, p_analytical_column_offsets):
            J = group.update_jacobian(J, values, column_offset=offset)

        self.itercount += 1
        if self.maxiter and self.itercount > self.maxiter:
            if orm.size == 0:
                orm = self.compute_orm(configuration=configuration)
            raise MaxIterDone(
                x=x,
                fun=np.ravel(orm-self.target),
                jac=J,
                nfev=len(self.f_history)+len(self.j_history),
                njev=len(self.j_history),
            )
        else:
            self.j_history.append((x.copy(), J))

        return J / self.uncertainty.ravel()[:,np.newaxis]

    def collect_numerical_and_analytical_parameters(
        self,
        x: array,
    ) -> tuple[list[tuple[NumericalParameterGroup,array]], list[tuple[AnalyticalParameterGroup,array]]]:
        """Separate the fitting parameters into numerical and analytical groups
           together with their parameter values.

        Args:
            x: Estimate of parameter values.

        Returns:
            The tuple ``(p_numerical, p_analytical)`` where ``p_numerical`` are the numerical
            parameters together with their values from `x`, as tuples, and ``p_analytical``
            are the analytical parameters together with their values from `x`, as tuples.
        """
        pv_numerical: list[tuple[NumericalParameterGroup, array]] = []
        pv_analytical: list[tuple[AnalyticalParameterGroup, array]] = []
        ix = iter(x)
        for group in self.parameters:
            values = np.fromiter(ix, count=group.count, dtype=x.dtype)
            if isinstance(group, NumericalParameterGroup):
                pv_numerical.append((group, values))
            elif isinstance(group, AnalyticalParameterGroup):
                pv_analytical.append((group, values))
            else:
                raise TypeError(f'Unknown type for parameter group: {type(group)}')
        assert is_iterator_exhausted(ix)
        return pv_numerical, pv_analytical

    def build_configuration_from_parameter_values(
        self,
        parameters_with_values: Collection[tuple[NumericalParameterGroup, array]],
    ) -> list[ParameterUpdate]:
        """Build and return the configuration for the given ``(parameters, values)`` pairs."""
        configuration: list[ParameterUpdate] = []
        for group, values in parameters_with_values:
            configuration.extend(group.build_configuration_from_values(values))
        return configuration


class MaxIterDone(Exception):
    def __init__(
        self,
        *,
        x: array,
        fun: array,
        jac: array,
        nfev: int,
        njev: int,
    ):
        self.x = x
        self.cost = self.compute_cost(fun)
        self.fun = fun
        self.jac = jac
        self.grad = jac.T @ fun
        self.nfev = nfev
        self.njev = njev
        self.status = 0
        self.message = 'maximum number of jacobian evaluations exceeded'
        self.success = False

    @staticmethod
    def compute_cost(residuals: array) -> float:
        return 0.5 * np.sum(residuals**2)


class MissingElementsError(Exception):
    def __init__(self, type_: str, names: Collection[str], /):
        super().__init__(
            f'The following {type_} elements could not be found in the model: '
            f'{sorted(names)!r}'
        )
        self.names = names
