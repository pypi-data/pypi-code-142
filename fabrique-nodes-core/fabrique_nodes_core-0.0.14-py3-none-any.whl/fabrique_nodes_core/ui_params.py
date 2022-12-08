default_ui_params = {
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

destructurer_ui_params = {
    **default_ui_params, 
    'has_code': True,
    'has_required': True,
    'has_visible': True,
    'has_special': True
}

structurer_ui_params = {
    **default_ui_params, 
    'has_code': True,
    'has_required': True,
    'has_visible': True,
    'has_special': True
}

@classmethod
class StringInput:
    default:str = ''

@classmethod
class BoolInput:
    default:bool = False
