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


class User(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "type",
        }
        
        class properties:
        
            @staticmethod
            def type() -> typing.Type['UserTypeEnum']:
                return UserTypeEnum
            id = schemas.UUIDSchema
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "username",
                    }
                    
                    class properties:
                        
                        
                        class username(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 150
                                regex=[{
                                    'pattern': r'^[\w.@+-]+$',  # noqa: E501
                                }]
                        
                        
                        class first_name(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 150
                        
                        
                        class last_name(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 150
                        
                        
                        class email(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                format = 'email'
                                max_length = 254
                        is_active = schemas.BoolSchema
                        is_staff = schemas.BoolSchema
                        is_superuser = schemas.BoolSchema
                        date_joined = schemas.DateTimeSchema
                        
                        
                        class user_permissions(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                @staticmethod
                                def items() -> typing.Type['Permission']:
                                    return Permission
                        
                            def __new__(
                                cls,
                                arg: typing.Union[typing.Tuple['Permission'], typing.List['Permission']],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'user_permissions':
                                return super().__new__(
                                    cls,
                                    arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> 'Permission':
                                return super().__getitem__(i)
                        
                        
                        class perm_codenames(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                
                                class items(
                                    schemas.StrSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        max_length = 200
                        
                            def __new__(
                                cls,
                                arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'perm_codenames':
                                return super().__new__(
                                    cls,
                                    arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        __annotations__ = {
                            "username": username,
                            "first_name": first_name,
                            "last_name": last_name,
                            "email": email,
                            "is_active": is_active,
                            "is_staff": is_staff,
                            "is_superuser": is_superuser,
                            "date_joined": date_joined,
                            "user_permissions": user_permissions,
                            "perm_codenames": perm_codenames,
                        }
                
                username: MetaOapg.properties.username
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["is_staff"]) -> MetaOapg.properties.is_staff: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["is_superuser"]) -> MetaOapg.properties.is_superuser: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["date_joined"]) -> MetaOapg.properties.date_joined: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["user_permissions"]) -> MetaOapg.properties.user_permissions: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["perm_codenames"]) -> MetaOapg.properties.perm_codenames: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["username", "first_name", "last_name", "email", "is_active", "is_staff", "is_superuser", "date_joined", "user_permissions", "perm_codenames", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> typing.Union[MetaOapg.properties.first_name, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> typing.Union[MetaOapg.properties.last_name, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["is_active"]) -> typing.Union[MetaOapg.properties.is_active, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["is_staff"]) -> typing.Union[MetaOapg.properties.is_staff, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["is_superuser"]) -> typing.Union[MetaOapg.properties.is_superuser, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["date_joined"]) -> typing.Union[MetaOapg.properties.date_joined, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["user_permissions"]) -> typing.Union[MetaOapg.properties.user_permissions, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["perm_codenames"]) -> typing.Union[MetaOapg.properties.perm_codenames, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["username", "first_name", "last_name", "email", "is_active", "is_staff", "is_superuser", "date_joined", "user_permissions", "perm_codenames", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    username: typing.Union[MetaOapg.properties.username, str, ],
                    first_name: typing.Union[MetaOapg.properties.first_name, str, schemas.Unset] = schemas.unset,
                    last_name: typing.Union[MetaOapg.properties.last_name, str, schemas.Unset] = schemas.unset,
                    email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
                    is_active: typing.Union[MetaOapg.properties.is_active, bool, schemas.Unset] = schemas.unset,
                    is_staff: typing.Union[MetaOapg.properties.is_staff, bool, schemas.Unset] = schemas.unset,
                    is_superuser: typing.Union[MetaOapg.properties.is_superuser, bool, schemas.Unset] = schemas.unset,
                    date_joined: typing.Union[MetaOapg.properties.date_joined, str, datetime, schemas.Unset] = schemas.unset,
                    user_permissions: typing.Union[MetaOapg.properties.user_permissions, list, tuple, schemas.Unset] = schemas.unset,
                    perm_codenames: typing.Union[MetaOapg.properties.perm_codenames, list, tuple, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *args,
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        is_active=is_active,
                        is_staff=is_staff,
                        is_superuser=is_superuser,
                        date_joined=date_joined,
                        user_permissions=user_permissions,
                        perm_codenames=perm_codenames,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class relationships(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                    
                        @staticmethod
                        def inbox_folder() -> typing.Type['Reltoone']:
                            return Reltoone
                    
                        @staticmethod
                        def home_folder() -> typing.Type['Reltoone']:
                            return Reltoone
                    
                        @staticmethod
                        def groups() -> typing.Type['Reltomany']:
                            return Reltomany
                        __annotations__ = {
                            "inbox_folder": inbox_folder,
                            "home_folder": home_folder,
                            "groups": groups,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["inbox_folder"]) -> 'Reltoone': ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["home_folder"]) -> 'Reltoone': ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["groups"]) -> 'Reltomany': ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["inbox_folder", "home_folder", "groups", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["inbox_folder"]) -> typing.Union['Reltoone', schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["home_folder"]) -> typing.Union['Reltoone', schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["groups"]) -> typing.Union['Reltomany', schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["inbox_folder", "home_folder", "groups", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    inbox_folder: typing.Union['Reltoone', schemas.Unset] = schemas.unset,
                    home_folder: typing.Union['Reltoone', schemas.Unset] = schemas.unset,
                    groups: typing.Union['Reltomany', schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'relationships':
                    return super().__new__(
                        cls,
                        *args,
                        inbox_folder=inbox_folder,
                        home_folder=home_folder,
                        groups=groups,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "type": type,
                "id": id,
                "attributes": attributes,
                "relationships": relationships,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    type: 'UserTypeEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'UserTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationships"]) -> MetaOapg.properties.relationships: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type"], typing_extensions.Literal["id"], typing_extensions.Literal["attributes"], typing_extensions.Literal["relationships"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'UserTypeEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> typing.Union[MetaOapg.properties.attributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationships"]) -> typing.Union[MetaOapg.properties.relationships, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type"], typing_extensions.Literal["id"], typing_extensions.Literal["attributes"], typing_extensions.Literal["relationships"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: 'UserTypeEnum',
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        relationships: typing.Union[MetaOapg.properties.relationships, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'User':
        return super().__new__(
            cls,
            *args,
            type=type,
            id=id,
            attributes=attributes,
            relationships=relationships,
            _configuration=_configuration,
        )

from papermerge_restapi_client.model.permission import Permission
from papermerge_restapi_client.model.reltomany import Reltomany
from papermerge_restapi_client.model.reltoone import Reltoone
from papermerge_restapi_client.model.user_type_enum import UserTypeEnum
