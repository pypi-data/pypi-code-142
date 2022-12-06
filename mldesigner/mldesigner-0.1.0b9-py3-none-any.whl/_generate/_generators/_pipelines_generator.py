# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from pathlib import Path
from typing import Dict, List
from azure.ai.ml.entities import Component
from azure.ai.ml.entities._job.pipeline.pipeline_job import PipelineJob

from mldesigner._generate._generate_package import generate_pkg_logger
from mldesigner._generate._generators._pipeline_generator import PipelineGenerator
from mldesigner._generate._generators._module_generator import \
    get_unique_component_func_name, _get_selected_component_name
from mldesigner._export._cycle_validator import CycleValidator


def _pipeline_get_unique_component_func_names(components: List[Component]):
    """Try to return unique component func names, raise exception when duplicate component are found."""
    func_name_to_component = []
    name_version_to_func_name = {}

    for component in components:
        component_selected_name = _get_selected_component_name(component)
        name_version = f"{component_selected_name}:{component.version}"

        # use name_version to judge whether two components are same
        if name_version in name_version_to_func_name:
            func_name = name_version_to_func_name[name_version]
            func_name_to_component.append(func_name)
            continue

        name_candidate = get_unique_component_func_name(func_name_to_component, component)
        func_name_to_component.append(name_candidate)
        name_version_to_func_name[name_version] = name_candidate
    return func_name_to_component


class PipelinesGenerator:
    PIPELINE_FILE_NAME = "main.py"
    PIPELINE_INIT_NAME = "__init__.py"
    def __init__(
        self,
        pipeline_entity: PipelineJob,
        pipeline_name: str,
        pattern_to_components: Dict[str, Component],
        force_regenerate=False,
        ):
        self._name_to_component = pattern_to_components
        self._pipeline_name = pipeline_name

        # sort the nodes to sort the components
        self._sorted_nodes = CycleValidator.sort(list(pipeline_entity.jobs.values()))

        # we use specific key format
        self._sorted_components = []
        for node in self._sorted_nodes:
            component_str = node.component
            self._sorted_components.append(self._name_to_component[component_str])

        # use sorted() to get the same name as generated in _module_generator.py
        _sorted_component_with_index = [(component, i) for i, component in enumerate(self._sorted_components)]
        _components_sort_by_sorted = sorted(_sorted_component_with_index, key=lambda c: f"{c[0].name}:{c[0].version}")
        _components = [item[0] for item in _components_sort_by_sorted]

        # handle conflicts
        name_to_components_in_sort_order = _pipeline_get_unique_component_func_names(_components)
        name_to_components = name_to_components_in_sort_order.copy()
        for i, component_index in enumerate(_components_sort_by_sorted):
            index = component_index[1]
            name_to_components[index] = name_to_components_in_sort_order[i]

        self._pipeline_generator = PipelineGenerator(
            pipeline_entity=pipeline_entity,
            sorted_nodes=self._sorted_nodes,
            name_to_components=name_to_components,
        )

        self._force_regenerate = force_regenerate

    def generate(self, target_dir: Path):
        if not self._name_to_component:
            return
        target_pipeline_folder = target_dir / self._pipeline_name
        if target_pipeline_folder.exists():
            if not self._force_regenerate:
                msg = f"Skip generating pipeline {target_pipeline_folder.as_posix()} since it's already exists."
                generate_pkg_logger.warning(msg)
                return
        else:
            target_pipeline_folder.mkdir(parents=True)

        with open(target_pipeline_folder / self.PIPELINE_INIT_NAME, 'w') as f:
            f.close()
        self._pipeline_generator.generate_to_file(target_pipeline_folder / self.PIPELINE_FILE_NAME)
