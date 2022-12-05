# SPDX-FileCopyrightText: 2022 Dominik Vilsmeier
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""This module contains functionality and utilities for dealing with fitting parameters.
"""

from __future__ import annotations

import itertools as it
from typing import (
    Collection, Iterable, Protocol, Sequence, Union,
)
from typing_extensions import TypeAlias

import numpy as np

from .model import (
    Jacobian, Model, ORM, OrmShape,
    ArrayElementParameter, NumberParameter,
    ParameterUpdate,
    add,
    Configuration,
)
from .utils import is_iterator_exhausted


__all__ = [
    'ParameterGroup', 'AnalyticalParameterGroup', 'NumericalParameterGroup',
    'GainErrors', 'HBpmGainErrors', 'HSteererGainErrors', 'VBpmGainErrors', 'VSteererGainErrors',
    'Quadrupoles', 'Multipoles',
    'NumberParameters',
    'update_orm_with_gain_errors', 'update_jacobian_with_gain_errors',
]


array = np.ndarray

Array1DIndex: TypeAlias = Union[int, slice, list[int], array]


class OrmIndexBuilder(Protocol):
    def __call__(self, i: int) -> tuple[Array1DIndex, Array1DIndex]:
        """Given the index `i` of a BPM or steerer, build an index object which
           identifies the corresponding ORM elements.

        The returned object can be used to index into an ORM to return the
        corresponding ORM elements as a one-dimensional array.

        Args:
            i: The index of a BPM or steerer.

        Returns:
            The tuple ``(ir, ic)`` where ``ir`` is the index object referring to row
            indices of the ORM and ``ic`` is the index object referring to column indices.
            Together, the tuple ``(ir, ic)`` can be used to index into an ORM in order to
            obtain the corresponding ORM elements.
        """
        ...


class ParameterGroup:
    """This class represents a group of similar parameters.

    The number of parameter values represented by this group is available from
    the ``count`` attribute. This can be different from the number of group
    members (denoted by the argument `n`). The ``count`` depends on the specific
    implementation of a parameter group.

    Args:
        n: The number of group members. One member may represent more than
           one parameter value.
    """

    def __init__(self, n: int):
        self.n = n

    @property
    def count(self) -> int:
        """The number of parameter values represented by this group."""
        raise NotImplementedError


class AnalyticalParameterGroup(ParameterGroup):
    """Parameter group which uses analytical formulas for its Jacobian.

    These parameters are typically not contained in the model as numerical
    quantities. Rather, their effect is added during a post-computational step.
    """

    def build_jacobian(self, orm: ORM) -> Jacobian:
        """Build the part of the Jacobian that corresponds to this parameter group.

        Args:
            orm: The ORM corresponding to the returned Jacobian.

        Returns:
            The Jacobian. It does not contain the contribution from evaluating
            the parameters of this group. This contribution can be added via
            :meth:`AnalyticalParameterGroup.update_jacobian`.
        """
        raise NotImplementedError

    def update_orm(self, orm: ORM, x: array) -> ORM:
        """Update the given `orm` with the given parameter estimates `x`.

        .. note:: This modifies the given `orm` in-place.

        Args:
            orm: The ORM without the contribution from evaluating the parameters
                 of this group.
            x: The current estimate of parameter values for this group.

        Returns:
            The ORM with the contribution from evaluating the parameters of this group added.
        """
        raise NotImplementedError

    def update_jacobian(self, jacobian: Jacobian, x: array, *, column_offset: int) -> Jacobian:
        """Update the given `jacobian` with the given parameter estimates `x`.

        .. note:: This modifies the given `jacobian` in-place.

        Args:
            jacobian: The full Jacobian containing the parts of all parameter groups
                (including this one) but without the contribution from evaluating
                the parameters of this group.
            x: The current estimate of parameter values for this group.
            column_offset: The offset in number of columns where this parameter group is
                located within the Jacobian.

        Returns:
            The Jacobian with the contribution from evaluating the parameters of this group added.
        """
        raise NotImplementedError


class GainErrors(AnalyticalParameterGroup):
    """Parameter group representing BPM and steerer gain errors.

    Args:
        n: See :class:`ParameterGroup`.
        orm_index_builder: See :class:`OrmIndexBuilder`.
        orm_shape: The shape of the ORM.
    """

    def __init__(self, n: int, orm_index_builder: OrmIndexBuilder, orm_shape: OrmShape):
        super().__init__(n=n)
        self.orm_index_builder = orm_index_builder
        self.orm_shape = orm_shape

    @property
    def count(self) -> int:
        return self.n

    def build_jacobian(self, orm: ORM) -> Jacobian:
        J = np.zeros((orm.size, self.n), dtype=orm.dtype)
        orm_indices = np.arange(orm.size).reshape(orm.shape)
        for i in range(self.n):
            index = self.orm_index_builder(i)
            J[orm_indices[index],i] = orm[index]
        return J

    def update_orm(self, orm: ORM, x: array) -> ORM:
        for i, e in enumerate(x):
            orm[self.orm_index_builder(i)] *= (1 + e)
        return orm

    def update_jacobian(self, jacobian: Jacobian, x: array, *, column_offset: int) -> Jacobian:
        def rv(x):
            return x[np.newaxis, :]

        def cv(x):
            return x[:, np.newaxis]

        def _generate_other_columns(start, stop):
            all_column_indices = set(range(jacobian.shape[1]))
            for col in range(start, stop):
                yield np.array(sorted(all_column_indices - {col}))

        orm_indices = np.arange(len(jacobian)).reshape(self.orm_shape)
        column_indices = _generate_other_columns(column_offset, column_offset+len(x))

        for i, e in enumerate(x):
            row = cv(orm_indices[self.orm_index_builder(i)])
            col = rv(next(column_indices))
            jacobian[row, col] *= (1 + e)

        assert is_iterator_exhausted(column_indices)

        return jacobian


class HBpmGainErrors(GainErrors):
    """Parameter group representing gain errors of horizontal BPMs."""

    def __init__(self, n: int, orm_shape: tuple[int,int]):
        super().__init__(
            n=n,
            orm_index_builder=lambda i: (i, slice(None)),
            orm_shape=orm_shape,
        )


class HSteererGainErrors(GainErrors):
    """Parameter group representing gain errors of horizontal steerers."""

    def __init__(self, n: int, orm_shape: tuple[int,int]):
        super().__init__(
            n=n,
            orm_index_builder=lambda i: (slice(None), i),
            orm_shape=orm_shape,
        )


class VBpmGainErrors(GainErrors):
    """Parameter group representing gain errors of vertical BPMs."""

    def __init__(self, n: int, orm_shape: tuple[int,int]):
        n_hbpms = orm_shape[0] - n
        super().__init__(
            n=n,
            orm_index_builder=lambda i, offset=n_hbpms: (i+offset, slice(None)),
            orm_shape=orm_shape,
        )


class VSteererGainErrors(GainErrors):
    """Parameter group representing gain errors of vertical steerers."""

    def __init__(self, n: int, orm_shape: tuple[int,int]):
        n_hsteerers = orm_shape[1] - n
        super().__init__(
            n=n,
            orm_index_builder=lambda i, offset=n_hsteerers: (slice(None), i+offset),
            orm_shape=orm_shape,
        )


class NumericalParameterGroup(ParameterGroup):
    """Parameter group which uses numerical estimates for its Jacobian.

    Args:
        n: See :class:`ParameterGroup`.
        delta: The parameters' delta increment to be used for computing the Jacobian
            via finite difference approximation.
    """

    def __init__(self, n: int, delta: float):
        super().__init__(n=n)
        self.delta = delta

    def build_configuration_from_values(self, x: array) -> Configuration:
        """Build a parameter configuration from the given values.

        Args:
            x: The parameter values for the group.

        Returns:
            The configuration containing the parameter values.

        Raises:
            ValueError: If the number of given values does not match the number of
                parameters contained in that group.
        """
        raise NotImplementedError


class Quadrupoles(NumericalParameterGroup):
    """Parameter group representing thick quadrupoles.

    .. note::
       This parameter group expects ``DK1L`` values as estimates,
       i.e. deviations from the quadrupoles' nominal integrated strengths K1L.
       However, the underlying quadrupole elements are varied by their ``K1``
       attribute, so these need to be thick quadrupoles.

    Args:
        names: The names of the quadrupoles.
        lengths: The lengths of the individual quadrupoles.
        delta: See :class:`NumericalParameterGroup`.
    """

    def __init__(
        self,
        names: Sequence[str],
        *,
        lengths: Sequence[float],
        delta: float = 1e-7,
    ):
        if len(names) != len(lengths):
            raise ValueError(
                f'The number of names and lengths must be identical '
                f'(received {len(names)=} vs. {len(lengths)=})'
            )
        super().__init__(n=len(names), delta=delta)
        self.names = names
        self.lengths = lengths

    @classmethod
    def from_model(cls, model: Model, *, names: Collection[str], delta: float = 1e-7) -> Quadrupoles:
        """Create a new quadrupoles parameter group by fetching relevant information
           from the given `model`.

        Args:
            model: The model will be queried for information about the lengths of quadrupoles.
            names, delta: See :class:`Quadrupoles`.

        Returns:
            :class:`Quadrupoles` parameter group.
        """
        lengths = [model.get_parameter_value(NumberParameter(name, 'l')) for name in names]
        return cls(names=list(names), lengths=lengths, delta=delta)

    @property
    def count(self) -> int:
        return self.n

    def build_configuration_from_values(self, x: array) -> Configuration:
        if len(x) != self.count:
            raise ValueError(
                f'The number of given values does not match the number of parameters '
                f'({len(x)} \N{Not Equal To} {self.count})'
            )
        config: list[ParameterUpdate] = []
        for name, dk1l, length in zip(self.names, x, self.lengths):
            config.append(
                ParameterUpdate(
                    NumberParameter(name, 'k1'),
                    add(dk1l / length),
                )
            )
        return config


class Multipoles(NumericalParameterGroup):
    """Parameter group representing thin multipoles.

    This parameter group expects ``KNL[1]`` and ``KSL[1]`` values as estimates
    (in that order for each multipole).

    .. note::
       The number of parameters represented by this group, ``count``,
       is twice the number of given sextupoles (``KNL`` and ``KSL``).

    Args:
        names: The names of the multipoles.
        delta: See :class:`NumericalParameterGroup`.
    """

    def __init__(
        self,
        names: Collection[str],
        *,
        delta: float = 1e-7,
    ):
        super().__init__(n=len(names), delta=delta)
        self.names = names

    @property
    def count(self) -> int:
        return 2*self.n

    def build_configuration_from_values(self, x: array) -> Configuration:
        if len(x) != self.count:
            raise ValueError(
                f'The number of given values does not match the number of parameters '
                f'({len(x)} \N{Not Equal To} {self.count})'
            )
        config: list[ParameterUpdate] = []
        for name, (k1nl, k1sl) in zip(self.names, x.reshape(self.n, 2)):
            config.append(
                ParameterUpdate(
                    ArrayElementParameter(name, 'knl', index=1),
                    add(k1nl),
                )
            )
            config.append(
                ParameterUpdate(
                    ArrayElementParameter(name, 'ksl', index=1),
                    add(k1sl),
                )
            )
        return config


class NumberParameters(NumericalParameterGroup):
    """Parameter group representing general floating point numbers.

    Args:
        names: The names of the individual parameters.
        delta: See :class:`NumericalParameterGroup`.
    """

    def __init__(
        self,
        names: Sequence[str],
        *,
        delta: float,
    ):
        super().__init__(n=len(names), delta=delta)
        self.names = names

    @property
    def count(self) -> int:
        return self.n

    def build_configuration_from_values(self, x: array) -> Configuration:
        if len(x) != self.count:
            raise ValueError(
                f'The number of given values does not match the number of parameters '
                f'({len(x)} \N{Not Equal To} {self.count})'
            )
        config: list[ParameterUpdate] = []
        for name, value in zip(self.names, x):
            config.append(ParameterUpdate(NumberParameter(name), add(value)))
        return config


def update_orm_with_gain_errors(
    orm: ORM,
    gain_errors: Iterable[float],
    *,
    hbpms: Collection[str],
    hsteerers: Collection[str],
    vbpms: Collection[str],
    vsteerers: Collection[str],
) -> ORM:
    """Convenience function for updating the given `orm` with the given `gain_errors`.

    .. note:: This updates the given `orm` in-place.

    Args:
        orm: The ORM.
        gain_errors: Iterable object containig the gain errors. The contained errors
            are assumed to correspond to `hbpms`, `hsteerers`, `vbpms`, `vsteerers`
            in that order.
        hbpms: The names of horizontal BPMs.
        hsteerers: The names of horizontal steerers.
        vbpms: The names of vertical BPMs.
        vsteerers: The names of vertical steerers.

    Returns:
        The updated ORM. Note that this is the same object as the original `orm`
        which is updated in-place.
    """
    groups_and_errors = build_parameter_groups_from_gain_errors(
        gain_errors,
        hbpms=hbpms,
        hsteerers=hsteerers,
        vbpms=vbpms,
        vsteerers=vsteerers,
    )
    for group, errors in groups_and_errors:
        orm = group.update_orm(orm, errors)
    return orm


def update_jacobian_with_gain_errors(
    jacobian: Jacobian,
    gain_errors: Iterable[float],
    *,
    hbpms: Collection[str],
    hsteerers: Collection[str],
    vbpms: Collection[str],
    vsteerers: Collection[str],
    column_offset: int,
) -> ORM:
    """Convenience function for updating the given `jacobian` with the given `gain_errors`.

    .. note:: This updates the given `jacobian` in-place.

    Args:
        jacobian: The Jacobian.
        gain_errors: Iterable object containig the gain errors. The contained errors
            are assumed to correspond to `hbpms`, `hsteerers`, `vbpms`, `vsteerers`
            in that order.
        hbpms: The names of horizontal BPMs.
        hsteerers: The names of horizontal steerers.
        vbpms: The names of vertical BPMs.
        vsteerers: The names of vertical steerers.
        column_offset: The column offset from the left of the location where the gain errors
            are located inside the Jacobian. That is, the `column_offset` must be the number
            of columns that are to the left of the gain errors "block".

    Returns:
        The updated Jacobian. Note that this is the same object as the original `jacobian`
        which is updated in-place.
    """
    groups_and_errors = build_parameter_groups_from_gain_errors(
        gain_errors,
        hbpms=hbpms,
        hsteerers=hsteerers,
        vbpms=vbpms,
        vsteerers=vsteerers,
    )
    offsets = it.accumulate((g.count for g,_ in groups_and_errors), initial=column_offset)
    for (group, errors), offset in zip(groups_and_errors, offsets):
        jacobian = group.update_jacobian(jacobian, errors, column_offset=offset)
    assert next(offsets) == sum(g.count for g,_ in groups_and_errors) + column_offset
    assert is_iterator_exhausted(offsets)
    return jacobian


def build_parameter_groups_from_gain_errors(
    gain_errors: Iterable[float],
    *,
    hbpms: Collection[str],
    hsteerers: Collection[str],
    vbpms: Collection[str],
    vsteerers: Collection[str],
) -> tuple[
    tuple[HBpmGainErrors, array],
    tuple[HSteererGainErrors, array],
    tuple[VBpmGainErrors, array],
    tuple[VSteererGainErrors, array],
]:
    """Convenience function for building the corresponding :class:`GainErrors`
       from the given `gain_errors` values.

    Args:
        gain_errors: Iterable object containig the gain errors. The contained errors
            are assumed to correspond to `hbpms`, `hsteerers`, `vbpms`, `vsteerers`
            in that order.
        hbpms: The names of horizontal BPMs.
        hsteerers: The names of horizontal steerers.
        vbpms: The names of vertical BPMs.
        vsteerers: The names of vertical steerers.

    Returns:
        4-tuple corresponding to `hbpms`, `hsteerers`, `vbpms`, `vsteerers` in that order,
        where each tuple element is another 2-tuple; these 2-tuple are of the form
        ``(group, values)`` where ``group`` is the parameter group (an instance of any of
        the subclasses of :class:`GainErrors`) and ``values`` are the corresponding gain errors.

    Raises:
        RuntimeError: If there are too few or many `gain_errors` values compared to the number
            of horizontal/vertical BPMs/steerers.
    """
    orm_shape = (len(hbpms) + len(vbpms), len(hsteerers) + len(vsteerers))
    all_names = [hbpms, hsteerers, vbpms, vsteerers]
    all_types = [HBpmGainErrors, HSteererGainErrors, VBpmGainErrors, VSteererGainErrors]
    ig = iter(gain_errors)
    all_errors = [np.array([*it.islice(ig, len(n))]) for n in all_names]
    if not all(len(e) == len(n) for e, n in zip(all_errors, all_names)):
        _n_total = sum(map(len, all_names))
        _n_given = sum(map(len, all_errors))
        raise RuntimeError(
            f'Fewer gain errors (n={_n_given}) '
            f'than BPMs/steerers (n={_n_total}) '
            f'were given.'
        )
    if not is_iterator_exhausted(ig):
        _n_total = sum(map(len, all_names))
        _n_remaining = sum(1 for _ in ig) + 1  # add 1 which has been consumed by `is_iterator_exhausted`
        raise RuntimeError(
            f'More gain errors (n={_n_total+_n_remaining}) '
            f'than BPMs/steerers (n={_n_total}) '
            f'were given.'
        )
    all_groups = [
        tp(n=len(names), orm_shape=orm_shape)
        for tp, names in zip(all_types, all_names)
    ]
    return tuple(zip(all_groups, all_errors))  # type: ignore
