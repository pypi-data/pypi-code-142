# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------


from azure.ai.ml._utils.utils import get_all_data_binding_expressions
from azure.ai.ml.entities._inputs_outputs import Input, Output
from mldesigner._generate._generators._base_generator import BaseGenerator
from mldesigner._utils import extract_input_output_name_from_binding
from mldesigner._exceptions import UserErrorException


class SingleComponentFuncGenerator(BaseGenerator):
    def __init__(self, component_entity, component_func_name, logger, **kwargs):    # pylint: disable=unused-argument
        super(SingleComponentFuncGenerator, self).__init__()
        self._node = component_entity
        self._node_name = self._node.name
        self._component_func_name = component_func_name
        self._params = self._get_params()

    @property
    def tpl_file(self):
        return self.TEMPLATE_PATH / "_components_code_def.template"

    @property
    def entry_template_keys(self):
        return [
            "node_name",
            "component_func_name",
            "params",
        ]

    @property
    def node_name(self):
        return self._node_name

    @property
    def component_func_name(self):
        return self._component_func_name

    @property
    def params(self):
        return self._params

    @staticmethod
    def _get_input_name(data):
        """
        data may in the following types:
        1. Input: In this case, it needs to return an Input entity
        2. Output: In this case, the binding expression is stored in Output.path
        3. str: data can be an int/float in string format, like "1", "2.0",
            or a binding expression, like "${{parent.jobs.a_job.outputs.a_port}}", "${{parent.inputs.a_input}}"
        """
        if isinstance(data, Input):
            input_params_list = []
            for k, v in data.items():
                if v:
                    input_params_list.append(f'{k}="{v}"')
            input_str = ", ".join(input_params_list)
            return f"Input({input_str})"
        if isinstance(data, Output):
            data = data.path

        # data should be string through the above steps, otherwise raise error
        if not isinstance(data, str):
            raise UserErrorException(f"Invalid data: {data}. The supported type here should be string.")

        if get_all_data_binding_expressions(data, ["parent", "jobs"]):
            expression = get_all_data_binding_expressions(data, ["parent", "jobs"])
        elif get_all_data_binding_expressions(data, ["parent", "inputs"]):
            expression = get_all_data_binding_expressions(data, ["parent", "inputs"])
        else:
            # in this case, name may be other types of input, we directly return name
            return f'"{data}"'
        return extract_input_output_name_from_binding(expression[0])

    def _get_params(self):
        params_dict = {}
        for node_name, node_input in self._node.inputs.items():
            if isinstance(node_input, Input):
                params_dict[node_name] = self._get_input_name(data=node_input)
            else:
                params_dict[node_name] = self._get_input_name(data=node_input._data) # pylint: disable=protected-access
        return params_dict
