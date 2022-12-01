# generated by datamodel-codegen:
#   filename:  api/dataInsight/createDataInsightChart.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...dataInsight import dataInsightChart
from ...type import basic, entityReference


class CreateDataInsightChart(BaseModel):
    class Config:
        extra = Extra.forbid

    name: basic.EntityName = Field(
        ..., description='Name that identifies this data insight chart.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name the data insight chart.'
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of the data insight chart.'
    )
    dataIndexType: Optional[dataInsightChart.DataReportIndex] = Field(
        None, description='Elasticsearch index name'
    )
    dimensions: Optional[List[dataInsightChart.ChartParameterValues]] = Field(
        None, description='Dimensions of the chart'
    )
    metrics: Optional[List[dataInsightChart.ChartParameterValues]] = Field(
        None, description='Metrics of the chart'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this chart'
    )
