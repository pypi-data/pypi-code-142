from sqlmodel import SQLModel, create_engine, Session, select
from sqlmodel.sql.expression import Select, SelectOfScalar
from typing import Any, Optional
import psycopg2
from fastapi import HTTPException
from sqlmodel.main import SQLModelMetaclass
from sqlalchemy.exc import IntegrityError, NoResultFound
from uuid import UUID

from etiket.app.models import User, Scope, Collection, Dataset, File, Upload
from etiket.core.config import settings
from etiket.core.exceptions import *

postgres_url = f"postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
engine = create_engine(postgres_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def commit_to_db(resource: Any, session: Session):

    try:
        session.add(resource)
        session.commit()
        session.refresh(resource)
        return resource

    except IntegrityError as e:
        session.rollback()
        raise HTTPException(
            status_code=422, detail=f"Resource with this name or key already exists"
        )
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Something unexpected went wrong")


def get_from_db_by_id(model: SQLModelMetaclass, id: Any, session: Session):

    db_item = session.get(model, id)
    if not db_item:
        raise HTTPException(
            status_code=404, detail=f"{model().__class__.__name__} with {id} not found"
        )

    return db_item


def get_from_db_by_uuid(model: SQLModelMetaclass, uuid: Any, session: Session):

    stmt = select(model).where(model.uuid == uuid)
    result = session.exec(stmt)
    try:
        db_item = result.one()
    except NoResultFound:
        raise HTTPException(
            status_code=404,
            detail=f"{model().__class__.__name__} with uuid {uuid} not found",
        )

    return db_item


def get_from_db_by_name(
    model: Any, name: Optional[str], offset: int, limit: int, session: Session
):

    stmt = select(model)
    if name is not None:
        stmt = stmt.where(model.name.like(name + "%"))
    items = session.exec(stmt.offset(offset).limit(limit)).all()

    return items


def get_scope_from_db_by_name(name: str, session: Session):

    db_scope = session.get(Scope, name)
    if not db_scope:
        raise HTTPException(status_code=404, detail=f"Scope {name} not found")

    return db_scope


def get_user_from_db_by_username(username: str, session: Session):

    stmt = select(User).where(User.username == username)
    result = session.exec(stmt)
    try:
        db_user = result.one()
    except NoResultFound:
        raise UserNotFoundException

    return db_user


def get_coll_from_db_by_scope_name(scope: str, name: str, session: Session):

    stmt = select(Collection).where(Collection.scope == scope, Collection.name == name)
    result = session.exec(stmt)
    try:
        db_collection = result.one()
    except NoResultFound:
        raise HTTPException(
            status_code=404,
            detail=f"Collection with scope {scope} and name {name} not found",
        )

    return db_collection


def get_dataset_from_db_by_scope_uuid(scope: str, uuid: UUID, session: Session):

    stmt = select(Dataset).where(Dataset.scope == scope, Dataset.uuid == uuid)
    result = session.exec(stmt)
    try:
        db_dataset = result.one()
    except NoResultFound:
        raise HTTPException(
            status_code=404,
            detail=f"Dataset with scope {scope} and uuid {uuid} not found",
        )

    return db_dataset


def get_file_from_db_by_scope_uuid(scope: str, uuid: UUID, session: Session):

    stmt = select(File).where(File.scope == scope, File.uuid == uuid)
    result = session.exec(stmt)
    try:
        db_file = result.one()
    except NoResultFound:
        raise HTTPException(
            status_code=404, detail=f"File with scope {scope} and uuid {uuid} not found"
        )

    return db_file


def get_upload_from_db_by_uuid(uuid: UUID, session: Session):

    db_upload = session.get(Upload, uuid)
    if not db_upload:
        raise HTTPException(status_code=404, detail=f"Upload with {uuid} not found")

    return db_upload
