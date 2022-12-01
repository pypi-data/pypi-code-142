#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# BSD 3-Clause License
#
# Copyright 2022, by the California Institute of Technology.
# ALL RIGHTS RESERVED. United States Government Sponsorship acknowledged.
# Any commercial use must be negotiated with the Office of Technology Transfer
# at the California Institute of Technology.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# This software may be subject to U.S. export control laws. By accepting this
# software, the user agrees to comply with all applicable U.S. export laws and
# regulations. User has the responsibility to obtain export licenses, or other
# export authority as may be required before exporting such information to
# foreign countries or providing access to foreign persons.
#
"""
LISA Glitch module

LISA Glitch generates glitch files to be injected in the instrument simulation with LISANode.

Authors:
    Jean-Baptiste Bayle <j2b.bayle@gmail.com>
    Eleonora Castelli <eleonora.castelli@unitn.it>
    Natalia Korsakova <natalia.korsakova@obspm.fr>
"""

import abc
import logging
import random
import importlib_resources
import importlib_metadata
import matplotlib.pyplot
import scipy.interpolate
import scipy.special
import numpy
import h5py


logger = logging.getLogger(__name__)


INJECTION_POINTS = [
    # Test-mass motion
    'tm_12', 'tm_23', 'tm_31', 'tm_13', 'tm_32', 'tm_21',
    # Laser frequency jumps
    'laser_12', 'laser_23', 'laser_31', 'laser_13', 'laser_32', 'laser_21',
]


