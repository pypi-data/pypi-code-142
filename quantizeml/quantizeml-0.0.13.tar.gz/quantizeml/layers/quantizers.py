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
from contextlib import contextmanager
import tensorflow as tf
import keras.backend as K
from keras.layers import Layer

from ..tensors import QTensor, QFloat, FixedPoint, ceil_log2
from .calibrable import Calibrable, CalibrableVariable


__all__ = ["deserialize_quantizer", "Quantizer", "Dequantizer", "WeightQuantizer",
           "OutputQuantizer"]


def deserialize_quantizer(quant_config, name, quantizer_class, mandatory=True):
    """Wrapper function of tf.keras.utils.deserialize_keras_object.

    It allows to select the right config from the config file dict,
    and raises an error if no config found or set to None.
    If one is found, it returns the corresponding deserialized Quantizer.

    Args:
        quant_config (dict): quantization config dictionnary.
        name (str): keras object name to deserialize.
        quantizer_class (object): the Quantizer subclass to instantiate.
        mandatory (bool, optional): flag to specify if the object to
            deserialize is mandatory. If yes raises an Error otherwise
            returns None. Defaults to True.

    Returns:
        :obj:`Quantizer`: the targeted deserialized Quantizer
        object.
    """
    object_dict = quant_config.get(name)
    if object_dict is None:
        if mandatory:
            raise KeyError(f"'{name}' should be specified.")
        return None

    # Check that object_dict has the right keys
    list_available_keys = {
        "trainable": bool,
        "bitwidth": int,
        "signed": bool,
        "axis": str,
        "momentum": float,
        "dtype": str,
        "scale_bits": int
    }
    for key in object_dict:
        if key == "scale_bits" and quantizer_class == OutputQuantizer:
            raise ValueError(f"'{name}' produces FixedPoint output. "
                             "It doesn't support 'scale_bits' key.")
        if key not in list_available_keys:
            raise KeyError(f"'{key}' is not a valid key for '{name}'.")
        if not isinstance(object_dict[key], list_available_keys[key]):
            raise ValueError(f"'{key}' should be of type {list_available_keys[key]}. "
                             f"Received {type(object_dict[key])}.")

    # Deserialize the object
    deserialize_dict = object_dict.copy()
    deserialize_dict["name"] = name
    return quantizer_class.from_config(deserialize_dict)


@contextmanager
def disable_partitioner(layer):
    partitioner = None
    try:  # Disable variable partitioning when creating the moving tensors
        if hasattr(layer, "_scope") and layer._scope:
            partitioner = layer._scope.partitioner
            layer._scope.set_partitioner(None)
        yield layer
    finally:  # Restore partitioner
        if partitioner:
            layer._scope.set_partitioner(partitioner)


class Quantizer(Layer):
    """The base class for all quantizers.

    The bitwidth defines the number of quantization levels on which the
    values will be quantized.
    For a quantizer that accepts unsigned values, the maximum quantization
    level is 2 ^ bitwidth - 1.
    For a quantizer that accepts signed values, we lose one bit of precision to
    store the sign.
    When the quantizer is signed, the quantization interval is asymmetric around
    zero (i.e range: [- 2 ^ (bitwidth - 1), 2 ^ (bitwidth - 1) - 1]).
    The quantization is actually performed on absolute values, between 0 and
    max_value, where:

    - max_value is either a scalar (per-tensor quantization), or a vector
      (per-axis quantization),
    - max_value is a static value on inference, and an adaptative value on training.

    Args:
        bitwidth (int): the quantization bitwidth.
        signed (bool, optional): whether the quantizer expects signed values or unsigned.
            Defaults to True.
        axis (str, optional): reduce across all tensor values ('per-tensor') or keep the
            last axis ('per-axis'). Defaults to 'per-tensor'.

    Note:
        To get more information about the moving average implementation, see the
        `BatchNormalizationLayer <https://bit.ly/3KcEaUh>`_ class.
    """

    def __init__(self, bitwidth, signed=True, axis="per-tensor", **kwargs):
        assert bitwidth > 1
        self.bitwidth = bitwidth
        self.signed = signed
        self.value_bits = bitwidth - 1 if signed else bitwidth
        self._axis = axis
        if not (isinstance(axis, str) and axis in ["per-tensor", "per-axis"]):
            raise ValueError(
                f"Only support reduction 'per-tensor' or 'per-axis'. Given {axis}.")
        super().__init__(**kwargs)

    def build(self, input_shape):
        """Build the layer.

        Args:
            input_shape (list): the shape of input tensor.
        """
        # Convert axis to a list of int
        if self._axis == "per-axis" and len(input_shape) > 1:
            self.axis = list(range(len(input_shape) - 1))
        else:
            self.axis = None

    def frac_bits(self, max_value):
        # Clamp the max_value to the next power-of-two
        int_bits = tf.cast(ceil_log2(max_value), tf.int32)
        int_bits = tf.clip_by_value(int_bits, 0, self.value_bits)
        # Evaluate fractional bits
        return self.value_bits - int_bits

    def get_config(self):
        """Get the config of the layer.

        Returns:
            dict: the config of the layer.
        """
        config = super().get_config()
        config.update({"bitwidth": self.bitwidth})
        config.update({"signed": self.signed})
        config.update({"axis": self._axis})
        return config


