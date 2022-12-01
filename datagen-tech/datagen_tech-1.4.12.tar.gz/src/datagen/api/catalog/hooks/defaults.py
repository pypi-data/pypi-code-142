import os.path

from datagen.api.assets import Human
from datagen.api.catalog.impl import PostLoad
from datagen.api.catalog.cache import SimpleInMemAssetCache

DEFAULTS_ERR = "{0} asset '{1}' does not exist in the catalog"


def parse_defaults(defaults_dicts: dict):
    from datagen.api import catalog

    eyes_dict, eyebrows_dict, hair_dict = defaults_dicts["eyes"], defaults_dicts["eyebrows"], defaults_dicts["hair"]
    try:
        default_eyes = catalog.eyes.parse(**eyes_dict)
    except KeyError:
        raise ValueError(DEFAULTS_ERR.format("Eyes", eyes_dict["id"]))
    try:
        default_eyebrows = catalog.eyebrows.parse(**eyebrows_dict)
    except KeyError:
        raise ValueError(DEFAULTS_ERR.format("Eyebrows", eyebrows_dict["id"]))
    try:
        default_hair = catalog.hair.parse(**hair_dict)
    except KeyError:
        raise ValueError(DEFAULTS_ERR.format("Hair", hair_dict["id"]))
    return default_eyes, default_eyebrows, default_hair


class AssignDefaultsToHuman(PostLoad[Human]):
    def __init__(self):
        self._cache = SimpleInMemAssetCache(
            cache_file_name=os.path.join("defaults", "humans.json"),
            cache_provider=parse_defaults,  # type: ignore
            provide_on_cache_load=False,
        )

    def __call__(self, asset: Human) -> None:
        try:
            asset.head.eyes, asset.head.eyebrows, asset.head.hair = self._cache.query(asset_id=asset.id)
        except KeyError:
            raise ValueError(f"Human asset '{asset.id}' does not have defaults assigned to it")
