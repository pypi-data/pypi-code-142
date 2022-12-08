import sys

from datagen.dev import ModuleFunctionalityWrapper
from datagen.api import assets
from datagen.api.impl import DatagenAPI

print("❗❗❗'datagen.api.datapoint' module is deprecated, please use 'datagen.api' instead.")

api = DatagenAPI()

sys.modules[__name__] = ModuleFunctionalityWrapper(functionality=api)  # type: ignore
