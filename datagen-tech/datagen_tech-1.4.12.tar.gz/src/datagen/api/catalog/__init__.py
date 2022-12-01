import sys

from datagen.dev import ModuleFunctionalityWrapper
from datagen.api.catalog.containers import AssetsCatalogContainer

_catalog = AssetsCatalogContainer().catalog()

sys.modules[__name__] = ModuleFunctionalityWrapper(functionality=_catalog)  # type: ignore
