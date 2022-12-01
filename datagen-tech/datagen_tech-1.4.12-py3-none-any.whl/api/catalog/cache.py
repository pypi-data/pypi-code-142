import abc
import json
from functools import lru_cache

from pathlib import Path
from typing import Optional, Generic, TypeVar, Dict, Callable, Union

Asset = TypeVar("Asset")

CachedContent = TypeVar("CachedContent")


class AssetCache(abc.ABC, Generic[Asset, CachedContent]):
    def __init__(self, cache_provider: Callable[[Dict], CachedContent]):
        self._cache_provider = cache_provider

    def query(
        self, asset_id: Optional[str] = None, limit: Optional[int] = None, **query_params
    ) -> Dict[str, CachedContent]:
        if asset_id is not None:
            return self._query_by_id(asset_id)
        else:
            return self._query_by_params(limit, **query_params)

    @abc.abstractmethod
    def _query_by_id(self, asset_id: str) -> CachedContent:
        ...

    @abc.abstractmethod
    def _query_by_params(self, limit: Optional[int], **query_params) -> Dict[str, CachedContent]:
        ...


class InMemAssetCache(AssetCache):
    def __init__(
        self,
        cache_file_name: str,
        cache_provider: Callable[[Dict], CachedContent],
        provide_on_cache_load: bool = True,
    ):
        self._cache_file_name = cache_file_name
        self._provide_on_load = provide_on_cache_load
        super().__init__(cache_provider=cache_provider)

    @property
    def _cache_file_path(self) -> Path:
        return Path(__file__).parent.joinpath("cache", self._cache_file_name)

    @property
    def _provide_on_query_match(self) -> bool:
        return not self._provide_on_load

    def __hash__(self):
        return hash(self._cache_file_name)

    def _query_by_id(self, asset_id: str) -> Dict[str, Union[Dict, CachedContent]]:
        asset_id_to_asset_cache_content = self._get_cache_content()
        asset_cache_content = asset_id_to_asset_cache_content[asset_id]
        if self._provide_on_query_match:
            asset_cache_content = self._cache_provider(asset_cache_content)
        return {asset_id: asset_cache_content}

    def _query_by_params(self, limit: Optional[int], **query_params) -> Dict[str, CachedContent]:
        matching_assets = {}
        for asset_id, asset_cache_content in self._get_cache_content().items():
            if len(matching_assets) == limit:
                break
            elif self._is_matching(asset_cache_content, query_params):
                if self._provide_on_query_match:
                    asset_cache_content = self._cache_provider(asset_cache_content)
                matching_assets[asset_id] = asset_cache_content
        return matching_assets

    @lru_cache(maxsize=None)
    def _get_cache_content(self) -> Dict[str, Union[Dict, CachedContent]]:
        cache_content = json.loads(self._cache_file_path.read_text())
        if self._provide_on_load:
            return {asset_id: self._cache_provider(asset_cache) for asset_id, asset_cache in cache_content.items()}
        else:
            return cache_content

    @abc.abstractmethod
    def _is_matching(self, asset_cache_content: CachedContent, query_params: dict) -> bool:
        pass


class SimpleInMemAssetCache(InMemAssetCache):
    def _query_by_id(self, asset_id: str) -> Union[Dict, CachedContent]:
        asset_cache_content = super()._query_by_id(asset_id)
        return asset_cache_content[asset_id]

    def _is_matching(self, asset_cache_content: CachedContent, query_params: dict) -> bool:
        raise NotImplemented(f"Cannot query {self.__class__.__name__} by params other then asset_id!")