class Glitch(abc.ABC):
    """Abstract base class to represent a single glitch signal.

    A glitch is a time-domain signal which is injected into the instrumental simulation at a
    given injection point, at a given time and for a given duration. This abstract class provides
    a common structure for all glitch classes.

    Sampling parameters (``dt``, ``size``, and ``t0``) are used to generate when creating a glitch file.
    Note that they are ignored when writing to an existing glitch file.

    .. admonition:: Units and time coordinates

        The physical unit and time coordinate associated with a glitch are defined by the associated
        injection point. Please refer to :doc:`injpoints` for more information.

    Args:
        inj_point (str): injection point, c.f. :const:`lisaglitch.INJECTION_POINTS`
        t_inj (float): injection time [s]
        dt (float): simulation sampling period [s]
        size (int): simulation size [samples]
        t0 (float): simulation initial time [s]
    """

    def __init__(self, inj_point, t_inj=0, dt=1/16, size=2592000, t0=0):

        self.git_url = 'https://gitlab.in2p3.fr/lisa-simulation/glitch'
        self.generator = self.__class__.__name__
        self.version = importlib_metadata.version('lisaglitch')
        logger.info("Initializing glitch (lisaglitch version %s)", self.version)

        if inj_point not in INJECTION_POINTS:
            raise ValueError(f"Invalid injection point '{inj_point}'")
        self.inj_point = inj_point #: Injection point.
        self.t_inj = float(t_inj) #: Injection time [s].

        self.dt = float(dt) #: Sampling period [s].
        self.t0 = float(t0) #: Initial time [s].
        self.size = int(size) #: Simulation size [samples].
        self.fs = 1 / self.dt #: Sampling frequency [Hz].
        self.duration = self.size * self.dt #: Simulation duration [s].
        self.t = self.t0 + numpy.arange(self.size) * self.dt #: Time array [s].

        if self.t_inj < self.t0 or self.t_inj > self.t[-1]:
            logger.warning("Injection time '%.2f' out of simulation time range '%.2f-%.2f'",
                self.t_inj, self.t0, self.t[-1])
            if self.t_inj < self.t0:
                logger.warning("Glitch injected before the simulation starts")
            elif self.t_inj > self.t[-1]:
                logger.warning("Glitch injected after the simulation ends")

    @abc.abstractmethod
    def compute_signal(self, t=None):
        """Compute the glitch time-domain signal.

        The time is expressed in the local coordinates of the injection. E.g., glitches injected in the
        test-mass onboard spacecraft 1 are expressed in the spacecraft proper time (TPS) of spacecraft 1.

        If ``t`` is None, we use the default sampling parameters of the glitch object.

        Args:
            t (array-like or None): time [s], or None for default sampling [s]

        Return:
            array-like: Time-domain glitch signal, of shape ``(len(t))``.
        """
        raise NotImplementedError

    @property
    def intrinsic_duration(self):
        """Return the intrinsic duration of the glitch.

        Most glitch models can define a time interval during which signal is significantly changing; even if
        the signal does not relaxes to its previous state (e.g., a glitch step does not fall back to zero), it
        asymptotically converges to some final value after a while. We call this its intrinsic duration.

        Concrete subclasses can override this method to define their own intrinsic duration.

        Return:
            float: Intrinsic glitch duration [s].
        """
        return 10

    def plot(self, output=None, tmin=None, tmax=None, title='Glitch signal'):
        """Plot glitch signal.

        If ``tmin`` or ``tmax`` are not given, we use the glitch injection time and intrinsic duration.

        Args:
            output (str or None): output file, None to show the plots
            tmin (float): min value for time axis [s]
            tmax (float): max value for time axis [s]
            title (str): plot title
        """
        # Compute glitch signal
        logger.info("Computing glitch signal")
        tmin = tmin if tmin is not None else self.t_inj - 1
        tmax = tmax if tmax is not None else self.t_inj + self.intrinsic_duration + 1
        size = (tmax - tmin) // self.dt
        t = tmin + numpy.arange(size, dtype=numpy.float64) * self.dt
        signal = self.compute_signal(t)
        # Plot glitch
        logger.info("Plotting glitch signal")
        matplotlib.pyplot.figure(figsize=(12, 4))
        matplotlib.pyplot.plot(t, signal)
        matplotlib.pyplot.grid()
        matplotlib.pyplot.xlabel("Time [s]")
        matplotlib.pyplot.ylabel("Signal")
        matplotlib.pyplot.title(title)
        # Save or show glitch
        if output is not None:
            logger.info("Saving plot to %s", output)
            matplotlib.pyplot.savefig(output, bbox_inches='tight')
        else:
            matplotlib.pyplot.show()

    def _write_metadata(self, hdf5, prefix=''):
        """Set all properties as HDF5 attributes on ``object``.

        Try to store all variables as attributes. If it is too large or its type is not
        supported, try to store a string representation; if this fails, log a warning.

        Args:
            hdf5 (h5py.File): an HDF5 file, or a dataset
            prefix (str): prefix for attribute names
        """
        for key, value in self.__dict__.items():
            pkey = f'{prefix}{key}'
            try:
                hdf5.attrs[pkey] = value
            except (TypeError, RuntimeError):
                try:
                    hdf5.attrs[pkey] = str(value)
                except RuntimeError:
                    logger.warning("Cannot write metadata '%s' on '%s'", pkey, hdf5)

    def write(self, path='glitch.h5', mode='a'):
        """Write the glitch to a glitch file.

        If the file does not exist, it is created with the glitch's sampling parameters and the
        glitch signal is computed according to these parameters and written to file. If the
        file already exists, the glitch signal is computed according to the file's sampling
        parameters and added to the file.

        When creating the glitch file, metadata are saved as attributes.

        When writing a glitch, we add attributes for each local variable on the associated
        injection point dataset, prefixed with ``inj<i>``, where i is the index of glitch
        in the injection point dataset.

        Args:
            path (str): path to the glitch file
            mode (str): opening mode
        """
        # Open orbit file
        logger.info("Opening or creating glitch file '%s'", path)
        with h5py.File(path, mode) as hdf5:
            # Create time dataset if needed, and write some attributes
            if 't' not in hdf5:
                logger.info("New glitch file, creating time dataset")
                hdf5['t'] = self.t
                logger.info("Setting global metadata")
                self._write_metadata(hdf5)
            t = hdf5['t'][:]
            # Create injection dataset if needed
            dname = self.inj_point
            if dname not in hdf5:
                logger.info("Creating injection dataset '%s'", dname)
                hdf5.create_dataset(dname, data=numpy.zeros_like(t))
                hdf5[dname].attrs['injection_count'] = 0
            # Add glitch to injection dataset
            logger.info("Adding glitch to injection dataset '%s'", dname)
            ninj = int(hdf5[dname].attrs['injection_count'])
            hdf5[dname][:] += self.compute_signal(t)
            # Setting metadata
            logger.info("Setting injection metadata")
            hdf5[dname].attrs['injection_count'] = ninj + 1
            self._write_metadata(hdf5[dname], prefix=f'inj{ninj}_')
        # Closing file
        logger.info("Closing glitch file %s", path)


