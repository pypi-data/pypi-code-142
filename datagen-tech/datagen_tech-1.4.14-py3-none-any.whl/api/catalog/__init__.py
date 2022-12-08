import sys

from datagen.dev import ModuleFunctionalityWrapper
from datagen.api.catalog.containers import AssetsCatalogContainer

catalog = AssetsCatalogContainer().catalog()

sys.modules[__name__] = ModuleFunctionalityWrapper(functionality=catalog)  # type: ignore
