# generated by datamodel-codegen:
#   filename:  entity/services/connections/metadata/amundsenConnection.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import AnyUrl, BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr

from .. import connectionBasicType


class AmundsenType(Enum):
    Amundsen = 'Amundsen'


class AmundsenConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[AmundsenType] = Field(
        AmundsenType.Amundsen, description='Service Type'
    )
    username: Optional[str] = Field(
        None, description='username to connect to the Amundsen Neo4j Connection.'
    )
    password: Optional[CustomSecretStr] = Field(
        None, description='password to connect to the Amundsen Neo4j Connection.'
    )
    hostPort: Optional[AnyUrl] = Field(
        None,
        description='Host and port of the Amundsen Neo4j Connection.',
        title='Host and Port',
    )
    maxConnectionLifeTime: Optional[int] = Field(
        '50',
        description='Maximum connection lifetime for the Amundsen Neo4j Connection.',
    )
    validateSSL: Optional[bool] = Field(
        'false', description='Enable SSL validation for the Amundsen Neo4j Connection.'
    )
    encrypted: Optional[bool] = Field(
        'false', description='Enable encryption for the Amundsen Neo4j Connection.'
    )
    modelClass: Optional[str] = Field(
        None, description='Model Class for the Amundsen Neo4j Connection.'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = None
