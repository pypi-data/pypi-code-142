# generated by datamodel-codegen:
#   filename:  dataInsight/type/percentageOfEntitiesWithOwnerByType.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field, confloat

from ...type import basic


class PercentageOfEntitiesWithOwnerByType(BaseModel):
    class Config:
        extra = Extra.forbid

    timestamp: Optional[basic.Timestamp] = Field(None, description='timestamp')
    entityType: Optional[str] = Field(
        None, description='Type of entity. Derived from the entity class.'
    )
    hasOwnerFraction: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Decimal fraction of entity with an owner.'
    )
    hasOwner: Optional[float] = Field(
        None, description='Decimal fraction of entity with an owner.'
    )
    entityCount: Optional[float] = Field(
        None, description='Decimal fraction of entity with an owner.'
    )
