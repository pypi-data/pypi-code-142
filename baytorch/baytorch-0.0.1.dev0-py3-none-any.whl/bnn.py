import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, random_split
from torch.nn.common_types import _size_2_t
from torch.nn.modules.utils import _single, _pair, _triple, _reverse_repeat_tuple

import numpy as np

from typing import Tuple, Union, Optional
from enum import Enum


def hessian(outputs, inputs):
    grad = torch.autograd.grad(outputs, inputs, retain_graph=True, create_graph=True) # compute gradient
    n = np.sum([x.numel() for x in grad]) # get number of parameters
    hessian = torch.zeros((n, n)) # empty hessian n x n
    
    flattened_grads = torch.hstack([x.flatten() for x in grad])
    
    for i, grad in enumerate(flattened_grads):
        gradgrad = torch.autograd.grad(grad, inputs, retain_graph=True)
        hessian[i] = torch.hstack([x.flatten() for x in gradgrad])
        
    return hessian


def model_hessian(outputs, model):
    for param in model.parameters():
        yield hessian(outputs, param)


def diagonal_gaussian_kl(mu_p, var_p, mu_q, var_q):
    """
        D_KL(p || q) with p = N(mu_p, var_p) and q = N(mu_q, var_q)
    """
    return .5 * (var_p / var_q - 1 + (mu_p - mu_q).pow(2) / var_q + torch.log(var_q / var_p)).sum()


def diagonal_gaussian_cross_entropy(mu_p, var_p, mu_q, var_q, weight=1):
    n = torch.numel(mu_p)
    return .5 * n * (1 + np.log(2*np.pi)) + .5 * var_p.pow(weight).log().sum() \
        + .5 * (var_p / var_q - 1 + (mu_p - mu_q).pow(2) / var_q + torch.log(var_q / var_p)).sum()


def diagonal_gaussian_entropy(var, weight=1):
    n = torch.numel(var)
    return .5 * n * (1 + np.log(2*np.pi)) + .5 * var.pow(weight).log().sum()


def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


class VFELoss:
    def __init__(self, loss_fn):
        super().__init__()
        self.loss_fn = loss_fn
        
    def __call__(self, model, *args, weight=None):
        if weight is None:
            weight = 1./count_parameters(model)
        complexity_cost = weight * model.complexity_cost()
        error_cost = self.loss_fn(*args)
        return complexity_cost + error_cost, (complexity_cost, error_cost)


class BayesianModule(nn.Module):
    def __init__(self):
        super().__init__()

    def complexity_cost(self):
        costs = 0
        for module in self.modules():
            if isinstance(module, BayesianModule) and module is not self:
                costs += module.complexity_cost()
        return costs
        

Mode = Enum('Mode', [('stochastic', None), ('mean', 0), ('meanpstd', 1), ('meanmstd', -1)])


class DiagonalGaussianModule(BayesianModule):
    def __init__(self):
        super().__init__()
        self._mode = Mode['stochastic']

    @property
    def mode(self):
        return self._mode
        
    @mode.setter
    def mode(self, value):
        self._mode = value if type(value) is Mode else Mode[value]
        for name, module in self.named_modules():
        #for module in self.modules():
            if isinstance(module, DiagonalGaussianModule) and module is not self:
                module.mode = value
        

