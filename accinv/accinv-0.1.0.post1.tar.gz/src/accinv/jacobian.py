# SPDX-FileCopyrightText: 2022 Dominik Vilsmeier
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Module containing functionality for computing the Jacobian of the ORM.

The layout of the Jacobian is based on the following convention:

* The ORM appears along the rows (``axis=0``) as a column-major flattened
  array.
* The columns of the Jacobian correspond to the various parameters in the same
  order in which those parameters have been specified.

In the following, in ``HH, HV, VH, VV`` the first letter denotes BPMs and the
second letter denotes steerers; e.g. ``HV`` means horizontal BPMs and vertical
steerers, i.e. the right upper block of the ORM. The ORM generally looks like:

.. code-block::

   +------+------+
   |      |      |
   |  HH  |  HV  |
   |      |      |
   +------+------+
   |      |      |
   |  VH  |  VV  |
   |      |      |
   +------+------+

Then the Jacobian looks like:

.. code-block::

   +---PARAMETERS---+
   |                |
   H                |
   H                |
   |                |
   +----------------+
   |                |
   H                |
   V                |
   |                |
   +----------------+
   |                |
   V                |
   H                |
   |                |
   +----------------+
   |                |
   V                |
   V                |
   |                |
   +----------------+

"""

from __future__ import annotations

from functools import partial
from math import pi
from typing import Any, Collection, Mapping, Optional, Protocol

import numpy as np
from numpy import cos, sin, sqrt, tan

from .model import (
    Configuration, Jacobian, Model, OpticsModel, ORM, TwissTable,
)
from .parameters import NumericalParameterGroup, Quadrupoles


__all__ = [
    'AnalyticalJacobianMethod', 'NumericalJacobianMethod',
    'ComputeOrmFunction', 'ComputeJacobianFunction',
]


array = np.ndarray


class ComputeOrmFunction(Protocol):
    def __call__(self, configuration: Optional[Configuration] = None) -> ORM:
        """Given the `configuration`, compute and return the corresponding ORM."""
        ...


class ComputeJacobianFunction(Protocol):
    def __call__(
        self,
        parameters: Collection[NumericalParameterGroup],
        configuration: Optional[Configuration] = None,
    ) -> tuple[Jacobian, ORM]:
        """Compute the Jacobian for the given `parameters` and `configuration`.

        Args:
            parameters: The parameter groups for which to compute the Jacobian.
                The individual parts of the Jacobian, along its columns, correspond to
                the order in which parameter groups are specified.
            configuration: The lattice configuration at which to compute the Jacobian.

        Returns:
            The tuple ``(jacobian, orm)``.
        """
        ...


class JacobianMethod:
    def compute(
        self,
        parameters: Collection[NumericalParameterGroup],
        configuration: Optional[Configuration] = None,
    ) -> tuple[Jacobian, ORM]:
        raise NotImplementedError

    compute.__doc__ = ComputeJacobianFunction.__call__.__doc__


class NumericalJacobianMethod(JacobianMethod):
    """Uses finite difference approximation (one step) to compute the Jacobian.

    Args:
        model: The model which will be used to compute ORMs to construct the Jacobian.
        hbpms: Names of horizontal BPMs.
        hsteerers: Names of horizontal steerers.
        vbpms: Names of vertical BPMs.
        vsteerers: Names of vertical steerers.
        compute_orm_kwargs: Keyword arguments for :meth:`Model.compute_orm`.
    """

    def __init__(
        self,
        *,
        model: Model,
        hbpms: Collection[str],
        hsteerers: Collection[str],
        vbpms: Collection[str],
        vsteerers: Collection[str],
        compute_orm_kwargs: Mapping[str, Any],
    ):
        self.model = model
        self.compute_orm: ComputeOrmFunction = partial(
            self.model.compute_orm,
            hbpms=hbpms,
            hsteerers=hsteerers,
            vbpms=vbpms,
            vsteerers=vsteerers,
            **compute_orm_kwargs,
        )

    def compute(
        self,
        parameters: Collection[NumericalParameterGroup],
        configuration: Optional[Configuration] = None,
    ) -> tuple[Jacobian, ORM]:
        parts: list[Jacobian] = []
        with self.model.temporary_update(configuration):
            baseline = self.compute_orm()
            for group in parameters:
                columns: list[array] = []
                updates = group.build_configuration_from_values(np.full(group.count, group.delta))
                for update in updates:
                    orm = self.compute_orm(configuration=[update])
                    columns.append((orm - baseline).ravel() / group.delta)
                parts.append(np.stack(columns, axis=1))
        return np.concatenate(parts, axis=1), baseline


class AnalyticalJacobianMethod(JacobianMethod):
    """Computes an analytical version of the Jacobian from Twiss data.

    Args:
        model: The optics model from which Twiss data is computed.
        hbpms: Names of horizontal BPMs.
        hsteerers: Names of horizontal steerers.
        vbpms: Names of vertical BPMs.
        vsteerers: Names of vertical steerers.
    """

    def __init__(
        self,
        *,
        model: OpticsModel,
        hbpms: Collection[str],
        hsteerers: Collection[str],
        vbpms: Collection[str],
        vsteerers: Collection[str],
    ):
        self.model = model
        self.hbpms = hbpms
        self.hsteerers = hsteerers
        self.vbpms = vbpms
        self.vsteerers = vsteerers

    def compute(
        self,
        parameters: Collection[NumericalParameterGroup],
        configuration: Optional[Configuration] = None,
    ) -> tuple[Jacobian, ORM]:
        _supported = (Quadrupoles,)
        if not_supported := [p for p in parameters if not isinstance(p, _supported)]:
            raise RuntimeError(
                f'Computation of analytical Jacobian currently only supports the following '
                f'parameters: {_supported!r}. '
                f'Thus, the following specified parameters are not supported: {not_supported!r}'
            )
        if not parameters:
            raise RuntimeError('No parameters were specified for the Jacobian computation')
        parts: list[Jacobian] = []
        for group in parameters:
            if isinstance(group, Quadrupoles):
                part, orm = self.compute_analytical_jacobian_for_quadrupoles(
                    quadrupoles=group,
                    configuration=configuration,
                )
            else:
                assert False, f'parameter group {group!r} not supported'
            parts.append(part)
        # It's somehow awkward to just return the ORM as computed by any of the specific
        # methods above. However, that is currently the only place to get it from.
        # Perhaps, in the future, a new function should be added to compute ORM from Twiss
        # data and then the specific methods would only compute the Jacobian.
        return np.concatenate(parts, axis=1), orm

    def compute_analytical_jacobian_for_quadrupoles(
        self,
        quadrupoles: Quadrupoles,
        configuration: Optional[Configuration] = None,
    ) -> tuple[Jacobian, ORM]:
        """Similar to :meth:`AnalyticalJacobianMethod.compute_analytical_jacobian`
           but for quadrupoles specifically."""
        twiss = self.model.compute_twiss(configuration=configuration)
        return self._compute_analytical_jacobian_for_quadrupoles(
            twiss=twiss,
            quadrupoles=quadrupoles.names,
        )

    def _compute_analytical_jacobian_for_quadrupoles(
        self,
        *,
        twiss: TwissTable,
        quadrupoles: Collection[str],
    ) -> tuple[Jacobian, ORM]:
        hbpms = self.hbpms
        hsteerers = self.hsteerers
        vbpms = self.vbpms
        vsteerers = self.vsteerers

        n_quadrupoles = len(quadrupoles)
        n_hbpms = len(hbpms)
        n_hsteerers = len(hsteerers)
        n_vbpms = len(vbpms)
        n_vsteerers = len(vsteerers)
        bpms = dict(x=hbpms, y=vbpms)
        steerers = dict(x=hsteerers, y=vsteerers)

        beta_dict = dict(x=twiss['betx'], y=twiss['bety'])
        mu_dict = dict(x=twiss['mux'], y=twiss['muy'])

        orm = {}
        J = {}

        for dim in 'xy':
            relevant_names = frozenset({*quadrupoles, *bpms[dim], *steerers[dim]})
            beta = {}
            mu = {}
            for n, b, m in zip(twiss['name'], beta_dict[dim], mu_dict[dim]):
                if n in relevant_names:
                    beta[n] = b
                    mu[n] = m * (2*pi)
            Q = mu_dict[dim][-1]

            M = len(bpms[dim])
            N = len(steerers[dim])
            # NaNs will be replaced below; this helps to verify that the whole array gets filled.
            orm[dim] = np.full((M, N), np.nan)
            J[dim] = np.full((M*N, n_quadrupoles), np.nan)

            for i, bpm in enumerate(bpms[dim]):
                for j, steerer in enumerate(steerers[dim]):

                    mu_min = min(mu[bpm], mu[steerer])
                    mu_max = max(mu[bpm], mu[steerer])
                    orbit_response = (
                          sqrt(beta[steerer]*beta[bpm])
                        / (2*sin(pi*Q))
                        * cos(pi*Q - abs(mu_max - mu_min))
                    )

                    orm[dim][i, j] = orbit_response

                    for k, quad in enumerate(quadrupoles):

                        if mu_min < mu_max < mu[quad] or mu[quad] < mu_min < mu_max:
                            integral = (
                                  sin(mu_max - mu_min)
                                * cos(2*pi*Q - abs(mu[quad] - mu_max) - abs(mu[quad] - mu_min))
                            )
                        elif mu_min < mu[quad] < mu_max:
                            integral = (
                                  sin(abs(mu[quad] - mu_min))*cos(2*pi*Q - abs(mu[quad] - mu_min))
                                + sin(abs(mu[quad] - mu_max))*cos(2*pi*Q - abs(mu[quad] - mu_max))
                            )
                        else:
                            assert False

                        J[dim][i*N+j, k] = (
                            (-1 if dim == 'x' else 1) * beta[quad]/2 * orbit_response * (
                                1 / (2*tan(pi*Q)) + tan(pi*Q - abs(mu[bpm] - mu[steerer]))/2
                                + cos(2*pi*Q - 2*abs(mu[quad] - mu[bpm])) / (2*sin(2*pi*Q))
                                + cos(2*pi*Q - 2*abs(mu[quad] - mu[steerer])) / (2*sin(2*pi*Q))
                                - tan(pi*Q - abs(mu[bpm] - mu[steerer]))/sin(2*pi*Q) * integral
                            )
                        )
            assert np.isnan(orm[dim]).sum() == 0
            assert np.isnan(J[dim]).sum() == 0

        zeros = np.zeros
        x_shape = orm['x'].shape
        y_shape = orm['y'].shape

        orm_blocks = [
            [orm['x']                       , zeros((x_shape[0], y_shape[1]))],
            [zeros((y_shape[0], x_shape[1])), orm['y']                       ],
        ]
        full_orm = np.block(orm_blocks)

        J_blocks = [
            [J['x'].T                                   , zeros((n_quadrupoles, n_hbpms*n_vsteerers))],
            [zeros((n_quadrupoles, n_vbpms*n_hsteerers)), J['y'].T                                   ],
        ]
        J3d = np.block([
            [
                b.reshape(len(b), *orm_blocks[i][j].shape)
                for j, b in enumerate(row)
            ]
            for i, row in enumerate(J_blocks)
        ])
        J2d = J3d.reshape(len(quadrupoles), full_orm.size).T

        return J2d, full_orm
