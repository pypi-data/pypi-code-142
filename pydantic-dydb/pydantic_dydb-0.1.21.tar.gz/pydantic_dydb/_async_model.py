from __future__ import annotations

from typing import Any, Optional, Union

import pydantic

from pydantic_dydb import _json
from pydantic_dydb._async_initialization import get_async_table_data
from pydantic_dydb._config import logger
from pydantic_dydb._constants import (
    EMPTY_BINARY_JSON,
    ITEM,
    ITEMS,
    LIST,
    MAP,
    STRING,
    str_to_type_mapping,
)


def handle_error(resp):
    if not (200 <= resp.status_code < 300):
        logger.info(f"{resp.status_code=} {resp.content=}")
        print(f"{resp.status_code=} {resp.content=}")
        logger.exception(
            f"hit error making request {resp.status_code=} {resp.content=}"
        )
        resp.raise_for_status()


def fix_item(cls, input_: dict):
    """
    Before dumping to dynamodb we have to add the correct type strings
    and make everything able to be serialized
    :param cls:
    :param input_:
    :return:
    """
    for k, v in input_.items():
        if isinstance(v, dict):
            for k1, v1 in v.items():
                if k1 in str_to_type_mapping:
                    input_[k] = v1
        else:
            input_[k] = v
    return input_


def _remove_types_from_list(list_):
    ret_list = []
    for item in list_:
        key, value = next(iter(item.items()))
        if key == MAP:
            ret_list.append(_remove_types_from_dict(value))
        elif key == LIST:
            ret_list.append(_remove_types_from_list(value))
        else:
            ret_list.append(value)
    return ret_list


def _remove_types_from_dict(dict_):
    ret_dict = {}
    for key, value in dict_.items():
        type_, v = next(iter(value.items()))
        if type_ == MAP:
            ret_dict[key] = _remove_types_from_dict(v)
        elif type_ == LIST:
            ret_dict[key] = _remove_types_from_list(v)
        else:
            ret_dict[key] = v
    return ret_dict


def _add_types_to_list(list_):
    ret_list = []
    for item in list_:
        if isinstance(item, dict):
            ret_list.append({MAP: _add_types_to_dict(item)})
        elif isinstance(item, list):
            ret_list.append({LIST: _add_types_to_list(item)})
        else:
            ret_list.append({"S": str(item)})
    return ret_list


def _add_types_to_dict(d):
    """
    When loading from dynamodb we get a dictionary with type strings before each type
    we need to clean this before we pass the dictionary to pydantic to load
    :param d:
    :return:
    """

    new_dict = {}
    for key, value in d.items():
        if isinstance(value, dict):
            new_dict[key] = {MAP: _add_types_to_dict(value)}
        elif isinstance(value, list):
            new_dict[key] = {LIST: _add_types_to_list(value)}
        else:
            new_dict[key] = {"S": str(value)}
    return new_dict


async def paginator(func: callable, request_body):
    last_evaluated_key = "LastEvaluatedKey"
    start_key = "ExclusiveStartKey"
    continue_key = False

    while continue_key is not None:
        if continue_key is not False:
            request_body[start_key] = continue_key
        resp = await func(_json.byte_dumps(request_body))
        handle_error(resp)
        json_dict = _json.loads(resp.content)
        continue_key = json_dict.get(last_evaluated_key, None)
        yield json_dict


