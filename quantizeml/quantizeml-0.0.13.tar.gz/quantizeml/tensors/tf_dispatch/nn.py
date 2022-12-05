#!/usr/bin/env python
# ******************************************************************************
# Copyright 2022 Brainchip Holdings Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ******************************************************************************
import tensorflow as tf
import keras

from ...debugging import assert_rank_at_least
from ..qtensor import QTensor
from ..fixed_point import FixedPoint
from ..qfloat import QFloat


@tf.experimental.dispatch_for_api(tf.linalg.matmul)
def fp_matmul(a: FixedPoint,
              b: QTensor,
              transpose_a=False,
              transpose_b=False,
              adjoint_a=False,
              adjoint_b=False,
              a_is_sparse=False,
              b_is_sparse=False,
              output_type=None,
              name=None):
    """Multiplies matrix `a` by matrix `b`, producing `a` * `b`.

    A `tf.Tensor` of the same type as `a` and `b` where each inner-most matrix
    is the product of the corresponding matrices in `a` and `b`, e.g. if all
    transpose or adjoint attributes are `False`:
    `output[..., i, j] = sum_k (a[..., i, k] * b[..., k, j])`,
    for all indices `i`, `j`.

    Note: This is matrix product, not element-wise product.


    Args:
        a (:obj:`FixedPoint`): a FixedPoint of rank > 1.
        b (:obj:`FixedPoint`): a FixedPoint with same rank as `a`.
        transpose_a (bool, optional): if `True`, `a` is transposed before multiplication.
            Defaults to False.
        transpose_b (bool, optional): if `True`, `b` is transposed before multiplication.
            Defaults to False.
        adjoint_a (bool, optional): if `True`, `a` is conjugated and transposed before
            multiplication. Defaults to False.
        adjoint_b (bool, optional): if `True`, `b` is conjugated and transposed before
            multiplication. Defaults to False.
        a_is_sparse (bool, optional): must be False, argument kept for compatibility with
            original tf.matmul. Defaults to False.
        b_is_sparse (bool, optional): must be False, argument kept for compatibility with
            original tf.matmul. Defaults to False.
        output_type (NoneType, optional): must be None, argument kept for compatibility
            with original tf.matmul. Defaults to None.
        name (str, optional): the name for the operation. Defaults to None.

    Returns:
        :obj:`FixedPoint`: the multiplied FixedPoint.
    """
    if a_is_sparse:
        raise TypeError(
            f"Unsupported argument: a_is_sparse, provided {a_is_sparse}")
    if b_is_sparse:
        raise TypeError(
            f"Unsupported argument: b_is_sparse, provided {b_is_sparse}")
    if output_type is not None:
        raise TypeError(
            f"Unsupported argument: output_type, provided {output_type}")

    # We don't support matmul between vectors
    assert_rank_at_least(a.values, 2)
    assert_rank_at_least(b.values, 2)

    # Since the last dimension is collapsed by the matmul, (a,b) must be quantized per-tensor
    if not transpose_a:
        a.assert_per_tensor()
    if transpose_b:
        b.assert_per_tensor()

    if isinstance(b, FixedPoint):
        b_frac_bits = b.frac_bits
    else:
        b_frac_bits = b.scales.frac_bits

    # Do matmul on values
    m_values = tf.matmul(a.values, b.values, transpose_a, transpose_b, adjoint_a, adjoint_b, name)
    if isinstance(b, QFloat):
        # Multiply by the scales
        m_values *= b.scales.values

    # Return a new FixedPoint
    return FixedPoint(m_values, a.frac_bits + b_frac_bits, a.value_bits)


@tf.experimental.dispatch_for_api(keras.backend.depthwise_conv2d)
def fp_depthwise_conv2d(x: FixedPoint,
                        depthwise_kernel: QFloat,
                        strides=(1, 1),
                        padding='valid',
                        data_format=None,
                        dilation_rate=(1, 1)):
    """ 2D convolution with separable filters.

    Args:
        x (obj:`FixedPoint`): input tensor.
        depthwise_kernel (:obj:`QFloat`): convolution kernel for the depthwise convolution.
        strides (tuple, optional): strides tuple (length 2). Defaults to (1, 1).
        padding (str, optional): `"same"` or `"valid"`. Defaults to 'valid'.
        data_format (str, optional): `"channels_last"` or `"channels_first"`. Defaults to None.
        dilation_rate (tuple, optional): tuple of integers, dilation rates for the separable
            convolution. Defaults to (1, 1).

    Returns:
        :obj:`FixedPoint`: output tensor.

    """
    # Unlike other convolutions, the depthwise does not require its inputs to
    # be quantized per-tensor as the input channels are processed independently

    # Do convolution on values
    conv_values = keras.backend.depthwise_conv2d(x.values, depthwise_kernel.values, strides,
                                                 padding, data_format, dilation_rate)
    # Multiply by the scales
    conv_values *= depthwise_kernel.scales.values

    # Return a new FixedPoint
    filters_frac_bits = depthwise_kernel.scales.frac_bits
    return FixedPoint(conv_values, x.frac_bits + filters_frac_bits, x.value_bits)


@tf.experimental.dispatch_for_api(tf.nn.convolution)
def fp_convolution(
        input: FixedPoint,
        filters: QFloat,
        strides=None, padding="VALID", data_format=None, dilations=None, name=None):
    """Perform the convolution operation between input and filter tensors.

    Args:
        input (:obj:`FixedPoint`): The input FixedPoint.
        filters (:obj:`QFloat`): The filters Qtensor.
        strides (list, optional): Sequence of N ints >= 1.  Specifies the output stride.
        padding (str, optional): A string, either `"VALID"` or `"SAME"`. The padding algorithm.
            Defaults to "VALID"
        data_format (str, optional): Specifies whether the channel dimension of
            the `input` and output is the last dimension (default, or if `data_format`
            does not start with "NC"), or the second dimension (if `data_format`
            starts with "NC").  For N=1, the valid values are "NWC" (default) and
            "NCW".  For N=2, the valid values are "NHWC" (default) and "NCHW".
            For N=3, the valid values are "NDHWC" (default) and "NCDHW".
        dilations (list, optional): Alias for dilation_rate. Sequence of N ints >= 1.
            Specifies the filter upsampling/input downsampling rate. Defaults to None.
        name (str, optional): the name for the Tensorflow ops. Defaults to None.

    Returns:
        :obj:`FixedPoint`: a FixedPoint containing the output values.
    """
    # Input must be quantized per-tensor because the products are eventually summed
    input.assert_per_tensor()

    # Do convolution on values
    conv_values = tf.nn.convolution(input.values, filters.values, strides, padding, data_format,
                                    dilations, name)
    # Multiply by the scales
    conv_values *= filters.scales.values

    # Return a new FixedPoint
    filters_frac_bits = filters.scales.frac_bits
    return FixedPoint(conv_values, input.frac_bits + filters_frac_bits, input.value_bits)
