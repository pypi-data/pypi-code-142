# coding: utf-8

"""
    Priceloop API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from priceloop_api import schemas  # noqa: F401


class ApiColumn(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "tpe",
            "position",
            "tableName",
        }
        
        class properties:
            name = schemas.StrSchema
            position = schemas.Int32Schema
            tableName = schemas.StrSchema
            tpe = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "position": position,
                "tableName": tableName,
                "tpe": tpe,
            }
    
    name: MetaOapg.properties.name
    tpe: MetaOapg.properties.tpe
    position: MetaOapg.properties.position
    tableName: MetaOapg.properties.tableName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["position"]) -> MetaOapg.properties.position: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tableName"]) -> MetaOapg.properties.tableName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tpe"]) -> MetaOapg.properties.tpe: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "position", "tableName", "tpe", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["position"]) -> MetaOapg.properties.position: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tableName"]) -> MetaOapg.properties.tableName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tpe"]) -> MetaOapg.properties.tpe: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "position", "tableName", "tpe", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        tpe: typing.Union[MetaOapg.properties.tpe, str, ],
        position: typing.Union[MetaOapg.properties.position, decimal.Decimal, int, ],
        tableName: typing.Union[MetaOapg.properties.tableName, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApiColumn':
        return super().__new__(
            cls,
            *args,
            name=name,
            tpe=tpe,
            position=position,
            tableName=tableName,
            _configuration=_configuration,
            **kwargs,
        )
