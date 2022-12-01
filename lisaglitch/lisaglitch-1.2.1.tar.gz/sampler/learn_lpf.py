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
# pylint: disable=all
"""
Learns the distribution for the LISA Pathfinder parameters using invertabale flows.

The implementation of the flows is based on Neural Spline Flows (https://arxiv.org/abs/1906.04032)
and is located in the directory '../flows'.

The code for the flow implementation is based on
    https://github.com/bayesiains/nsf
    https://github.com/tonyduan/normalizing-flows/blob/master/nf/flows.py
    https://github.com/karpathy/pytorch-normalizing-flows

Author:
    Natalia Korsakova <natalia.korsakova@obspm.fr>
    Jean-Baptiste Bayle <j2b.bayle@gmail.com>
"""

import logging
import importlib_resources
import numpy as np
import torch
import torch.optim as optim
import matplotlib.pyplot as plt

from lisaglitch.lpfdistrib import initialise_network

logger = logging.getLogger(__name__)


def load_data(path_dir):
    """Load points that represent samples from the LFP glitch datameter distribution.

    Args:
        path_dir: path to text file

    Returns:
        2-tuple (beta, amp) for Poisson parameter and amplitude.
    """
    all_param = np.loadtxt(path_dir, comments='#', delimiter=' ', skiprows=0, usecols=(0,1), unpack=False)
    beta, amp = all_param[:, 0], all_param[:, 1]
    return beta, amp


def normalise(dist_var):
    """Normalize and take log of the values, so that the distribution is easier to fit."""
    # Make negative amplitudes positive
    log_dist_var = np.log(np.abs(dist_var))
    logger.debug('x.min = %s', log_dist_var.min())
    logger.debug('x.max = %s', log_dist_var.max())

    return (log_dist_var - log_dist_var.min()) / (log_dist_var.max() - log_dist_var.min())


def main():
    """Load data and fit density.

    Load the data with the estimated parameters for the LISA Pathfinder glitches from the matched
    filter search, and choose the flow to fit the density to the data.
    """

    if torch.cuda.is_available():
        dev = "cuda:0"
        dtype = torch.cuda.FloatTensor
    else:
        dev = "cpu"
        dtype = torch.FloatTensor

    torch.set_default_tensor_type('torch.cuda.FloatTensor')

    data_dir = importlib_resources.files('lisaglitch') / 'data'
    beta_cold, amp_cold = load_data(data_dir / '2021-09-17-effective_glitch_parameters_cold.txt')
    beta_ordinary, amp_ordinary = load_data(data_dir / '2021-09-17-effective_glitch_parameters_ordinary.txt')

    beta = normalise(np.r_[beta_cold, beta_ordinary])
    amp = normalise(np.r_[amp_cold, amp_ordinary])

    data = torch.from_numpy(np.c_[beta, amp].astype(np.float32)).type(dtype)
    logger.debug('data.shape = %s', data.shape)

    plt.figure()
    plt.plot(beta, amp, 'bo')
    plt.savefig('original_data.png')

    model, optimizer = initialise_network(dev)

    anneal_learning_rate = 1
    num_training_steps = 150000

    if anneal_learning_rate:
        scheduler = optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max = num_training_steps, eta_min=0, last_epoch=-1)
    else:
        scheduler = None

    model.train()
    batch_size = 530
    num_iterations = 150001

    for k in range(num_iterations):

        ind = np.random.choice(amp.shape[0] - 1, batch_size)
        x_point = data[ind,:]

        zsample, prior_logprob, log_det = model(x_point)
        logprob = prior_logprob + log_det
        loss = -torch.sum(logprob)

        model.zero_grad()
        loss.backward()
        optimizer.step()

        if anneal_learning_rate:
            scheduler.step()

        if k % 100 == 0:
            logger.debug('k = &s   .....   %s', k, loss.item())
            for param_group in optimizer.param_groups:
                logger.debug('lr = %s', param_group['lr'])

        if (k - 1) % 5000 == 0:
            # Do not forget to evaluate here. However we do not have so much space for that.
            # Save checkpoint for every iteration
            checkpoint_path = f'./checkpoint_{k}.pt'
            torch.save({
                'epoch': k,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'loss': loss,}, checkpoint_path)

            zsample = model.sample(256 * 100)
            z_point = zsample[-1]
            z_point = z_point.detach().cpu().numpy()

            plt.figure()
            plt.plot(z_point[:,0], z_point[:,1], 'bo')
            plt.legend(['data', 'z->x'])
            plt.axis('scaled')
            plt.title('z -> x')
            plt.savefig('new_distribution.png')


if __name__=='__main__':
    main()
