import datetime
from enum import Enum
from typing import List, Literal, Optional, Union

from pydantic import BaseModel, Field

from .experiment import ExperimentResponse, PositiveLabel
from .model_config import ModelConfigResponse
from .utils import RootBaseModel


class LabelSentiment(str, Enum):
    positive = "positive"
    unset = "unset"
    negative = "negative"


class UserResponse(BaseModel):
    email_address: str = Field(
        title="Email address", description="The user's email address."
    )
    full_name: Optional[str] = Field(
        title="Full name", description="The user's full name."
    )


class FeedbackLabel(BaseModel):
    name: str = Field(
        title="Feedback label name", description="Name of feedback label."
    )
    sentiment: LabelSentiment = Field(
        default=LabelSentiment.unset,
        title="Feedback label sentiment",
        description="Sentiment of feedback label. If 'positive', the label will be treated as positive user feedback.",
    )  # Default value used for request model


class CategoricalFeedbackGroup(BaseModel):
    name: str = Field(
        title="Feedback group name", description="Name of feedback group."
    )
    labels: List[FeedbackLabel]
    type: Literal["categorical"] = Field(
        title="Type of feedback group",
        description="The feedback group's type. E.g. 'categorical'.",
    )


class TextFeedbackGroup(BaseModel):
    name: str = Field(
        title="Feedback group name", description="Name of feedback group."
    )
    type: Literal["text"] = Field(
        title="Type of feedback group",
        description="The feedback group's type. E.g. 'text'.",
    )


class FeedbackGroups(RootBaseModel):
    __root__: List[Union[TextFeedbackGroup, CategoricalFeedbackGroup]]


class ProjectResponse(BaseModel):
    id: str = Field(title="Project ID", description="Project ID")
    internal_id: int = Field(
        title="Internal project ID",
        description="Project ID for internal Humanloop use.",
    )
    name: str = Field(title="Project name", description="Unique project name.")
    active_experiment: Optional[ExperimentResponse] = Field(
        title="Active experiment",
        description="Experiment that has been set as the project's active deployment. "
        "At most one of active_experiment and active_model_config can be set.",
    )
    active_model_config: Optional[ModelConfigResponse] = Field(
        title="Active model configuration",
        description="Model configuration that has been set as the project's active deployment. "
        "At most one of active_experiment and active_model_config can be set.",
    )
    users: List[UserResponse] = Field(
        title="Project users",
        description="Users associated to the project.",
    )
    data_count: int = Field(
        title="Number of datapoints",
        description="The count of datapoints that have been logged to the project.",
    )

    feedback_groups: FeedbackGroups = Field(
        title="Feedback groups",
        description="The feedback groups that have been defined in the project.",
    )

    created_at: datetime.datetime
    updated_at: datetime.datetime


class CreateProjectRequest(BaseModel):
    name: str = Field(title="Project name", description="Unique project name.")


class UpdateProjectRequest(BaseModel):
    active_experiment_id: Optional[str] = Field(
        title="Active experiment ID",
        description="ID for an experiment to set as the project's active deployment. "
        "Starts with 'exp_'. "
        "At most one of 'active_experiment_id' and 'active_model_config_id' can be set.",
    )
    active_model_config_id: Optional[str] = Field(
        title="Active model configuration ID",
        description="ID for a model configuration to set as the project's active deployment. "
        "Starts with 'config_'. "
        "At most one of 'active_experiment_id' and 'active_model_config_id' can be set.",
    )
    positive_labels: Optional[List[PositiveLabel]] = Field(
        title="List of feedback labels to consider as positive actions",
        description="The full list of labels to treat as positive user feedback.",
    )
