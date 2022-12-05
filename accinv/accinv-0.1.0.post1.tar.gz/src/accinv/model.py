# SPDX-FileCopyrightText: 2022 Dominik Vilsmeier
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Module containing accelerator models and corresponding utilities.

Orbit Response Matrix (ORM)
---------------------------

The layout of the ORM is based on the following convention:

* BPMs appear along the rows (``axis=0``). First all horizontal BPMs,
  followed by all vertical BPMs.
* Steerers appear along the columns (``axis=1``). First all horizontal steerers,
  followed by all vertical steerers.

.. code-block::

   +---HSTEERERS---+---VSTEERERS---+
   |               |               |
   H               |               |
   B               |               |
   P               |               |
   M               |               |
   S               |               |
   |               |               |
   +---------------+---------------+
   |               |               |
   V               |               |
   B               |               |
   P               |               |
   M               |               |
   S               |               |
   |               |               |
   +---------------+---------------+

"""

from __future__ import annotations

from collections.abc import Collection, Container
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from subprocess import DEVNULL
import sys
from typing import (
    Generic, Iterator, Optional, Protocol, TextIO, TypeVar, TypedDict,
    Union,
)
from typing_extensions import TypeAlias

from cpymad.madx import Madx as cpymad_Madx  # type: ignore
from cpymad.madx import Table as cpymad_Table  # type: ignore
import numpy as np
from numpy.typing import NDArray


__all__ = [
    'Model', 'OpticsModel', 'Madx',
    'NumberParameter', 'ArrayElementParameter',
    'ParameterUpdate',
    'replace_with', 'add',
    'TwissTable',
    'UnknownElementError',
]


array = np.ndarray

Data: TypeAlias = Union[float, array]
D = TypeVar('D', float, array)
ParameterValues: TypeAlias = dict[str, float]

Filepath: TypeAlias = Union[Path, str]
ORM: TypeAlias = NDArray[np.float64]
OrmShape: TypeAlias = tuple[int, int]
Jacobian: TypeAlias = NDArray[np.float64]
JacobianShape: TypeAlias = tuple[int, int]


class TwissTable(TypedDict):
    """This class represents selected columns from Twiss data computation."""
    name: array
    betx: array
    bety: array
    alfx: array
    alfy: array
    mux: array
    muy: array
    x: array
    y: array


@dataclass(frozen=True)
class ParameterIdentifier:
    """Identifier for model parameters.

    Args:
        name: The name of either a global parameter or a lattice element (see `attribute`).
        attribute: (optional) The attribute of the lattice element specified via `name`.
                   If not given, `name` is assumed to represent a global parameter.
    """
    name: str
    attribute: str = ''


class ParameterType(Generic[D]):
    def get_value(self, data: D) -> float:
        """Extract the relevant value from the given `data` structure.

        Args:
            data: The data structure which holds the parameter's value.

        Returns:
            The extracted value.
        """
        raise NotImplementedError

    def set_value(self, data: D, value: float) -> D:
        """Update the given `data` structure with the given `value`.

        .. note::
           If `data` is mutable then the update is applied in-place and thus
           it modifies the `data` instance. Otherwise, a new instance is created.

        Args:
            data: The data structure to be updated.
            value: The value used for the update.

        Returns:
            The updated data structure. If the given `data` is mutable,
            then ``new_data is data``, as the update has modified the
            original `data` instance.
        """
        raise NotImplementedError


class NumberParameterType(ParameterType[float]):
    """Parameter type representing a single floating point number."""

    def get_value(self, data: float) -> float:
        return data

    def set_value(self, data: float, value: float) -> float:
        return value


class ArrayElementParameterType(ParameterType[array]):
    """Parameter type representing an array element located at a specific index.

    Args:
        index: The index of the array element.
    """

    def __init__(self, index: int):
        self.index = index

    def get_value(self, data: array) -> float:
        return data[self.index]

    def set_value(self, data: array, value: float) -> array:
        data[self.index] = value
        return data


class Parameter(Generic[D]):
    """Model parameter represented by its identifier and type."""

    id: ParameterIdentifier
    type: ParameterType[D]

    def __init__(self, id: ParameterIdentifier, type: ParameterType[D]):
        self.id = id
        self.type = type


class NumberParameter(Parameter[float]):
    """Model parameter representing a single floating point number."""

    def __init__(self, name: str, attribute: str = ''):
        super().__init__(ParameterIdentifier(name, attribute), NumberParameterType())


class ArrayElementParameter(Parameter[array]):
    """Model parameter representing an array element located at a specific index."""

    def __init__(self, name: str, attribute: str = '', *, index: int):
        super().__init__(ParameterIdentifier(name, attribute), ArrayElementParameterType(index))


class UpdateStrategy(Protocol):
    def __call__(self, old: float) -> float:
        """Given the `old` value, return a new, updated value."""
        ...


def replace_with(new: float) -> UpdateStrategy:
    """Create an update strategy which replaces old values with the given `new` one."""
    def _constant(old: float) -> float:
        return new
    _constant.__doc__ = f'Ignore the argument and return {new!r}'
    return _constant


def add(new: float) -> UpdateStrategy:
    """Create an update strategy which adds the given `new` value to the old values."""
    def _add(old: float) -> float:
        return old + new
    _add.__doc__ = f'Compute the sum of `old` and {new!r}'
    return _add


class ParameterUpdate(Generic[D]):
    """This class represents the foreseen update of a model parameter's value.

    Args:
        parameter: The model parameter to be updated.
        update_strategy: The update strategy to be used.
    """

    parameter: Parameter[D]
    transform: UpdateStrategy

    def __init__(
        self,
        parameter: Parameter[D],
        update_strategy: UpdateStrategy,
    ):
        self.parameter = parameter
        self.transform = update_strategy

    def apply(self, old: D) -> D:
        """Apply the parameter update, producing an updated data structure.

        Args:
            old: The old data structure.

        Returns:
            The updated data structure (possibly the same object as `old`, if mutable).
        """
        old_value = self.parameter.type.get_value(old)
        new_value = self.transform(old_value)
        return self.parameter.type.set_value(old, new_value)


Configuration: TypeAlias = Collection[ParameterUpdate]


class Model:
    def get_element_names(
        self,
        *containers: Container[str],
    ) -> tuple[list[str], ...]:
        """For each given container, return a list of element names from the model
           that are part of that container.

        Args:
            containers: One or multiple objects that support ``in``; element names of the model
                will be checked against these containers.

        Returns:
            A tuple, one item for each given container, where each item contains the names
            of all elements for which the corresponding container indicated that it contains
            that name.
        """
        raise NotImplementedError

    def get_parameter(self, parameter: Parameter[D]) -> D:
        """Get the current data of the given `parameter`."""
        raise NotImplementedError

    def set_parameter(self, parameter: Parameter[D], new_data: D) -> None:
        """Set the data of the given `parameter` to the specified `new_data`."""
        raise NotImplementedError

    def compute_orbit(
        self,
        *,
        hbpms: Collection[str],
        vbpms: Collection[str],
        configuration: Optional[Configuration] = None,
    ) -> tuple[array, array]:
        """Compute the orbit at the given horizontal and vertical BPMs.

        Args:
            hbpms: The names of horizontal BPMs.
            vbpms: The names of vertical BPMs.
            configuration: (optional) Temporary parameter updates for the duration of the orbit
                computation (see :meth:`Model.temporary_update`).

        Returns:
            The tuple ``(x_orbit, y_orbit)``, where ``x_orbit`` is the x-orbit at horizontal BPMs
            and ``y_orbit`` is the y-orbit at vertical BPMs.

        Raises:
            UnknownElementError: If any of the specified BPM names is not found in the model.
        """
        raise NotImplementedError

    def get_parameter_value(self, parameter: Parameter) -> float:
        """Get the current value of the given `parameter`."""
        return parameter.type.get_value(self.get_parameter(parameter))

    def set_parameter_value(self, parameter: Parameter, new_value: float) -> None:
        """Set the current value of the given `parameter` to the specified `new_value`."""
        old_data = self.get_parameter(parameter)
        new_data = parameter.type.set_value(old_data, new_value)
        self.set_parameter(parameter, new_data)

    def update(
        self,
        configuration: Optional[Configuration] = None,
        *,
        quadrupoles: Optional[ParameterValues] = None,
        quadrupoles_delta_k1l: Optional[ParameterValues] = None,
        steerers: Optional[ParameterValues] = None,
    ) -> None:
        """Update the model's parameters.

        .. note::
           If both ``quadrupoles`` and ``quadrupoles_delta_k1l`` are given, the latter takes
           into account the already updated values from ``quadrupoles``.

        Args:
            configuration: Parameter updates. Overrides other specifications.
            quadrupoles: Keys must be names of quadrupoles and values their desired ``k1`` values.
            quadrupoles_delta_k1l: These values will be added to the quadrupoles' current K1L settings
                (i.e. their integrated strength). Keys must be the quadrupoles' names.
            steerers: Keys must be names of steerers and values their desired ``kick`` values.
        """
        config = self.build_configuration_from_parameter_values(
            quadrupoles=quadrupoles,
            quadrupoles_delta_k1l=quadrupoles_delta_k1l,
            steerers=steerers,
        )
        if configuration:
            config.extend(configuration)
        for update in config:
            old_data = self.get_parameter(update.parameter)
            new_data = update.apply(old_data)
            self.set_parameter(update.parameter, new_data)

    @contextmanager
    def temporary_update(
        self,
        configuration: Optional[Configuration] = None,
        *,
        quadrupoles: Optional[ParameterValues] = None,
        quadrupoles_delta_k1l: Optional[ParameterValues] = None,
        steerers: Optional[ParameterValues] = None,
    ) -> Iterator[None]:
        """Temporarily update the model's parameters.

        On entrance, the parameters will be set to the specified values.
        On exit, the parameters will be reset to their original values.

        Args:
            See :meth:`Model.update`.

        Returns:
            A context manager handling the parameter updates.
        """
        config = self.build_configuration_from_parameter_values(
            quadrupoles=quadrupoles,
            quadrupoles_delta_k1l=quadrupoles_delta_k1l,
            steerers=steerers,
        )
        if configuration:
            config.extend(configuration)

        restore_previous_state: list[ParameterUpdate] = []
        for update in config:
            current_value = self.get_parameter_value(update.parameter)
            restore_previous_state.append(
                ParameterUpdate(
                    update.parameter,
                    replace_with(current_value),
                )
            )

        self.update(config)
        yield
        self.update(restore_previous_state)

    def compute_orm(
        self,
        *,
        hbpms: Collection[str],
        hsteerers: Collection[str],
        vbpms: Collection[str],
        vsteerers: Collection[str],
        kicks: Collection[float],
        configuration: Optional[Configuration] = None,
    ) -> ORM:
        """Compute the ORM for the given `[hv]steerers` and `kicks`, observed at the given `[hv]bpms`.

        Args:
            hbpms: Collection of horizontal BPM names.
            hsteerers: Collection of horizontal steerer names.
            vbpms: Collection of vertical BPM names.
            vsteerers: Collection of vertical steerer names.
            kicks: Steerer kick values for which orbits are computed.
            configuration: See :meth:`Model.temporary_update`. The updates are non-persistent.

        Returns:
            The computed ORM. The left upper block corresponds to horizontal and
            the right lower block to vertical dimension.
        """
        if len(kicks) == 0:
            raise ValueError('At least one steerer kick value must be specified')
        elif len(kicks) == 1:
            _compute_orm = self._compute_orm_2_point
        else:
            _compute_orm = self._compute_orm_n_point
        with self.temporary_update(configuration):
            orm = _compute_orm(hbpms=hbpms, vbpms=vbpms, steerers=[*hsteerers, *vsteerers], kicks=kicks)
        return orm

    def _compute_orm_2_point(
        self,
        *,
        hbpms: Collection[str],
        vbpms: Collection[str],
        steerers: Collection[str],
        kicks: Collection[float],
    ) -> ORM:
        if len(kicks) != 1:
            raise ValueError('2-point ORM method must specify exactly one steerer kick value')
        kick, = kicks
        baseline = np.concatenate(self.compute_orbit(hbpms=hbpms, vbpms=vbpms))
        orbits = self._compute_orbit_matrix(hbpms=hbpms, vbpms=vbpms, steerers=steerers, kick=kick)
        orm = (orbits - baseline[:,np.newaxis]) / kick
        return orm

    def _compute_orm_n_point(
        self,
        *,
        hbpms: Collection[str],
        vbpms: Collection[str],
        steerers: Collection[str],
        kicks: Collection[float],
    ) -> ORM:
        if len(kicks) < 1:
            raise ValueError('n-point ORM method must specify at least one steerer kick value')
        baseline = np.concatenate(self.compute_orbit(hbpms=hbpms, vbpms=vbpms))
        orbits = [
            self._compute_orbit_matrix(hbpms=hbpms, vbpms=vbpms, steerers=steerers, kick=kick)
            for kick in kicks
        ]
        kicks_with_baseline = np.array([*kicks, 0])
        orbits.append(np.tile(baseline[:,np.newaxis], (1, len(steerers))))
        orbits_zero_offset = np.stack(orbits) - baseline[np.newaxis,:,np.newaxis]
        response, *__ = np.linalg.lstsq(
            kicks_with_baseline[:,np.newaxis],
            orbits_zero_offset.reshape(len(kicks_with_baseline), -1),
            rcond=None,
        )
        orm = response.reshape(orbits_zero_offset.shape[1:])
        return orm

    def _compute_orbit_matrix(
        self,
        *,
        hbpms: Collection[str],
        vbpms: Collection[str],
        steerers: Collection[str],
        kick: float,
    ) -> array:
        columns = []
        for steerer in steerers:
            update = ParameterUpdate(NumberParameter(steerer, 'kick'), add(kick))
            x_orbit, y_orbit = self.compute_orbit(
                hbpms=hbpms,
                vbpms=vbpms,
                configuration=[update],
            )
            columns.append(np.concatenate([x_orbit, y_orbit]))
        return np.stack(columns, axis=1)

    def build_configuration_from_parameter_values(
        self,
        *,
        quadrupoles: Optional[ParameterValues] = None,
        quadrupoles_delta_k1l: Optional[ParameterValues] = None,
        steerers: Optional[ParameterValues] = None,
    ) -> list[ParameterUpdate]:
        """Generate a new configuration from the given type-specific parameter values.

        Args:
            quadrupoles: Replaces the ``k1`` attribute of specified quadrupoles with
                the specified values.
            quadrupoles_delta_k1l: Increments the ``k1`` attribute of specified quadrupoles by
                the specified values (converting ``K1L`` to ``K1``).
            steerers: Replaces the ``kick`` attribute of specified steerers with
                the specified values.

        Returns:
            Configuration object containing the specified parameter updates.
        """
        config: list[ParameterUpdate] = []
        if quadrupoles:
            config.extend(
                ParameterUpdate(NumberParameter(name, 'k1'), replace_with(value))
                for name, value in quadrupoles.items()
            )
        if steerers:
            config.extend(
                ParameterUpdate(NumberParameter(name, 'kick'), replace_with(value))
                for name, value in steerers.items()
            )
        if quadrupoles_delta_k1l:
            for name, value in quadrupoles_delta_k1l.items():
                length = self.get_parameter_value(NumberParameter(name, 'l'))
                config.append(
                    ParameterUpdate(NumberParameter(name, 'k1'), add(value/length))
                )
            del name, value, length
        return config


class OpticsModel(Model):
    def compute_twiss(
        self,
        configuration: Optional[Configuration] = None,
    ) -> TwissTable:
        """Compute Twiss data.

        Args:
            configuration: See :meth:`Model.temporary_update`. The updates are non-persistent.

        Returns:
            Twiss data as a dictionary.
        """
        raise NotImplementedError

    def compute_tunes(
        self,
        configuration: Optional[Configuration] = None,
    ) -> tuple[float, float]:
        """Compute the tunes for the two decoupled modes.

        Args:
            configuration: See :meth:`Model.temporary_update`. The updates are non-persistent.

        Returns:
            The tuple ``(Q1, Q2)`` containing the tunes for, respectively, mode 1 and mode 2.
        """
        twiss = self.compute_twiss(configuration=configuration)
        return twiss['mux'][-1], twiss['muy'][-1]

    def compute_beta_beating(
        self,
        quadrupoles_delta_k1l: ParameterValues,
    ) -> tuple[array, array]:
        """Compute the beta beating for the given quadrupole errors with respect to the current setting.

        Args:
            quadrupoles_delta_k1l: See :meth:`Model.temporary_update`. The updates are non-persistent.

        Returns:
            The tuple ``(beta_beating_x, beta_beating_y)`` containing the simulated beta beating
            for, respectively, mode 1 and mode 2.
        """
        twiss0 = self.compute_twiss()
        with self.temporary_update(quadrupoles_delta_k1l=quadrupoles_delta_k1l):
            twiss1 = self.compute_twiss()
        beta_beating_x = twiss1['betx']/twiss0['betx'] - 1
        beta_beating_y = twiss1['bety']/twiss0['bety'] - 1
        return beta_beating_x, beta_beating_y


class Madx(OpticsModel):
    """This model uses cpymad as a backend."""

    def __init__(self, *, path: Filepath, stdout: Union[int, TextIO, bool] = False):
        if stdout is False:
            stdout = DEVNULL
        elif stdout is True:
            stdout = sys.stdout
        self.madx = cpymad_Madx(stdout=stdout)
        self.madx.call(file=f'{Path(path).resolve()!s}')

    def get_element_names(self, *containers: Container[str]) -> tuple[list[str], ...]:
        names: list[list[str]] = [[] for _ in containers]
        for name in self.madx.elements:
            for i, container in enumerate(containers):
                if name in container:
                    names[i].append(name)
        return tuple(names)

    def get_parameter(self, parameter: Parameter[D]) -> D:
        if parameter.id.attribute:
            element = getattr(self.madx.elements, parameter.id.name)
            return element[parameter.id.attribute]
        else:
            return self.madx.globals[parameter.id.name]

    def set_parameter(self, parameter: Parameter[D], new_data: D) -> None:
        if parameter.id.attribute:
            element = getattr(self.madx.elements, parameter.id.name)
            element[parameter.id.attribute] = new_data
        else:
            self.madx.globals[parameter.id.name] = new_data

    def compute_twiss(
        self,
        configuration: Optional[Configuration] = None,
    ) -> TwissTable:
        with self.temporary_update(configuration):
            twiss = self._compute_twiss()
        return TwissTable(
            name=np.array(
                [
                    self._get_element_name_from_twiss_table_entry(n)
                    for n in twiss['name']
                ],
                dtype='U32',  # Maximum identifier length from MADX is 16.
            ),
            betx=twiss['betx'],
            bety=twiss['bety'],
            alfx=twiss['alfx'],
            alfy=twiss['alfy'],
            mux=twiss['mux'],
            muy=twiss['muy'],
            x=twiss['x'],
            y=twiss['y'],
        )

    def _compute_twiss(self, *, centre=True, **kwargs) -> cpymad_Table:
        """Compute Twiss data using model-specific internal data strucures."""
        return self.madx.twiss(centre=centre, **kwargs).copy()

    def compute_orbit(
        self,
        *,
        hbpms: Collection[str],
        vbpms: Collection[str],
        configuration: Optional[Configuration] = None,
    ) -> tuple[array, array]:
        twiss = self.compute_twiss(configuration=configuration)
        orbit = {}
        for name, x, y in zip(twiss['name'], twiss['x'], twiss['y']):
            name = self._get_element_name_from_twiss_table_entry(name)
            orbit[name] = dict(x=x, y=y)
        del name, x, y
        bpms_dict = dict(x=hbpms, y=vbpms)
        orbit_at_bpms: dict[str,list[float]] = {d: [] for d in bpms_dict}
        for dim, values in orbit_at_bpms.items():
            for bpm in bpms_dict[dim]:
                try:
                    xy = orbit[bpm]
                except KeyError:
                    raise UnknownElementError(f'BPM {bpm!r} not found in Twiss table', name=bpm)
                else:
                    values.append(xy[dim])
        return np.array(orbit_at_bpms['x']), np.array(orbit_at_bpms['y'])

    @staticmethod
    def _get_element_name_from_twiss_table_entry(entry: str) -> str:
        return entry.split(':')[0]


class UnknownElementError(Exception):
    name: str

    def __init__(self, msg: str, *, name: str):
        super().__init__(msg)
        self.name = name