class AsyncTableBaseModel(pydantic.BaseModel):
    class DoesNotExist(Exception):
        pass

    def __init__(self, **data: Any):
        self._setup_class()
        super().__init__(**data)

    def __get__(self, instance, owner):
        """
        needed only to ease coding.
        temp solution for pycharm bug : https://youtrack.jetbrains.com/issue/PY-36176
        """
        super(__class__, self).__get__(instance, owner)
        return self

    async def save(self):
        table_data = get_async_table_data()
        hash_key_value = self.Config.hash_key_attribute

        payload = {
            table_data.hash_key: {
                STRING: f"{self.__class__.__name__}{table_data.delimiter}{self.__getattribute__(hash_key_value)}"
            },
        }

        if table_data.range_key and self.Config.range_key_attribute:
            range_key_value = self.Config.range_key_attribute
            payload[table_data.range_key] = {
                STRING: f"{self.__class__.__name__}{table_data.delimiter}{self.__getattribute__(range_key_value)}"
            }

        payload.update(self._dydb_dump())
        body = dict(TableName=table_data.table_name, Item=payload)
        resp = await table_data.dydb.put_item(_json.byte_dumps(body))
        handle_error(resp)

    def _dydb_dump(self) -> dict:
        loaded_dict = _json.loads(bytes(self.json(), "utf-8"))
        return _add_types_to_dict(loaded_dict)

    @classmethod
    async def get(cls, *, hash_key, range_key: Optional[str]):
        cls._setup_class()
        table_data = get_async_table_data()

        if (
            range_key is None
            and table_data.range_key
            and cls.Config.range_key_attribute
        ):
            raise Exception(f"Missing expected range key argument")

        key = {
            table_data.hash_key: {
                STRING: f"{cls.__name__}{table_data.delimiter}{hash_key}"
            },
        }

        if table_data.range_key and cls.Config.range_key_attribute:
            key[table_data.range_key] = {
                STRING: f"{cls.__name__}{table_data.delimiter}{range_key}"
            }

        body = _json.byte_dumps(
            dict(
                TableName=table_data.table_name,
                Key=key,
                AttributesToGet=cls.Config.attr_to_get,
            )
        )
        resp = await table_data.dydb.get_item(body)
        handle_error(resp)

        content = resp.content

        if content == EMPTY_BINARY_JSON:
            raise cls.DoesNotExist(
                f"Item with hash key:{hash_key} and range key:{range_key} was not found"
            )

        cleaned_item = _remove_types_from_dict(_json.loads(content)[ITEM])
        return cls.parse_obj(cleaned_item)

    @classmethod
    async def batch_get(cls, items: Union[list[str] | list[tuple[str, str]]]):
        # todo implement multiple batch calls if partial results obtained
        table_data = get_async_table_data()
        requests = []

        for item in items:
            if (
                len(item) == 1
                and table_data.range_key
                and cls.Config.range_key_attribute
            ):
                raise Exception(f"Missing expected range value in item {item}")

            if isinstance(item, tuple):
                primary_value = f"{cls.__name__}{table_data.delimiter}{item[0]}"
            else:
                primary_value = f"{cls.__name__}{table_data.delimiter}{item}"

            if table_data.range_key and cls.Config.range_key_attribute:
                secondary_value = f"{cls.__name__}{table_data.delimiter}{item[1]}"
                request = {
                    table_data.hash_key: {STRING: primary_value},
                    table_data.range_key: {STRING: secondary_value},
                }

            else:
                request = {table_data.hash_key: {STRING: primary_value}}
            requests.append(request)

        chunks = _chunks(requests, 100)

        for chunk in chunks:
            body = dict(
                RequestItems={
                    table_data.table_name: {
                        "AttributesToGet": cls.Config.attr_to_get,
                        "Keys": chunk,
                    }
                }
            )
            resp = await table_data.dydb.batch_get(_json.byte_dumps(body))
            handle_error(resp)
            items = _json.loads(resp.content)["Responses"][table_data.table_name]
            for item in items:
                cleaned_item = _remove_types_from_dict(item)
                data = cls.parse_obj(cleaned_item)
                yield data

    @classmethod
    async def scan(cls):
        # todo implement retries if request limit exceeded
        cls._setup_class()
        table_data = get_async_table_data()
        use_range_key = table_data.range_key and cls.Config.range_key_attribute
        prefix = f"{cls.__name__}{table_data.delimiter}"
        key_conditions = {
            table_data.hash_key: {
                "AttributeValueList": [{STRING: use_range_key}],
                "ComparisonOperator": "CONTAINS",
            }
        }

        if use_range_key:
            key_conditions[table_data.range_key] = {
                "AttributeValueList": [{STRING: use_range_key}],
                "ComparisonOperator": "CONTAINS",
            }

        request_body = dict(
            TableName=table_data.table_name,
            ReturnConsumedCapacity="TOTAL",
            AttributesToGet=cls.Config.attr_to_get,
            KeyConditions=key_conditions,
        )

        pages = paginator(table_data.dydb.scan, request_body)

        async for page in pages:
            for item in page[ITEMS]:
                try:
                    if not item[table_data.hash_key][STRING].startswith(prefix):
                        continue
                    if use_range_key and not item[table_data.range_key][
                        STRING
                    ].startswith(prefix):
                        continue
                    cleaned_item = _remove_types_from_dict(item)
                    yield cls.parse_obj(cleaned_item)
                except pydantic.ValidationError:
                    pass

    @classmethod
    async def query(cls, primary_key_value: str, filter_range=False):
        # todo implement retries if request limit exceeded
        cls._setup_class()
        table_data = get_async_table_data()

        key_conditions = {
            table_data.hash_key: {
                "AttributeValueList": [
                    {STRING: f"{cls.__name__}{table_data.delimiter}{primary_key_value}"}
                ],
                "ComparisonOperator": "EQ",
            }
        }

        if table_data.range_key and cls.Config.range_key_attribute and filter_range:
            key_conditions[table_data.range_key] = {
                "AttributeValueList": [
                    {STRING: f"{cls.__name__}{table_data.delimiter}"}
                ],
                "ComparisonOperator": "CONTAINS",
            }

        request_body = dict(
            TableName=table_data.table_name,
            ReturnConsumedCapacity="TOTAL",
            AttributesToGet=cls.Config.attr_to_get,
            KeyConditions=key_conditions,
        )

        pages = paginator(table_data.dydb.query, request_body)
        async for page in pages:
            for item in page[ITEMS]:
                try:
                    cleaned_item = _remove_types_from_dict(item)
                    yield cls.parse_obj(cleaned_item)
                except pydantic.ValidationError:
                    pass

    @classmethod
    async def delete(cls, hash_key: str, range_key: Optional[str] = None):
        cls._setup_class()
        table_data = get_async_table_data()

        if (
            range_key is None
            and table_data.range_key
            and cls.Config.range_key_attribute
        ):
            raise Exception(f"Missing expected range key argument")

        payload = {
            table_data.hash_key: {
                STRING: f"{cls.__name__}{table_data.delimiter}{hash_key}"
            },
        }

        if table_data.range_key and cls.Config.range_key_attribute:
            payload[table_data.range_key] = {
                STRING: f"{cls.__name__}{table_data.delimiter}{range_key}"
            }

        body = dict(TableName=table_data.table_name, Key=payload)
        resp = await table_data.dydb.delete(_json.byte_dumps(body))
        handle_error(resp)

    async def delete_obj(self):
        table_data = get_async_table_data()
        hash_key_value = self.Config.hash_key_attribute

        payload = {
            table_data.hash_key: {
                STRING: f"{self.__class__.__name__}{table_data.delimiter}{self.__getattribute__(hash_key_value)}"
            },
        }

        if table_data.range_key and self.Config.range_key_attribute:
            range_key_value = self.Config.range_key_attribute
            payload[table_data.range_key] = {
                STRING: f"{self.__class__.__name__}{table_data.delimiter}{self.__getattribute__(range_key_value)}"
            }

        body = dict(
            TableName=table_data.table_name,
            Key=payload,
        )

        resp = await table_data.dydb.delete(_json.byte_dumps(body))
        handle_error(resp)

    @classmethod
    def _setup_class(cls):
        try:
            cls.Config.is_setup
        except AttributeError:
            if not getattr(cls.Config, "hash_key_attribute", None):
                try:
                    hash_key = cls.Config.hash_key
                except AttributeError:
                    raise Exception(
                        f"Required hash_key attribute not present in Config"
                    )

                try:
                    hash_key_attribute = cls.__dict__["__fields__"][hash_key]
                except KeyError:
                    if not isinstance(type(hash_key), str):
                        Exception(
                            f"Config class attribute hash_key is expected to be {str} but is {type(hash_key)}"
                        )
                    raise Exception(
                        f"Config class attribute hash_key value: {hash_key} is not an attribute of {cls.__name__}"
                    )

                if hash_key_attribute.type_ is not str:
                    raise Exception(
                        f"Hash key attribute type is required to be {str} but is {hash_key_attribute.type_}"
                    )

                cls.Config.hash_key_attribute = hash_key_attribute

            if not getattr(cls.Config, "range_key_attribute", None):
                range_key = getattr(cls.Config, "range_key", None)

                if range_key:
                    try:
                        range_key_attribute = cls.__dict__["__fields__"][range_key]
                    except KeyError:
                        if not isinstance(type(range_key), str):
                            raise Exception(
                                f"Config class attribute range_key is expected to be {str} but is {type(range_key)}"
                            )
                        raise Exception(
                            f"Config class attribute range_key: {range_key} is not an attribute of {cls.__name__}"
                        )
                    if range_key_attribute.type_ is not str:
                        raise Exception(
                            f"range key attribute type is required to be {str} but is {range_key_attribute.type_}"
                        )
                else:
                    range_key_attribute = None
                cls.Config.range_key_attribute = range_key_attribute

            if not getattr(cls.Config, "json_loads", None):
                cls.Config.json_loads = _json.loads
            if not getattr(cls.Config, "json_dumps", None):
                cls.Config.json_dumps = _json.str_dumps
            if not getattr(cls.Config, "attr_to_get", None):
                cls.Config.attr_to_get = [key for key in cls.__fields__.keys()]
            cls.Config.is_setup = True