class StepGlitch(Glitch):
    """Step glitch.

    A step glitch is vanishing before ``t_inj``, and is ``level`` after.

    Args:
        level (float): amplitude [injection point unit]
        **kwargs: all other args from :class:`lisaglitch.Glitch`
    """
    def __init__(self, level=1, **kwargs):
        super().__init__(**kwargs)
        self.level = float(level) #: Amplitude [injection point unit].

    @property
    def intrinsic_duration(self):
        return 1

    def compute_signal(self, t=None):
        if t is None:
            t = self.t
        return numpy.where(t >= self.t_inj, self.level, 0)


class RectangleGlitch(Glitch):
    """Rectangular glitch.

    A rectangular glitch is vanishing except between ``t_inj`` and ``t_inj + width``,
    where it is ``level``.

    Args:
        width (float): width of the rectangle (glitch duration) [s]
        level (float): amplitude [injection point unit]
        **kwargs: all other args from :class:`lisaglitch.Glitch`
    """
    def __init__(self, width, level=1, **kwargs):
        super().__init__(**kwargs)
        self.width = float(width) #: Glitch duration) [s].
        self.level = float(level) #: Amplitude [injection point unit].

    @property
    def intrinsic_duration(self):
        return self.width

    def compute_signal(self, t=None):
        if t is None:
            t = self.t
        inside = numpy.logical_and(t >= self.t_inj, t < self.t_inj + self.width)
        return numpy.where(inside, self.level, 0)


class OneSidedDoubleExpGlitch(Glitch):
    r"""One-sided double-exponential glitch, used to model LISA Pathfinder glitches [m/s2].

    A one-sided double-exponential glitch begins at  begins at :math:`t_\text{inj}`, ramps up to
    an amplitude :math:`A / (t_\text{rise} - t_\text{fall})` via the :math:`t_\text{rise}` timescale,
    and flattens off via the :math:`t_\text{fall}` timescale to 0.

    Defining :math:`\delta t = t - t_\text{inj}`, the signal is given by

    .. math::

        \frac{A (e^{-\delta t / t_\text{rise}} - e^{-\delta t / t_\text{fall}})}{t_\text{rise}
        - t_\text{fall}} \qs

    and converges to 0 when :math:`t` goes to infinity.

    When :math:`t_\text{fise} = t_\text{fall}`, the previous equation becomes singular.
    We use the following continuous extension,

    .. math::

        \frac{A \delta t  e^{-\delta t / t_\text{fall}}}{t_\text{fall}^2} \qs

    Args:
        t_rise: rise timescale [s]
        t_fall: fall timescale [s]
        level: amplitude [injection point unit]
    """

    def __init__(self, t_rise, t_fall, level=1, **kwargs):
        super().__init__(**kwargs)
        self.t_rise = float(t_rise) #: Rise timescale [s].
        self.t_fall = float(t_fall) #: Fall timescale [s].
        self.level = float(level) #: Amplitude [injection point unit].

    @property
    def intrinsic_duration(self):
        return 5 * (self.t_rise + self.t_fall)

    def compute_signal(self, t=None):
        if t is None:
            t = self.t
        delta_t = t - self.t_inj
        if self.t_fall != self.t_rise:
            dbexp = numpy.exp(-delta_t / self.t_rise) - numpy.exp(-delta_t / self.t_fall)
            y_inside = self.level * dbexp / (self.t_rise - self.t_fall)
        else:
            y_inside = self.level * delta_t * numpy.exp(-delta_t / self.t_fall) / self.t_fall**2
        return numpy.where(delta_t >= 0, y_inside, 0)


class IntegratedOneSidedDoubleExpGlitch(Glitch):
    r"""Integrated one-sided double-exponential glitch, used to model LISA Pathfinder glitches [m/s].

    The integrated signal implemented here is given by

    .. math::

        A \qty[1 - \frac{t_\text{rise} e^{-\delta t / t_\text{rise}} - t_\text{fall}
        e^{-\delta t / t_\text{fall}}}{t_\text{rise} - t_\text{fall}}] \qc

    and converges to :math:`A` when :math:`t` goes to infinity.

    When :math:`t_\text{rise} = t_\text{fall} \neq 0`, the previous expression becomes
    singular. We use use the following continuous extension,

    .. math::

        A \qty[1 - \qty(1 + \frac{\delta t}{t_\text{fall}}) e^{-\delta t / t_\text{fall}}] \qs

    Args:
        t_rise (float): rise timescale [s]
        t_fall (float): fall timescale [s]
        level (float): amplitude [injection point unit]
    """

    def __init__(self, t_rise, t_fall, level=1, **kwargs):
        super().__init__(**kwargs)
        self.t_rise = float(t_rise) #: Rise timescale [s].
        self.t_fall = float(t_fall) #: Fall timescale [s].
        self.level = float(level) #: Amplitude [injection point unit].

    @property
    def intrinsic_duration(self):
        return 5 * (self.t_rise + self.t_fall)

    def compute_signal(self, t=None):
        if t is None:
            t = self.t
        delta_t = t - self.t_inj
        if self.t_fall != self.t_rise:
            dbexp = self.t_rise * numpy.exp(-delta_t / self.t_rise) - self.t_fall * numpy.exp(-delta_t / self.t_fall)
            y_inside = self.level * (1 - dbexp / (self.t_rise - self.t_fall))
        else:
            y_inside = self.level * (1 - (1 + delta_t / self.t_fall) * numpy.exp(-delta_t / self.t_fall))
        return numpy.where(delta_t >= 0, y_inside, 0)


