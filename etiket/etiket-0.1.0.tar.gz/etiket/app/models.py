from typing import List, Optional, Union, Dict, Any, Type, TypeVar
from enum import Enum
from uuid import uuid4, UUID
from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel, Column, DateTime, JSON, BigInteger
from datetime import datetime, timedelta
from pydantic import BaseModel, AnyUrl, Json
from pydantic import constr, EmailStr, SecretStr, ConstrainedStr
from sqlalchemy.dialects import postgresql, sqlite
import re

from etiket.core.config import settings
from etiket.core.types import (
    filestr,
    metastr,
    collectionstr,
    datasetstr,
    scopestr,
    namestr,
    usernamestr,
    FileType,
    FileStatus,
    UploadConcat,
)


BigIntegerType = BigInteger()
if settings.ETIKET_TEST:
    BigIntegerType = BigIntegerType.with_variant(sqlite.INTEGER(), "sqlite")
else:
    BigIntegerType = BigIntegerType.with_variant(postgresql.BIGINT(), "postgresql")


class ScopeUserLink(SQLModel, table=True):
    scope: Optional[str] = Field(
        default=None,
        foreign_key="scope.name",
        primary_key=True,
    )
    user_id: Optional[int] = Field(
        default=None,
        foreign_key="user.id",
        primary_key=True,
    )


class CollectionDatasetLink(SQLModel, table=True):
    collection_id: Optional[int] = Field(
        default=None,
        foreign_key="collection.id",
        primary_key=True,
    )
    dataset_id: Optional[int] = Field(
        default=None,
        foreign_key="dataset.id",
        primary_key=True,
    )


class ScopeBase(SQLModel):
    name: scopestr() = Field(default=..., primary_key=True)
    description: str
    restricted: bool = False
    archived: bool = False


class Scope(ScopeBase, table=True):
    created: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), default=datetime.utcnow),
        nullable=False,
    )
    modified: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True), onupdate=datetime.utcnow, default=datetime.utcnow
        ),
        nullable=False,
    )
    collections: List["Collection"] = Relationship(back_populates="scopes")
    datasets: List["Dataset"] = Relationship(back_populates="scopes")
    users: List["User"] = Relationship(
        back_populates="scopes", link_model=ScopeUserLink
    )


class ScopeRead(ScopeBase):
    created: Optional[datetime]
    modified: Optional[datetime]


class ScopeCreate(ScopeBase):
    pass


class ScopeUpdate(SQLModel):
    description: Optional[str]
    restricted: Optional[bool]
    archived: Optional[bool]


class UserBase(SQLModel):
    username: usernamestr() = Field(default=..., unique=True)
    firstname: namestr()
    lastname: namestr()
    email: EmailStr
    active: bool = True
    admin: bool = False


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str = None
    created: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), default=datetime.utcnow),
        nullable=False,
    )
    modified: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True), onupdate=datetime.utcnow, default=datetime.utcnow
        ),
        nullable=False,
    )
    scopes: List["Scope"] = Relationship(
        back_populates="users", link_model=ScopeUserLink
    )


class UserRead(UserBase):
    created: Optional[datetime]
    modified: Optional[datetime]


class UserCreate(UserBase):
    hashed_password: str


class UserUpdate(SQLModel):
    username: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    email: Optional[str]
    active: Optional[str]
    admin: Optional[bool]
    hashed_password: Optional[str]


class CollectionBase(SQLModel):
    name: collectionstr() = Field(default=..., index=True)
    description: Optional[str] = None
    scope: str = Field(default=..., foreign_key="scope.name")


class Collection(CollectionBase, table=True):
    id: Optional[int] = Field(
        default=None, sa_column=Column(BigIntegerType, primary_key=True)
    )
    created: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), default=datetime.utcnow),
        nullable=False,
    )
    modified: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True), onupdate=datetime.utcnow, default=datetime.utcnow
        ),
        nullable=False,
    )
    datasets: List["Dataset"] = Relationship(
        back_populates="collections", link_model=CollectionDatasetLink
    )
    scopes: Optional["Scope"] = Relationship(back_populates="collections")
    __table_args__ = (UniqueConstraint("scope", "name", name="COLL_SCOPE_UQ"),)


class CollectionRead(CollectionBase):
    created: Optional[datetime]
    modified: Optional[datetime]


class CollectionCreate(CollectionBase):
    pass


class CollectionUpdate(SQLModel):
    name: Optional[collectionstr()]
    description: Optional[str]


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: str


