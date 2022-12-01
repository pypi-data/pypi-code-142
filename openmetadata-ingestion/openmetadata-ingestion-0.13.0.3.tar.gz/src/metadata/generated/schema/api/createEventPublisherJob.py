# generated by datamodel-codegen:
#   filename:  api/createEventPublisherJob.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ..settings import eventPublisherJob


class CreateEventPublisherJob(BaseModel):
    class Config:
        extra = Extra.forbid

    publisherType: eventPublisherJob.PublisherType
    runMode: eventPublisherJob.RunMode
    entities: Optional[List[str]] = Field(
        ['all'], description='List of Entities to Reindex', unique_items=True
    )
    recreateIndex: Optional[bool] = Field(
        False, description='This schema publisher run modes.'
    )
    batchSize: Optional[int] = Field(
        100, description='Maximum number of events sent in a batch (Default 10).'
    )
    flushIntervalInSec: Optional[int] = Field(
        30,
        description='Maximum time to wait before sending request to ES in seconds(Default 30)',
    )