class TwoSidedDoubleExpGlitch(Glitch):
    r"""Integrated two-sided double-exponential glitch, used to model LISA Pathfinder glitches [m/s2].

    A two-sided double-exponential glitch begins at :math:`t_\text{inj}`, ramps up to level :math:`A` via
    the :math:`t_\text{rise}` timescale, oscillates around zero and then and flattens off via the
    :math: `t_\text{fall}` timescale to 0.

    Defining :math:`\delta t = t - t_\text{inj}`, the signal is given by

    .. math::

        \frac{1}{t_\text{fall} - t_\text{rise}}
        \qty[\frac{D + t_\text{fall} A}{t_\text{rise}} e^{-\delta t / t_\text{rise}}
            - \frac{D + t_\text{rise} A}{t_\text{fall}} e^{-\delta t / t_\text{fall}}] \qc

    and falls back to 0 when :math:`t` goes to infinity.

    When :math:`t_\text{fise} = t_\text{fall}`, the previous equation becomes singular.
    We use the following continuous extension,

    .. math::

        A \qty[1 - \qty(1 - \frac{\delta t}{t_\text{fall}} - \delta t \frac{D}{A t_\text{fall}^2})
        e^{-\delta t / t_\text{fall}}] \qs

    Args:
        t_rise (float): rise timescale [s]
        t_fall (float): fall timescale [s]
        level (float): amplitude [injection point unit]
        displacement (float): induced displacement [m]
    """

    def __init__(self, t_rise, t_fall, level=1, displacement=1, **kwargs):
        super().__init__(**kwargs)
        self.t_rise = float(t_rise) #: Rise timescale [s].
        self.t_fall = float(t_fall) #: Fall timescale [s].
        self.level = float(level) #: Amplitude [injection point unit].
        self.displacement = float(displacement) #: Induced displacement [m].

    @property
    def intrinsic_duration(self):
        return 5 * (self.t_rise + self.t_fall)

    def compute_signal(self, t=None):
        if t is None:
            t = self.t
        delta_t = t - self.t_inj
        if self.t_fall != self.t_rise:
            dbexp = (self.displacement + self.level * self.t_fall) / self.t_rise * numpy.exp(-delta_t / self.t_rise) \
                - (self.displacement + self.level * self.t_rise) / self.t_fall * numpy.exp(-delta_t / self.t_fall)
            y_inside = dbexp / (self.t_rise - self.t_fall)
        else:
            dbexp = -delta_t * (self.displacement + self.level * self.t_fall) \
            + self.t_fall * (self.displacement + 2 * self.level * self.t_fall)
            y_inside = dbexp * numpy.exp(-delta_t / self.t_fall) / self.t_fall**3
        return numpy.where(delta_t >= 0, y_inside, 0)


