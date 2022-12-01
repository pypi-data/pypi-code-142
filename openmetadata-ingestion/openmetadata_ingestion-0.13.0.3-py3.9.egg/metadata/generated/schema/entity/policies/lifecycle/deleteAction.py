# generated by datamodel-codegen:
#   filename:  entity/policies/lifecycle/deleteAction.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field, conint


class LifecycleDeleteAction(BaseModel):
    class Config:
        extra = Extra.forbid

    daysAfterCreation: Optional[conint(ge=1)] = Field(
        None,
        description='Number of days after creation of the entity that the deletion should be triggered.',
    )
    daysAfterModification: Optional[conint(ge=1)] = Field(
        None,
        description='Number of days after last modification of the entity that the deletion should be triggered.',
    )
