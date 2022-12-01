# generated by datamodel-codegen:
#   filename:  entity/services/connections/dashboard/redashConnection.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import AnyUrl, BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr

from .. import connectionBasicType


class RedashType(Enum):
    Redash = 'Redash'


class RedashConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[RedashType] = Field(
        RedashType.Redash, description='Service Type', title='Service Type'
    )
    username: str = Field(..., description='Username for Redash', title='Username')
    hostPort: AnyUrl = Field(
        ..., description='URL for the Redash instance', title='Host and Port'
    )
    apiKey: CustomSecretStr = Field(
        ..., description='API key of the redash instance to access.', title='API Key'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