@tf.keras.utils.register_keras_serializable()
class WeightQuantizer(Quantizer):
    """A trivial uniform quantizer that has only one scale for everything.

    Scale is dynamic (depends on inputs), and it can be read via the scale property.

    Args:
        bitwidth (int): the quantization bitwidth.
        scale_bits (int, optional): the number of bits for the scaling. Defaults to None.
    """

    def __init__(self, bitwidth, scale_bits=None, **kwargs):
        if not isinstance(bitwidth, int) or bitwidth < 2:
            raise ValueError(
                f"Bitwidth should be an int >= 2, currently {bitwidth}")
        self.scale_bits = scale_bits
        super().__init__(bitwidth, **kwargs)

    def call(self, inputs, training=None):
        """Update the max_value from the new inputs, and quantize them in three steps:

            1. Check if the inputs are float values,
            2. Compute the max_value,
            3. Quantize the inputs.

        Args:
            inputs (:obj:`tensorflow.Tensor` or :obj:`QTensor`): the inputs tensor.
            training (bool, optional): the training mode. Defaults to None.

        Returns:
            :obj:`tensorflow.Tensor`: the quantized tensor.
        """
        if isinstance(inputs, QTensor):
            raise ValueError(
                f"{type(inputs)} input is not supported. WeightQuantizer only accepts float"
                " inputs.")

        # Compute the max_value from the inputs
        max_value = tf.math.reduce_max(tf.math.abs(inputs), self.axis)
        # Return a QFloat if scale_bits provided
        if self.scale_bits:
            float_max = tf.stop_gradient(max_value)
            return QFloat.quantize(inputs, float_max, self.value_bits, self.scale_bits)
        # Return a FixedPoint if no scale_bits provided
        frac_bits = tf.stop_gradient(self.frac_bits(max_value))
        return FixedPoint.quantize(inputs, self.value_bits, frac_bits)

    def get_config(self):
        """Get the config of the layer.

        Returns:
            dict: the config of the layer.
        """
        config = super().get_config()
        config.update({"scale_bits": self.scale_bits})
        return config


