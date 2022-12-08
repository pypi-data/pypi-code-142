from dependency_injector import containers

from datagen.dev import PluginsFactory
from datagen.utilities.camera import CameraUtils


class UtilsContainer(containers.DeclarativeContainer):
    camera = PluginsFactory(CameraUtils)
