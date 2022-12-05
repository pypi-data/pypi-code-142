from functools import partial
from typing import Any, Callable, Mapping, Optional, Sequence, Type, TypeVar

from sqlalchemy import update
from sqlalchemy.orm import attributes
from sqlalchemy.orm.instrumentation import instance_state

from dropland.data.repositories import SqlModelRepository
from dropland.util import is_awaitable
from .engine import SqlAlchemyAsyncEngine
from .model import SqlaModel

SqlaModelType = TypeVar('SqlaModelType', bound=SqlaModel, covariant=True)
SqlaModelTypeFactory = Callable[..., SqlaModelType]


class SqlaModelRepository(SqlModelRepository[SqlaModelType]):
    def __init__(self, model_class: Type[SqlaModelType],
                 engine: SqlAlchemyAsyncEngine,
                 model_factory: Optional[SqlaModelTypeFactory] = None):
        super(SqlaModelRepository, self).__init__(model_class, model_factory)
        self._engine = engine
        self._model_factory = partial(self._construct_instances, self._model_factory)

        model_class.__table__.metadata = engine.metadata
        model_class.__table__.schema = engine.metadata.schema
        model_class.metadata = model_class.registry.metadata = engine.metadata

    def get_engine(self) -> SqlAlchemyAsyncEngine:
        return self._engine

    async def _construct_instances(
            self, model_factory, _from_cache: bool = False,
            **kwargs: Mapping[str, Any]) -> SqlaModelType:
        if not _from_cache:
            return model_factory(**kwargs)

        instance = model_factory()
        assert instance

        if is_awaitable(instance):
            instance = await instance

        for k, v in kwargs.items():
            try:
                attributes.set_committed_value(instance, k, v)
            except KeyError:
                setattr(instance, k, v)

        state = attributes.instance_state(instance)
        if state.session_id or state.key:
            return instance

        async with self._engine.session() as session:
            state.session_id = session.sync_session.hash_key

            def _set(sync_session):
                # noinspection PyProtectedMember
                sync_session._register_persistent(state)  # type: ignore

            await session.run_sync(_set)

        return instance

    #
    # Retrieve operations
    #

    async def get(self, id_value: Any, **kwargs) -> Optional[SqlaModelType]:
        async with self._engine.session() as session:
            query = self.model_class.query_get(id_value, **kwargs)
            if row := (await session.execute(query)).first():
                # noinspection PyProtectedMember
                return row._mapping[self.model_class]
        return None

    async def get_any(self, indices: Sequence[Any], **kwargs) -> Sequence[Optional[SqlaModelType]]:
        async with self._engine.session() as session:
            query = self.model_class.query_any(indices, **kwargs)
            rows = (await session.execute(query)).all()
            # noinspection PyProtectedMember
            objects = [row._mapping[self.model_class] for row in rows]

        objects = {obj.get_id_value(): obj for obj in objects if obj is not None}
        return [objects[id_value] if id_value in objects else None for id_value in indices]

    async def list(
            self, filters: Optional[Sequence[Any]] = None, sorting: Optional[Sequence[Any]] = None,
            skip: int = 0, limit: int = 0, params: Mapping[str, Any] = None, **kwargs) -> Sequence[SqlaModelType]:
        query = self.model_class.query_list(filters or [], sorting or [], skip, limit, params, **kwargs)
        async with self._engine.session() as session:
            if rows := (await session.execute(query)).all():
                # noinspection PyProtectedMember
                return [row._mapping[self.model_class] for row in rows]
            return []

    async def count(self, filters: Optional[Sequence[Any]] = None, params: Mapping[str, Any] = None, **kwargs) -> int:
        async with self._engine.session() as session:
            query = self.model_class.query_count(filters, params, **kwargs)
            return await session.scalar(query)

    async def exists(self, id_value: Any, **kwargs) -> bool:
        async with self._engine.session() as session:
            query = self.model_class.query_exists(id_value, **kwargs)
            return bool(await session.scalar(query))

    async def exists_by(self, filters: Sequence[Any], params: Mapping[str, Any] = None, **kwargs) -> bool:
        if not filters or not isinstance(filters, list):
            return False

        async with self._engine.session() as session:
            query = self.model_class.query_exists_by(filters, params, **kwargs)
            return bool(await session.scalar(query))

    async def load(self, instance: SqlaModelType, only: Sequence[str] = None) -> bool:
        iss = instance_state(instance)

        if iss.was_deleted or iss.transient:
            return False

        only = set(only) if only else None
        async with self._engine.session() as session:
            await session.refresh(instance, attribute_names=only)
            return True

    #
    # Modification operations
    #

    async def create(self, data: Mapping[str, Any], **kwargs) -> Optional[SqlaModelType]:
        instance = await self.model_class.construct(data, **kwargs)
        async with self._engine.session() as session:
            session.add(instance)
            await session.flush(objects=[instance])
        return instance

    async def update_by_id(self, id_value: Any, data: Mapping[str, Any], **kwargs) -> bool:
        query = self.model_class.query_get(id_value, query=update(self.model_class, values=data))
        async with self._engine.session() as session:
            cursor = await session.execute(query)
            return cursor.rowcount == 1

    async def update_by(self, filters: Sequence[Any], data: Mapping[str, Any],
                        /, params: Mapping[str, Any] = None, **kwargs) -> int:
        query = self.model_class.query_update(filters, params, **kwargs).values(data)
        async with self._engine.session() as session:
            cursor = await session.execute(query)
            return cursor.rowcount

    async def save(self, instance: SqlaModelType, **kwargs) -> bool:
        iss = instance_state(instance)

        if iss.was_deleted:
            return False

        async with self._engine.session() as session:
            if iss.transient:
                session.add(instance)
            await session.flush(objects=[instance])
            return True

    async def save_all(self, objects: Sequence[SqlaModelType], **kwargs) -> bool:
        async with self._engine.session() as session:
            for obj in objects:
                session.add(obj)

            await session.run_sync(lambda s: s.bulk_save_objects(objects))
            await session.flush(objects=objects)
            return True

    async def delete(self, instance: SqlaModelType) -> bool:
        if instance_state(instance).was_deleted:
            return False

        async with self._engine.session() as session:
            await session.delete(instance)
            await session.flush(objects=[instance])
            return True

    async def delete_all(self, indices: Sequence[Any] = None) -> int:
        if indices is None:
            query = self.model_class.query_for_delete()
        else:
            query = self.model_class.query_any(indices, query=self.model_class.query_for_delete())

        async with self._engine.session() as session:
            cursor = await session.execute(query)

        return cursor.rowcount

    async def delete_by_id(self, id_value: Any) -> bool:
        query = self.model_class.query_get(id_value, query=self.model_class.query_for_delete())
        async with self._engine.session() as session:
            cursor = await session.execute(query)
            return 1 == cursor.rowcount

    async def delete_by(self, filters: Sequence[Any], /, params: Mapping[str, Any] = None, **kwargs) -> int:
        query = self.model_class.query_delete(filters, params, **kwargs)
        async with self._engine.session() as session:
            cursor = await session.execute(query)
            return cursor.rowcount
