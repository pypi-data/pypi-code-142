# generated by datamodel-codegen:
#   filename:  type/dailyCount.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field, conint

from . import basic


class DailyCountOfSomeMeasurement(BaseModel):
    class Config:
        extra = Extra.forbid

    count: conint(ge=0) = Field(
        ..., description='Daily count of a measurement on the given date.'
    )
    date: basic.Date
