import datetime
from enum import Enum
from uuid import uuid4

from sqlalchemy import ARRAY
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Enum as EnumField
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import DeclarativeMeta

from server.database import db

BaseModel: DeclarativeMeta = db.Model


class UserModel(BaseModel):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(), nullable=False)
    created_on = Column(DateTime(), default=datetime.datetime.now())


class UserOrganization(BaseModel):
    __tablename__ = "organization_users"
    id = Column(Integer(), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    organization_id = Column(
        UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False
    )
    __table_args__ = (UniqueConstraint("user_id", "organization_id", name="uix_1"),)


class FileType(Enum):
    DATA = "data"
    RATINGS = "ratings"
    OTHER = "other"


class RawFileModel(BaseModel):
    __tablename__ = "raw_files"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    filename = Column(String(255))
    organization_id = Column(
        UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False
    )
    file_type = Column(
        EnumField("data", "ratings", "other", name="FileType"), default="data"
    )


class FileMapModel(BaseModel):
    __tablename__ = "file_map"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    # TODO check if we must make this relation 1:1
    file_id = Column(UUID(as_uuid=True), ForeignKey("raw_files.id"), unique=True)
    id_column = Column(String(), default="")
    title_column = Column(String(), default="")
    data_columns = Column(ARRAY(String()), nullable=False)
    data_separator = Column(String(), default="|")


class UserRating(BaseModel):
    __tablename__ = "user_ratings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String(), nullable=False)
    rating = Column(Float(), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    organization_id = Column(
        UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False
    )


class RecommendationsModel(BaseModel):
    __tablename__ = "user_recommendations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    organization_id = Column(
        UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False
    )
    recommendations = Column(JSON(), nullable=False)
