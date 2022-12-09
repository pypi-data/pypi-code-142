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
"""Functions to convert weights from quantizeml quantized Keras models to Akida.

"""
import tensorflow as tf
from quantizeml.layers import WeightQuantizer
import numpy as np


def quantize_weights(quantizer, w):
    """Returns quantized variable as numpy arrays.

    Args:
        quantizer (:obj:`WeightQuantizer`): the quantizer object.
        w (:obj:`np.ndarray`): the weights to quantize.

    Returns:
        tuple: the quantized weights and the scales. The scales are by defaults
            set to 1 if a FixedPointQuantizer was used.

    """
    assert isinstance(quantizer, WeightQuantizer)
    w_tf = tf.constant(w)
    wq = quantizer(w_tf)
    w_ak = wq.values.numpy()
    if getattr(quantizer, "scale_bits", False):
        scales_ak = wq.scales.values.numpy()
        return w_ak, scales_ak

    return w_ak, np.array([1])


def broadcast_and_set_variables(layer_ak, variables):
    """Adapts variables to akida variables shapes if necessary, and sets them.

    Args:
        layer_ak (:obj:`akida.Layer`): the targeted akida layer.
        variables (dict): dictionary of variables
    """
    for var_name in variables:
        var = variables[var_name]
        # If the variable is a scalar, broadcast it across the target akida
        # variable's last dimension.
        if np.isscalar(var) or len(var) == 1:
            shape = layer_ak.variables[var_name].shape
            var = np.full(shape, variables[var_name])

        layer_ak.variables[var_name] = var
