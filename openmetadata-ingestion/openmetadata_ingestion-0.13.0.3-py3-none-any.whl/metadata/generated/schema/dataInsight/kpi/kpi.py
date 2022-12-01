# generated by datamodel-codegen:
#   filename:  dataInsight/kpi/kpi.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic, entityHistory, entityReference
from . import basic as basic_1


class Kpi(BaseModel):
    class Config:
        extra = Extra.forbid

    id: Optional[basic.Uuid] = Field(
        None, description='Unique identifier of this KPI Definition instance.'
    )
    name: basic.EntityName = Field(
        ..., description='Name that identifies this KPI Definition.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this KPI Definition.'
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    description: basic.Markdown = Field(
        ..., description='Description of the KpiObjective.'
    )
    metricType: basic_1.KpiTargetType
    dataInsightChart: entityReference.EntityReference = Field(
        ..., description='Data Insight Chart Referred by this Kpi Objective.'
    )
    targetDefinition: List[basic_1.KpiTarget] = Field(
        ..., description='Metrics from the chart and the target to achieve the result.'
    )
    kpiResult: Optional[basic_1.KpiResult] = Field(
        None, description='Result of the Kpi'
    )
    startDate: basic.Timestamp = Field(..., description='Start Date for the KPIs')
    endDate: basic.Timestamp = Field(..., description='End Date for the KPIs')
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this KPI definition.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
