import json
from pathlib import Path
from typing import Type

from dependency_injector import containers, providers
from pydantic import BaseModel

from datagen.api import assets
from datagen.api.catalog import attributes
from datagen.api.catalog.hooks import AssignDefaultsToHuman
from datagen.api.catalog.attributes import AssetAttributesCache
from datagen.api.catalog.impl import AssetCatalog, DatagenAssetsCatalog, AssetLoadingHooks


def create_human(id: str) -> assets.Human:
    with open(Path(__file__).parent.joinpath("human_templates", "neutral.json")) as f:
        human_dict = json.load(f)
        human_dict["id"] = id
    return assets.Human.parse_obj(human_dict)


def asset_parsing_provider(asset_model: Type[BaseModel]):
    def parse(id: str, **asset_body_json):
        return asset_model.parse_obj({"id": id, **asset_body_json})

    return providers.Callable(parse).provider


class AssetProvidersContainer(containers.DeclarativeContainer):

    human = providers.Callable(create_human).provider

    eyes = asset_parsing_provider(assets.Eyes)

    hair = asset_parsing_provider(assets.Hair)

    glasses = asset_parsing_provider(assets.Glasses)

    mask = asset_parsing_provider(assets.Mask)

    background = asset_parsing_provider(assets.Background)


class AssetsCatalogContainer(containers.DeclarativeContainer):

    assets_providers = providers.Container(AssetProvidersContainer)

    humans = providers.Singleton(
        AssetCatalog,
        asset_provider=assets_providers.human,
        cache=providers.Singleton(
            AssetAttributesCache,
            attributes_type=attributes.HumanAttributes,
            cache_file_name="humans.json",
        ),
        hooks=providers.Singleton(
            AssetLoadingHooks, post_load=providers.List(providers.Singleton(AssignDefaultsToHuman))
        ),
    )

    eyes = providers.Singleton(
        AssetCatalog,
        asset_provider=assets_providers.eyes,
        cache=providers.Singleton(
            AssetAttributesCache,
            attributes_type=attributes.EyesAttributes,
            cache_file_name="eyes.json",
        ),
    )

    hair = providers.Singleton(
        AssetCatalog,
        asset_provider=assets_providers.hair,
        cache=providers.Singleton(
            AssetAttributesCache,
            attributes_type=attributes.HairAttributes,
            cache_file_name="hair.json",
        ),
    )

    eyebrows = providers.Singleton(
        AssetCatalog,
        asset_provider=assets_providers.hair,
        cache=providers.Singleton(
            AssetAttributesCache,
            attributes_type=attributes.EyebrowsAttributes,
            cache_file_name="eyebrows.json",
        ),
    )

    beards = providers.Singleton(
        AssetCatalog,
        asset_provider=assets_providers.hair,
        cache=providers.Singleton(
            AssetAttributesCache,
            attributes_type=attributes.BeardAttributes,
            cache_file_name="beards.json",
        ),
    )

    glasses = providers.Singleton(
        AssetCatalog,
        asset_provider=assets_providers.glasses,
        cache=providers.Singleton(
            AssetAttributesCache,
            attributes_type=attributes.GlassesAttributes,
            cache_file_name="glasses.json",
        ),
    )

    masks = providers.Singleton(
        AssetCatalog,
        asset_provider=assets_providers.mask,
        cache=providers.Singleton(
            AssetAttributesCache,
            attributes_type=attributes.MaskAttributes,
            cache_file_name="masks.json",
        ),
    )

    backgrounds = providers.Singleton(
        AssetCatalog,
        asset_provider=assets_providers.background,
        cache=providers.Singleton(
            AssetAttributesCache,
            attributes_type=attributes.BackgroundAttributes,
            cache_file_name="backgrounds.json",
        ),
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