class IntegratedTwoSidedDoubleExpGlitch(Glitch):
    r"""Integrated two-sided double-exponential glitch, used to model LISA Pathfinder glitches [m/s].

    The integrated signal implemented here is given by

    .. math::

        A + \frac{\qty[e^{-\delta t / t_\text{rise}} (D + A t_\text{fall})
        - e^{-\delta t / t_\text{fall}} (D + A t_\text{rise})]}{t_\text{fall} - t_\text{rise}} \qc

    and falls back to 0 when :math:`t` goes to infinity.

    When :math:`t_\text{fise} = t_\text{fall}`, the previous equation becomes singular.
    We use the following continuous extension,

    .. math::

        A \qty[1 - \qty(1 - \frac{\delta t}{t_\text{fall}} - \frac{D \delta t}{A t_\text{fall}^2})
        e^{-\delta t / t_\text{fall}}] \qs

    Args:
        t_rise (float): rise timescale [s]
        t_fall (float): fall timescale [s]
        level (float): amplitude [injection point unit]
        displacement (float): induced displacement [m]
    """

    def __init__(self, t_rise, t_fall, level=1, displacement=1, **kwargs):
        super().__init__(**kwargs)
        self.t_rise = float(t_rise) #: Rise timescale [s].
        self.t_fall = float(t_fall) #: Fall timescale [s].
        self.level = float(level) #: Amplitude [injection point unit].
        self.displacement = float(displacement) #: Induced displacement [m].

    @property
    def intrinsic_duration(self):
        return 5 * (self.t_rise + self.t_fall)

    def compute_signal(self, t=None):
        if t is None:
            t = self.t
        delta_t = t - self.t_inj
        if self.t_fall != self.t_rise:
            dbexp = (self.displacement + self.level * self.t_fall) * numpy.exp(-delta_t / self.t_rise) \
                - (self.displacement + self.level * self.t_rise) * numpy.exp(-delta_t / self.t_fall)
            y_inside = self.level + dbexp / (self.t_rise - self.t_fall)
        else:
            y_inside = self.level * (1 - (1 - delta_t / self.t_fall - delta_t * self.displacement \
                / (self.level * self.t_fall**2)) * numpy.exp(-delta_t / self.t_fall))
        return numpy.where(delta_t >= 0, y_inside, 0)


class ShapeletGlitch(Glitch):
    r"""Exponential shapelet glitch.

    The glitch signal is given by the normalized 1D hydrogen atom wavefunctions.
    For the default case ``n = 1``, the signal is given by

    .. math::

        2 L \delta t \beta^{-1.5} e^{-\delta t / \beta} \qc

    where :math:`\delta t = t - t_\text{inj}`.

    For other values of ``n``,

    .. math::

        2 L (-1)^{n-1} \delta t \beta^{-1.5} n^{-2.5} L^1_{n-1} \frac{\delta t}{n \beta} e^{-\delta t / (n \beta)} \qc

    where :math:`L^1_{n-1}(t)` is the generalized Laguerre polynomial.

    This model was used to fit the LISA Pathfinder glitches and produce estimate of the the glitch
    distribution, as well as the production of LDC data.

    Args:
        level (float): amplitude [injection point unit]
        beta (float): damping time [s]
        quantum_n (int): number of shapelet components (quantum energy level)
    """

    def __init__(self, level=1, beta=1, quantum_n=1, **kwargs):
        super().__init__(**kwargs)

        self.level = float(level) #: Amplitude [injection point unit].
        self.beta = float(beta) #: Damping time [s].
        self.quantum_n = int(quantum_n) #: Number of shapelet components (quantum energy level).

    def compute_signal(self, t=None):
        if t is None:
            t = self.t

        delta_t = t - self.t_inj
        t_inside = delta_t >= 0
        normalized_t = 2 * delta_t[t_inside] / (self.quantum_n * self.beta)

        # Scipy special functions are written in C, and are not
        # correctly recognized by Pylint, so disabling linting here
        # pylint: disable=no-member
        laguerre = scipy.special.eval_genlaguerre(self.quantum_n - 1, 1, normalized_t)

        y_inside = numpy.zeros_like(t)
        y_inside[t_inside] = \
            2 * self.level * (-1)**(self.quantum_n - 1) \
            * delta_t[t_inside] * self.beta**(-1.5) * self.quantum_n**(-2.5) \
            * laguerre * numpy.exp(-normalized_t / 2)

        return y_inside


class IntegratedShapeletGlitch(Glitch):
    r"""Single-component (``n = 1``) integrated exponential shapelet glitch.

    The glitch signal is given by the normalized 1D hydrogen atom wavefunctions,
    which we integrate over time with ``n = 1``,

    .. math::

        \frac{2 L}{\sqrt{\beta}} \qty[1 - \qty(1 + \frac{\delta t}{\beta}) e^{- \delta t / \beta}] \qs

    This model was used to fit the LISA Pathfinder glitches and produce estimate of the the glitch
    distribution, as well as the production of LDC data.

    Args:
        level (float): amplitude [injection point unit]
        beta (float): damping time [s]
    """

    def __init__(self, level=1, beta=1, **kwargs):
        super().__init__(**kwargs)

        self.level = float(level) #: Amplitude [injection point unit].
        self.beta = float(beta) #: Damping time [s].

    def compute_signal(self, t=None):
        if t is None:
            t = self.t

        delta_t = t - self.t_inj
        t_inside = delta_t >= 0
        normalized_t = delta_t[t_inside] / self.beta

        result = numpy.zeros_like(t)
        result[t_inside] = \
            2 * self.level / numpy.sqrt(self.beta) \
            * (1 - (1 + normalized_t) * numpy.exp(-normalized_t))

        return result


