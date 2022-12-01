#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=all
"""
Neural Spline Flow.

References:
    Paper reference: Durkan et al. <https://arxiv.org/abs/1906.04032>
    Code reference: slightly modified from <https://github.com/tonyduan/normalizing-flows/blob/master/nf/flows.py>
    Based on original implementation from <https://github.com/bayesiains/nsf>
"""

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from .resnet import ResidualNet


DEFAULT_MIN_BIN_WIDTH = 1e-3
DEFAULT_MIN_BIN_HEIGHT = 1e-3
DEFAULT_MIN_DERIVATIVE = 1e-3


class MLP(nn.Module):
    """Define a simple fully connected 4-layer MLP."""

    def __init__(self, number_in, number_out, number_hidden):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(number_in, number_hidden),
            nn.ReLU(),
            nn.Linear(number_hidden, number_hidden),
            nn.ReLU(),
            nn.Linear(number_hidden, number_hidden),
            nn.ReLU(),
            nn.Linear(number_hidden, number_out),
            nn.ReLU()
        )

    def forward(self, x_input):
        """Forward pass for training."""
        return self.net(x_input)


def searchsorted(bin_locations, inputs, eps=1e-6):
    """Search."""
    bin_locations[..., -1] += eps
    return torch.sum(inputs[..., None] >= bin_locations, dim=-1) - 1


def unconstrained_RQS(inputs,
                      unnormalized_widths,
                      unnormalized_heights,
                      unnormalized_derivatives,
                      inverse=False,
                      tail_bound=1.0,
                      min_bin_width=DEFAULT_MIN_BIN_WIDTH,
                      min_bin_height=DEFAULT_MIN_BIN_HEIGHT,
                      min_derivative=DEFAULT_MIN_DERIVATIVE):
    """Unconstrained Rational Quadratic Spline."""

    inside_intvl_mask = (inputs >= -tail_bound) & (inputs <= tail_bound)
    outside_interval_mask = ~inside_intvl_mask

    outputs = torch.zeros_like(inputs)
    logabsdet = torch.zeros_like(inputs)

    unnormalized_derivatives = F.pad(unnormalized_derivatives, pad=(1, 1))
    constant = np.log(np.exp(1 - min_derivative) - 1)
    unnormalized_derivatives[..., 0] = constant
    unnormalized_derivatives[..., -1] = constant

    outputs[outside_interval_mask] = inputs[outside_interval_mask]
    logabsdet[outside_interval_mask] = 0

    if inside_intvl_mask is False:
        raise ValueError("Input outside domain")

    if torch.any(inside_intvl_mask):
        outputs[inside_intvl_mask], logabsdet[inside_intvl_mask] = RQS(
            inputs=inputs[inside_intvl_mask],
            unnormalized_widths=unnormalized_widths[inside_intvl_mask, :],
            unnormalized_heights=unnormalized_heights[inside_intvl_mask, :],
            unnormalized_derivatives=unnormalized_derivatives[inside_intvl_mask, :],
            inverse=inverse,
            left=-tail_bound, right=tail_bound, bottom=-tail_bound, top=tail_bound,
            min_bin_width=min_bin_width,
            min_bin_height=min_bin_height,
            min_derivative=min_derivative
        )
    return outputs, logabsdet


