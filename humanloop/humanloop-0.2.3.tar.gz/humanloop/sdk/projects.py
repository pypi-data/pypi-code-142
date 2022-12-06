from typing import Dict, List, Literal, Optional, Union

from humanloop.api.models.experiment import PositiveLabel
from humanloop.api.models.generic import PaginatedData
from humanloop.api.models.log import LogResponse
from humanloop.api.models.project import (
    CategoricalFeedbackGroup,
    CreateProjectRequest,
    FeedbackLabel,
    LabelSentiment,
    ProjectResponse,
    TextFeedbackGroup,
    UpdateProjectRequest,
)
from humanloop.sdk.init import _get_client


def get_projects(
    page: int = 0, size: int = 10, filter: Optional[str] = None
) -> PaginatedData[ProjectResponse]:
    """Retrieve a paginated list of projects associated to your user.

    Args:
        page: Page index
            Page offset for pagination
        size: Page size
            Page size for pagination. Number of projects to fetch.
        filter: Project name filter
            Case-insensitive filter for project name.
    """
    client = _get_client()
    return client.get_projects(page=page, size=size, filter=filter)


def get_project(project_id: str) -> ProjectResponse:
    """Get the project with the given ID.

    Args:
        project_id: Project ID
            String ID of project. Starts with `pr_`.
    """
    client = _get_client()
    return client.get_project(project_id=project_id)


def create_project(project: str) -> ProjectResponse:
    """Create a project with the specified name.

    An error will be raised if the user is already associated to a project with
    that name.

    Args:
        project: Project name
            Unique project name.
    """
    client = _get_client()
    return client.create_project(CreateProjectRequest(name=project))


def set_active_model_config(project_id: str, model_config_id: str) -> ProjectResponse:
    """Set the active model config for the project.

    This will unset the active experiment if one is set.

    Args:
        project_id: Project ID
            String ID of project. Starts with `pr_`.
    """
    client = _get_client()
    return client.update_project(
        project_id=project_id,
        update=UpdateProjectRequest(active_model_config_id=model_config_id),
    )


def set_active_experiment(project_id: str, experiment_id: str) -> ProjectResponse:
    """Set the active experiment for the project.

    This will unset the active model config if one is set.

    Args:
        project_id: Project ID
            String ID of project. Starts with `pr_`.
    """
    client = _get_client()
    return client.update_project(
        project_id=project_id,
        update=UpdateProjectRequest(active_experiment_id=experiment_id),
    )


def set_positive_labels(
    project_id: str, positive_labels: List[Union[PositiveLabel, Dict[str, str]]]
) -> ProjectResponse:
    """Set the feedback labels to be treated as positive user feedback used in
    calculating top-level project metrics.

    Args:
        project_id: Project ID
            String ID of project. Starts with `pr_`.
        positive_labels: List of labels to be considered as positive user feedback
            List of `{ "group": group, "label": label }` dicts.
    """
    client = _get_client()
    return client.update_project(
        project_id=project_id,
        update=UpdateProjectRequest(positive_labels=positive_labels),
    )


def remove_active_model_config(project_id: str) -> ProjectResponse:
    """Remove the project's active model config, if set.

    Args:
        project_id: Project ID
            String ID of project. Starts with `pr_`.
    """
    client = _get_client()
    return client.delete_active_model_config(project_id=project_id)


def remove_active_experiment(project_id: str) -> ProjectResponse:
    """Remove the project's active experiment, if set.

    Args:
        project_id: Project ID
            String ID of project. Starts with `pr_`.
    """
    client = _get_client()
    return client.delete_active_experiment(project_id=project_id)


def add_feedback_group(
    project_id: str,
    feedback_group: str,
    type: Literal["text", "categorical"],
    labels: Optional[List[str]] = None,
) -> List[Union[TextFeedbackGroup, CategoricalFeedbackGroup]]:
    """Add a new feedback group to your project.

    Feedback groups of type "text" and "categorical" are currently supported.
    When creating a feedback group of type "categorical", you can specify a
    list of labels to create.
    If creating a feedback group of type "text", "labels" should not be
    provided.
    """
    if type == "text" and labels is not None:
        raise ValueError(
            "Cannot create a feedback group of type text while specifying a list of labels."
        )

    if type == "text":
        groups = [TextFeedbackGroup(name=feedback_group, type=type)]
    elif type == "categorical":
        groups = [
            CategoricalFeedbackGroup(
                name=feedback_group,
                type=type,
                labels=[
                    FeedbackLabel(name=label, sentiment=LabelSentiment.unset)
                    for label in (labels or [])
                ],
            )
        ]
    else:
        raise ValueError(
            f"Unknown feedback group type. Should be one of 'text' or 'categorical'. Found: {type}"
        )

    client = _get_client()
    return client.add_feedback_labels_and_groups(
        project_id=project_id,
        groups=groups,
    ).__root__


def add_feedback_labels(
    project_id: str, feedback_group: str, labels: List[str]
) -> List[Union[TextFeedbackGroup, CategoricalFeedbackGroup]]:
    """Add feedback labels to a categorical feedback group"""
    client = _get_client()
    return client.add_feedback_labels_and_groups(
        project=project_id,
        groups=[
            CategoricalFeedbackGroup(
                name=feedback_group,
                type="categorical",
                labels=[
                    FeedbackLabel(name=label, sentiment=LabelSentiment.unset)
                    for label in labels
                ],
            )
        ],
    ).__root__


def export_datapoints(
    project_id: str, page: int = 0, size: int = 10
) -> PaginatedData[LogResponse]:
    """Export all logged datapoints associated to your project.

    Results are paginated and sorts the logs based on `created_at` in descending order.

    Args:
        project_id: Project ID
            String ID of project. Starts with `pr_`.
        page: Page index
            Page offset for pagination
        size: Page size
            Page size for pagination. Number of projects to fetch.
    """
    client = _get_client()
    return client.export_datapoints(project_id=project_id, page=page, size=size)


__all__ = [
    "get_projects",
    "get_project",
    "create_project",
    "set_active_model_config",
    "set_active_experiment",
    "remove_active_model_config",
    "remove_active_experiment",
    "add_feedback_group",
    "add_feedback_labels",
    "export_datapoints",
]
