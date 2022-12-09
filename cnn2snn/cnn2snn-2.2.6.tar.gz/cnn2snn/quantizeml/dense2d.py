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
"""Functions to convert QuantizedDense to Akida.
"""
from akida import LayerType, Dense2D
import quantizeml.layers as qlayers
import numpy as np

from .weights import quantize_weights, broadcast_and_set_variables


def _set_dense2d_variables(ak_layer, k_layer):
    """Computes and sets the variables for an Akida Dense2D layer.

    This function converts the variables of a Keras layer and sets them into
    the corresponding variables of the equivalent Akida layer.

    Args:
        layer_ak (:obj:`akida.Layer`): the targeted akida layer.
        k_layer (:obj:`tf.keras.Layer`): the source quantized layer.
    """
    assert isinstance(k_layer, qlayers.QuantizedDense)
    assert ak_layer.parameters.layer_type == LayerType.Dense2D
    # Prepare a dict for akida variables
    variables_ak = {}
    # Convert and store the kernel/bias of the QuantizedDense layer
    # get the QuantizedDense weights
    kernel = k_layer.kernel.numpy()
    weights_ak = quantize_weights(k_layer.weight_quantizer, kernel)

    # get the QuantizedDense bias
    bias = k_layer.bias.numpy()
    bias_ak = quantize_weights(k_layer.bias_quantizer, bias)

    variables_ak["weights"] = weights_ak[0].astype(np.int8)
    variables_ak["weights_scales"] = weights_ak[1].astype(np.int32)
    variables_ak["bias"] = bias_ak[0].astype(np.int32)
    # Get the QuantizedDense layer shifts
    variables_ak["input_shift"] = k_layer.input_shift.value.numpy().astype(
        np.uint8)
    variables_ak["prod_shift"] = k_layer.prod_shift.value.numpy().astype(
        np.uint8)
    variables_ak["bias_shift"] = k_layer.bias_shift.value.numpy().astype(
        np.uint8)
    out_quantizer = getattr(k_layer, "out_quantizer", False)
    if out_quantizer:
        variables_ak["output_shift"] = out_quantizer.shift.value.numpy(
        ).astype(np.int8)

    broadcast_and_set_variables(ak_layer, variables_ak)


def _create_dense2d(layer):
    """Parses a quantizeml QuantizedDense layer and returns the params to
    create the corresponding Akida Dense2D layer.

    Args:
        layer (:obj:`tf.keras.Layer`): the quantizeml QuantizedDense layer to
            convert.
        params (dict): will contain the parameters of the future Akida Dense2D
            layer.

    """
    assert isinstance(layer, qlayers.QuantizedDense)

    if isinstance(
            layer.weight_quantizer, qlayers.WeightQuantizer) and getattr(
            layer.weight_quantizer, "scale_bits", False):
        weights_scale_bits = layer.weight_quantizer.scale_bits
    else:
        # Set the value to default
        weights_scale_bits = 8
    # Find out if there is a quantizer
    out_quantizer = getattr(layer, "out_quantizer", False)
    # In quantizeml one reserves automaticaly one bit for the sign, but in akida
    # this is rather checked during the clipping operations.
    buffer_bits = layer.buffer_bitwidth + 1
    if out_quantizer:
        output_bits = out_quantizer.bitwidth
    else:
        # Default to buffer bitwidth
        output_bits = buffer_bits

    return Dense2D(units=layer.units,
                   weights_bits=layer.weight_quantizer.bitwidth,
                   weights_scale_bits=weights_scale_bits,
                   bias_bits=layer.bias_quantizer.bitwidth,
                   output_bits=output_bits,
                   buffer_bits=buffer_bits,
                   name=layer.name)


def convert_quantized_dense(model_ak, layer_k):
    """Converts QuantizedDense layer and its variables and adds it to the
    Akida's model.

    Args:
        layer (:obj:`tf.keras.Layer`): the quantizeml QuantizedDense layer to
            convert.
        :obj:`akida.Model`: the Akida model where the model will be added.
    """
    if not isinstance(layer_k, qlayers.QuantizedDense):
        raise TypeError(f"Layer {layer_k.name} was expected to be "
                        "QuantizedDense")
    layer_ak = _create_dense2d(layer_k)
    model_ak.add(layer_ak)
    _set_dense2d_variables(layer_ak, layer_k)
