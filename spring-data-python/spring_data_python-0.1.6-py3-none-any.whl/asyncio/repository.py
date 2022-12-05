from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional

from springdata.domain import Page, Sort, Pageable

T = TypeVar("T")
ID = TypeVar("ID")


class CrudRepository(ABC, Generic[T, ID]):
    """
    Interface for generic CRUD operations on a repository for a specific type.
    """

    @abstractmethod
    async def clear(self) -> None:
        """
        Deletes all entities managed by the repository.
        """
        raise NotImplementedError()

    @abstractmethod
    async def count(self) -> int:
        """
        Returns the number of entities available.

        :return: the number of entities.
        """
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, entity: T) -> None:
        """
        Deletes a given entity.

        :param entity: must not be None.
        :raises ValueError: in case the given entity is None.
        """
        raise NotImplementedError()

    @abstractmethod
    async def delete_all(self, entities: List[T]) -> None:
        """
        Deletes the given entities.

        :param entities: must not be None. Must not contain None elements.
        :raises ValueError: in case the given entities or one of its entities is None.
        """
        raise NotImplementedError()

    @abstractmethod
    async def delete_all_by_id(self, ids: List[ID]) -> None:
        """
        Deletes all entities with the given IDs.

        Entities that aren't found in the persistence store are silently ignored.

        :param ids: must not be None. Must not contain None elements.
        :raises ValueError: in case the given ids or one of its elements is None.
        """
        raise NotImplementedError()

    @abstractmethod
    async def delete_by_id(self, id_: ID) -> None:
        """
        Deletes the entity with the given id.

        If the entity is not found in the persistence store it is silently ignored.

        :param id_: must not be None.
        :raises ValueError: if id is None.
        """
        raise NotImplementedError()

    @abstractmethod
    async def exists_by_id(self, id_: ID) -> bool:
        """
        Returns whether an entity with the given id exists.

        :param id_: must not be None.
        :return: true if an entity with the given id exists, false otherwise.
        :raises ValueError: if id is None.
        """
        raise NotImplementedError()

    @abstractmethod
    async def find_all(self, sort: Optional[Sort] = None) -> List[T]:
        """
        Returns all entities.

        :param sort: the specification to sort the results by, default to None.
        :return: all entities.
        """
        raise NotImplementedError()

    @abstractmethod
    async def find_all_by_id(
        self,
        ids: List[ID],
        sort: Optional[Sort] = None,
    ) -> List[T]:
        """
        Returns all entities with the given IDs.

        If some or all ids are not found, no entities are returned for these IDs.

        :param ids: must not be None nor contain any None values.
        :param sort: the specification to sort the results by, default to None.
        :return: guaranteed to be not None. The size can be equal or less than the number of given ids.
        :raises ValueError: in case the given ids or one of its elements is None.
        """
        raise NotImplementedError()

    @abstractmethod
    async def find_by_id(self, id_: ID) -> Optional[T]:
        """
        Retrieves an entity by its id.

        :param id_: must not be None.
        :return: the entity with the given id or None if none found.
        :raises ValueError: if id is None.
        """
        raise NotImplementedError()

    @abstractmethod
    async def save(self, entity: T) -> T:
        """
        Saves a given entity.

        Use the returned instance for further operations as the save operation might have changed the entity instance
        completely.

        :param entity: must not be None.
        :return: the saved entity, will never be None.
        :raises ValueError: in case the given entity is None.
        """
        raise NotImplementedError()

    @abstractmethod
    async def save_all(self, entities: List[T]) -> List[T]:
        """
        Saves all given entities.

        :param entities: must not be None nor must it contain None.
        :return: the saved entities; will never be None. The returned iterable will have the same size as the iterable
                 passed as an argument.
        :raises ValueError: in case the given entities or one of its entities is None.
        """
        raise NotImplementedError()


class PagingRepository(Generic[T, ID], CrudRepository[T, ID]):
    """
    Interface to retrieve entities using the pagination.
    """

    @abstractmethod
    async def find_page(
        self,
        pageable: Pageable,
        sort: Optional[Sort] = None,
    ) -> Page[T]:
        """
        Returns a :class:`Page` of entities meeting the paging restriction provided in the :class:`Pageable` object.

        :param pageable: must not be None.
        :param sort: the specification to sort the results by, default to None.
        :return: a page of entities.
        :raises ValueError: in case the :class:`Pageable` is None.
        """
        raise NotImplementedError()
