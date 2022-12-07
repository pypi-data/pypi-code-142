import abc
from typing import TypeVar, Generic, Union, Dict, List, Type

import numpy as np
import pandas as pd

try:
    from collections import Sequence
except ImportError:
    from collections.abc import Sequence  # >=Python 3.10

from rich import pretty as pretty_rich
from pydantic import Extra

from datagen.api.catalog.attributes import AssetAttributes, Enum, AllOf, AnyOf, Exactly
from datagen.api.assets import Human, Hair, Eyes, Glasses, Mask, Background

Asset = TypeVar("Asset")


class AssetCreationHook(abc.ABC, Generic[Asset]):
    @abc.abstractmethod
    def __call__(self, *args) -> None:
        ...


class PreProvisionHook(AssetCreationHook, abc.ABC, Generic[Asset]):
    @abc.abstractmethod
    def __call__(self, asset_id: str) -> dict:
        ...


class PostLoadHook(AssetCreationHook, abc.ABC, Generic[Asset]):
    @abc.abstractmethod
    def __call__(self, asset: Asset) -> None:
        ...


class AssetCreationHooks(Generic[Asset]):
    def __init__(self, hooks: List[AssetCreationHook]):
        self._hooks = hooks

    @property
    def _pre_provision_hooks(self) -> List[PreProvisionHook]:
        return list(filter(lambda h: isinstance(h, PreProvisionHook), self._hooks))  # type: ignore

    def pre_provision(self, asset_id: str) -> dict:
        preload_params = {}
        for h in self._pre_provision_hooks:
            preload_params.update(**h(asset_id))
        return preload_params

    @property
    def _post_load_hooks(self) -> List[PostLoadHook]:
        return list(filter(lambda h: isinstance(h, PostLoadHook), self._hooks))  # type: ignore

    def post_load(self, asset: Asset) -> None:
        for h in self._post_load_hooks:
            h(asset)


class AssetInstancesProvisioner(Generic[Asset]):
    def __init__(
        self,
        asset_type: Type[Asset],
        asset_attributes_type: Type[AssetAttributes],
        asset_id_to_asset_attrs: dict,
        hooks: List[AssetCreationHook[Asset]],
    ):
        self._asset_type = asset_type
        self._asset_attributes_type = asset_attributes_type
        self._asset_id_to_asset_attrs = asset_id_to_asset_attrs
        self._hooks = AssetCreationHooks(hooks)

    def provision(self, asset_id: str) -> Asset:
        pre_provision_params = self._hooks.pre_provision(asset_id)
        asset = self._asset_type(id=asset_id, **pre_provision_params)
        self._add_attributes(asset)
        return asset

    def _add_attributes(self, asset: Asset):
        asset.Config.extra = Extra.allow
        asset.attributes = self._get_attributes(asset)
        asset.Config.extra = Extra.forbid

    def _get_attributes(self, asset: Asset) -> AssetAttributes:
        asset_attrs = self._asset_id_to_asset_attrs[asset.id]
        if isinstance(asset_attrs, dict):
            asset_attrs = self._asset_id_to_asset_attrs[asset.id] = self._load_attrs(asset_attrs)
        return asset_attrs

    def _load_attrs(self, attrs_dict: dict) -> AssetAttributes:
        return self._asset_attributes_type.Schema().load(attrs_dict)

    def parse(self, asset_id: str, asset_body_dict: dict) -> Asset:
        asset = self._asset_type.parse_obj({"id": asset_id, **asset_body_dict})
        self._add_attributes(asset)
        return asset

    def post_load(self, asset: Asset) -> Asset:
        self._hooks.post_load(asset)
        return asset


class CatalogInstancesCache(Generic[Asset]):
    def __init__(self, provisioner: AssetInstancesProvisioner):
        self._provisioner = provisioner
        self._cache = {}

    def get(self, asset_id: str) -> Asset:
        asset = self._load(asset_id)
        asset = self._provisioner.post_load(asset)
        return asset

    def _load(self, asset_id) -> Asset:
        try:
            asset = self._cache[asset_id]
        except KeyError:
            asset = self._cache.setdefault(asset_id, self._provisioner.provision(asset_id))
        return asset


class AssetInstancesList(Sequence):
    def __init__(self, instances_cache: CatalogInstancesCache, assets_ids: List[str]):
        self._instances_cache = instances_cache
        self._assets_ids = assets_ids

    def __repr__(self):
        return f"<{self.__class__.__name__}({len(self)})>"

    def __iter__(self):
        return AssetInstancesIter(self)

    def __len__(self):
        return len(self._assets_ids)

    def __getitem__(self, index):
        return self._instances_cache.get(self._assets_ids[index])

    def __contains__(self, element):
        return element in self._assets_ids


class AssetInstancesIter:
    def __init__(self, instances_list: AssetInstancesList):
        self._idx = 0
        self._instances_list = instances_list

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx < len(self._instances_list):
            self._idx += 1
            return self._instances_list[self._idx - 1]
        else:
            raise StopIteration


