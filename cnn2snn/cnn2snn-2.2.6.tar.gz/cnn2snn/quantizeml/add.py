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
"""Functions to convert QuantizedAdd to Akida.
"""
from akida import LayerType, Add
import quantizeml.layers as qlayers
import numpy as np

from .weights import broadcast_and_set_variables
from .layer_utils import get_inbound_layers_names


def _set_add_variables(ak_layer, k_layer):
    """Computes and sets the variables for an Akida Add layer.

    This function converts the variables of a Keras layer and sets them into
    the corresponding variables of the equivalent Akida layer.

    Args:
        layer_ak (:obj:`akida.Layer`): the targeted akida layer.
        k_layer (:obj:`tf.keras.Layer`): the source quantized layer.
    """
    assert isinstance(k_layer, qlayers.QuantizedAdd)
    assert ak_layer.parameters.layer_type == LayerType.Add
    # Prepare a dict for akida variables
    variables_ak = {}
    variables_ak["a_shift"] = k_layer.a_shift.value.numpy().astype(np.uint8)
    variables_ak["b_shift"] = k_layer.b_shift.value.numpy().astype(np.uint8)
    out_quantizer = getattr(k_layer, "out_quantizer", False)
    if out_quantizer:
        variables_ak["output_shift"] = out_quantizer.shift.value.numpy(
        ).astype(np.int8)

    broadcast_and_set_variables(ak_layer, variables_ak)


def _create_add(layer):
    """Parses a quantizeml QuantizedAdd layer and returns the corresponding
    Akida Add layer.

    Args:
        layer (:obj:`tf.keras.Layer`): the quantizeml QuantizedAdd layer to
            convert.
    """
    assert isinstance(layer, qlayers.QuantizedAdd)
    # In quantizeml one reserves automaticaly one bit for the sign, but in akida
    # this is rather checked during the clipping operations.
    buffer_bits = layer.buffer_bitwidth + 1
    if getattr(layer, 'out_quantizer', False):
        output_bits = layer.out_quantizer.bitwidth
    else:
        output_bits = buffer_bits
    return Add(output_bits=output_bits,
               buffer_bits=buffer_bits,
               name=layer.name)


def convert_quantized_add(model_ak, layer_k):
    """Converts QuantizedAdd layer and its variables and adds it to the
    Akida's model.

    Args:
        layer (:obj:`tf.keras.Layer`): the quantizeml QuantizedAdd layer to
            convert.
        :obj:`akida.Model`: the Akida model where the model will be added.
    """
    if not isinstance(layer_k, qlayers.QuantizedAdd):
        raise TypeError(f"Layer {layer_k.name} was expected to be "
                        "QuantizedAdd")
    # Get inbound layers names
    inbound_layers_names = get_inbound_layers_names(layer_k)
    # Retrieve the akida layers version of the inbound layers.
    inbound_layers_ak = [
        model_ak.get_layer(ly) for ly in inbound_layers_names
    ]
    # Create and add layer to the akida model
    layer_ak = _create_add(layer_k)
    model_ak.add(layer_ak, inbound_layers_ak)
    # Set the akida layer converted variables
    _set_add_variables(layer_ak, layer_k)
