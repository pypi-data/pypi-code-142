#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Anders Hafreager.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from ipywidgets import DOMWidget
from traitlets import Unicode
from traittypes import Array
from .exceptions import *

from ._frontend import module_name, module_version
import numpy as np

def array_to_binary(ar, obj=None):
    if ar is not None:
        ar = ar.astype(np.float32)
        mv = memoryview(ar)
        # 'nested' is just to show the (de)serialization goes all fine
        return {'data': mv, 'shape': ar.shape}
    else:
        return None
def binary_to_array(value, obj=None):
    global last_value, setters
    setters += 1
    #print(">>", value) # print msg'es get lost, but check the websocket output
    last_value = value # or keep a reference to a global for debugging
    return np.frombuffer(value['data'], dtype=np.float32)
    #return np.frombuffer(value['data'], dtype=np.float32)

array_binary_serialization = dict(to_json=array_to_binary, from_json=binary_to_array)

class Visualizer(DOMWidget):
    """TODO: Add docstring here
    """
    _model_name = Unicode('VisualizerModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('VisualizerView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    particle_positions = Array(np.asarray([])).tag(sync=True, **array_binary_serialization)
    particle_radii = Array(np.asarray([])).tag(sync=True, **array_binary_serialization)
    particle_colors = Array(np.asarray([])).tag(sync=True, **array_binary_serialization)

    def set_atom_types(self, types):
        from .atom_types import atom_types

        for type in types:
            if type not in atom_types:
                raise InvalidAtomType(type)
        new_particle_colors = np.zeros(3 * len(types))
        new_particle_radii = np.zeros(len(types))
        for i, type in enumerate(types):
            r = atom_types[type]['color']['r']
            g = atom_types[type]['color']['g']
            b = atom_types[type]['color']['b']
            new_particle_colors[3 * i + 0] = r
            new_particle_colors[3 * i + 1] = g
            new_particle_colors[3 * i + 2] = b
            new_particle_radii[i] = atom_types[type]['radius']
        self.particle_colors = new_particle_colors
        self.particle_radii = new_particle_radii

    

