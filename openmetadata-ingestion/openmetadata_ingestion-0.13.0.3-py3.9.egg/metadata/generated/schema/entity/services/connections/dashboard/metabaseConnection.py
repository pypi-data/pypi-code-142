# generated by datamodel-codegen:
#   filename:  entity/services/connections/dashboard/metabaseConnection.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import AnyUrl, BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr

from .. import connectionBasicType


class MetabaseType(Enum):
    Metabase = 'Metabase'


class MetabaseConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[MetabaseType] = Field(
        MetabaseType.Metabase, description='Service Type', title='Service Type'
    )
    username: str = Field(
        ...,
        description='Username to connect to Metabase. This user should have privileges to read all the metadata in Metabase.',
        title='Username',
    )
    password: Optional[CustomSecretStr] = Field(
        None, description='Password to connect to Metabase.', title='Password'
    )
    hostPort: AnyUrl = Field(
        ...,
        description='Host and Port of the Metabase instance.',
        title='Host and Port',
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