class TimeSeriesGlitch(Glitch):
    """Glitch with signal from a Numpy array.

    To honor the glitch's sampling parameters, the input data may be resampled using
    spline interpolation. If you do not wish to interpolate, make sure to instantiate
    the glitch with sampling parameters matching your data.

    Args:
        t (array-like): times associated with ``tseries`` [s]
        tseries (array-like): glitch signal [injection point unit]
        interp_order (int): spline-interpolation order [one of 1, 2, 3, 4, 5]
        ext (str):
            extrapolation mode for elements out of range, see
            `scipy.interpolate.InterpolatedUnivariateSpline
            <https://docs.scipy.org/doc/scipy/reference/reference/generated/
            scipy.interpolate.InterpolatedUnivariateSpline.html>`_
        **kwargs: all other args from :class:`lisaglitch.Glitch`
    """

    def __init__(self, t, tseries, interp_order=1, ext='const', **kwargs):
        super().__init__(**kwargs)
        self.interp_order = int(interp_order)
        self.tseries_duration = t[-1] - t[0]
        self.ext = str(ext) #: Extrapolation mode for elements out of range.

        # Compute spline interpolation
        logger.info("Computing spline interpolation from time series")
        self.interpolant = scipy.interpolate.InterpolatedUnivariateSpline(
            t + self.t_inj, tseries, k=self.interp_order, ext=self.ext, check_finite=True
        ) #: Glitch signal interpolating function.

    @property
    def intrinsic_duration(self):
        return self.tseries_duration

    def compute_signal(self, t=None):
        if t is None:
            t = self.t
        return self.interpolant(t)


class HDF5Glitch(TimeSeriesGlitch):
    """Glitch with signal read from a HDF5 file.

    A glitch time-series is extracted from a dataset and injected at time ``t_inj``.

    Give the full path to a given dataset as ``node`` argument, or use the path to a group to
    pick a random dataset inside this group. Use the root ``/`` to pick a random dataset
    in the entire HDF5 file.

    To honor the glitch's sampling parameters, the input data may be resampled using
    spline interpolation. If you do not wish to interpolate, make sure to instantiate
    the glitch with sampling parameters matching your data.

    Args:
        path (str): path to HDF5 file
        node (str): path to dataset, or group to pick a random dataset
        exclude (list of str): datasets to exclude when picking a random dataset
    """

    def __init__(self, path, node='/', exclude=None, **kwargs):
        self.path = str(path) #: Path to HDF5 file.
        logger.info("Opening HDF5 file '%s'", self.path)
        hdf5 = h5py.File(self.path, 'r')

        # Exclude time dataset by default
        if exclude is None:
            exclude = ['t']
        self.exclude = exclude

        # Pick dataset
        self.node = str(node)
        group = hdf5[self.node]
        if isinstance(group, h5py.Group):
            logger.debug("Picking a random dataset in group '%s'", self.node)
            dataset_names = []
            group.visititems(lambda _, node: self._append_dataset_name(node, dataset_names))
            self.dataset = random.choice(dataset_names)
            while self.dataset in self.exclude:
                self.dataset = random.choice(dataset_names)
        elif isinstance(group, h5py.Dataset):
            logger.debug("Using user-provided dataset '%s'", self.node)
            self.dataset = self.node #: Glitch dataset.

        # Read dataset and time vector
        logger.info("Reading dataset '%s'", self.dataset)
        dataset = hdf5[self.dataset]

        hdf5_dt = float(self._get_closest_attr('dt', dataset))
        try:
            hdf5_t0 = float(self._get_closest_attr('t0', dataset))
        except KeyError:
            hdf5_t0 = 0
        try:
            hdf5_size = int(self._get_closest_attr('size', dataset))
        except KeyError:
            hdf5_size = len(dataset)

        hdf5_t = hdf5_t0 + numpy.arange(hdf5_size, dtype=numpy.float64) * hdf5_dt
        super().__init__(hdf5_t, dataset[:], **kwargs)

        logger.info("Closing HDF5 file '%s'", self.path)
        hdf5.close()

    @staticmethod
    def _append_dataset_name(node, datasets):
        """Append node's name to ``datasets`` if node is a dataset.

        Use this method with :meth:`h5py.Group.visititems` to list datasets in a group.

        Args:
            node (str): HDF5 node, either a dataset or a group
            datasets (list of str): list on which to append the dataset's name
        """
        if isinstance(node, h5py.Dataset):
            datasets.append(node.name)

    @staticmethod
    def _get_closest_attr(attr, node):
        """Get value of attribute ``attr`` of the nearest ancestor of ``node``.

        We try to return the value of attribute ``attr`` on the node; if it does not exist, we go up
        the file hierarchy and try to read and return the attribute on the nearest ancestor.

        Args:
            node (str): a group or a dataset in an HDF5 file

        Raises:
            ``KeyError`` if no ancestor defines the attribute ``attr``.
        """
        if attr in node.attrs:
            return node.attrs[attr]
        if node.parent == node:
            raise KeyError(f"the attribute '{attr}' is not defined on '{node.file.filename}'")
        return HDF5Glitch._get_closest_attr(attr, node.parent)

    def plot(self, output=None, tmin=None, tmax=None, title=None):
        """Plot glitch signal.

        See `Glitch.plot()`.
        """
        if title is None:
            title = f"Glitch from dataset '{self.dataset}' in '{self.path}'"
        super().plot(output, tmin, tmax, title)