@tf.keras.utils.register_keras_serializable()
class OutputQuantizer(Calibrable, Quantizer):
    """A uniform quantizer that aligns its quantization range to a Power-of-two.
    Its max_value is updated during the calibration by the moving average algorithm,
    inspired by the BatchNormalizationLayer moving average algorithm.

    Args:
        bitwidth (int): the quantization bitwidth.
        signed (bool): whether the quantizer expects signed values or unsigned.
        momentum (float, optional): the momentum for the moving average. Defaults to 0.9.

    Note:
        To get more information about the moving average implementation, see the
        `BatchNormalizationLayer <https://bit.ly/3KcEaUh>`_ class:
    """

    def __init__(self, momentum=0.9, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.momentum = momentum
        # Add object that will store the shift values.
        self.shift = CalibrableVariable()

    def build(self, input_shape):
        """Build the layer.

        Args:
            input_shape (list): the shape of input tensor.
        """
        super().build(input_shape)

        # Declares the constant/vector that will store the maximum values of the input.
        with disable_partitioner(self):
            self.max_value = self.add_weight(
                name="max_value",
                shape=input_shape[-1] if self.axis is not None else (),
                dtype=tf.float32,
                initializer="ones",
                synchronization=tf.VariableSynchronization.ON_READ,
                trainable=False,
                aggregation=tf.VariableAggregation.MEAN,
                experimental_autocast=False,
            )

    @staticmethod
    def _assign_new_value(variable, value):
        """Given a variable, assign a new value to it. Function taken of
        `BatchNormalizationLayer <https://bit.ly/3v0gzll>`_ code.

        Args:
            variable (:obj:`tensorflow.Variable`): the variable to assign.
            value (:obj:`tensorflow.Tensor`): the new value to assign.

        Returns:
            :obj:`tensorflow.Tensor`: the new value of the variable.
        """
        with K.name_scope("AssignNewValue") as scope:
            # Expected match shape
            value_r = tf.reshape(value, tf.shape(variable))
            if tf.compat.v1.executing_eagerly_outside_functions():
                return variable.assign(value_r, name=scope)
            else:
                with tf.compat.v1.colocate_with(variable):
                    return tf.compat.v1.assign(variable, value_r, name=scope)

    @staticmethod
    def _assign_moving_average(variable, value, momentum, inputs_size):
        """Given a variable, assign a new value to it, using a moving average.
        Function taken of `BatchNormalizationLayer <https://bit.ly/3JUcLGd>`_ code.

        Args:
            variable (:obj:`tensorflow.Variable`): the variable to assign.
            value (:obj:`tensorflow.Tensor`): the new value to assign.
            momentum (float): the momentum for the moving average.
            inputs_size (int): the size of the inputs.

        Returns:
            :obj:`tensorflow.Tensor`: the new value of the variable.
        """

        def calculate_update_delta():
            decay = tf.convert_to_tensor(1.0 - momentum, name="decay")
            if decay.dtype != variable.dtype.base_dtype:
                decay = tf.cast(decay, variable.dtype.base_dtype)
            # Expected match shape
            value_r = tf.reshape(value, tf.shape(variable))
            update_delta = (variable - tf.cast(value_r, variable.dtype)) * decay
            if inputs_size is not None:
                update_delta = tf.where(
                    inputs_size > 0, update_delta, K.zeros_like(update_delta))
            return update_delta

        with K.name_scope("AssignMovingAvg") as scope:
            if tf.compat.v1.executing_eagerly_outside_functions():
                return variable.assign_sub(calculate_update_delta(), name=scope)
            else:
                with tf.compat.v1.colocate_with(variable):
                    return tf.compat.v1.assign_sub(variable, calculate_update_delta(), name=scope)

    def call(self, inputs, training=None):
        """Update the max_value from moving average, and quantize the inputs in three steps:

            1. Check that the inputs Tensor is a FixedPoint,
            2. Update the max_value from moving average, only if calibration is enabled and
            3. Quantize the inputs.

        Args:
            inputs (:obj:`tensorflow.Tensor` or :obj:`QTensor`): the inputs tensor.
            training (bool, optional): the training mode. Defaults to None.

        Returns:
            :obj:`tensorflow.Tensor`: the quantized tensor.
        """
        if not isinstance(inputs, FixedPoint):
            raise TypeError("The OutputQuantizer accepts only FixedPoint inputs."
                            f"Received {type(inputs)} inputs.")

        if inputs.value_bits <= self.value_bits:
            msg = f"Quantizing a {inputs.value_bits}-bit QTensor to "\
                f"{self.value_bits}-bit is pointless."
            if inputs.value_bits < self.value_bits:
                msg += " Use a promotion instead."
            raise ValueError(msg)

        if self.calibration:
            # Retrieve information from the inputs and update the weights
            input_batch_size = tf.shape(inputs)[0]
            if tf.reduce_all(tf.math.equal(self.max_value, tf.constant(1.))):
                momentum = tf.constant(-1.)
            else:
                momentum = tf.convert_to_tensor(self.momentum)
            # Compute the new value for all weights
            max_value = tf.math.reduce_max(tf.math.abs(inputs.to_float()), self.axis)
            # If max_values never updated set their newly computed values otherwise
            # update with moving average algorithm
            if momentum == -1:
                OutputQuantizer._assign_new_value(self.max_value, max_value)
            else:
                OutputQuantizer._assign_moving_average(
                    self.max_value, max_value, momentum, input_batch_size)

        # Quantize/downscale the input
        frac_bits = tf.stop_gradient(self.frac_bits(self.max_value))
        inputs, shift_value = inputs.downscale(frac_bits, self.value_bits)
        # update shift values
        self.shift(shift_value)
        return inputs

    def get_config(self):
        """Get the config of the layer.

        Returns:
            dict: the config of the layer.
        """
        config = super().get_config()
        config.update({"momentum": self.momentum})
        return config


@tf.keras.utils.register_keras_serializable()
class Dequantizer(Layer):
    """ Layer that allows to dequantize its inputs.
    """

    def call(self, inputs, training=None):
        """Convert QTensor inputs to float.

        Args:
            inputs (:obj:`tensorflow.Tensor` or :obj:`QTensor`): the inputs tensor(s).
            training (bool, optional): the training mode. Defaults to None.

        Returns:
            :obj:`tensorflow.Tensor`: the dequantized tensor(s).
        """
        def dequantize(x):
            if isinstance(x, QTensor):
                return x.to_float()
            return x

        if isinstance(inputs, (list, tuple)):
            return [dequantize(x) for x in inputs]

        return dequantize(inputs)
