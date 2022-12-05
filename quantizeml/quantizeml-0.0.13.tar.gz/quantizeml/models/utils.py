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
Common utility methods used in quantization models.
"""

from copy import deepcopy
from pathlib import Path
import numpy as np
import tensorflow_addons as tfa
from keras.models import clone_model, load_model as kload_model, Model
import warnings

from quantizeml.layers.quantizers import Quantizer, Dequantizer

from ..layers import Calibrable

__all__ = ['load_model', 'deep_clone_model', 'set_calibrate', 'insert_layer', 'load_weights',
           'save_weights']


def load_model(model_path, custom_layers={}, compile_model=True):
    """Loads a model with Vision Transformer custom layers.

    Args:
        model_path (str): path of the model to load
        custom_layers (dict, optional): custom layers to add to the model. Defaults to {}.
        compile_model (bool, optional): whether to compile the model. Defaults to True.

    Returns:
        :class:`keras.models.Model`: the loaded model
    """
    # Given that all layers were imported in __init__.py, they are registered.
    # Therefore, we just need append GroupNormalization in the custom layers.
    custom_layers.update({'GroupNormalization': tfa.layers.GroupNormalization})
    return kload_model(model_path, custom_objects=custom_layers, compile=compile_model)


def deep_clone_model(model, *args, **kwargs):
    """Clone a model, assign variable to variable. Useful when a clone function is used,
    and new layers have not the same number of parameters as the original layer.

    Args:
        model (:class:`keras.models.Model`): model to be cloned
        args, kwargs (optional): arguments pass to :func:`keras.models.clone_model` function

    Returns:
        :class:`keras.models.Model`: the cloned model
    """
    new_model = clone_model(model, *args, **kwargs)
    variables_dict = {var.name: var for var in model.variables}
    apply_weights_to_model(new_model, variables_dict, False)
    return new_model


def set_calibrate(model, value):
    """Enable or disable calibration for all layers in a model.

    Args:
        model (:class:`keras.models.Model`): model to be calibrated
        value (bool): True to enable calibration, False to disable it
    """
    for layer in model.layers:
        if isinstance(layer, Calibrable):
            layer.calibration = value


def insert_layer(model, target_layer_name, new_layer):
    """ Inserts the given layer in the model before or after the layer with the name
    target_layer_name depending on the type of new_layer.

    Note that new_layer type is restricted to (Quantizer, Dequantizer) and a Quantizer will be added
    before new_layer while a Dequantizer will be added after

    Args:
        model (keras.Model): the model to update
        target_layer_name (str): name of the layer after which to insert a layer
        new_layer (keras.Layer): layer to insert

    Raises:
        ValueError: when target_layer_name is not found in model or new_layer is not in (Quantizer,
            Dequantizer)

    Returns:
        keras.Model: the new model
    """
    # Check that the model has a layer with then given target_layer_name
    if not any(ly.name == target_layer_name for ly in model.layers):
        raise ValueError(f'{target_layer_name} not found in model.')

    # Check added layer type
    if not isinstance(new_layer, (Quantizer, Dequantizer)):
        raise ValueError(f'Inserted layer must be of type Quantizer or Dequantizer, \
                        received {type(new_layer)}.')

    # Create a clone model to prevent messing with the original model
    clone_model = deep_clone_model(model)

    # Auxiliary dictionary to describe the network graph
    network_dict = {'input_layers_of': {}, 'new_output_tensor_of': {}}

    # Set the input layers of each layer
    for layer in clone_model.layers:
        for node in layer._outbound_nodes:
            layer_name = node.outbound_layer.name
            if layer_name not in network_dict['input_layers_of']:
                network_dict['input_layers_of'].update({layer_name: [layer.name]})
            else:
                network_dict['input_layers_of'][layer_name].append(layer.name)

    # Set the output tensor of the input layer
    network_dict['new_output_tensor_of'].update({clone_model.layers[0].name: clone_model.input})

    # Iterate over all layers after the input
    model_outputs = []
    insert_before = isinstance(new_layer, Quantizer)
    for layer in clone_model.layers[1:]:
        # Determine input tensors
        layer_input = []
        for layer_aux in network_dict['input_layers_of'][layer.name]:
            input = network_dict['new_output_tensor_of'][layer_aux]
            if isinstance(input, tuple):
                network_dict['new_output_tensor_of'][layer_aux] = input[1:]
                input = input[0]
            layer_input.append(input)
        if len(layer_input) == 1:
            layer_input = layer_input[0]

        # Insert layer if name matches the given layer name
        if layer.name == target_layer_name:
            if insert_before:
                # Apply one Quantizer by input then current layer
                if isinstance(layer_input, list):
                    inputs = []
                    for i in range(len(layer_input)):
                        copied_layer = deepcopy(new_layer)
                        copied_layer._name += "_" + str(i)
                        y = copied_layer(layer_input[i])
                        inputs.append(y)
                    x = inputs
                else:
                    x = new_layer(layer_input)
                x = layer(x)
            else:
                # Apply current layer then new layer
                x = layer(layer_input)
                if isinstance(x, tuple):
                    x = tuple(new_layer(i) for i in x)
                else:
                    x = new_layer(x)
        else:
            x = layer(layer_input)

        # Set new output tensor (the original one, or the one of the inserted layer)
        network_dict['new_output_tensor_of'].update({layer.name: x})

        # Save tensor in output list if it is output in initial model
        if layer.name in clone_model.output_names:
            model_outputs.append(x)

    new_model = Model(inputs=clone_model.inputs, outputs=model_outputs)
    variables_dict = {var.name: var for var in model.variables}
    apply_weights_to_model(new_model, variables_dict, False)
    return new_model


def apply_weights_to_model(model, weights, verbose=True):
    """Loads weights from a dictionary and apply it to a model.

    Go through the dictionary of weights, find the corresponding variable in the
    model and partially load its weights.

    Args:
        model (keras.Model): the model to update
        weights (dict): the dictionary of weights
        verbose (bool, optional): if True, throw warning messages if a dict item is not found in the
            model. Defaults to True.
    """
    if len(weights) == 0:
        warnings.warn("There is no weight to apply to the model.")
        return

    # Go through the dictionary of weights with each item
    for key, value in weights.items():
        value_applied = False
        for dest_var in model.variables:
            if key == dest_var.name:
                # Apply the current item value
                dest_var.assign(value)
                value_applied = True
                break
        if not value_applied and verbose:
            warnings.warn(f"Variable '{key}' not found in the model.")


def load_weights(model, weights_path):
    """Loads weights from a npz file and apply it to a model.

    Go through the dictionary of weights of the npz file, find the corresponding variable in the
    model and partially load its weights.

    Args:
        model (keras.Model): the model to update
        weights_path (str): the path of the npz file to load
    """
    # Check the npz file validity
    path = Path(weights_path)
    if not path.is_file():
        raise ValueError(f"File `{weights_path}` not found.")

    # Open the npz file
    weights_dict = np.load(weights_path)

    # Apply the weights to the model
    apply_weights_to_model(model, weights_dict)


def save_weights(model, weights_path):
    """Save model weights on an npz file.

    Takes a model and save the weights of all its layers into an npz file.

    Args:
        model (keras.Model): the model to save its weights
        weights_path (str): the path of the npz file to save
    """
    weights_dict = {}
    for var in model.variables:
        weights_dict[var.name] = var

    np.savez(weights_path, **weights_dict)
