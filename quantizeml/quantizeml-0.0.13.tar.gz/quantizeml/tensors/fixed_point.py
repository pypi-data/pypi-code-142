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

from .qtensor import QTensor, round_through, floor_through, pow2, ceil_log2
from ..debugging import assert_equal, assert_none_equal, assert_less, assert_less_equal


class FixedPoint(QTensor):
    """A Tensor of integer values representing fixed-point numbers

    Args:
        values (:obj:`tensorflow.Tensor`): a tensor of integer values
        frac_bits (:obj:`tensorflow.Tensor`, optional): an integer tensor of
            fractional bits. Defaults to 0.
        value_bits (int, optional): the number of value bits. Defaults to 32.
    """
    frac_bits: tf.Tensor = 0.

    def __init__(self, values, frac_bits=0, value_bits=32):
        # We store fractional bits in a float tensor to speed up calculations
        if isinstance(frac_bits, tf.Tensor):
            self.frac_bits = tf.cast(frac_bits, tf.float32)
        else:
            self.frac_bits = tf.convert_to_tensor(frac_bits, tf.float32)
        assert_less_equal(0, self.frac_bits, "The frac_bits must be positive.")
        self.value_bits = value_bits
        # We store integer values in a float tensor to speed up calculations
        if isinstance(values, tf.Tensor):
            values = tf.cast(values, tf.float32)
        else:
            values = tf.convert_to_tensor(values, dtype=tf.float32)
        # Clamp to fixed-point boundaries
        self.values = QTensor.clamp(values, value_bits)
        self.shape = self.values.shape

    @property
    def per_tensor(self):
        return tf.rank(self.frac_bits) == 0

    @staticmethod
    def quantize(x, value_bits, frac_bits=None):
        r"""Converts a float Tensor to a FixedPoint

        It converts the original float values into integer values so that:

        .. math:: {x_{int}} = round(x * 2^{frac\_bits})

        Note: 2^-frac_bits represents the FixedPoint precision.

        Before returning, the resulting integer values are clipped to the
        maximum integer values that can be stored for the specified value bits:

            [-2^value_bits, 2^value_bits - 1]

        If frac_bits is not specified, the method starts by evaluating the number
        of bits to dedicate to represent the integer part of the float tensor,
        clipped to value_bits:

        .. math:: int_bits = ceil(log2(x))

        Note: this number can be negative when x < 1.

        It then evaluates the offset of the least significant bit of the fractional
        part of the float starting from zero. This represents the fractional bits:

        .. math:: frac_bits = value_bits - int_bits

        Args:
            x (:obj:`tensorflow.Tensor`): a tensor of float values.
            value_bits (int): the number of value bits
            frac_bits (:obj:`tensorflow.Tensor`, optional): an integer tensor of fractional bits.
                Defaults to None.

        Returns:
            a :obj:`FixedPoint`
        """
        if frac_bits is None:
            if isinstance(x, int) or tf.reduce_all(x == tf.math.round(x)):
                # The input does not need to be quantized
                frac_bits = 0
            else:
                # Evaluate integer bits
                int_bits = ceil_log2(tf.abs(x))
                frac_bits = tf.maximum(0, value_bits - int_bits)
        # Project float into integer fixed-point space
        values = round_through(x * pow2(frac_bits))
        return FixedPoint(values, frac_bits, value_bits)

    @property
    def sign(self):
        """Returns the sign of the FixedPoint

        Returns:
            :obj:`FixedPoint`: the sign as a FixedPoint.
        """
        return FixedPoint(tf.math.sign(self.values), 0, self.value_bits)

    def to_float(self):
        return self.values / pow2(self.frac_bits)

    def promote(self, bits):
        """Increase the number of value bits

        Args:
            bits (int): the new number of value bits

        Returns:
            :obj:`FixedPoint`: a FixedPoint with increased value bits
        """
        if not isinstance(bits, int):
            raise TypeError("Bitwidth must be an integer")
        if bits < 0:
            raise ValueError("Invalid bitwidth")
        if bits < self.value_bits:
            raise ValueError(f"Cannot reduce value bits from {self.value_bits} to {bits}: "
                             "use a quantizer instead")
        return FixedPoint(self.values, self.frac_bits, bits)

    def align(self, other=None):
        """Align fractional bits

        This returns an equivalent FixedPoint with a scalar fractional bit
        corresponding to the maximum of:

            - the initial fractional bits on all channels,
            - when specified, the other FixedPoint fractional bits on all channels.

        This is required before performing an operation that adds or subtracts
        elements along the last dimension, to make sure all these elements are
        in the same scale.

        Args:
            other(:obj:`FixedPoint`): a FixedPoint to align to

        Returns:
            tuple(:obj:`FixedPoint`, :obj:`tf.Tensor`): a new FixedPoint with aligned
                fractional bits and the shift that was applied.
        """
        max_frac_bits = tf.reduce_max(self.frac_bits)
        if other is not None:
            if not isinstance(other, FixedPoint):
                raise ValueError("Other must be a FixedPoint")
            max_frac_bits = tf.math.maximum(max_frac_bits, tf.reduce_max(other.frac_bits))
        shift = max_frac_bits - self.frac_bits
        assert_less(shift, self.value_bits, "Cannot align the FixedPoint as it saturates its "
                    f"{self.value_bits}-bit buffer.")
        values = FixedPoint._lshift(self.values, shift)
        return FixedPoint(values, max_frac_bits, self.value_bits), shift

    def downscale(self, frac_bits, value_bits):
        """Encode a FixedPoint with a lower bitwidth

        It applies a left/right shift to the source FixedPoint values to align
        them on the target maximum fractional bits.

        It then clips them to the boundaries specified by the target value bits.

        Args:
            frac_bits (:obj:`tensorflow.Tensor`): the target fractional bits
            value_bits (int): the target value bits

        Returns:
            a :obj:`FixedPoint`
        """
        if value_bits > self.value_bits:
            raise ValueError(
                f"Cannot increase value bits from {self.value_bits} to {value_bits}:"
                "use a promotion instead")
        frac_bits = tf.cast(frac_bits, tf.float32)
        # Evaluate the shift to apply to reach the target precision
        shift = frac_bits - self.frac_bits
        assert_less(tf.abs(shift), self.value_bits, "Cannot downscale the FixedPoint as it "
                    f"saturates its {self.value_bits}-bit buffer.")
        # The shift can be positive (left-shift) or negative (right-shift)
        # In float it can be simulated by flooring after multiplying by the
        # positive/negative shift PoT:
        # - for positive shift, the results are integer and can safely be floored,
        # - for negative shift, flooring simulates a right_shift.
        values = floor_through(self.values * pow2(shift) + 0.5)
        # return a new FixedPoint with the target precision and bitwidth
        return FixedPoint(values, frac_bits, value_bits), shift

    @staticmethod
    def _rshift(values, shift):
        return floor_through(values / pow2(shift))

    @staticmethod
    def _lshift(values, shift):
        return values * pow2(shift)

    def shift(self, s):
        """Apply a tensor-wide left or right shift.

        This takes a tensor of shift values and apply them on each item of the
        FixedPoint values.

        The shift values should positive or negative integer:

        - if the value is positive, it is a left-shift,
        - if the value is negative, it is a right-shift.

        The resulting FixedPoint has the same value bits and fractional bits as
        the source FixedPoint, which means that clipping is applied on
        left-shift and flooring is applied on right-shift.

        Args:
            s (:obj:`tensorflow.Tensor`): the shift values for each pixel.

        Returns:
            :obj:`FixedPoint`: the result as a FixedPoint
        """
        values = floor_through(self.values * pow2(s))
        return FixedPoint(values, self.frac_bits, self.value_bits)

    def __rshift__(self, shift):
        """Right shift the FixedPoint values

        This operation has no direct equivalent in float arithmetics: it corresponds to a division
        of the corresponding float by a power-of-two, then a flooring to the quantization interval.

        Args:
            shift (:obj:`tensorflow.Tensor`): the power of 2 to divide by

        Returns:
            :obj:`FixedPoint`: the result as a FixedPoint
        """
        shift = tf.cast(shift, tf.float32)
        assert_less_equal(0, shift, "Shift must be all positive")
        assert_equal(tf.rank(shift) <= tf.rank(self.frac_bits), True,
                     "The shift's rank must be less than or equal to the rank of frac_bits. "
                     f"Received {tf.rank(shift)} > {tf.rank(self.frac_bits)}."
                     "That means it is not possible to fold the shift into the FixedPoint. "
                     "Please use FixedPoint.shift instead of '>>'.")

        # The shift can be folded into the fractional bits,
        s_frac_bits = self.frac_bits + shift
        # keeping the same values
        s_values = self.values
        # Return a new FixedPoint with updated fractional bits,
        # which is equivalent in hardward without performing any operation
        return FixedPoint(s_values, s_frac_bits, self.value_bits)

    def __lshift__(self, shift):
        """Left shift the FixedPoint values

        This operation has no direct equivalent in float arithmetics: it corresponds to a
        multiplication of the corresponding float by a power-of-two, then a flooring to the
        quantization interval.

        Args:
            shift (:obj:`tensorflow.Tensor`): the power of 2 to multiply by

        Returns:
            :obj:`FixedPoint`: the result as a FixedPoint
        """
        assert_less_equal(0, shift, "Shift must be all positive")
        # Simply apply the shift on the values
        s_values = FixedPoint._lshift(self.values, shift)
        # Return a new FixedPoint with updated values
        return FixedPoint(s_values, self.frac_bits, self.value_bits)

    def _align_values(self, other):
        # The sub fractional bits are the max of both terms
        frac_bits = tf.math.maximum(self.frac_bits, other.frac_bits)
        self_values = FixedPoint._lshift(
            self.values, (frac_bits - self.frac_bits))
        other_values = FixedPoint._lshift(
            other.values, (frac_bits - other.frac_bits))
        return frac_bits, self_values, other_values

    def __add__(self, other):
        if isinstance(other, int):
            # Convert integer into a 32-bit fixed-point with no fractional bits,
            # aligned with the current FixedPoint
            return self + FixedPoint.quantize(other, 32, self.frac_bits)
        elif isinstance(other, FixedPoint):
            # Check that self and other are per-tensor
            self.assert_per_tensor()
            other.assert_per_tensor()
            # Check that self and other are aligned
            assert_equal(self.frac_bits, other.frac_bits)
            # Return a new FixedPoint
            return FixedPoint(self.values + other.values, self.frac_bits, self.value_bits)
        raise TypeError(
            f"Unsupported operand type(s) for +: 'FixedPoint' and '{type(other)}'")

    def __sub__(self, other):
        if isinstance(other, int):
            # Convert integer into a 32-bit fixed-point with no fractional bits,
            # aligned with the current FixedPoint
            return self - FixedPoint.quantize(other, 32, self.frac_bits)
        elif isinstance(other, FixedPoint):
            # Check that self and other are per-tensor
            self.assert_per_tensor()
            other.assert_per_tensor()
            # Check that self and other are aligned
            assert_equal(self.frac_bits, other.frac_bits)
            # Return a new FixedPoint
            return FixedPoint(self.values - other.values, self.frac_bits, self.value_bits)
        raise TypeError(
            f"Unsupported operand type(s) for -: 'FixedPoint' and '{type(other)}'")

    def __mul__(self, other):
        if isinstance(other, int):
            return self * FixedPoint(other)
        elif isinstance(other, FixedPoint):
            # The product between fixed-point is straight-forward
            p_values = self.values * other.values
            # Return a new FixedPoint whose frac bits is the sum of both terms
            return FixedPoint(p_values, self.frac_bits + other.frac_bits, self.value_bits)
        raise TypeError(
            f"Unsupported operand type(s) for *: 'FixedPoint' and '{type(other)}'")

    def __truediv__(self, other):
        if isinstance(other, int):
            return self / FixedPoint(other)
        elif isinstance(other, FixedPoint):
            assert_none_equal(other.values, 0.0, "Cannot divide by 0.")
            # The division between fixed-point is straight-forward
            d_values = floor_through(self.values / other.values)
            # Return a new FixedPoint whose frac bits from other is subtracted.
            return FixedPoint(d_values, self.frac_bits - other.frac_bits, self.value_bits)
        raise TypeError(
            f"Unsupported operand type(s) for /: 'FixedPoint' and '{type(other)}'")

    def __pow__(self, power):
        if isinstance(power, int):
            if power == 0:
                return FixedPoint(tf.ones_like(self.values), 0, self.value_bits)
            elif power == 1:
                return FixedPoint(self.values, self.frac_bits, self.value_bits)
            elif power > 1:
                return self * self ** (power - 1)
            else:
                raise NotImplementedError(
                    "Negative powers are not implemented yet")
        raise TypeError(
            f"Unsupported operand type(s) for **: 'FixedPoint' and '{type(power)}'")

    def __gt__(self, other):
        if not isinstance(other, FixedPoint):
            raise TypeError(
                f"Unsupported operand type(s) for >: 'FixedPoint' and '{type(other)}'")
        _, s_values, o_values = self._align_values(other)
        return s_values > o_values

    def __ge__(self, other):
        if not isinstance(other, FixedPoint):
            raise TypeError(
                f"Unsupported operand type(s) for >=: 'FixedPoint' and '{type(other)}'")
        _, s_values, o_values = self._align_values(other)
        return s_values >= o_values

    def __eq__(self, other):
        if not isinstance(other, FixedPoint):
            raise TypeError(
                f"Unsupported operand type(s) for ==: 'FixedPoint' and '{type(other)}'")
        _, s_values, o_values = self._align_values(other)
        return s_values == o_values

    def __ne__(self, other):
        if not isinstance(other, FixedPoint):
            raise TypeError(
                f"unsupported operand type(s) for !=: 'FixedPoint' and '{type(other)}'")
        _, s_values, o_values = self._align_values(other)
        return s_values != o_values

    def __lt__(self, other):
        if not isinstance(other, FixedPoint):
            raise TypeError(
                f"Unsupported operand type(s) for <: 'FixedPoint' and '{type(other)}'")
        _, s_values, o_values = self._align_values(other)
        return s_values < o_values

    def __le__(self, other):
        if not isinstance(other, FixedPoint):
            raise TypeError(
                f"Unsupported operand type(s) for <=: 'FixedPoint' and '{type(other)}'")
        _, s_values, o_values = self._align_values(other)
        return s_values <= o_values

    def abs(self):
        """Returns the absolute value of the FixedPoint

        Returns:
            :obj:`FixedPoint`: the absolute value.
        """
        return FixedPoint(tf.math.abs(self.values), self.frac_bits, self.value_bits)

    def floor(self):
        """Floors the FixedPoint

        Returns:
            tuple(:obj:`FixedPoint`, :obj:`tf.Tensor`): a new FixedPoint without
                fractional bits and the shift that was applied.
        """
        # Divide values to remove fractional bits
        values = FixedPoint._rshift(self.values, self.frac_bits)
        return FixedPoint(values, 0, self.value_bits), self.frac_bits
