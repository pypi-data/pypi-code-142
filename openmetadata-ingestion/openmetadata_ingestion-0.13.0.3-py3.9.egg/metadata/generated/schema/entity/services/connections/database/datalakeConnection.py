# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/datalakeConnection.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Extra, Field

from .....security.credentials import awsCredentials, gcsCredentials
from .. import connectionBasicType


class DatalakeType(Enum):
    Datalake = 'Datalake'


class S3Config(BaseModel):
    securityConfig: Optional[awsCredentials.AWSCredentials] = Field(
        None, title='DataLake S3 Security Config'
    )


class GCSConfig(BaseModel):
    securityConfig: Optional[gcsCredentials.GCSCredentials] = Field(
        None, title='DataLake GCS Security Config'
    )


class DatalakeConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[DatalakeType] = Field(
        DatalakeType.Datalake, description='Service Type', title='Service Type'
    )
    configSource: Union[S3Config, GCSConfig] = Field(
        ...,
        description='Available sources to fetch files.',
        title='DataLake Configuration Source',
    )
    bucketName: Optional[str] = Field(
        '', description='Bucket Name of the data source.', title='Bucket Name'
    )
    prefix: Optional[str] = Field(
        '', description='Prefix of the data source.', title='Prefix'
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
