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
"""Parsing functions to generate an Akida model from a Keras model quantized with quantizeml api.
"""

import quantizeml.layers as qlayers
from akida import Model

from .dense2d import convert_quantized_dense
from .add import convert_quantized_add
from .input_data import convert_input
from .shiftmax import convert_quantized_shiftmax
from .attention import convert_quantized_attention
from .stem import convert_quantized_stem_layers, stem_layers


def generate_model(model, input_is_image):
    """Generates an Akida model.

    This function creates an Akida model by iterating through the layers of the
    quantized model. For each layer, the corresponding akida layer is created and
    added to the Akida model.

    Args:
        model (:obj:`tf.keras.Model`): a Keras model to convert.
        input_is_image (bool): True if input is an 8-bit unsigned tensors (like images).

    Returns:
        :obj:`akida.Model`: the generated Akida model.

    """
    model_ak = Model()

    # Convert the stem block layer if the keras model has one, otherwise convert the
    # keras InputLayer into an InputData layer
    stem_block = stem_layers(model)
    if len(stem_block) != 0:
        input_shape = model.input_shape[1:]
        convert_quantized_stem_layers(model_ak, input_shape, stem_block)
    else:
        convert_input(model_ak, model.layers[0], input_is_image)

    # Convert the remaining layers
    for layer in model.layers[len(stem_block) + 1:]:
        # Create and add layer to the akida model
        if isinstance(layer, qlayers.QuantizedDense):
            convert_quantized_dense(model_ak, layer)
        elif isinstance(layer, qlayers.QuantizedAdd):
            convert_quantized_add(model_ak, layer)
        elif isinstance(layer, qlayers.QuantizedShiftmax):
            convert_quantized_shiftmax(model_ak, layer)
        elif isinstance(layer, qlayers.QuantizedAttention):
            convert_quantized_attention(model_ak, layer)
        else:
            # If you got here, the layer is not supported: raise an error.
            raise RuntimeError(f"Layer {layer.name}: unsupported type "
                               f"{layer.__class__.__name__}.")

    return model_ak
