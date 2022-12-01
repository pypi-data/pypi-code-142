# generated by datamodel-codegen:
#   filename:  type/queryParserData.json
#   timestamp: 2022-12-01T12:36:50+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Extra, Field


class ParsedData(BaseModel):
    tables: List[str] = Field(..., description='List of tables used in query')
    databaseName: Optional[str] = Field(
        None, description='Database associated with the table in the query'
    )
    joins: Optional[Dict[str, Any]] = Field(
        None,
        description='Maps each parsed table name of a query to the join information',
    )
    sql: str = Field(..., description='SQL query')
    serviceName: str = Field(
        ..., description='Name that identifies this database service.'
    )
    userName: Optional[str] = Field(
        None, description='Name of the user that executed the SQL query'
    )
    date: Optional[str] = Field(None, description='Date of execution of SQL query')
    databaseSchema: Optional[str] = Field(
        None, description='Database schema of the associated with query'
    )


class QueryParserData(BaseModel):
    class Config:
        extra = Extra.forbid

    parsedData: Optional[List[ParsedData]] = None
