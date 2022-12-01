# generated by datamodel-codegen:
#   filename:  configuration/slackEventPubConfiguration.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ..type import changeEvent


class SlackPublisherConfiguration(BaseModel):
    class Config:
        extra = Extra.forbid

    name: str = Field(..., description='Publisher Name')
    webhookUrl: Optional[str] = Field(None, description='Webhook URL')
    openMetadataUrl: Optional[str] = Field(None, description='OpenMetadata URL')
    filters: List[changeEvent.EventFilter] = Field(..., description='Filters')
    batchSize: Optional[int] = Field(10, description='Batch Size')
