# generated by datamodel-codegen:
#   filename:  type/schedule.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from . import basic


class Schedule(BaseModel):
    class Config:
        extra = Extra.forbid

    startDate: Optional[basic.DateTime] = Field(
        None, description='Start date and time of the schedule.'
    )
    repeatFrequency: Optional[basic.Duration] = Field(
        None,
        description="Repeat frequency in ISO 8601 duration format. Example - 'P23DT23H'.",
    )
