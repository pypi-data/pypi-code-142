# generated by datamodel-codegen:
#   filename:  entity/services/connections/metadata/atlasConnection.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import AnyUrl, BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr

from .. import connectionBasicType


class AtlasType(Enum):
    Atlas = 'Atlas'


class AtlasConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[AtlasType] = Field(AtlasType.Atlas, description='Service Type')
    username: Optional[str] = Field(
        None,
        description='username to connect  to the Atlas. This user should have privileges to read all the metadata in Atlas.',
    )
    password: Optional[CustomSecretStr] = Field(
        None, description='password to connect  to the Atlas.'
    )
    hostPort: Optional[AnyUrl] = Field(
        None, description='Host and port of the data source.', title='Host and Port'
    )
    entityTypes: Optional[str] = Field(
        None, description='entity types of the data source.'
    )
    serviceType: Optional[str] = Field(
        None, description='service type of the data source.'
    )
    atlasHost: Optional[str] = Field(None, description='Atlas Host of the data source.')
    dbService: Optional[str] = Field(
        None, description='source database of the data source.'
    )
    messagingService: Optional[str] = Field(
        None, description='messaging service source of the data source.'
    )
    database: Optional[str] = Field(
        None,
        description='Database of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single database. When left blank , OpenMetadata Ingestion attempts to scan all the databases in Atlas.',
    )
    connectionOptions: Optional[connectionBasicType.ConnectionOptions] = None
    connectionArguments: Optional[connectionBasicType.ConnectionArguments] = None
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = None