class AttributesDataFrame:
    def __init__(self, attributes_df: pd.DataFrame):
        self._df = attributes_df

    def query(self, attributes: Dict[str, Union[Enum, AllOf, AnyOf, Exactly]], limit: int = None) -> List[str]:
        if attributes:
            df = self._df.loc[self._create_query_series(attributes)]
        else:
            df = self._df
        return list(df.index)[:limit]

    def _create_query_series(self, attributes: Dict[str, Union[Enum, AllOf, AnyOf, Exactly]]) -> pd.Series:
        attrs_series_list = [
            self._create_attr_series(attr_name, attr_query_val) for attr_name, attr_query_val in attributes.items()
        ]
        return np.logical_and.reduce(attrs_series_list)  # type: ignore

    def _create_attr_series(self, attr_name: str, attr_query_val: Union[Enum, AllOf, AnyOf, Exactly]) -> pd.Series:
        if isinstance(attr_query_val, Enum):
            return self._create_series(attr_name, attr_query_val)
        elif isinstance(attr_query_val, (AllOf, AnyOf)):
            series_list = [self._create_series(attr_name, attr_val) for attr_val in attr_query_val]
            operator = np.logical_and if isinstance(attr_query_val, AllOf) else np.logical_or
            return operator.reduce(series_list)  # type: ignore

    def _create_series(self, attr_name: str, attr_val: Enum) -> pd.Series:
        return self._df[f"{attr_val.value}_{attr_name}"].__eq__(True)

    @staticmethod
    def from_dict(asset_id_to_asset_attrs: dict) -> "AttributesDataFrame":
        attrs_dataframe_dict = {}
        for asset_id, asset_attrs_dict in asset_id_to_asset_attrs.items():
            attrs_dataframe_dict[asset_id] = AttributesDataFrame._get_dataframe_row(asset_attrs_dict)
        attr_dataframe = pd.DataFrame.from_dict(attrs_dataframe_dict, orient="index")
        return AttributesDataFrame(attr_dataframe)

    @staticmethod
    def _get_dataframe_row(asset_attrs_dict: dict) -> dict:
        dataframe_row = {}
        for attr_name, attr_value in asset_attrs_dict.items():
            if not isinstance(attr_value, list):
                attr_value = [attr_value]
            for v in attr_value:
                dataframe_row[v + "_" + attr_name] = True
        return dataframe_row


class AssetCatalog(Generic[Asset]):
    def __init__(
        self,
        asset_type: Type[Asset],
        asset_attributes_type: Type[AssetAttributes],
        asset_id_to_asset_attrs: dict,
        hooks: List[AssetCreationHook[Asset]] = [],
    ):

        self._provisioner = AssetInstancesProvisioner(asset_type, asset_attributes_type, asset_id_to_asset_attrs, hooks)
        self._instances_cache = CatalogInstancesCache(self._provisioner)
        self._attributes_df = AttributesDataFrame.from_dict(asset_id_to_asset_attrs)

    def get(
        self, id: str = None, limit: int = None, **attributes
    ) -> Union[Asset, List[Asset], Dict[str, AssetAttributes], AssetAttributes]:
        if id:
            return self._instances_cache.get(id)
        else:
            matching_assets_ids = self._attributes_df.query(attributes, limit)
            if limit == 1:
                return self._instances_cache.get(matching_assets_ids[0])
            else:
                return AssetInstancesList(self._instances_cache, matching_assets_ids)

    def count(self, **attributes) -> int:
        return len(self._attributes_df.query(attributes))

    def parse(self, id: str, **asset_body) -> Asset:
        return self._provisioner.parse(asset_id=id, asset_body_dict=asset_body)


class DatagenAssetsCatalog:
    def __init__(
        self,
        humans: AssetCatalog[Human],
        hair: AssetCatalog[Hair],
        eyes: AssetCatalog[Eyes],
        eyebrows: AssetCatalog[Hair],
        beards: AssetCatalog[Hair],
        glasses: AssetCatalog[Glasses],
        masks: AssetCatalog[Mask],
        backgrounds: AssetCatalog[Background],
    ):
        self._humans = humans
        self._hair = hair
        self._eyes = eyes
        self._eyebrows = eyebrows
        self._beards = beards
        self._glasses = glasses
        self._masks = masks
        self._backgrounds = backgrounds

        pretty_rich.install()

    @property
    def humans(self) -> AssetCatalog[Human]:
        return self._humans

    @property
    def hair(self) -> AssetCatalog[Hair]:
        return self._hair

    @property
    def eyes(self) -> AssetCatalog[Eyes]:
        return self._eyes

    @property
    def eyebrows(self) -> AssetCatalog[Hair]:
        return self._eyebrows

    @property
    def beards(self) -> AssetCatalog[Hair]:
        return self._beards

    @property
    def glasses(self) -> AssetCatalog[Glasses]:
        return self._glasses

    @property
    def masks(self) -> AssetCatalog[Mask]:
        return self._masks

    @property
    def backgrounds(self) -> AssetCatalog[Background]:
        return self._backgrounds
