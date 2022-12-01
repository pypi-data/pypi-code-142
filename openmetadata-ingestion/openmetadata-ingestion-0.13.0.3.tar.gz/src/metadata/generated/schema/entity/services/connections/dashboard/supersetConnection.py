# generated by datamodel-codegen:
#   filename:  entity/services/connections/dashboard/supersetConnection.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, Optional

from pydantic import AnyUrl, BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr

from .. import connectionBasicType


class SupersetType(Enum):
    Superset = 'Superset'


class SupersetConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[SupersetType] = Field(
        SupersetType.Superset, description='Service Type', title='Service Type'
    )
    hostPort: AnyUrl = Field(
        ..., description='URL for the superset instance.', title='Host and Port'
    )
    username: str = Field(..., description='Username for Superset.', title='Username')
    password: Optional[CustomSecretStr] = Field(
        None, description='Password for Superset.', title='Password'
    )
    provider: Optional[str] = Field(
        'db',
        description="Authentication provider for the Superset service. For basic user/password authentication, the default value `db` can be used. This parameter is used internally to connect to Superset's REST API.",
        title='Provider',
    )
    connectionOptions: Optional[Dict[str, Any]] = Field(
        None,
        description='Additional connection options that can be sent to service during the connection.',
        title='Connection Options',
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
