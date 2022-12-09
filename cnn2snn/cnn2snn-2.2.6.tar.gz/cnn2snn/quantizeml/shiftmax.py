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
"""Functions to convert QuantizedShiftmax to Akida.
"""
from akida import LayerType, Shiftmax
import quantizeml.layers as qlayers
import numpy as np

from .weights import broadcast_and_set_variables


def _set_shiftmax_variables(ak_layer, k_layer):
    """Computes and sets the variables for an Akida Shiftmax layer.

    This function converts the variables of a Keras layer and sets them into
    the corresponding variables of the equivalent Akida layer.

    Args:
        layer_ak (:obj:`akida.Layer`): the targeted akida layer.
        k_layer (:obj:`tf.keras.Layer`): the source quantized layer.
    """
    assert isinstance(k_layer, qlayers.QuantizedShiftmax)
    assert ak_layer.parameters.layer_type == LayerType.Shiftmax
    # Prepare a dict for akida variables
    variables_ak = {}
    variables_ak["input_shift"] = k_layer.input_shift.value.numpy().astype(
        np.uint8)
    broadcast_and_set_variables(ak_layer, variables_ak)


def _create_shiftmax(layer):
    """Parses a quantizeml QuantizedShiftmax layer and returns the
    corresponding Akida Shiftmax layer.

    Args:
        layer (:obj:`tf.keras.Layer`): the quantizeml QuantizedShiftmax layer
            to convert.
    """
    assert isinstance(layer, qlayers.QuantizedShiftmax)
    return Shiftmax(output_bits=layer.exp_bitwidth + 1,
                    buffer_bits=layer.buffer_bitwidth,
                    name=layer.name)


def convert_quantized_shiftmax(model_ak, layer_k):
    """Converts QuantizedShiftmax layer and its variables and adds it to the
    Akida's model.

    Args:
        layer (:obj:`tf.keras.Layer`): the quantizeml QuantizedShiftmax layer
            to convert.
        :obj:`akida.Model`: the Akida model where the model will be added.
    """
    if not isinstance(layer_k, qlayers.QuantizedShiftmax):
        raise TypeError(f"Layer {layer_k.name} was expected to be "
                        "QuantizedShiftmax")
    # Create and add layer to the akida model
    layer_ak = _create_shiftmax(layer_k)
    model_ak.add(layer_ak)
    # Set the akida layer converted variables
    _set_shiftmax_variables(layer_ak, layer_k)
