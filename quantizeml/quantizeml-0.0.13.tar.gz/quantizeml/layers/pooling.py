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

from keras.layers import MaxPool2D, GlobalAveragePooling2D

from .calibrable import Calibrable, CalibrableVariable
from .quantizers import deserialize_quantizer, OutputQuantizer
from ..tensors import FixedPoint, MAX_BUFFER_BITWIDTH

__all__ = ["QuantizedMaxPool2D", "QuantizedGlobalAveragePooling2D"]


@tf.keras.utils.register_keras_serializable()
class QuantizedMaxPool2D(MaxPool2D):
    """A max pooling layer that operates on quantized inputs.

    """

    def call(self, inputs):
        # Raise an error if the inputs are not FixedPoint
        if not isinstance(inputs, FixedPoint):
            raise TypeError(f"QuantizedMaxPool2D only accepts FixedPoint inputs. \
                             Receives {type(inputs)} inputs.")

        outputs = super().call(inputs.values)
        return FixedPoint(outputs, inputs.frac_bits, inputs.value_bits)


@tf.keras.utils.register_keras_serializable()
class QuantizedGlobalAveragePooling2D(Calibrable, GlobalAveragePooling2D):
    """A global average pooling layer that operates on quantized inputs.

     Args:
        quant_config (dict, optional): the serialized quantization configuration.
            Defaults to empty configuration.
    """

    def __init__(self, quant_config={}, **kwargs):
        super().__init__(**kwargs)
        self.quant_config = quant_config
        self.out_quantizer = deserialize_quantizer(
            self.quant_config, "output_quantizer", OutputQuantizer, False)
        self.buffer_bitwidth = self.quant_config.get("buffer_bitwidth", MAX_BUFFER_BITWIDTH) - 1
        assert self.buffer_bitwidth > 0, "The buffer_bitwidth must be a strictly positive integer."

        # Add objects that will store the shift values.
        self.input_shift = CalibrableVariable()

    def build(self, input_shape):
        super().build(input_shape)
        # Build the spatial size
        self.spatial_size = (input_shape[1] * input_shape[2])

    def call(self, inputs, training=None):
        # Raise an error if the inputs are not FixedPoint
        if not isinstance(inputs, FixedPoint):
            raise TypeError(f"QuantizedGlobalAveragePooling2D only accepts FixedPoint inputs. \
                             Receives {type(inputs)} inputs.")

        # Promote input to prevent overflow in the reduce_sum op, then align them
        inputs, shift = inputs.promote(self.buffer_bitwidth).align()
        self.input_shift(shift)
        inputs_sum = tf.reduce_sum(inputs, axis=[1, 2], keepdims=self.keepdims)
        inputs_mean = inputs_sum / self.spatial_size

        if self.out_quantizer is not None:
            return self.out_quantizer(inputs_mean, training=training)
        return inputs_mean

    def get_config(self):
        config = super().get_config()
        config.update({"quant_config": self.quant_config})
        return config