class DiagonalGaussianLayer(DiagonalGaussianModule):
    def __init__(self):
        super().__init__()
        self.weight_mean = None
        self.weight_rho = None
        self.bias_mean = None
        self.bias_rho = None

        self.prior_weight_mean = None
        self.prior_weight_std = None
        self.prior_bias_mean = None
        self.prior_bias_std = None

        self._learn_mean = None
        self._learn_std = None

        self._bias = None

    @property
    def learn_mean(self):
        return self._learn_mean

    @learn_mean.setter
    def learn_mean(self, value):
        assert type(value) is bool
        self._learn_mean = value

        if self.weight_mean is not None:
            self.weight_mean.requires_grad_(value)

        if self.bias_mean is not None:
            self.bias_mean.requires_grad_(value)
        
    @property
    def learn_std(self):
        return self._learn_std

    @learn_std.setter
    def learn_std(self, value):
        assert type(value) is bool
        self._learn_std = value

        if self.weight_std is not None:
            self.weight_std.requires_grad_(value)

        if self.bias_std is not None:
            self.bias_std.requires_grad_(value)
        
    @property
    def weight_std(self):
        return torch.log1p(torch.exp(self.weight_rho)) 

    @weight_std.setter
    def weight_std(self, var):
        assert var.numel() == self.bias_rho.numel()
        with torch.no_grad():
            self.weight_rho.data.copy_(torch.log(torch.expm1(var)).reshape(*self.weight_rho.shape))

    @property
    def weight(self):
        # if mode is stochastic, the value is sampled. otherwise depending on the mode, we either go mean, mean+std or mean-std
        eps = torch.zeros_like(self.weight_mean).normal_(0, 1) if self.mode == Mode.stochastic else self.mode.value
        return self.weight_mean + self.weight_std * eps

    @property
    def bias_std(self):
        return torch.log1p(torch.exp(self.bias_rho)) if self.bias_rho is not None else None

    @bias_std.setter
    def bias_std(self, var):
        assert var.numel() == self.bias_rho.numel()
        with torch.no_grad():
            self.bias_rho.data.copy_(torch.log(torch.expm1(var)).reshape(*self.bias_rho.shape))

    @property
    def bias(self):
        if self._bias:
            # if mode is stochastic, the value is sampled. otherwise depending on the mode, we either go mean, mean+std or mean-std
            eps = torch.zeros_like(self.bias_mean).normal_(0, 1) if self.mode == Mode.stochastic else self.mode.value
            return self.bias_mean + self.bias_std * eps

        return None

    def _apply(self, fn):
        super()._apply(fn)
        self.weight_mean = fn(self.weight_mean)
        self.weight_rho = fn(self.weight_rho)

        if self._bias:
            self.bias_mean = fn(self.bias_mean)
            self.bias_rho = fn(self.bias_rho)

        self.prior_weight_mean = fn(self.prior_weight_mean) if self.prior_weight_mean is not None else None
        self.prior_weight_std = fn(self.prior_weight_std) if self.prior_weight_std is not None else None
        self.prior_bias_mean = fn(self.prior_bias_mean) if self.prior_bias_mean is not None else None
        self.prior_bias_std = fn(self.prior_bias_std) if self.prior_bias_std is not None else None

        return self    

    def complexity_cost(self):
        if self.prior_weight_mean is None or self.prior_weight_std is None or \
           self.prior_bias_mean is None or self.prior_bias_std is None:

            cost = diagonal_gaussian_entropy(self.weight_std.pow(2))
            if self._bias:
                cost += diagonal_gaussian_entropy(self.bias_std.pow(2))

            return -cost

        else:
            cost = diagonal_gaussian_kl(self.weight_mean, self.weight_std.pow(2), 
                                        self.prior_weight_mean, self.prior_weight_std.pow(2))
            if self._bias:
                cost += diagonal_gaussian_kl(self.bias_mean, self.bias_std.pow(2), 
                                             self.prior_bias_mean, self.prior_bias_std.pow(2))

            return cost