def _chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


# def batch_delete(
#     items: list[tuple[Type[TableBaseModel], str]]
#     | list[tuple[Type[TableBaseModel], str, str]]
# ):
#     # todo implement multiple delete calls if unprocessed items
#     # todo implement retries if request limit exceeded
#     table_data = get_table_data()
#
#     requests = []
#     for item in items:
#         if len(item) == 2 is None and table_data.range_key and cls.Config.range_key_attribute:
#             raise Exception(f"Missing expected range key argument")
#
#         item[0]._setup_class()
#         if len(item) == 3:
#             request = {
#                 "DeleteRequest": {
#                     table_data.hash_key: {
#                         STRING: f"{item[0].__class__.__name__}{table_data.delimiter}{item[1]}"
#                     },
#                     table_data.range_key: {
#                         STRING: f"{item[0].__class__.__name__}{table_data.delimiter}{item[2]}"
#                     },
#                 }
#             }
#         else:
#             request = {"DeleteRequest": {table_data.hash_key: {STRING: item[1]}}}
#         requests.append(request)
#
#     chunks = _chunks(requests, 25)
#
#     for chunk in chunks:
#         body = dict(RequestItems=chunk)
#         resp = table_data.dydb.batch_write(_json.byte_dumps(body))
#     return


async def async_batch_delete_obj(items: list[AsyncTableBaseModel]):
    # todo implement multiple delete calls if unprocessed items
    # todo implement retries if request limit exceeded
    table_data = get_async_table_data()

    requests = []
    for item in items:
        hash_key_value = item.Config.hash_key_attribute
        primary_value = f"{item.__class__.__name__}{table_data.delimiter}{item.__getattribute__(hash_key_value)}"

        if table_data.range_key and item.Config.range_key_attribute:
            range_key_value = item.Config.range_key_attribute
            secondary_value = f"{item.__class__.__name__}{table_data.delimiter}{item.__getattribute__(range_key_value)}"
            request = {
                "DeleteRequest": {
                    "Key": {
                        table_data.hash_key: {STRING: primary_value},
                        table_data.range_key: {STRING: secondary_value},
                    }
                }
            }
        else:
            request = {
                "DeleteRequest": {"Key": {table_data.hash_key: {STRING: primary_value}}}
            }
        requests.append(request)

    chunks = _chunks(requests, 25)

    for chunk in chunks:
        body = dict(RequestItems={table_data.table_name: chunk})
        resp = await table_data.dydb.batch_write(_json.byte_dumps(body))
        handle_error(resp)
    return