class DatasetBase(SQLModel):
    name: datasetstr() = Field(default=..., index=True)
    uuid: Optional[UUID] = Field(default_factory=uuid4)
    scope: str = Field(default=..., foreign_key="scope.name")
    creator: Optional[str] = None
    description: Optional[str] = None
    meta: Dict[metastr(), Union[List[metastr()], metastr()]] = Field(
        default=None, sa_column=Column(JSON)
    )
    started: Optional[datetime] = None
    duration: Optional[timedelta] = None
    ranking: int = Field(default=0, index=True)


class Dataset(DatasetBase, table=True):
    id: Optional[int] = Field(
        default=None, sa_column=Column(BigIntegerType, primary_key=True)
    )
    created: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), default=datetime.utcnow),
        nullable=False,
        index=True,
    )
    modified: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True), onupdate=datetime.utcnow, default=datetime.utcnow
        ),
        nullable=False,
    )
    files: List["File"] = Relationship(back_populates="dataset")
    collections: List["Collection"] = Relationship(
        back_populates="datasets", link_model=CollectionDatasetLink
    )
    scopes: Optional["Scope"] = Relationship(back_populates="datasets")
    __table_args__ = (UniqueConstraint("scope", "uuid", name="DATASET_SCOPE_UQ"),)


class DatasetCreate(DatasetBase):
    pass


class DatasetRead(DatasetBase):
    created: Optional[datetime]
    modified: Optional[datetime]


class DatasetUpdate(SQLModel):
    name: Optional[datasetstr()]
    started: Optional[datetime]
    duration: Optional[timedelta]
    description: Optional[str]
    creator: Optional[str]
    ranking: Optional[int]


class DatasetMeta(SQLModel):
    meta: Dict[metastr(), Union[List[metastr()], metastr()]]


class DatasetMetaKeys(SQLModel):
    keys: List[metastr()]


class FileBase(SQLModel):
    name: filestr() = Field(default=..., index=True)
    uuid: Optional[UUID] = Field(default_factory=uuid4, index=True)
    creator: str = None
    etag: str = None
    size: int = None
    mimetype: str = "application/octet-stream"
    altlocation: AnyUrl = None
    version_id: str = None
    rating: int = 0
    immutable: bool = True
    filetype: Optional[FileType]


class File(FileBase, table=True):
    id: Optional[int] = Field(
        default=None, sa_column=Column(BigIntegerType, primary_key=True)
    )
    dataset_id: Optional[int] = Field(default=None, foreign_key="dataset.id")
    scope: str = Field(default=..., foreign_key="scope.name")
    status: FileStatus = "unavailable"
    location: str = None
    s3_bucket: str = None
    s3_key: str = None
    created: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), default=datetime.utcnow),
        nullable=False,
    )
    modified: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True), onupdate=datetime.utcnow, default=datetime.utcnow
        ),
        nullable=False,
    )
    uploads: List["Upload"] = Relationship(back_populates="file")
    dataset: Optional[Dataset] = Relationship(back_populates="files")
    __table_args__ = (UniqueConstraint("scope", "uuid", name="FILE_SCOPE_UQ"),)


class FileCreate(FileBase):
    dataset_uuid: UUID
    scope: str


class FileInDatasetCreate(FileBase):
    pass


class FileInDatasetRead(FileBase):
    created: Optional[datetime]
    modified: Optional[datetime]
    status: FileStatus


class FileRead(FileInDatasetRead):
    scope: str


class FileUpdate(SQLModel):
    name: Optional[filestr()]
    mimetype: Optional[str]
    filetype: Optional[FileType]
    rating: Optional[int]


class UploadBase(SQLModel):
    uuid: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    location: str
    expires: Optional[datetime]
    offset: int = 0
    length: int
    concat: bool = False
    completed: bool = False


class Upload(UploadBase, table=True):
    file: Optional[File] = Relationship(back_populates="uploads")
    file_id: Optional[int] = Field(default=None, foreign_key="file.id")


class DatasetWithFilesCreate(DatasetCreate):
    files: List[FileInDatasetCreate] = []


class CollectionInDatasetRead(BaseModel):
    name: str
    description: Optional[str]


class DatasetReadExtended(DatasetRead):
    files: List[FileInDatasetRead] = []
    collections: List[CollectionInDatasetRead]


class CollectionReadExtended(CollectionRead):
    datasets: List[DatasetRead] = []
    scopes: ScopeRead


class UserReadExtended(UserRead):
    scopes: List[ScopeRead] = []


class ScopeReadExtended(ScopeRead):
    users: List[UserRead] = []
    collections: List[CollectionRead] = []
