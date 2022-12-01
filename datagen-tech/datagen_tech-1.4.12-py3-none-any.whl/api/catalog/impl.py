import abc

from rich import pretty as pretty_rich

from dataclasses import dataclass, field
from typing import Optional, TypeVar, Generic, Union, Dict, List

from dependency_injector import providers
from pydantic import Extra

from datagen.api.catalog.attributes import AssetAttributes, AssetAttributesCache
from datagen.api.assets import Hair, Human, Eyes, Glasses, Mask, Background

Asset = TypeVar("Asset")


class PostLoad(abc.ABC, Generic[Asset]):
    @abc.abstractmethod
    def __call__(self, asset: Asset) -> None:
        ...


class AssetLoadingHooks(Generic[Asset]):
    def __init__(self, post_load: List[PostLoad[Asset]] = []):
        self._post_load = post_load

    def post_load(self, asset: Asset) -> None:
        for h in self._post_load:
            h(asset)


class AssetCatalog(Generic[Asset]):
    def __init__(
        self, asset_provider: providers.Provider, cache: AssetAttributesCache, hooks: AssetLoadingHooks[Asset] = None
    ):
        self._asset_provider = asset_provider
        self._cache = cache
        self._hooks = hooks

    def get(
        self, id: Optional[str] = None, limit: Optional[int] = None, load_assets: bool = True, **attributes
    ) -> Union[Asset, List[Asset], Dict[str, AssetAttributes], AssetAttributes]:
        asset_id_to_attrs = self._cache.query(asset_id=id, limit=limit, **attributes)
        single_asset = id or limit == 1
        if single_asset:
            asset_id, asset_attrs = next(iter(asset_id_to_attrs.items()))
            return self._load_asset(asset_id, asset_attrs) if load_assets else asset_attrs
        else:
            return self._load(asset_id_to_attrs) if load_assets else asset_id_to_attrs

    def _load(self, assets: Dict[str, AssetAttributes]) -> List[Asset]:
        loaded_assets = []
        for asset_id, asset_attributes in assets.items():
            asset = self._load_asset(asset_id, asset_attributes)
            loaded_assets.append(asset)
        return loaded_assets

    def _load_asset(self, asset_id: str, attributes: AssetAttributes) -> Asset:
        asset = self._asset_provider(id=asset_id)
        self._add_attributes(asset, attributes)
        self._apply_post_load(asset)
        return asset

    def _apply_post_load(self, asset):
        if self._hooks:
            self._hooks.post_load(asset)

    def parse(self, id: str, **asset_body_json) -> Asset:
        asset = self._asset_provider(id=id, **asset_body_json)
        asset_attributes = self.get(id=id, load_assets=False)
        self._add_attributes(asset, asset_attributes)
        return asset

    def _add_attributes(self, asset: Asset, attributes: AssetAttributes):
        asset.Config.extra = Extra.allow
        asset.attributes = attributes
        asset.Config.extra = Extra.forbid

    def count(self, **attributes) -> int:
        return len(self._cache.query(**attributes))


@dataclass
class DatagenAssetsCatalog:
    humans: AssetCatalog[Human]
    hair: AssetCatalog[Hair]
    eyes: AssetCatalog[Eyes]
    eyebrows: AssetCatalog[Hair]
    beards: AssetCatalog[Hair]
    glasses: AssetCatalog[Glasses]
    masks: AssetCatalog[Mask]
    backgrounds: AssetCatalog[Background]

    def __post_init__(self):
        pretty_rich.install()
