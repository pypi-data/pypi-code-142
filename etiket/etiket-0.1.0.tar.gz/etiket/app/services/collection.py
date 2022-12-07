from uuid import UUID
from sqlmodel import Session, select

from etiket.core.exceptions import (
    UserNotInScopeException,
    DatasetAlreadyPartOfCollectionException,
    DatasetAlreadyNotPartOfCollectionException,
)
from etiket.app.models import (
    Collection,
    CollectionCreate,
    CollectionUpdate,
)
from etiket.app.crud.db import (
    get_scope_from_db_by_name,
    commit_to_db,
    get_coll_from_db_by_scope_name,
    get_dataset_from_db_by_scope_uuid,
)


class CollectionService:
    def __init__(self):
        pass

    async def create_collection(self, collection: CollectionCreate, user, session):
        scope = get_scope_from_db_by_name(collection.scope, session)
        if user not in scope.users:
            raise UserNotInScopeException(scope.name)
        db_collection = Collection.from_orm(collection)
        db_collection = commit_to_db(db_collection, session)
        return db_collection

    async def get_collections(
        self, scope: str, name: str, offset: int, limit: int, session
    ):
        stmt = select(Collection)
        stmt = stmt.where(Collection.scope == scope)
        if name is not None:
            stmt = stmt.where(Collection.name.like(name + "%"))
        collections = session.exec(
            stmt.order_by(Collection.scope, Collection.name).offset(offset).limit(limit)
        ).all()
        return collections

    async def get_collection(self, scope: str, name: str, session):
        collection = get_coll_from_db_by_scope_name(scope, name, session)
        return collection

    async def add_dataset_to_collection(
        self, scope: str, name: str, dataset_uuid: UUID, user, session
    ):
        collection = get_coll_from_db_by_scope_name(scope, name, session)
        if user not in collection.scopes.users:
            raise UserNotInScopeException(scope)
        dataset = get_dataset_from_db_by_scope_uuid(scope, dataset_uuid, session)
        if dataset in collection.datasets:
            raise DatasetAlreadyPartOfCollectionException(scope, dataset_uuid, name)
        collection.datasets.append(dataset)
        collection = commit_to_db(collection, session)
        return collection

    async def remove_dataset_from_collection(
        self, scope: str, name: str, dataset_uuid: UUID, user, session
    ):
        collection = get_coll_from_db_by_scope_name(scope, name, session)
        if user not in collection.scopes.users:
            raise UserNotInScopeException(scope)
        dataset = get_dataset_from_db_by_scope_uuid(scope, dataset_uuid, session)
        if dataset not in collection.datasets:
            raise DatasetAlreadyNotPartOfCollectionException(scope, dataset_uuid, name)
        collection.datasets.remove(dataset)
        collection = commit_to_db(collection, session)
        return collection

    async def update_collection(
        self, scope: str, name: str, collection: CollectionUpdate, user, session
    ):
        db_collection = get_coll_from_db_by_scope_name(scope, name, session)
        if user not in db_collection.scopes.users:
            raise UserNotInScopeException(scope)
        collection_data = collection.dict(exclude_unset=True)
        for key, value in collection_data.items():
            if value is None:
                continue
            setattr(db_collection, key, value)
        db_collection = commit_to_db(db_collection, session)
        return db_collection
