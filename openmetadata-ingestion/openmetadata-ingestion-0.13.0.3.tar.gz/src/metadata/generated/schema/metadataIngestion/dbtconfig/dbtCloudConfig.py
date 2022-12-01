# generated by datamodel-codegen:
#   filename:  metadataIngestion/dbtconfig/dbtCloudConfig.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr


class DbtCloudConfig(BaseModel):
    class Config:
        extra = Extra.forbid

    dbtCloudAuthToken: CustomSecretStr = Field(
        ...,
        description='DBT cloud account authentication token',
        title='DBT Cloud Authentication Token',
    )
    dbtCloudAccountId: str = Field(
        ..., description='DBT cloud account Id', title='DBT Cloud Account Id'
    )
    dbtCloudProjectId: Optional[str] = Field(
        None,
        description="In case of multiple projects in a DBT cloud account, specify the project's id from which you want to extract the DBT run artifacts",
        title='DBT Cloud Project Id',
    )
    dbtUpdateDescriptions: Optional[bool] = Field(
        False,
        description='Optional configuration to update the description from DBT or not',
    )
