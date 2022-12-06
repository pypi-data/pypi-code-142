# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from typing import List
import re
from azure.ai.ml._utils.utils import get_all_data_binding_expressions
from azure.ai.ml.entities import Component
from azure.ai.ml.entities._inputs_outputs import Input, Output
from azure.ai.ml.entities._job.pipeline.pipeline_job import PipelineJob
from mldesigner._generate._generators._base_generator import BaseGenerator
from mldesigner._generate._generators._component_func_generator import SingleComponentFuncGenerator
from mldesigner._generate._generate_package import generate_pkg_logger
from mldesigner._utils import extract_input_output_name_from_binding


class PipelineGenerator(BaseGenerator):
    def __init__(
        self,
        pipeline_entity: PipelineJob,
        sorted_nodes: List[Component],
        name_to_components: List[str],
    ):
        self.pipeline_entity = pipeline_entity
        self._sorted_nodes = sorted_nodes
        self._component_func_names = name_to_components
        self.url = self.pipeline_entity.studio_url
        self.logger = generate_pkg_logger

        component_import_all = self._component_func_names.copy()
        for i in range(len(self._component_func_names)):    # pylint: disable=consider-using-enumerate
            if self._sorted_nodes[i].name == self._component_func_names[i]:
                self._component_func_names[i] += '_func'
                component_import_all[i] += f" as {self._component_func_names[i]}"

        self.component_import = list(set(component_import_all))
        self.component_import.sort(key=component_import_all.index)
        self._node_generators = [
            SingleComponentFuncGenerator(self._sorted_nodes[i], self._component_func_names[i], self.logger)
            for i in range(len(self._sorted_nodes))
        ]
        self.contain_float_or_number = False
        self.pipeline_param_defines, self.pipeline_param_assignments = self._pipeline_param_traversal()

    @property
    def azure_ai_ml_imports(self):
        return [
            "from azure.ai.ml import Input, dsl",
        ]

    @property
    def dsl_pipeline_param_assignments(self):
        dsl_pipeline_param_dict = {}
        dsl_pipeline_param_dict["display_name"] = f'"{self.pipeline_entity.display_name}"'
        dsl_pipeline_param_dict["description"] = f'"{self.pipeline_entity.description}"'
        if self.pipeline_entity.properties["azureml.defaultDataStoreName"]:
            dsl_pipeline_param_dict[
                "default_datastore"
            ] = f'"{self.pipeline_entity.properties["azureml.defaultDataStoreName"]}"'
        if self.pipeline_entity.compute:
            dsl_pipeline_param_dict["default_compute_target"] = f'"{self.pipeline_entity.compute}"'
        return dsl_pipeline_param_dict

    def _pipeline_param_traversal(self):
        pipeline_param_def_dict, pipeline_param_assign_dict, pipeline_param_def_with_default_dict = {}, {}, {}
        for pipeline_input in self.pipeline_entity.inputs.values():
            input_name = pipeline_input._name   # pylint: disable=protected-access
            input_value = pipeline_input._data  # pylint: disable=protected-access
            if isinstance(input_value, str):    # input_value is an int/float in the format of string or other strings
                if re.compile(r'^(-?[0-9]\d*)(\.\d+|\d*)$').match(input_value):
                    self.contain_float_or_number = True
                pipeline_param_def_with_default_dict[input_name] = f'"{input_value}"'
                pipeline_param_assign_dict[input_name] = f'"{input_value}"'
            if isinstance(input_value, Input):  # input_value is an Input
                pipeline_param_def_dict[input_name] = None
                input_params_list = []
                for k, v in input_value.items():
                    if v:
                        input_params_list.append(f'{k}="{v}"')
                input_str = ", ".join(input_params_list)
                pipeline_param_assign_dict[input_name] = f"Input({input_str})"
        # let non-default param be the first keys of pipeline_param_def_dict
        pipeline_param_def_dict.update(pipeline_param_def_with_default_dict)
        return pipeline_param_def_dict, pipeline_param_assign_dict

    @property
    def pipeline_outputs(self):
        pipeline_output_dict = {}
        for node in self.pipeline_entity.jobs.values():
            node_name = node.name
            for output in node.outputs.values():
                # pylint: disable=protected-access
                node_output_name = output._name
                pipeline_output_name = self._get_pipeline_output_name(output._data)
                if pipeline_output_name:
                    pipeline_output_dict[pipeline_output_name] = f"{node_name}.outputs.{node_output_name}"
        return pipeline_output_dict

    @classmethod
    def _get_pipeline_output_name(cls, name):
        if isinstance(name, Output):
            name = name.path
        expression = get_all_data_binding_expressions(name, ["parent", "outputs"])
        if expression:
            return extract_input_output_name_from_binding(expression[0])

    @property
    def pipeline_func_name(self):
        return self.pipeline_entity.display_name

    @property
    def component_node_strs(self):
        return [g.generate() for g in self._node_generators]

    @property
    def tpl_file(self):
        return self.TEMPLATE_PATH / "_pipeline_def.template"

    @property
    def pipeline_compute(self):
        if self.pipeline_entity.settings.default_compute:
            return self.pipeline_entity.settings.default_compute
        if self.pipeline_entity.compute:
            return self.pipeline_entity.compute
        return {}

    @property
    def entry_template_keys(self) -> list:
        return [
            "url",
            "contain_float_or_number",
            "azure_ai_ml_imports",
            "component_import",
            "dsl_pipeline_param_assignments",
            "pipeline_param_defines",
            "pipeline_func_name",
            "component_node_strs",
            "pipeline_outputs",
            "pipeline_param_assignments",
            "pipeline_compute",
            "pipeline_entity",
        ]
