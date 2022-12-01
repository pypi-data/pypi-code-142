# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/athenaConnection.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import AnyUrl, BaseModel, Extra, Field

from .....security.credentials import awsCredentials
from .. import connectionBasicType


class AthenaType(Enum):
    Athena = 'Athena'


class AthenaScheme(Enum):
    awsathena_rest = 'awsathena+rest'


class AthenaConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[AthenaType] = Field(
        AthenaType.Athena, description='Service Type', title='Service Type'
    )
    scheme: Optional[AthenaScheme] = Field(
        AthenaScheme.awsathena_rest,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    awsConfig: awsCredentials.AWSCredentials = Field(
        ..., title='AWS Credentials Configuration'
    )
    s3StagingDir: AnyUrl = Field(
        ...,
        description='S3 Staging Directory. Example: s3://postgres/input/',
        title='S3 Staging Directory',
    )
    workgroup: str = Field(
        ..., description='Athena workgroup.', title='Athena Workgroup'
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
    supportsProfiler: Optional[connectionBasicType.SupportsProfiler] = Field(
        None, title='Supports Profiler'
    )
