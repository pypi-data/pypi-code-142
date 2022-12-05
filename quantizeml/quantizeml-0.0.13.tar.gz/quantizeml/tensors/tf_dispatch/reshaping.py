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
from typing import List

from ..fixed_point import FixedPoint


@tf.experimental.dispatch_for_api(tf.shape)
def fp_shape(input: FixedPoint, out_type=tf.dtypes.int32, name=None):
    return tf.shape(input.values, out_type, name)


@tf.experimental.dispatch_for_api(tf.reshape)
def fp_reshape(tensor: FixedPoint, shape, name=None):
    tensor.assert_per_tensor()
    output = tf.reshape(tensor.values, shape, name)
    return FixedPoint(output, tensor.frac_bits, tensor.value_bits)


@tf.experimental.dispatch_for_api(tf.transpose)
def fp_transpose(a: FixedPoint, perm=None, conjugate=False, name="transpose"):
    a.assert_per_tensor()
    output = tf.transpose(a.values, perm, conjugate, name)
    return FixedPoint(output, a.frac_bits, a.value_bits)


@tf.experimental.dispatch_for_api(tf.broadcast_to)
def fp_brodcast_to(input: FixedPoint, shape, name=None):
    """Broadcast a FixedPoint tensor for a compatible shape.

    Args:
        input (:obj:`FixedPoint`): a FixedPoint to broadcast.
        shape (:obj:`tf.Tensor`): an 1-D `int` Tensor representing
            the shape of the desired output. Must be one of the
            following types: `int32`, `int64`.
        name (str, optional): a name for the operation. Defaults to None.

    Returns:
        :obj:`FixedPoint`: the brodcasted output. Has the same
            type as `input`.
  """
    # Check first that the last dimension is unchanged
    tf.assert_equal(input.shape[-1], shape[-1], message="To brodcast FixedPoint input,\
                        last dimension should remain unchanged")
    output = tf.broadcast_to(input.values, shape, name)
    return FixedPoint(output, input.frac_bits, input.value_bits)


@tf.experimental.dispatch_for_api(tf.concat)
def fp_concat(values: List[FixedPoint], axis, name="concat"):
    """Concatenates FixedPoint tensors along one dimension.

    Args:
        values (List of :obj:`FixedPoint`): List of FixedPoint tensors
            to concatenate.
        axis (list): Dimension along which to concatenate.
        name (str, optional): the name for the Tensorflow ops.
            Defaults to "concat".

    Returns:
        :obj:`FixedPoint`: the concatenate output FixedPoint.
    """
    if len(values) == 1:
        return FixedPoint(values[0].values, values[0].frac_bits, values[0].value_bits)

    # For now we only support concatenation of one or two elements
    tf.assert_equal(
        len(values),
        2, f"We only support concatenation of one or two FixedPoint. \
           Receives {len(values)} tensors as input.")

    # For now we don't support concatenation over last dimension
    rank_input = tf.rank(values[0].values)
    if axis < 0:
        dim = axis + rank_input
    else:
        dim = axis
    tf.Assert(tf.math.not_equal(dim, rank_input - 1),
              ['we do not support concatenation over last axis. axis is:', axis])

    # FixedPoint tensors to concatenate should be per-tensor
    values[0].assert_per_tensor()
    values[1].assert_per_tensor()

    tf.assert_equal(values[0].frac_bits, values[1].frac_bits, message=f"the two\
            FixedPoint must have the same frac_bits. Receives {values[0].frac_bits}\
            and {values[1].frac_bits}")
    values_out = tf.concat([values[0].values, values[1].values], axis, name)

    return FixedPoint(
        values_out, values[0].frac_bits, max(
            values[0].value_bits, values[1].value_bits))


@tf.experimental.dispatch_for_api(tf.expand_dims)
def fp_expand_dims(input: FixedPoint, axis, name=None):
    """Returns a tensor with a length 1 axis inserted at index `axis`.

    Args:
        input (FixedPoint): a `Tensor`.
        axis (int): integer specifying the dimension index at which to expand the shape of `input`.
            Given an input of D dimensions, `axis` must be in range `[-(D+1), D]` (inclusive).
        name (str, optional): name of the output `Tensor`. Defaults to None.

    Returns:
        FixedPoint: a tensor with the same data as `input`, with an additional dimension inserted at
            the index specified by `axis`.
    """
    # Only support per-tensor inputs
    input.assert_per_tensor()

    # Expand dimension on values
    values = tf.expand_dims(input.values, axis, name)

    # Return a new FixedPoint
    return FixedPoint(values, input.frac_bits, input.value_bits)


@tf.experimental.dispatch_for_api(tf.compat.v1.gather)
def fp_gather(params: FixedPoint, indices, validate_indices=None,
              name=None, axis=None, batch_dims=0):
    """Gather slices from params along axis.

    Args:
        params (:obj:`FixedPoint`, :obj:`QFloat`): the input QTensor.
        indices (int, list): the indices to gather.
        validate_indices (bool, optional): whether to validate the indices. Defaults to None.
        name (str, optional): the name for the Tensorflow ops. Defaults to None.
        axis (int, optional): the axis to gather along. Defaults to None.
        batch_dims (int, optional): the number of batch dimensions to keep. Defaults to 0.

    Returns:
        :obj:`QTensor`: a QTensor containing the gathered values.
    """
    # We do not support gather along the last axis if the QTensor is per-axis
    if axis in (-1, len(params.shape)):
        params.assert_per_tensor()
    # Create a new QTensor, gather the indices in a desired axis
    x_gather = tf.gather(params.values, indices, validate_indices, axis, batch_dims, name)
    return FixedPoint(x_gather, params.frac_bits, params.value_bits)
