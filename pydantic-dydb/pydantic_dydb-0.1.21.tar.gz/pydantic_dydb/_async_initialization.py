from typing import Any, Optional

import pydantic
from minimal_dydb import AsyncDynamoDB, CredentialManagerBase, auto_credential_manager

from pydantic_dydb import _json


class _AsyncTableData(pydantic.BaseModel):
    table_name: pydantic.constr(min_length=1)
    region: pydantic.constr(min_length=1)
    hash_key: pydantic.constr(min_length=1)
    range_key: Optional[pydantic.constr(min_length=1)]
    dydb: Any
    delimiter: pydantic.constr(min_length=1)


__table_data = None


def get_async_table_data() -> _AsyncTableData:
    if __table_data is None:
        raise Exception("Table data should not be done, run the async init")
    return __table_data


class InitArgs(pydantic.BaseModel):
    table_name: pydantic.constr(min_length=1)
    region_name: pydantic.constr(min_length=1)
    credential_manager: Optional[Any]
    endpoint: Optional[pydantic.HttpUrl]
    delimiter: pydantic.constr(min_length=1)


async def async_init(
    *,
    table_name: str,
    region_name: str,
    credential_manager: Optional[CredentialManagerBase] = None,
    endpoint: Optional[str] = None,
    delimiter: Optional[str] = ";",
):
    args = InitArgs(
        table_name=table_name,
        region_name=region_name,
        credential_manager=credential_manager,
        endpoint=endpoint,
        delimiter=delimiter,
    )

    if args.endpoint is None:
        endpoint = f"https://dynamodb.{region_name}.amazonaws.com"

    if credential_manager is None:
        credential_manager = auto_credential_manager()

    assert isinstance(
        credential_manager, CredentialManagerBase
    ), f"expected {credential_manager=} to be object of inherited from CredentialManagerBase"

    dydb = AsyncDynamoDB(
        region=region_name,
        credential_manager=credential_manager,
        endpoint=endpoint,
    )

    table_request_json = _json.byte_dumps({"TableName": table_name})
    response = await dydb.describe_table(table_request_json)
    response.raise_for_status()
    table_json = _json.loads(response.content)
    kwargs = {}
    for attribute in table_json["Table"]["KeySchema"]:
        key_type = attribute["KeyType"]
        attribute_name = attribute["AttributeName"]

        if key_type == "HASH":
            kwargs["hash_key"] = attribute_name
        if key_type == "RANGE":
            kwargs["range_key"] = attribute_name

    kwargs.update(
        {
            "table_name": table_name,
            "region": region_name,
            "dydb": dydb,
            "delimiter": delimiter,
        }
    )

    global __table_data
    __table_data = _AsyncTableData(**kwargs)
