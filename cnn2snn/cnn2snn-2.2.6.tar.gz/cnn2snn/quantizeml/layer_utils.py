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
"""Utility function to convert layer to akida.
"""


def get_inbound_layers_names(layer):
    """Returns the inbounds layers names of a layer.

    Args:
        layer (:obj:`tf.keras.Layer`): The source layer.

    Returns:
        :list: the inbounds layers names.
    """
    # Get inbound layers names
    inbound_layers_names = []
    in_node = layer._inbound_nodes[0]
    inbound_layers = in_node.inbound_layers
    for layer in inbound_layers:
        inbound_layers_names.append(layer.name)
    return inbound_layers_names
