import sys

from .containers import DatagenContainer
from .components.dataset import DatasetConfig
from datagen.dev import version as __version__, ModuleFunctionalityWrapper

datagen = DatagenContainer().datagen()

sys.modules[__name__] = ModuleFunctionalityWrapper(functionality=datagen)  # type: ignore
