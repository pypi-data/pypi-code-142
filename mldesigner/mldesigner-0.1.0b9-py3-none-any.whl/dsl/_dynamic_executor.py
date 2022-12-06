# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import inspect
import os
from pathlib import Path

from mldesigner import Output
from mldesigner._component_executor import execute_logger
from mldesigner._constants import (
    IMPORT_AZURE_AI_ML_ERROR_MSG,
    AssetTypes,
    DynamicDefaultEnv,
    ExecutorTypes,
    SupportedParameterTypes,
)
from mldesigner._dependent_component_executor import DependentComponentExecutor
from mldesigner._exceptions import ImportException, RequiredParamParsingError, SystemErrorException, UserErrorException
from mldesigner._utils import inject_sys_path

try:
    from azure.ai.ml import Input, MLClient
    from azure.ai.ml.constants._component import IOConstants
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml.entities import Environment, PipelineComponent, PipelineJob
    from azure.ai.ml.entities._inputs_outputs import GroupInput, is_group
    from azure.ai.ml.identity import AzureMLOnBehalfOfCredential
except ImportError:
    raise ImportException(IMPORT_AZURE_AI_ML_ERROR_MSG)

asset_types = AssetTypes()


class DynamicExecutor(DependentComponentExecutor):
    """Currently dynamic executor will only work in compile time."""

    PIPELINE_COMPONENT_KEY = "azureml.pipelines.subPipelineComponent"
    PIPELINE_COMPONENT_ID_KEY = "azureml.pipelines.dynamicSubPipelineComponentId"
    DYNAMIC_COMPONENT_PROPERTY_KEY = "azureml.pipelines.dynamic"
    SUPPORTED_RETURN_PARAM_TYPES = [getattr(asset_types, k) for k in dir(asset_types) if k.isupper()] + list(
        SupportedParameterTypes
    )

    def __init__(self, **kwargs):
        """Initialize a DynamicExecutor with a function to enable calling the function with command line args."""
        super(DynamicExecutor, self).__init__(**kwargs)

        # Add dynamic hint to properties
        properties = self._entity_args.get("properties", {})
        properties[self.DYNAMIC_COMPONENT_PROPERTY_KEY] = "true"
        self._entity_args["properties"] = properties
        self._type = ExecutorTypes.DYNAMIC
        # store pipeline component meta in executor for debug
        self._execution_result = {}

    @classmethod
    def _update_outputs_to_args(cls, args, outputs):
        # won't add outputs to command args for dynamic executor
        pass

    @classmethod
    def _get_outputs_from_return_annotation(cls, func):
        """Convert return annotation to Outputs.

        Supported type:
            1. dsl output type. func() -> Output(type='boolean', is_control=True) will be keep as they are.
            2. primitive output type, such as Output(type='string', is_control=True) will be converted to Output type.
            3. group type. func()->OutputClass will add output1 and output2 to component defined, with OutputClass:
                @group
                class OutputClass:
                    output1: bool
                    output2: Boolean(is_control=True)

        Note:
            - Single output without dataclass will be named as 'output'.
              If there are duplicate outputs, exception will be raised. i.e.
                func(output: Output)->Output  # Exception raised.
            - Nested dataclass object is not support.
        """
        # TODO: move this logic to ExecutorBase when @group is supported in all executors
        return_annotation = inspect.signature(func).return_annotation

        if is_group(return_annotation):
            fields = getattr(return_annotation, IOConstants.GROUP_ATTR_NAME)
            fields_mapping = {}
            for name, annotation in fields.values.items():
                if isinstance(annotation, GroupInput):
                    raise UserErrorException("Nested group return annotation is not supported.")
                # normalize annotation since currently annotation in @group will be converted to Input
                if isinstance(annotation, Input):
                    annotation = Output(type=annotation.type)
                fields_mapping.update(
                    cls._get_standard_output_annotation(annotation=annotation, func=func, output_name=name)
                )
            cls._unify_return_annotations(return_annotations=fields_mapping)
            return fields_mapping

        return super(DynamicExecutor, cls)._get_outputs_from_return_annotation(func=func)

    def _update_outputs_to_execution_args(self, args, param):
        # won't add outputs to execution args for dynamic executor
        pass

    @classmethod
    def _validate_unprovided_params(cls, type_name, param):
        # Note: unprovided outputs won't raise exception
        if type_name == "Input" and not param.optional:
            raise RequiredParamParsingError(name=param.name)

    def execute(self, args: dict = None):
        """Execute the dynamic component with arguments."""
        # pylint: disable=protected-access,
        self._execution_result = {}
        original_func = self._func

        execute_logger.info("Provided args: '%s'", args)
        args = self._parse(args)
        execute_logger.info("Parsed args: '%s'", args)
        param_args, return_args = {}, {}
        # Split outputs specified by param and by return annotation
        for k, v in args.items():
            if k in self._return_mapping:
                return_args[k] = v
            else:
                param_args[k] = v

        # In case component function import other modules inside the function, need file directory in sys.path
        file_dir = str(Path(self._entry_file).parent)
        with inject_sys_path(file_dir):
            execute_logger.info("====================== User Logs ======================")
            # "compile" dynamic pipeline to pipeline job
            pipeline_job = pipeline(original_func)(**args)
            execute_logger.info("==================== User Logs End ====================")

        if not isinstance(pipeline_job, PipelineJob):
            raise SystemErrorException(
                f"Expecting compiled dynamic subgraph to be a PipelineJob, got {type(pipeline_job)} instead."
            )

        # 1. extract pipeline component.
        pipeline_component = pipeline_job.component

        # 2. validate pipeline component.
        try:
            pipeline_component_dict = pipeline_component._to_dict()
        except Exception as e:  # pylint: disable=broad-except
            execute_logger.error("Failed to serialize pipeline component: %s", e)
            pipeline_component_dict = {}

        # return the generated pipeline component dict and log in stream outputs for debugging
        self._execution_result[self.PIPELINE_COMPONENT_KEY] = pipeline_component_dict
        execute_logger.info("Generated pipeline component: %s", pipeline_component_dict)
        pipeline_component_inputs = pipeline_component_dict.get("inputs")
        pipeline_component_outputs = pipeline_component_dict.get("outputs")

        try:
            command_component_dict = self.component._to_dict()
        except Exception as e:  # pylint: disable=broad-except
            execute_logger.error("Failed to serialize command component: %s", e)
            command_component_dict = {}

        command_component_inputs = command_component_dict.get("inputs")
        command_component_outputs = command_component_dict.get("outputs")

        # warning if created pipeline component has different interface as command component
        error_message = (
            "Generated pipeline component has different {name} with original dynamic component. "
            "Pipeline component {name}: {field}, dynamic subgraph {name}: {field2}"
        )

        if pipeline_component_inputs != command_component_inputs:
            # pylint: disable=logging-format-interpolation
            execute_logger.warning(
                error_message.format(name="inputs", field=pipeline_component_inputs, field2=command_component_inputs)
            )
        if pipeline_component_outputs != command_component_outputs:
            # pylint: disable=logging-format-interpolation
            execute_logger.warning(
                error_message.format(name="outputs", field=pipeline_component_outputs, field2=command_component_outputs)
            )

        # 3. create pipeline component if is online run.
        if self._is_online_run():
            pipeline_component = self._create_pipeline_component(pipeline_component)
            # add created pipeline component id to execution result for debug
            self._execution_result[self.PIPELINE_COMPONENT_ID_KEY] = pipeline_component.id
            execute_logger.info("Created pipeline component: %s", pipeline_component.id)

        execute_logger.info("==================== System Logs End ====================")
        # executor won't write anything to command outputs
        # DCM will make sure inner pipeline jobs output bind to this command outputs

        return {}

    def _create_pipeline_component(self, pipeline_component: PipelineComponent) -> PipelineComponent:
        """Create pipeline component using obo token, return created pipeline component."""
        execute_logger.info("Creating pipeline component")

        # step1: connect client with obo token
        ml_client = self._get_ml_client()

        # step2: create anonymous pipeline component
        pipeline_component = ml_client.components.create_or_update(pipeline_component, is_anonymous=True)

        # step3: write component id to run history
        self._write_properties_to_run_history({self.PIPELINE_COMPONENT_ID_KEY: pipeline_component.id})

        execute_logger.info("Finished create pipeline component: %s", pipeline_component.id)
        return pipeline_component

    @classmethod
    def _is_online_run(cls):
        """Check if the run is online."""
        # TODO: find a better way
        return os.getenv("AZUREML_RUN_ID") is not None

    @classmethod
    def _get_ml_client(cls):
        # May return a different one if executing in local
        return MLClient(
            workspace_name=os.getenv("AZUREML_ARM_WORKSPACE_NAME"),
            subscription_id=os.getenv("AZUREML_ARM_SUBSCRIPTION"),
            resource_group_name=os.getenv("AZUREML_ARM_RESOURCEGROUP"),
            credential=AzureMLOnBehalfOfCredential(),
        )

    @classmethod
    def _get_default_env(cls):
        """Return default environment."""
        return Environment(image=DynamicDefaultEnv.IMAGE, conda_file=DynamicDefaultEnv.CONDA_FILE)
