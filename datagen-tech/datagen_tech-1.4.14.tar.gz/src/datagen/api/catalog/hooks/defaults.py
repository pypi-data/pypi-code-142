from datagen.api import assets
from datagen.api.assets import Human
from datagen.api.catalog.impl import PreProvisionHook
from datagen.dev import load_resource


class HumansDefaultsHook(PreProvisionHook[Human]):
    def __init__(self):
        self._asset_id_to_asset_defaults = load_resource("..", "cache", "humans", "defaults.json")

    def __call__(self, asset_id: str) -> dict:
        from datagen.api import catalog

        defaults = self._asset_id_to_asset_defaults[asset_id]
        default_eyes = catalog.eyes.parse(**defaults["eyes"])
        default_eyebrows = catalog.eyebrows.parse(**defaults["eyebrows"])
        default_hair = catalog.hair.parse(**defaults["hair"])
        return {"head": assets.Head(eyes=default_eyes, eyebrows=default_eyebrows, hair=default_hair)}
