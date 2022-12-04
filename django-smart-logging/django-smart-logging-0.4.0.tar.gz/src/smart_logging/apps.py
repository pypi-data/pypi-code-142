from django.apps import AppConfig
from django.conf import settings


class Config(AppConfig):
    name = "smart_logging"

    def ready(self):
        from .manager import manager

        manager.set_config(settings.LOGGING)
        manager.init()
