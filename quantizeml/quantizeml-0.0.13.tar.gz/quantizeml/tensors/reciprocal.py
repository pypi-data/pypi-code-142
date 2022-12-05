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
import numpy as np
from typing import Union
from .qtensor import pow2
from .fixed_point import FixedPoint
from .lookup import RegisterCustomHashTable

QTENSOR_T = Union[FixedPoint, tf.Tensor]


def _get_static_hash_table(range_bitwidth: int, frac_bits: int):
    """Given an input range bitwitdh, register a static hash table which contains
    the reciprocal values between (-2**range_bitwidth) and (2**range_bitwidth - 1).

    Args:
        range_bitwidth (int): the bitwidth of the range of the table.
        frac_bits (int): the resolution of fractional bits.

    Returns:
        :obj:`tf.lookup.StaticHashTable`: the static hash table.
    """
    def _serialize_hash_table():
        # Given that StaticHashTable does not support Tensor, all the values are computed in
        # numpy directly.
        keys_tensor = np.array(range(1, 2**range_bitwidth), dtype=np.int32)
        vals_tensor = np.floor(1 / keys_tensor * 2.0 ** frac_bits).astype(np.float32)
        return keys_tensor, vals_tensor, 0

    # Register the table if it does not exist as a global variable
    table_name = f'reciprocal_lut_{frac_bits}_{range_bitwidth}bits'
    with RegisterCustomHashTable(table_name, _serialize_hash_table) as register:
        table = register.get_table()
    return table


def reciprocal_lut(
        x: QTENSOR_T, frac_bits: int = None, out_value_bits: int = 32, name: str = None):
    """Compute the reciprocal of a FixedPoint value, using a lookup table.

    Args:
        x (:obj:`FixedPoint` or :obj:`tf.Tensor`): the value to compute its reciprocal.
        frac_bits (int, optional): the resolution of fractional bits. Defaults to None.
        out_value_bits (int, optional): the number of bits of the output. Defaults to 32.
        name (str, optional): the name of the operation. Defaults to None.

    Returns:
        :obj:`FixedPoint` or :obj:`tf.Tensor`: the reciprocal of x.
    """
    # Retrieves the reciprocal lookup table only if x is a FixedPoint
    if not isinstance(x, FixedPoint):
        return tf.math.reciprocal(x)

    # Retrieves the hash static table of x.value_bits
    frac_bits = frac_bits or x.frac_bits
    hash_table = _get_static_hash_table(x.value_bits, frac_bits)

    # Given that the input is a FixedPoint, it is guarantee the equivalence below:
    # float(1/x) = 1 / float(x) =  1/x.values * 2^x.frac_bits
    # Then, we can approximate the reciprocal of x to:
    # float(1/x) ~= reciprocal_lut(x.values) * 2^x.frac_bits
    # in two steps:
    # 1. Compute the reciprocal of x.values of absolute value
    x_inv = FixedPoint(hash_table(x.abs().values), frac_bits, out_value_bits)
    # 2. Scale by 2**x.frac_bits
    return x_inv * FixedPoint(pow2(x.frac_bits)) * x.sign
