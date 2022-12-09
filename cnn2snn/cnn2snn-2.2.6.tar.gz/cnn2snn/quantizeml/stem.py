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
"""Functions to convert Stem block quantized layers to Akida.
Those layers are:
    - The Embedding layer
    - The Reshape layer
    - The ClassToken (+ the DistToken for distilled models) layer(s)
    - The AddPosEmbedding layer
"""
from akida import LayerType, Stem
import quantizeml.layers as qlayers
import numpy as np

from .weights import quantize_weights, broadcast_and_set_variables


def stem_layers(model_k):
    """Returns the Stem layers of a quantized transformer model.
    For now the Stem is composed only of the Embedding QuantizedConv2D
    and QuantizedReshape.

    Args:
        model_k (:obj:`keras.Model`): the quantized transformer model.

    Return:
        list: the stem block layers.
    """
    stem_block = []

    # The stem of a transfomer model starts with a QuantizedConv2D layer
    # (i.e layer just after the InputLayer layer), followed by an optionnal
    # QuantizedReshape
    if isinstance(model_k.layers[1], qlayers.QuantizedConv2D):
        layer = model_k.layers[1]
        assert layer.kernel_size == layer.strides
        assert layer.padding == 'valid'
        stem_block.append(layer)
        # add the QuantizedReshape layer to the stem if available
        if len(model_k.layers) > 2 and isinstance(model_k.layers[2],
                                                  qlayers.QuantizedReshape):
            stem_block.append(model_k.layers[2])

    return stem_block


def _set_stem_variables(ak_layer, stem_layers):
    """Computes and sets the variables for an Akida Stem layer.

    This function converts the variables of a Keras layers and sets them into
    the corresponding variables of the equivalent Akida layer.

    Args:
        ak_layer (:obj:`akida.Layer`): the targeted akida layer.
        k_layers (list): list of the source quantized layers.
    """
    assert ak_layer.parameters.layer_type == LayerType.Stem

    # Note for now only the Embedding layer conversion is handled
    # the Embedding (i.e the QuantizedConv2D layer) should be the
    # first layer of the Stem
    embedding_layer = stem_layers[0]

    # Prepare a dict for akida variables
    variables_ak = {}
    # Convert and store the kernel/bias of the Embedding layer
    # get the Embedding weights
    kernel = embedding_layer.kernel.numpy()
    weights_ak = quantize_weights(embedding_layer.weight_quantizer, kernel)

    # get the Embedding bias
    bias = embedding_layer.bias.numpy()
    bias_ak = quantize_weights(embedding_layer.bias_quantizer, bias)

    variables_ak["weights"] = weights_ak[0].astype(np.int8)
    variables_ak["weights_scales"] = weights_ak[1].astype(np.int32)
    variables_ak["bias"] = bias_ak[0].astype(np.int32)
    # Get the Embedding layer shifts
    variables_ak["prod_shift"] = embedding_layer.conv_shift.value.numpy(
    ).astype(np.uint8)
    variables_ak["bias_shift"] = embedding_layer.bias_shift.value.numpy(
    ).astype(np.uint8)
    out_quantizer = getattr(embedding_layer, "out_quantizer", False)
    if out_quantizer:
        variables_ak["output_shift"] = out_quantizer.shift.value.numpy(
        ).astype(np.int8)

    broadcast_and_set_variables(ak_layer, variables_ak)


def _create_stem(input_shape, layers):
    """Parses the quantizeml quantized layers of the Stem block and returns the
    params to create the corresponding Akida Stem layer.

    Args:
        input_shape (tuple): the input shape of the Stem.
        layers (list): the quantizeml quantized layers of the Stem to convert.
    """
    # Note: for now only the Embedding layer conversion is handled
    embedding_layer = layers[0]

    if isinstance(embedding_layer.weight_quantizer,
                  qlayers.WeightQuantizer) and getattr(
                      embedding_layer.weight_quantizer, "scale_bits", False):
        weights_scale_bits = embedding_layer.weight_quantizer.scale_bits
    else:
        # Set the value to default
        weights_scale_bits = 8
    # Find out if there is a quantizer
    out_quantizer = getattr(embedding_layer, "out_quantizer", False)
    # In quantizeml one reserves automaticaly one bit for the sign, but in akida
    # this is rather checked during the clipping operations.
    buffer_bits = embedding_layer.buffer_bitwidth + 1
    if out_quantizer:
        output_bits = out_quantizer.bitwidth
    else:
        # Default to buffer bitwidth
        output_bits = buffer_bits

    collapse_spatial_dims = True
    if len(layers) > 1 and not isinstance(layers[1], qlayers.QuantizedReshape):
        collapse_spatial_dims = False

    return Stem(input_shape=input_shape,
                filters=embedding_layer.filters,
                kernel_size=embedding_layer.kernel_size[0],
                weights_bits=embedding_layer.weight_quantizer.bitwidth,
                weights_scale_bits=weights_scale_bits,
                bias_bits=embedding_layer.bias_quantizer.bitwidth,
                output_bits=output_bits,
                buffer_bits=buffer_bits,
                collapse_spatial_dims=collapse_spatial_dims,
                name="Stem")


def convert_quantized_stem_layers(model_ak, input_shape, layers_k):
    """Converts QuantizedDense layer and its variables and adds it to the
    Akida's model.

    Args:
        model_ak (:obj:`akida.Model`): the Akida model where the model will be added.
        input_shape (tuple): the input shape of the Stem.
        layers_k (list): the quantizeml quantized layers of the Stem to convert.
    """
    # Note: for now only the Embedding layer conversion is handled
    embedding_layer = layers_k[0]
    if not isinstance(embedding_layer, qlayers.QuantizedConv2D):
        raise TypeError(f"Layer {embedding_layer.name} was expected to be "
                        "QuantizedConv2D")
    layer_ak = _create_stem(input_shape, layers_k)
    model_ak.add(layer_ak)
    _set_stem_variables(layer_ak, layers_k)
