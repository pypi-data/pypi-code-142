from uuid import UUID
from datetime import datetime
from typing import List
from sqlmodel import Session, select
from sqlalchemy.orm.attributes import flag_modified

from etiket.core.exceptions import (
    UserNotInScopeException,
)
from etiket.app.models import (
    Dataset,
    Collection,
    DatasetCreate,
    DatasetUpdate,
    DatasetMeta,
    DatasetMetaKeys,
    DatasetReadExtended,
)
from etiket.app.crud.db import (
    get_scope_from_db_by_name,
    commit_to_db,
    get_dataset_from_db_by_scope_uuid,
)


class DatasetService:
    def __init__(self):
        pass

    async def create_dataset(
        self, dataset: DatasetCreate, user, session
    ) -> DatasetReadExtended:
        db_dataset = Dataset.from_orm(dataset)
        scope = get_scope_from_db_by_name(db_dataset.scope, session)
        if user not in scope.users:
            raise UserNotInScopeException(scope.name)
        db_dataset = commit_to_db(db_dataset, session)
        return db_dataset

    async def get_datasets(
        self,
        scope: str,
        collection: str,
        name: str,
        since: datetime,
        until: datetime,
        ranking: int = 0,
        offset: int,
        limit: int,
        session,
    ) -> List[DatasetReadExtended]:
        stmt = select(Dataset)
        stmt = stmt.where(Dataset.scope == scope)
        stmt = stmt.where(Dataset.ranking >= ranking)
        if collection:
            stmt = stmt.join(Dataset.collections).where(
                Collection.name.like(collection + "%")
            )
        if name:
            stmt = stmt.where(Dataset.name.like(name + "%"))
        if since:
            stmt = stmt.where(Dataset.created >= since)
        if until:
            stmt = stmt.where(Dataset.created <= until)

        datasets = session.exec(
            stmt.order_by(Dataset.created).offset(offset).limit(limit)
        ).all()
        return datasets

    async def get_dataset(
        self, scope: str, dataset_uuid: UUID, session
    ) -> DatasetReadExtended:
        dataset = get_dataset_from_db_by_scope_uuid(scope, dataset_uuid, session)
        return dataset

    async def add_metadata_to_dataset(
        self, scope: str, dataset_uuid: UUID, add_meta: DatasetMeta, user, session
    ) -> DatasetReadExtended:
        db_dataset = get_dataset_from_db_by_scope_uuid(scope, dataset_uuid, session)
        if user not in db_dataset.scopes.users:
            raise UserNotInScopeException(scope)
        existing_metadata = {}
        if db_dataset.meta:
            existing_metadata = db_dataset.meta
        for key, value in add_meta.meta.items():
            val = existing_metadata.get(key)
            if val:
                if type(existing_metadata[key]) != list:
                    existing_metadata[key] = [existing_metadata[key]]
                if type(val) == list:
                    existing_metadata[key] += value
                else:
                    existing_metadata[key] += [value]
            else:
                existing_metadata[key] = value
        flag_modified(db_dataset, "meta")
        db_dataset = commit_to_db(db_dataset, session)
        return db_dataset

    async def set_metadata_for_dataset(
        self, scope: str, dataset_uuid: UUID, set_meta: DatasetMeta, user, session
    ) -> DatasetReadExtended:
        db_dataset = get_dataset_from_db_by_scope_uuid(scope, dataset_uuid, session)
        if user not in db_dataset.scopes.users:
            raise UserNotInScopeException(scope)
        existing_metadata = {}
        if db_dataset.meta:
            existing_metadata = db_dataset.meta
        for key, value in set_meta.meta.items():
            existing_metadata[key] = value
        flag_modified(db_dataset, "meta")
        db_dataset = commit_to_db(db_dataset, session)
        return db_dataset

    async def delete_metadata_from_dataset(
        self, scope: str, dataset_uuid: UUID, del_meta: DatasetMetaKeys, user, session
    ) -> DatasetReadExtended:
        db_dataset = get_dataset_from_db_by_scope_uuid(scope, dataset_uuid, session)
        if user not in db_dataset.scopes.users:
            raise UserNotInScopeException(scope)
        existing_metadata = {}
        if db_dataset.meta:
            existing_metadata = db_dataset.meta
            for key in del_meta.keys:
                try:
                    del existing_metadata[key]
                except KeyError:
                    pass
            flag_modified(db_dataset, "meta")
            db_dataset = commit_to_db(db_dataset, session)
        return db_dataset

    async def update_dataset(
        self, scope: str, dataset_uuid: UUID, dataset: DatasetUpdate, user, session
    ) -> DatasetReadExtended:
        db_dataset = get_dataset_from_db_by_scope_uuid(scope, dataset_uuid, session)
        if user not in db_dataset.scopes.users:
            raise UserNotInScopeException(scope)
        dataset_data = dataset.dict(exclude_unset=True)
        for key, value in dataset_data.items():
            if value is None:
                continue
            setattr(db_dataset, key, value)
        db_dataset = commit_to_db(db_dataset, session)
        return db_dataset
