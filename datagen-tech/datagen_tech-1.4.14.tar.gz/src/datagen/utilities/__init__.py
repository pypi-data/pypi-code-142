__all__ = ["camera"]

from datagen.utilities.camera import CameraUtils
from datagen.utilities.container import UtilsContainer


utils_container = UtilsContainer()

camera: CameraUtils = utils_container.camera()
