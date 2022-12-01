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
Samples the times of occurance from the Poisson distribution.
Samples the parameters of the glitch from the previously learned LPF distribution.

Author:
    Natalia Korsakova <natalia.korsakova@obspm.fr>
    Jean-Baptiste Bayle <j2b.bayle@gmail.com>
"""

import logging
import importlib_resources
import numpy as np
import torch
import lisaglitch
import lisaglitch.lpfdistrib
import lisaglitch.random


logger = logging.getLogger(__name__)


def iterative_sampler(lam, lpf_param, t0, dt, size, inj_points, out_glitch_filename):
    """Sample glitches and write them to glitch file to fill the desired time range.

    We start at t0, evaluate next arrival time, sample one set of LPF parameters,
    write glitch to file, and repeat until we reach the end of the simulation.

    Args:
        lam: Poisson's lambda parameter [/s]
        lpf_param: instance of the class that has functionality to sample LPF parameters
        t0: starting time of the interval [s]
        dt: cadence [s]
        size: sample size of the interval [samples]
        inj_points: injection point, i.e. the point at the instrument where glitch is injected
        out_glitch_filename: name of the file where glitch time series are written to
    """
    generate_lpf_param = lpf_param.generator()

    t_last = t0
    duration = t0 + size * dt

    while True:
        # Randomly sample the time of the next glitch appearance
        t_inj = lisaglitch.random.poisson_arrival(lam, t_last)
        t_last = t_inj

        if t_inj < duration:
            logger.debug('Write to file for t_inj = %s', t_inj)
            beta, level = next(generate_lpf_param)
            lisaglitch.IntegratedShapeletGlitch(
                inj_point=np.random.choice(inj_points),
                t0=t0,
                size=size,
                dt=dt,
                t_inj=t_inj,
                beta=beta,
                level=level).write(path=out_glitch_filename)
        else:
            break


def array_sampler(lam, lpf_param, number_samples, t0, dt, size, inj_points, out_glitch_filename):
    """Sample a given number of glitches and write them to a glitch file.

    Args:
        lam: Poisson's lambda parameter [/s]
        lpf_param: instance of the class that has functionality to sample LPF parameters
        number_samples: desired number of glitches per interval [samples]
        t0: starting time of the interval [s]
        dt: cadence [s]
        size: sample size of the interval [samples]
        inj_points: injection point, i.e. the point at the instrument where glitch is injected
        out_glitch_filename: name of the file where glitch time series are written to
    """
    arrivals = lisaglitch.random.poisson_arrival(lam, t0, size=number_samples)

    # If some glitch arrival times are larger than the length of the time series,
    # we remove them from the list
    if np.any(arrivals > t0 + size * dt):
        first_index = np.argmax(arrivals > t0 + size * dt)
        arrivals = arrivals[:first_index]
        number_samples = len(arrivals)

    inj_points = np.random.choice(inj_points, size=number_samples)
    betas, levels = lpf_param.generate(number_samples)
    signs = np.random.choice([-1, 1], size=number_samples)
    levels *= signs

    for beta, level, arrival, inj_point in zip(betas, levels, arrivals, inj_points):
        logger.debug('Write to file for t_inj = %s', arrival)
        lisaglitch.IntegratedShapeletGlitch(
            inj_point=inj_point,
            t0=t0,
            size=size,
            dt=dt,
            t_inj=arrival,
            beta=beta,
            level=level).write(path=out_glitch_filename)


def main():
    """Sample glitch parameters and write glitches to a glitch file.

    The time of occurance are drawn from a Poisson distribution, while the glitch
    parameters are drawn from a the previously learned LPF distribution.
    """
    if torch.cuda.is_available():
        device = "cuda:0"
    else:
        device = "cpu"
    torch.set_default_tensor_type('torch.cuda.FloatTensor')

    # Initialise sampler with the trained weights
    data_dir = importlib_resources.files('lisaglitch') / 'data'
    path = data_dir / 'checkpoint.pt'

    # Ranges of physical parameters to renormalise back from [0,1]
    min_beta = -2.3025850929940455
    max_beta = 10.819778284410283
    min_amp = -55.742988125334776
    max_amp = -17.65578323582705

    lpf_param = lisaglitch.lpfdistrib.LPFGlitchParameterSampler(device, min_beta, max_beta, min_amp, max_amp)
    lpf_param.define_model()
    lpf_param.load_model(path)

    # List of the injection points to sample from
    inj_points = ['tm_12', 'tm_23', 'tm_31', 'tm_13', 'tm_32', 'tm_21']

    # Chose if we estimate lambda from file or set it by hand.
    lambda_read = True
    if lambda_read:
        path_intervals = data_dir / '2021-09-17-intervals_ordinary.txt'
        poisson_lambda = lisaglitch.lpfdistrib.estimate_poisson_beta(path_intervals)
    else:
        poisson_lambda = 1.0 / 86400 # one glitch per day

    # Define parameters of the time series
    t0 = 0.0
    dt = 5.0
    size = 6311520

    out_glitch_filename = 'glitch_filename.h5'

    # Choose if we sample glitches one after the other or all simultaneously
    sample_multiple = True
    number_samples = 356
    if not sample_multiple:
        iterative_sampler(poisson_lambda, lpf_param, t0, dt, size, inj_points, out_glitch_filename)
    else:
        array_sampler(poisson_lambda, lpf_param, number_samples, t0, dt, size, inj_points, out_glitch_filename)


if __name__ == "__main__":
    main()
