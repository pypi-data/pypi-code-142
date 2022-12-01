# generated by datamodel-codegen:
#   filename:  entity/services/connections/serviceConnection.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from typing import Optional, Union

from pydantic import BaseModel, Extra, Field

from .. import (
    dashboardService,
    databaseService,
    messagingService,
    metadataService,
    mlmodelService,
    pipelineService,
)


class ServiceConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Union[
        dashboardService.DashboardConnection,
        databaseService.DatabaseConnection,
        messagingService.MessagingConnection,
        metadataService.MetadataConnection,
        pipelineService.PipelineConnection,
        mlmodelService.MlModelConnection,
    ] = Field(..., description='Supported services')


class ServiceConnectionModel(BaseModel):
    class Config:
        extra = Extra.forbid

    serviceConnection: Optional[ServiceConnection] = Field(
        None, description='Service Connection.'
    )