def RQS(inputs,
        unnormalized_widths,
        unnormalized_heights,
        unnormalized_derivatives,
        inverse=False,
        left=0.0,
        right=1.0,
        bottom=0.0,
        top=1.0,
        min_bin_width=DEFAULT_MIN_BIN_WIDTH,
        min_bin_height=DEFAULT_MIN_BIN_HEIGHT,
        min_derivative=DEFAULT_MIN_DERIVATIVE):
    """Rational Quadratic Spline."""

    if torch.min(inputs) < left or torch.max(inputs) > right:
        raise ValueError("Input outside domain")

    num_bins = unnormalized_widths.shape[-1]

    if min_bin_width * num_bins > 1.0:
        raise ValueError('Minimal bin width too large for the number of bins')
    if min_bin_height * num_bins > 1.0:
        raise ValueError('Minimal bin height too large for the number of bins')

    widths = F.softmax(unnormalized_widths, dim=-1)
    widths = min_bin_width + (1 - min_bin_width * num_bins) * widths
    cumwidths = torch.cumsum(widths, dim=-1)
    cumwidths = F.pad(cumwidths, pad=(1, 0), mode='constant', value=0.0)
    cumwidths = (right - left) * cumwidths + left
    cumwidths[..., 0] = left
    cumwidths[..., -1] = right
    widths = cumwidths[..., 1:] - cumwidths[..., :-1]

    derivatives = min_derivative + F.softplus(unnormalized_derivatives)

    heights = F.softmax(unnormalized_heights, dim=-1)
    heights = min_bin_height + (1 - min_bin_height * num_bins) * heights
    cumheights = torch.cumsum(heights, dim=-1)
    cumheights = F.pad(cumheights, pad=(1, 0), mode='constant', value=0.0)
    cumheights = (top - bottom) * cumheights + bottom
    cumheights[..., 0] = bottom
    cumheights[..., -1] = top
    heights = cumheights[..., 1:] - cumheights[..., :-1]

    if inverse:
        bin_idx = searchsorted(cumheights, inputs)[..., None]
    else:
        bin_idx = searchsorted(cumwidths, inputs)[..., None]

    input_cumwidths = cumwidths.gather(-1, bin_idx)[..., 0]
    input_bin_widths = widths.gather(-1, bin_idx)[..., 0]

    input_cumheights = cumheights.gather(-1, bin_idx)[..., 0]
    delta = heights / widths
    input_delta = delta.gather(-1, bin_idx)[..., 0]

    input_derivatives = derivatives.gather(-1, bin_idx)[..., 0]
    input_derivatives_plus_one = derivatives[..., 1:].gather(-1, bin_idx)
    input_derivatives_plus_one = input_derivatives_plus_one[..., 0]

    input_heights = heights.gather(-1, bin_idx)[..., 0]

    if inverse:
        a = (((inputs - input_cumheights) * (input_derivatives \
            + input_derivatives_plus_one - 2 * input_delta) \
            + input_heights * (input_delta - input_derivatives)))
        b = (input_heights * input_derivatives - (inputs - input_cumheights) \
            * (input_derivatives + input_derivatives_plus_one \
            - 2 * input_delta))
        c = - input_delta * (inputs - input_cumheights)

        discriminant = b.pow(2) - 4 * a * c
        assert (discriminant >= 0).all()

        root = (2 * c) / (-b - torch.sqrt(discriminant))
        outputs = root * input_bin_widths + input_cumwidths

        theta_one_minus_theta = root * (1 - root)
        denominator = input_delta \
                      + ((input_derivatives + input_derivatives_plus_one \
                      - 2 * input_delta) * theta_one_minus_theta)
        derivative_numerator = input_delta.pow(2) \
                               * (input_derivatives_plus_one * root.pow(2) \
                                + 2 * input_delta * theta_one_minus_theta \
                                + input_derivatives * (1 - root).pow(2))
        logabsdet = torch.log(derivative_numerator) - 2 * torch.log(denominator)
        return outputs, -logabsdet
    else:
        theta = (inputs - input_cumwidths) / input_bin_widths
        theta_one_minus_theta = theta * (1 - theta)

        numerator = input_heights * (input_delta * theta.pow(2) \
                    + input_derivatives * theta_one_minus_theta)
        denominator = input_delta + ((input_derivatives \
                      + input_derivatives_plus_one - 2 * input_delta) \
                      * theta_one_minus_theta)
        outputs = input_cumheights + numerator / denominator

        derivative_numerator = input_delta.pow(2) \
                               * (input_derivatives_plus_one * theta.pow(2) \
                                + 2 * input_delta * theta_one_minus_theta \
                                + input_derivatives * (1 - theta).pow(2))
        logabsdet = torch.log(derivative_numerator) - 2 * torch.log(denominator)
        return outputs, logabsdet


class NSF_CL(nn.Module):
    """Neural spline flow, coupling layer from [1].

    [1] Durkan et al. (2019)
    """
    def __init__(self, dim, K=5, B=3, hidden_dim=8, base_network=ResidualNet):
        super().__init__()
        self.dim = dim
        self.K = K
        self.B = B
        self.f1 = base_network(dim // 2, (3 * K - 1) * dim // 2, hidden_dim)
        self.f2 = base_network(dim // 2, (3 * K - 1) * dim // 2, hidden_dim)

    def forward(self, x):
        """Forward pass."""
        log_det = torch.zeros(x.shape[0])
        lower, upper = x[:, :self.dim // 2], x[:, self.dim // 2:]
        out = self.f1(lower).reshape(-1, self.dim // 2, 3 * self.K - 1)
        W, H, D = torch.split(out, self.K, dim = 2)
        W, H = torch.softmax(W, dim = 2), torch.softmax(H, dim = 2)
        W, H = 2 * self.B * W, 2 * self.B * H
        D = F.softplus(D)
        upper, ld = unconstrained_RQS(upper, W, H, D, inverse=False, tail_bound=self.B)
        log_det += torch.sum(ld, dim = 1)
        out = self.f2(upper).reshape(-1, self.dim // 2, 3 * self.K - 1)
        W, H, D = torch.split(out, self.K, dim = 2)
        W, H = torch.softmax(W, dim = 2), torch.softmax(H, dim = 2)
        W, H = 2 * self.B * W, 2 * self.B * H
        D = F.softplus(D)
        lower, ld = unconstrained_RQS(lower, W, H, D, inverse=False, tail_bound=self.B)
        log_det += torch.sum(ld, dim = 1)
        return torch.cat([lower, upper], dim = 1), log_det

    def backward(self, z):
        """Backward pass to sample."""
        log_det = torch.zeros(z.shape[0])
        lower, upper = z[:, :self.dim // 2], z[:, self.dim // 2:]
        out = self.f2(upper).reshape(-1, self.dim // 2, 3 * self.K - 1)
        W, H, D = torch.split(out, self.K, dim = 2)
        W, H = torch.softmax(W, dim = 2), torch.softmax(H, dim = 2)
        W, H = 2 * self.B * W, 2 * self.B * H
        D = F.softplus(D)
        lower, ld = unconstrained_RQS(lower, W, H, D, inverse=True, tail_bound=self.B)
        log_det += torch.sum(ld, dim = 1)
        out = self.f1(lower).reshape(-1, self.dim // 2, 3 * self.K - 1)
        W, H, D = torch.split(out, self.K, dim = 2)
        W, H = torch.softmax(W, dim = 2), torch.softmax(H, dim = 2)
        W, H = 2 * self.B * W, 2 * self.B * H
        D = F.softplus(D)
        upper, ld = unconstrained_RQS(upper, W, H, D, inverse = True, tail_bound = self.B)
        log_det += torch.sum(ld, dim = 1)
        return torch.cat([lower, upper], dim = 1), log_det
