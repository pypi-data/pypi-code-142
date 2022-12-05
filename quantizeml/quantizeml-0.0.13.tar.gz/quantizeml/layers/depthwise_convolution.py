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
"""
QuantizedDepthwiseConv2D layer definition.
"""

import tensorflow as tf
from keras import backend
from keras.layers import DepthwiseConv2D

from ..tensors import FixedPoint, MAX_BUFFER_BITWIDTH
from .calibrable import Calibrable, CalibrableVariable
from .quantizers import deserialize_quantizer, WeightQuantizer, OutputQuantizer


__all__ = ["QuantizedDepthwiseConv2D"]


@tf.keras.utils.register_keras_serializable()
class QuantizedDepthwiseConv2D(Calibrable, DepthwiseConv2D):
    """ A depthwise convolutional layer that operates on quantized inputs and weights.

    Args:
        quant_config (dict, optional): the serialized quantization configuration.
            Defaults to empty configuration.
    """

    def __init__(self, *args, quant_config={}, **kwargs):
        super().__init__(*args, **kwargs)
        self.quant_config = quant_config

        self.out_quantizer = deserialize_quantizer(
            self.quant_config, "output_quantizer", OutputQuantizer, False)

        self.weight_quantizer = deserialize_quantizer(
            self.quant_config, "weight_quantizer", WeightQuantizer, True)
        if self.use_bias:
            self.bias_quantizer = deserialize_quantizer(
                self.quant_config, "bias_quantizer", WeightQuantizer, True)

        self.buffer_bitwidth = self.quant_config.get("buffer_bitwidth", MAX_BUFFER_BITWIDTH) - 1
        assert self.buffer_bitwidth > 0, "The buffer_bitwidth must be a strictly positive integer."

        # Add objects that will store the shift values.
        self.input_shift = CalibrableVariable()
        if self.use_bias:
            self.output_shift = CalibrableVariable()
            self.bias_shift = CalibrableVariable()

    def call(self, inputs, training=None):
        # raise an error if the inputs are not FixedPoint or tf.Tensor
        if not isinstance(inputs, (FixedPoint, tf.Tensor)):
            raise TypeError(f"QuantizedDepthwiseConv2D only accepts FixedPoint\
                               or tf.Tensor inputs. Receives {type(inputs)} inputs.")

        # Quantize the weights
        depthwise_kernel = self.weight_quantizer(self.depthwise_kernel, training)

        if isinstance(inputs, tf.Tensor):
            # Assume the inputs are integer stored as float, which is the only tf.Tensor
            # inputs that are allowed
            inputs = FixedPoint(inputs, 0, 8)

        # Promote inputs to avoid saturation, then align them
        inputs, shift = inputs.promote(self.buffer_bitwidth).align()
        self.input_shift(shift)

        outputs = backend.depthwise_conv2d(
            inputs,
            depthwise_kernel,
            strides=self.strides,
            padding=self.padding,
            dilation_rate=self.dilation_rate,
            data_format=self.data_format)

        if self.use_bias:
            bias = self.bias_quantizer(self.bias, training)

            # Align intermediate outputs and biases before adding them
            outputs, shift = outputs.align(bias)
            self.output_shift(shift)
            bias, shift = bias.promote(self.buffer_bitwidth).align(outputs)
            self.bias_shift(shift)
            outputs = tf.add(outputs, bias)

        if self.out_quantizer is not None:
            outputs = self.out_quantizer(outputs)
        return outputs

    def get_config(self):
        config = super().get_config()
        config["quant_config"] = self.quant_config
        return config
