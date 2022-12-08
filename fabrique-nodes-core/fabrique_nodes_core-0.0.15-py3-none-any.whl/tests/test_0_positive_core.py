import os
import sys
# noinspection PyPackageRequirements
import pytest
# noinspection PyPackageRequirements

cur_file_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = f'{cur_file_dir}/../fabrique_nodes_core'
sys.path.append(lib_dir)
os.chdir(cur_file_dir)

import tests.import_spoofer as import_spoofer

from fabrique_nodes_core import (BaseNode, NodeConfig, NodeModel, 
                                 PortModel, port_type, root_port, 
                                 default_ui_params, destructurer_ui_params, structurer_ui_params)

expected_default_ui_params = {
    'has_inputs': True, 
    'has_outputs': True, 
    'has_visible': False, 
    'has_code': False, 
    'has_special': False, 
    'has_required': False, 
    'name_from_code': True,
    'valid_input_types': [], 
    'valid_output_types': [], 
    'valid_subtypes': []
}

def test_def_ui():
   assert default_ui_params == expected_default_ui_params

def test_base_node():
    assert BaseNode.initial_config is None
    assert hasattr(BaseNode, 'type_')
    assert BaseNode.ui_params == expected_default_ui_params