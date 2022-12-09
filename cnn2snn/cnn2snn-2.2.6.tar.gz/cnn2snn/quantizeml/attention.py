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
"""Functions to convert QuantizedAttention to Akida.
"""
from akida import LayerType, Attention
import quantizeml.layers as qlayers
import numpy as np

from .weights import broadcast_and_set_variables
from .layer_utils import get_inbound_layers_names


def _set_attention_variables(ak_layer, k_layer):
    """Computes and sets the variables for an Akida Attention layer.

    This function converts the variables of a Keras layer and sets them into
    the corresponding variables of the equivalent Akida layer.

    Args:
        ak_layer (:obj:`akida.Layer`): the targeted akida layer.
        k_layer (:obj:`tf.keras.Layer`): the source quantized layer.
    """
    assert isinstance(k_layer, qlayers.QuantizedAttention)
    assert ak_layer.parameters.layer_type == LayerType.Attention
    # Prepare a dict for akida variables
    variables_ak = {}

    # Get the QuantizedAttention layer shifts
    variables_ak["value_shift"] = k_layer.values_shift.value.numpy().astype(
        np.uint8)
    variables_ak[
        "shiftmax_input_shift"] = k_layer.softmax_op.input_shift.value.numpy(
        ).astype(np.uint8)
    out_quantizer = getattr(k_layer, "out_quantizer", False)
    if out_quantizer:
        variables_ak["output_shift"] = out_quantizer.shift.value.numpy(
        ).astype(np.int8)

    broadcast_and_set_variables(ak_layer, variables_ak)


def _create_attention(layer):
    """Parses a quantizeml QuantizedAttention layer and returns the params to
    create the corresponding Akida Attention layer.

    Args:
        layer (:obj:`tf.keras.Layer`): the quantizeml QuantizedAttention layer to
            convert.
    """
    assert isinstance(layer, qlayers.QuantizedAttention)

    # Find out if there is a quantizer
    out_quantizer = getattr(layer, "out_quantizer", False)
    # In quantizeml one bit is reserved automatically for the sign, but in akida
    # this is rather checked during the clipping operations.
    buffer_bits = layer.buffer_bitwidth + 1
    if out_quantizer:
        output_bits = out_quantizer.bitwidth
    else:
        # Default to buffer bitwidth
        output_bits = buffer_bits

    # As with output_bits and buffer_bits, shiftmax_output_bits is set with one
    # bit more.
    shiftmax_output_bits = layer.softmax_op.exp_bitwidth + 1

    return Attention(num_heads=layer.num_heads,
                     output_bits=output_bits,
                     buffer_bits=buffer_bits,
                     shiftmax_output_bits=shiftmax_output_bits,
                     name=layer.name)


def convert_quantized_attention(model_ak, layer_k):
    """Converts QuantizedAttention layer and its variables and adds it to the
    Akida's model.

    Args:
        model_ak (:obj:`akida.Model`): the Akida model where the model will
            be added.
        layer_k (:obj:`tf.keras.Layer`): the quantizeml QuantizedAttention
            layer to convert.
    """
    # Get inbound layers names
    inbound_layers_names = get_inbound_layers_names(layer_k)
    # Retrieve the akida layers version of the inbound layers.
    inbound_layers_ak = [
        model_ak.get_layer(ly) for ly in inbound_layers_names
    ]
    if not isinstance(layer_k, qlayers.QuantizedAttention):
        raise TypeError(f"Layer {layer_k.name} was expected to be "
                        "QuantizedAttention")
    layer_ak = _create_attention(layer_k)
    model_ak.add(layer_ak, inbound_layers_ak)
    _set_attention_variables(layer_ak, layer_k)