class LPFLibraryGlitch(HDF5Glitch):
    """Glitch from a LISA Pathfinder glitch library.

    The LISA Pathfinder glitch library has the following structure::

        timeseries / runXX / glitchYY

    You can specify a run and glitch number, or leave them as ``None`` to let the
    class pick a random run and/or glitch.

    A default LPF glitch library is included with the package. Use ``'default'`` as
    the path to use it.

    The LPF glitch library provides acceleration signals, used by default by this class.
    If you wish to inject velocity glitch, use `integrated=True` to use an analytic
    time integrated version of the signal.

    Args:
        path (str): path to LPF glitch library (``'default'`` for default library)
        run (int or None): run number, or None to sample a random run
        glitch (int or None): glitch number, or None to sample a random glitch
        integrated (bool): whether to integrate glitch signal (use a velocity glitch)
    """

    def __init__(self, path='default', run=None, glitch=None, integrated=False, **kwargs):

        # Default library
        if path == 'default':
            logger.debug("Using default LPF glitch library")
            path = importlib_resources.files('lisaglitch') / 'data' / 'lpf-glitch-library.h5'

        self.library = str(path) #: Path to LPF glitch library.
        logger.info("Opening LPF glitch library '%s'", self.library)
        hdf5 = h5py.File(self.library, 'r')

        # Pick run
        if run is None:
            self.run = None
            logger.debug("Picking a random run in library '%s'", self.library)
            random_group = random.choice(list(hdf5['timeseries'].keys()))
            self.run_group = f'timeseries/{random_group}'
        else:
            self.run = int(run)
            logger.debug("Using user-provided run '%s'", self.run)
            self.run_group = f'timeseries/run{self.run:02}'

        try:
            run_group_object = hdf5[self.run_group]
        except KeyError as error:
            raise KeyError(f"run group '{self.run_group}' not found in '{self.library}'") from error

        # Pick glitch
        if glitch is None:
            self.glitch = None
            logger.debug("Picking a random glitch in run '%s'", self.run)
            random_dataset = random.choice(list(run_group_object.keys()))
            self.glitch_dataset = f'{self.run_group}/{random_dataset}'
        else:
            self.glitch = int(glitch)
            logger.debug("Using user-provided glitch '%s'", self.glitch)
            self.glitch_dataset = f'{self.run_group}/glitch{self.glitch:02}' #: Path to glitch dataset.

        try:
            hdf5[self.glitch_dataset]
        except KeyError as error:
            raise KeyError(f"glitch dataset '{self.glitch_dataset}' not found in '{self.library}'") from error

        logger.info("Closing LPF glitch library '%s'", self.library)
        hdf5.close()

        super().__init__(self.library, self.glitch_dataset, **kwargs)

        self.integrated = bool(integrated) #: Whether to integrate glitch signal (use a velocity glitch).
        if self.integrated:
            # Integrate interpolant once analytically
            logger.debug("Integrating LPF library acceleration glitch signal to velocity")
            self.interpolant = self.interpolant.antiderivative()


