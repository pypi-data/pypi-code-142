from collections import defaultdict
from typing import Any, Optional, Protocol, Sequence

from .base import AbstractModel
from ..context import get_context


class ModelLocalCacheMixin(Protocol):
    @classmethod
    def _add_to_local_cache(cls, instances: Sequence[AbstractModel]):
        ctx = get_context()

        if not hasattr(ctx, 'cache'):
            ctx.cache = defaultdict(lambda: defaultdict(dict))

        for instance in instances:
            if instance is not None:
                ctx.cache[cls][instance.get_id_value()] = instance

    @classmethod
    def _get_from_local_cache(cls, indices: Sequence[Any]) -> Sequence[Optional[AbstractModel]]:
        ctx = get_context()

        if not hasattr(ctx, 'cache'):
            ctx.cache = defaultdict(lambda: defaultdict(dict))

        return [ctx.cache[cls].get(id_value) for id_value in indices]

    @classmethod
    def _drop_from_local_cache(cls, indices: Sequence[Any] = None) -> Sequence[bool]:
        ctx = get_context()

        if not hasattr(ctx, 'cache'):
            ctx.cache = defaultdict(lambda: defaultdict(dict))

        if indices is None:
            ctx.cache[cls] = defaultdict(dict)
            return [True]

        return [ctx.cache[cls].pop(id_value, None) is None for id_value in indices]

    @classmethod
    def _has_in_local_cache(cls, indices: Sequence[Any]) -> Sequence[bool]:
        ctx = get_context()

        if not hasattr(ctx, 'cache'):
            ctx.cache = defaultdict(lambda: defaultdict(dict))

        return [id_value in ctx.cache[cls] for id_value in indices]

    # noinspection PyProtectedMember
    @classmethod
    async def _register_instances(cls, objects: Sequence[AbstractModel]):
        await super()._register_instances(objects)
        cls._add_to_local_cache(objects)

    # noinspection PyProtectedMember
    @classmethod
    async def _unregister_indices(cls, indices: Sequence[Any] = None):
        cls._drop_from_local_cache(indices)
        await super()._unregister_indices(indices)
