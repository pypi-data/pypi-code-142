import sys

from datagen.dev import ModuleFunctionalityWrapper
from datagen.api.impl import DatagenAPI
from datagen.api import catalog

from datagen.utilities import camera as camera_utils  # type: ignore

api = DatagenAPI()

sys.modules[__name__] = ModuleFunctionalityWrapper(functionality=api)  # type: ignore
