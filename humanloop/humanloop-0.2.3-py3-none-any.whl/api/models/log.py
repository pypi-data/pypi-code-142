import datetime
from typing import List, Optional, Union

from pydantic import BaseModel, Field, validator

from .model_config import ModelConfig, ProjectModelConfigResponse
from .utils import KeyValues, RootBaseModel


class Feedback(BaseModel):
    group: str = Field(
        title="Feedback group",
        description="Name of feedback group this feedback belongs to.",
    )
    label: Optional[str] = Field(
        title="Label",
        description="A categorical label to characterize the type of feedback. "
        "Only one of `label` or `text` should be provided for each feedback.",
    )
    text: Optional[str] = Field(
        title="Text",
        description="Text feedback. Can be used to record model corrections from "
        "your users. Only one of `label` or `text` should be provided "
        "for each feedback.",
    )
    data_id: Optional[str] = Field(
        title="Datapoint ID",
        description="ID to associate the feedback to a previously logged datapoint."
        "When providing instant feedback as part of the hl.log(...) call "
        "you don't need to provide a data_id.",
    )
    user: Optional[str] = Field(
        title="User",
        description="A unique identifier to who provided the feedback. "
        "This gets passed through to the provider as required.",
    )

    created_at: Optional[datetime.datetime] = Field(
        title="Created at",
        description="Timestamp for when the feedback was created. "
        "If not provided, the time the call was made will be used "
        "as a timestamp.",
    )

    @validator("text")
    def check_label_or_text(cls, v, values):
        if values["label"] is not None and v:
            raise ValueError(
                "Only one of label or text should be provided "
                "for each instance of feedback"
            )
        return v


class ListFeedbackRequest(RootBaseModel):
    __root__: Union[Feedback, List[Feedback]]


class Log(BaseModel):
    project: str = Field(
        title="Project name",
        description="Unique project name. If it does not exist, a new project will "
        "be created.",
    )
    trial_id: Optional[str] = Field(
        title="Trial ID",
        description="Unique ID of trial to associate to a log to inform an experiment.",
    )
    inputs: KeyValues = Field(
        title="Model input data",
        description="List of (name, value) pairs for the inputs used by your prompt "
        "template, or directly by your model.",
    )
    output: str = Field(
        title="Model output",
        description="Generated output from your model for the provided inputs.",
    )
    source: Optional[str] = Field(
        title="Source of generation",
        description="What was source of the model used for this generation? "
        "e.g. website-landing-page",
    )
    model_config: Optional[ModelConfig] = Field(
        title="Model config",
        description="The model config used for this generation",
    )
    metadata: Optional[KeyValues] = Field(
        title="Metadata",
        description="Any additional metadata that you would like to log for reference.",
    )
    feedback: Optional[Union[Feedback, List[Feedback]]] = Field(
        title="Feedback labels",
        description="Optional parameter to provide feedback with your logged datapoint.",
    )
    created_at: Optional[datetime.datetime] = Field(
        title="Created at",
        description="Timestamp for when the log was created. "
        "If not provided, the time the log call was made will be used "
        "as a timestamp.",
    )


class ListLogRequest(RootBaseModel):
    __root__: Union[Log, List[Log]]


class CreateLogResponse(BaseModel):
    id: str = Field(
        title="Datapoint ID",
        description="String ID of logged datapoint. Starts with `data_`.",
    )
    project_id: str = Field(
        title="Project ID",
        description="String ID of project the datapoint belongs to. Starts with `pr_`.",
    )


class ListCreateLogResponse(RootBaseModel):
    __root__: Union[CreateLogResponse, List[CreateLogResponse]]


class LogResponse(Log):
    id: str = Field(
        title="Datapoint ID",
        description="String ID of logged datapoint. Starts with `data_`.",
    )
    project_id: str = Field(
        title="Project ID",
        description="String ID of project the datapoint belongs to. Starts with `pr_`.",
    )
    inputs: KeyValues = Field(
        title="Model input data",
        description="List of (name, value) pairs for the inputs used by your prompt "
        "template, or directly by your model.",
    )
    output: str = Field(
        title="Model output",
        description="Generated output from your model for the provided inputs.",
    )
    source: Optional[str] = Field(
        title="Source of generation",
        description="What was source of the model used for this generation? "
        "e.g. website-landing-page",
    )
    model_config: Optional[ProjectModelConfigResponse] = Field(
        title="Model config",
        description="The model config used for this generation",
    )
    metadata: Optional[KeyValues] = Field(
        title="Metadata",
        description="Additional metadata logged for reference.",
    )
    feedback: Optional[Union[Feedback, List[Feedback]]] = Field(
        title="Feedback",
        description="Feedback associated to the datapoint.",
    )
    created_at: Optional[datetime.datetime] = Field(
        title="Created at", description="Timestamp for when the log was created."
    )
