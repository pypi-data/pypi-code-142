# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/postgresConnection.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr

from .. import connectionBasicType


class PostgresType(Enum):
    Postgres = 'Postgres'


class PostgresScheme(Enum):
    postgresql_psycopg2 = 'postgresql+psycopg2'


class PostgresConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[PostgresType] = Field(
        PostgresType.Postgres, description='Service Type', title='Service Type'
    )
    scheme: Optional[PostgresScheme] = Field(
        PostgresScheme.postgresql_psycopg2,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    username: str = Field(
        ...,
        description='Username to connect to Postgres. This user should have privileges to read all the metadata in Postgres.',
        title='Username',
    )
    password: Optional[CustomSecretStr] = Field(
        None, description='Password to connect to Postgres.', title='Password'
    )
    hostPort: str = Field(
        ..., description='Host and port of the Postgres service.', title='Host and Port'
    )
    database: Optional[str] = Field(
        None,
        description='Database of the data source. This is optional parameter, if you would like to restrict the metadata reading to a single database. When left blank, OpenMetadata Ingestion attempts to scan all the databases.',
        title='Database',
    )
    connectionOptions: Optional[connectionBasicType.ConnectionOptions] = Field(
        None, title='Connection Options'
    )
    connectionArguments: Optional[connectionBasicType.ConnectionArguments] = Field(
        None, title='Connection Arguments'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
    supportsUsageExtraction: Optional[
        connectionBasicType.SupportsUsageExtraction
    ] = None
    supportsLineageExtraction: Optional[
        connectionBasicType.SupportsLineageExtraction
    ] = None
    supportsProfiler: Optional[connectionBasicType.SupportsProfiler] = Field(
        None, title='Supports Profiler'
    )
    supportsDatabase: Optional[connectionBasicType.SupportsDatabase] = Field(
        None, title='Supports Profiler'
    )
    supportsQueryComment: Optional[connectionBasicType.SupportsQueryComment] = Field(
        None, title='Supports Query Comment'
    )
