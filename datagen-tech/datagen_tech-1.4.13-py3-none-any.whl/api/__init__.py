import sys

from datagen.dev import ModuleFunctionalityWrapper
from datagen.api.impl import DatagenAPI

from datagen.api import catalog

api = DatagenAPI()

sys.modules[__name__] = ModuleFunctionalityWrapper(functionality=api)  # type: ignore