class LPFLibraryModelGlitch():
    r"""Double-exponential glitch using parameters from a LPF glitch library.

    Glitch parameters are read from the library, and either :class:`lisaglitch.OneSidedDoubleExpGlitch`
    or :class:`lisaglitch.TwoSidedDoubleExpGlitch` class is used to generate the signal.

    The LISA Pathfinder glitch library has the following structure::

        legacy_params / runXX / glitchYY

    You can specify a run and glitch number, or leave them as ``None`` to let the
    class pick a random run and/or glitch.

    A default LPF glitch library is included with the package. Use ``'default'`` as
    the path to use it.

    Args:
        path (str): path to LPF glitch library (``'default'`` for default library)
        run (int or None): run number, or None to sample a random run
        glitch (int or None): glitch number, or None to sample a random glitch
        integrated (bool): whether to integrate glitch signal (use a velocity glitch)

    Attributes:
        library: Path to LPF glitch library.
        run_group: Path to run group.
        glitch_dataset: Path to glitch dataset.
        integrated: Whether to integrate glitch signal (use a velocity glitch).
    """

    def __new__(cls, path='default', run=None, glitch=None, integrated=False, **kwargs):

        # Default library
        if path == 'default':
            logger.debug("Using default LPF glitch library")
            path = importlib_resources.files('lisaglitch') / 'data' / 'lpf-glitch-library.h5'

        library = str(path)
        logger.info("Opening LPF glitch library '%s'", library)
        hdf5 = h5py.File(library, 'r')

        # Pick run
        if run is None:
            run = None
            logger.debug("Picking a random run in library '%s'", library)
            random_group = random.choice(list(hdf5['legacy_params'].keys()))
            run_group = f'legacy_params/{random_group}'
        else:
            run = int(run)
            logger.debug("Using user-provided run '%s'", run)
            run_group = f'legacy_params/run{run:02}'

        try:
            run_group_object = hdf5[run_group]
        except KeyError as error:
            raise KeyError(f"run group '{run_group}' not found in '{library}'") from error

        # Pick glitch
        if glitch is None:
            glitch = None
            logger.debug("Picking a random glitch in run '%s'", run)
            random_dataset = random.choice(list(run_group_object.keys()))
            glitch_dataset = f'{run_group}/{random_dataset}'
        else:
            glitch = int(glitch)
            logger.debug("Using user-provided glitch '%s'", glitch)
            glitch_dataset = f'{run_group}/glitch{glitch:02}'

        try:
            legacy_params = hdf5[glitch_dataset][:]
        except KeyError as error:
            raise KeyError(f"glitch dataset '{glitch_dataset}' not found in '{library}'") from error

        logger.info("Closing LPF glitch library '%s'", library)
        hdf5.close()

        # Retreive parameters
        level = float(legacy_params[0])
        t_rise = float(legacy_params[2])
        t_fall = float(legacy_params[3])
        displacement = float(legacy_params[4])

        if not integrated:
            # Initialize the acceleration glitch
            if displacement != 0:
                instance = TwoSidedDoubleExpGlitch(t_rise, t_fall, level, displacement, **kwargs)
            else:
                instance = OneSidedDoubleExpGlitch(t_rise, t_fall, level, **kwargs)
        else:
            # Initialize the (integrated) velocity glitch
            if displacement != 0:
                instance = IntegratedTwoSidedDoubleExpGlitch(t_rise, t_fall, level, displacement, **kwargs)
            else:
                instance = IntegratedOneSidedDoubleExpGlitch(t_rise, t_fall, level, **kwargs)

        # Set parameters as attributes on the glitch instance
        instance.library = library
        instance.integrated = integrated
        instance.run = run
        instance.run_group = run_group
        instance.glitch = glitch
        instance.glitch_dataset = glitch_dataset
        instance.legacy_params = legacy_params
        instance.plot = lambda *args, **kwargs: LPFLibraryModelGlitch.plot(instance, *args, **kwargs)

        return instance

    @staticmethod
    def plot(instance, output=None, tmin=None, tmax=None, title=None):
        """Plot glitch signal.

        See :meth:`lisaglitch.Glitch.plot`.
        """
        if title is None:
            title = f"Double-exp. glitch from fitted parameters of '{instance.glitch_dataset}' in '{instance.library}'"
        instance.__class__.plot(instance, output, tmin, tmax, title)