async def async_batch_write(items: list[AsyncTableBaseModel]):
    # todo implement multiple write calls if unprocessed items
    # todo implement retries if request limit exceeded
    put_request = "PutRequest"
    table_data = get_async_table_data()

    requests = []

    for item in items:
        hash_key_value = item.Config.hash_key_attribute
        primary_value = f"{item.__class__.__name__}{table_data.delimiter}{item.__getattribute__(hash_key_value)}"

        if table_data.range_key and item.Config.range_key_attribute:
            range_key_value = item.Config.range_key_attribute
            secondary_value = f"{item.__class__.__name__}{table_data.delimiter}{item.__getattribute__(range_key_value)}"
            request = {
                put_request: {
                    ITEM: {
                        table_data.hash_key: {STRING: primary_value},
                        table_data.range_key: {STRING: secondary_value},
                    }
                }
            }
        else:
            request = {
                put_request: {ITEM: {table_data.hash_key: {STRING: primary_value}}}
            }

        request[put_request][ITEM].update(item._dydb_dump())

        requests.append(request)

    chunks = _chunks(requests, 25)

    for chunk in chunks:
        body = dict(RequestItems={table_data.table_name: chunk})
        resp = await table_data.dydb.batch_write(_json.byte_dumps(body))
        handle_error(resp)
    return
