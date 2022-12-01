# coding: utf-8

"""
    Papermerge REST API

    Document management system designed for digital archives  # noqa: E501

    The version of the OpenAPI document: 2.1.0b16
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

from papermerge_restapi_client import schemas  # noqa: F401


class PaginatedTagList(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class data(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Tag']:
                        return Tag
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Tag'], typing.List['Tag']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'data':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Tag':
                    return super().__getitem__(i)
            
            
            class meta(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class pagination(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    page = schemas.IntSchema
                                    pages = schemas.IntSchema
                                    count = schemas.IntSchema
                                    __annotations__ = {
                                        "page": page,
                                        "pages": pages,
                                        "count": count,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["pages"]) -> MetaOapg.properties.pages: ...
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["page", "pages", "count", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> typing.Union[MetaOapg.properties.page, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["pages"]) -> typing.Union[MetaOapg.properties.pages, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["page", "pages", "count", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *args: typing.Union[dict, frozendict.frozendict, ],
                                page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                pages: typing.Union[MetaOapg.properties.pages, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'pagination':
                                return super().__new__(
                                    cls,
                                    *args,
                                    page=page,
                                    pages=pages,
                                    count=count,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "pagination": pagination,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["pagination"]) -> MetaOapg.properties.pagination: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["pagination", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["pagination"]) -> typing.Union[MetaOapg.properties.pagination, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pagination", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    pagination: typing.Union[MetaOapg.properties.pagination, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'meta':
                    return super().__new__(
                        cls,
                        *args,
                        pagination=pagination,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class links(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class next(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            class MetaOapg:
                                format = 'uri'
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'next':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class prev(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            class MetaOapg:
                                format = 'uri'
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'prev':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class first(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            class MetaOapg:
                                format = 'uri'
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'first':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class last(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            class MetaOapg:
                                format = 'uri'
                        
                        
                            def __new__(
                                cls,
                                *args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'last':
                                return super().__new__(
                                    cls,
                                    *args,
                                    _configuration=_configuration,
                                )
                        __annotations__ = {
                            "next": next,
                            "prev": prev,
                            "first": first,
                            "last": last,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["next"]) -> MetaOapg.properties.next: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["prev"]) -> MetaOapg.properties.prev: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["first"]) -> MetaOapg.properties.first: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["last"]) -> MetaOapg.properties.last: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["next", "prev", "first", "last", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["next"]) -> typing.Union[MetaOapg.properties.next, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["prev"]) -> typing.Union[MetaOapg.properties.prev, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["first"]) -> typing.Union[MetaOapg.properties.first, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["last"]) -> typing.Union[MetaOapg.properties.last, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["next", "prev", "first", "last", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    next: typing.Union[MetaOapg.properties.next, None, str, schemas.Unset] = schemas.unset,
                    prev: typing.Union[MetaOapg.properties.prev, None, str, schemas.Unset] = schemas.unset,
                    first: typing.Union[MetaOapg.properties.first, None, str, schemas.Unset] = schemas.unset,
                    last: typing.Union[MetaOapg.properties.last, None, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'links':
                    return super().__new__(
                        cls,
                        *args,
                        next=next,
                        prev=prev,
                        first=first,
                        last=last,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "data": data,
                "meta": meta,
                "links": links,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> MetaOapg.properties.meta: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "meta", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union[MetaOapg.properties.meta, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "meta", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union[MetaOapg.properties.data, list, tuple, schemas.Unset] = schemas.unset,
        meta: typing.Union[MetaOapg.properties.meta, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaginatedTagList':
        return super().__new__(
            cls,
            *args,
            data=data,
            meta=meta,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from papermerge_restapi_client.model.tag import Tag
