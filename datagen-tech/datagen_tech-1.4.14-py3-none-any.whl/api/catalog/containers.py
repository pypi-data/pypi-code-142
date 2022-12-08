from functools import partial

from dependency_injector import containers, providers

from datagen.dev import load_resource
from datagen.api import assets
from datagen.api.catalog import attributes
from datagen.api.catalog.hooks import HumansDefaultsHook
from datagen.api.catalog.impl import AssetCatalog, DatagenAssetsCatalog

load_cache_resource = partial(load_resource, "cache")


class AssetsCatalogContainer(containers.DeclarativeContainer):

    humans = providers.Singleton(
        AssetCatalog,
        asset_type=assets.Human,
        asset_attributes_type=attributes.HumanAttributes,
        asset_id_to_asset_attrs=load_cache_resource("humans", "attributes.json"),
        hooks=providers.List(providers.Singleton(HumansDefaultsHook)),
    )

    eyes = providers.Singleton(
        AssetCatalog,
        asset_type=assets.Eyes,
        asset_attributes_type=attributes.EyesAttributes,
        asset_id_to_asset_attrs=load_cache_resource("eyes.json"),
    )

    hair = providers.Singleton(
        AssetCatalog,
        asset_type=assets.Hair,
        asset_attributes_type=attributes.HairAttributes,
        asset_id_to_asset_attrs=load_cache_resource("hair.json"),
    )

    eyebrows = providers.Singleton(
        AssetCatalog,
        asset_type=assets.Hair,
        asset_attributes_type=attributes.EyebrowsAttributes,
        asset_id_to_asset_attrs=load_cache_resource("eyebrows.json"),
    )

    beards = providers.Singleton(
        AssetCatalog,
        asset_type=assets.Hair,
        asset_attributes_type=attributes.BeardAttributes,
        asset_id_to_asset_attrs=load_cache_resource("beards.json"),
    )

    glasses = providers.Singleton(
        AssetCatalog,
        asset_type=assets.Glasses,
        asset_attributes_type=attributes.GlassesAttributes,
        asset_id_to_asset_attrs=load_cache_resource("glasses.json"),
    )

    masks = providers.Singleton(
        AssetCatalog,
        asset_type=assets.Mask,
        asset_attributes_type=attributes.MaskAttributes,
        asset_id_to_asset_attrs=load_cache_resource("masks.json"),
    )

    backgrounds = providers.Singleton(
        AssetCatalog,
        asset_type=assets.Background,
        asset_attributes_type=attributes.BackgroundAttributes,
        asset_id_to_asset_attrs=load_cache_resource("backgrounds.json"),
    )

    catalog = providers.Singleton(
        DatagenAssetsCatalog,
        humans=humans,
        hair=hair,
        eyes=eyes,
        eyebrows=eyebrows,
        beards=beards,
        glasses=glasses,
        backgrounds=backgrounds,
        masks=masks,
    )
