# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from pathlib import Path
from typing import List

from azure.ai.ml import MLClient
from azure.ai.ml.entities._builders import Command, Pipeline

from mldesigner._exceptions import UserErrorException
from mldesigner._export._parse_url import _parse_designer_url
from mldesigner._generate._generators._pipeline_code_generator import (
    PipelineCodeGenerator,
)
from mldesigner._utils import (
    _is_arm_id,
    _is_name_version,
    _is_name_label,
    get_credential_auth,
    AMLVersionedArmId,
    parse_name_version,
)


def _load_component_from_pipeline(client, job_entity):
    name2component_dict = {}
    for node in job_entity.jobs.values():  # pylint: disable=no-member
        # pylint: disable=unidiomatic-typecheck
        if isinstance(node, Command):
            component_str = node.component
            if _is_arm_id(component_str):
                arm_id = AMLVersionedArmId(component_str)
                component = client.components.get(name=arm_id.asset_name, version=arm_id.asset_version)
            elif _is_name_version(component_str):
                asset_name, asset_version = parse_name_version(component_str)
                component = client.components.get(name=asset_name, version=asset_version)
            elif _is_name_label(component_str):
                arm_id = AMLVersionedArmId(component_str)
                component = client.components.get(name=arm_id.asset_name, label=arm_id.asset_version)
            else:
                raise UserErrorException(
                    f"The component:{node.component} of node {node.name} is invalid."
                )
            name2component_dict[component_str] = component
        elif isinstance(node, Pipeline):
            # TODO: generate code for pipeline with subgraphs
            raise UserErrorException("Generating code for pipeline with subgraphs is not supported currently")
        else:
            node_type = type(node)
            raise UserErrorException(f"Generating code for pipeline with {node_type} node is not supported currently")
    return name2component_dict


def _export(source: str, include_components: List[str] = None):  # pylint: disable=unused-argument
    """Export pipeline source to code.

    :param source: Pipeline job source, currently supported format is pipeline run URL
    :param include_components: Included components to download snapshot.
        Use * to export all components,
        Or list of components used in pipeline.
        If not specified, all components in pipeline will be exported without downloading snapshot.
    :return:
    """
    # get subscription_id, resource_group, workspace_name, run_id from url
    (
        subscription_id,
        resource_group,
        workspace_name,
        draft_id,
        run_id,
        endpoint_id,
        published_pipeline_id,
    ) = _parse_designer_url(source)

    # validate: raise error when the job type is not pipeline job
    if draft_id:
        raise UserErrorException("Invalid url. Export pipeline draft is not supported.")
    if endpoint_id:
        raise UserErrorException("Invalid url. Export pipeline endpoint is not supported.")
    if published_pipeline_id:
        raise UserErrorException("Invalid url. Export published pipeline is not supported.")

    credential = get_credential_auth()
    # get pipeline entity
    client = MLClient(
        credential=credential,
        resource_group_name=resource_group,
        subscription_id=subscription_id,
        workspace_name=workspace_name,
    )
    job_entity = client.jobs.get(run_id)

    # validate: raise error when the PipelineJob.jobs contain no nodes
    if len(job_entity.jobs) == 0:
        raise UserErrorException("Unsupported Pipeline Job: failed to retrieve child jobs.")

    pattern_to_components = _load_component_from_pipeline(client, job_entity)
    pipeline_code_generator = PipelineCodeGenerator(
        asset=source,
        pipeline_entity=job_entity,
        target_dir=Path("."),
        force_regenerate=False,
        pattern_to_components=pattern_to_components,
    )
    pipeline_code_generator.generate(target_dir=Path(f"./{str(job_entity.display_name)}"))
