from typing import List, Optional, Union

from pydantic import BaseModel, Field

from .utils import RootBaseModel


class FeedbackResponse(BaseModel):
    id: str = Field(
        title="Feedback ID",
        description="String ID of user feedback. Starts with `ann_`.",
    )
    label: Optional[str] = Field(
        title="Label",
        description="A categorical label to characterize the type of feedback. "
        "Only one of `label` or `text` will be populated for each feedback.",
    )
    text: Optional[str] = Field(
        title="Text",
        description="Text feedback. Can be used to record model corrections from "
        "your users. "
        "Only one of `label` or `text` will be populated for each feedback.",
    )
    group: str = Field(
        title="Feedback group",
        description="Name of feedback group this feedback belongs to.",
    )
    data_id: str = Field(
        title="Datapoint ID",
        description="String ID of logged datapoint that this feedback pertains to. Starts with `data_`.",
    )
    user: Optional[str] = Field(
        title="User", description="A unique reference to who provided the feedback."
    )


class ListFeedbackResponse(RootBaseModel):
    __root__: Union[FeedbackResponse, List[FeedbackResponse]]