class DiagonalGaussianConvNd(DiagonalGaussianLayer):
    def __init__(self,
                 in_channels: int,
                 out_channels: int,
                 kernel_size: Tuple[int, ...],
                 stride: Tuple[int, ...],
                 padding: Tuple[int, ...],
                 dilation: Tuple[int, ...],
                 transposed: bool,
                 output_padding: Tuple[int, ...],
                 groups: int,
                 bias: bool,
                 padding_mode: str,
                 device=None, dtype=None,
                 learn_mean=True, learn_std=True,
                 prior_weight_mean=None, prior_weight_std=None,
                 prior_bias_mean=None, prior_bias_std=None) -> None:
        super().__init__()

        factory_kwargs = {'device': device, 'dtype': dtype}
        if in_channels % groups != 0:
            raise ValueError('in_channels must be divisible by groups')
        if out_channels % groups != 0:
            raise ValueError('out_channels must be divisible by groups')
        valid_padding_strings = {'same', 'valid'}
        if isinstance(padding, str):
            if padding not in valid_padding_strings:
                raise ValueError(
                    "Invalid padding string {!r}, should be one of {}".format(
                        padding, valid_padding_strings))
            if padding == 'same' and any(s != 1 for s in stride):
                raise ValueError("padding='same' is not supported for strided convolutions")

        valid_padding_modes = {'zeros', 'reflect', 'replicate', 'circular'}
        if padding_mode not in valid_padding_modes:
            raise ValueError("padding_mode must be one of {}, but got padding_mode='{}'".format(
                valid_padding_modes, padding_mode))

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.dilation = dilation
        self.transposed = transposed
        self.output_padding = output_padding
        self.groups = groups
        self.padding_mode = padding_mode

        # `_reversed_padding_repeated_twice` is the padding to be passed to
        # `F.pad` if needed (e.g., for non-zero padding types that are
        # implemented as two ops: padding + conv). `F.pad` accepts paddings in
        # reverse order than the dimension.
        if isinstance(self.padding, str):
            self._reversed_padding_repeated_twice = [0, 0] * len(kernel_size)
            if padding == 'same':
                for d, k, i in zip(dilation, kernel_size,
                                   range(len(kernel_size) - 1, -1, -1)):
                    total_padding = d * (k - 1)
                    left_pad = total_padding // 2
                    self._reversed_padding_repeated_twice[2 * i] = left_pad
                    self._reversed_padding_repeated_twice[2 * i + 1] = (
                        total_padding - left_pad)
        else:
            self._reversed_padding_repeated_twice = _reverse_repeat_tuple(self.padding, 2)

        if transposed:
            self.weight_mean = nn.Parameter(torch.zeros((in_channels, out_channels // groups, *kernel_size), 
                                                        **factory_kwargs),
                                            requires_grad=learn_mean)

            self.weight_std = nn.Parameter(torch.zeros((in_channels, out_channels // groups, *kernel_size), 
                                                       **factory_kwargs),
                                           requires_grad=learn_std)

        else:
            self.weight_mean = nn.Parameter(torch.zeros((out_channels, in_channels // groups, *kernel_size), 
                                                        **factory_kwargs),
                                            requires_grad=learn_mean)

            self.weight_rho = nn.Parameter(torch.log(torch.expm1(torch.ones((out_channels, in_channels // groups, *kernel_size), 
                                                     **factory_kwargs))),
                                           requires_grad=learn_std)

        if bias:
            self.bias_mean = nn.Parameter(torch.zeros(out_channels, **factory_kwargs), 
                                          requires_grad=learn_mean)

            self.bias_rho = nn.Parameter(torch.log(torch.expm1(torch.ones(out_channels, **factory_kwargs))), 
                                         requires_grad=learn_std)

        self.learn_mean = learn_mean
        self.learn_std = learn_std

        self._bias = bias

        self.prior_weight_mean = prior_weight_mean.to(**factory_kwargs) if prior_weight_mean is not None else None
        self.prior_weight_std = prior_weight_std.to(**factory_kwargs) if prior_weight_std is not None else None
        self.prior_bias_mean = prior_bias_mean.to(**factory_kwargs) if prior_bias_mean is not None else None
        self.prior_bias_std = prior_bias_std.to(**factory_kwargs) if prior_bias_std is not None else None

    def forward(self, x):
        return F.conv2d(x, self.weight, self.bias, 
                        self.stride, self.padding, 
                        self.dilation, self.groups)


class DiagonalGaussianConv2d(DiagonalGaussianConvNd):
    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: _size_2_t,
        stride: _size_2_t = 1,
        padding: Union[str, _size_2_t] = 0,
        dilation: _size_2_t = 1,
        groups: int = 1,
        bias: bool = True,
        padding_mode: str = 'zeros',  # TODO: refine this type
        device=None,
        dtype=None
    ) -> None:
        factory_kwargs = {'device': device, 'dtype': dtype}
        kernel_size_ = _pair(kernel_size)
        stride_ = _pair(stride)
        padding_ = padding if isinstance(padding, str) else _pair(padding)
        dilation_ = _pair(dilation)
        super().__init__(
            in_channels, out_channels, kernel_size_, stride_, padding_, dilation_,
            False, _pair(0), groups, bias, padding_mode, **factory_kwargs)

    def build_from(self, conv: nn.Conv2d):
        #bconv = DiagonalGaussianConv2d(conv.in_channels, conv.out_channels, conv.kernel_size,
        #                                 conv.stride, conv.padding, conv.dilation, conv.groups,
        #                                 conv.bias is not None, conv.padding_mode,
        #                                 conv.weight.device, conv.weight.dtype)
        
        self.in_channels = conv.in_channels 
        self.out_channels = conv.out_channels
        self.kernel_size = conv.kernel_size
        self.stride = conv.stride 
        self.padding = conv.padding 
        self.dilation = conv.dilation
        self.transposed = conv.transposed
        self.groups = conv.groups
        self.output_padding = conv.output_padding
        self._bias = conv.bias is not None
        self.padding_mode = conv.padding_mode

        self.weight_mean = conv.weight
        self.bias_mean = conv.bias

    def _conv_forward(self, input: torch.Tensor, weight: torch.Tensor, bias: Optional[torch.Tensor]):
        if self.padding_mode != 'zeros':
            return F.conv2d(F.pad(input, self._reversed_padding_repeated_twice, mode=self.padding_mode),
                            weight, bias, self.stride,
                            _pair(0), self.dilation, self.groups)
        return F.conv2d(input, weight, bias, self.stride,
                        self.padding, self.dilation, self.groups)

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        return self._conv_forward(input, self.weight, self.bias)


class DiagonalGaussianLinear(DiagonalGaussianLayer):
    def __init__(self, in_features: int, out_features: int, bias: bool=True,
                 device=None, dtype=None,
                 learn_mean=True, learn_std=True,
                 prior_weight_mean=None, prior_weight_std=None,
                 prior_bias_mean=None, prior_bias_std=None) -> None:
        super().__init__()

        factory_kwargs = {'device': device, 'dtype': dtype}
        self.in_features, self.out_features = in_features, out_features

        self.weight_mean = nn.Parameter(torch.zeros(out_features, in_features, **factory_kwargs),
                                        requires_grad=learn_mean)
        self.weight_rho = nn.Parameter(torch.log(torch.expm1(torch.ones(out_features, in_features, **factory_kwargs))),
                                       requires_grad=learn_std)

        # initialize bias if requested
        if bias:
            self.bias_mean = nn.Parameter(torch.zeros(out_features, **factory_kwargs), 
                                          requires_grad=learn_mean)
            self.bias_rho = nn.Parameter(torch.log(torch.expm1(torch.ones(out_features, **factory_kwargs))),
                                         requires_grad=learn_std)

        self.learn_mean = learn_mean
        self.learn_std = learn_std

        self._bias = bias

        self.prior_weight_mean = prior_weight_mean.to(**factory_kwargs) if prior_weight_mean is not None else None
        self.prior_weight_std = prior_weight_std.to(**factory_kwargs) if prior_weight_std is not None else None
        self.prior_bias_mean = prior_bias_mean.to(**factory_kwargs) if prior_bias_mean is not None else None
        self.prior_bias_std = prior_bias_std.to(**factory_kwargs) if prior_bias_std is not None else None

    def build_from(self, linear: nn.Linear):
        self.weight_mean = nn.Parameter(torch.zeros_like(self.weight_mean).copy_(linear.weight), 
                                        requires_grad=self.learn_mean)

        if linear.bias is not None:
            self._bias = True
            self.bias_mean = nn.Parameter(torch.zeros_like(self.bias_mean).copy_(linear.bias), 
                                          requires_grad=self.learn_mean)

    def forward(self, x):
        return F.linear(x, self.weight, self.bias)

