from django.conf import settings
from django.core.signals import setting_changed
from django.dispatch import receiver

HANDLERS_NONE = 0
HANDLERS_VIEW = 1
HANDLERS_CHANGE = 2

SMART_LOG_INSPECT = getattr(settings, "SMART_LOG_INSPECT", False)
SMART_LOG_HANDLERS = getattr(settings, "SMART_LOG_HANDLERS", HANDLERS_NONE)
SMART_LOG_MAXSIZE = getattr(settings, "SMART_LOG_MAXSIZE", 100)
SMART_LOG_FORMAT = "%(levelname)s %(asctime)s %(module)s: %(message)s"
SMART_LOG_PREFIX = getattr(settings, "SMART_LOG_PREFIX", "smart-log") or "smart-log"
SMART_LOG_REDIS = getattr(settings, "SMART_LOG_REDIS", "redis://0.0.0.0/0")
SMART_LOG_DEBUG = getattr(settings, "SMART_LOG_DEBUG", False)
SMART_LOG_LOGGERS = getattr(settings, "SMART_LOG_LOGGERS", None)
SMART_LOG_IGNORE_INSPECT = getattr(settings, "SMART_LOG_IGNORE_INSPECT", None)

EVENTS = "%s:%s" % (SMART_LOG_PREFIX, "events")
REGISTRY = "%s:%s" % (SMART_LOG_PREFIX, "registry")
LOGGER = "%s:%s" % (SMART_LOG_PREFIX, "logs")
ONLINE_LOGGER_NAME = "__online__"
COLUMN_HANDLERS = bool(SMART_LOG_HANDLERS) or SMART_LOG_INSPECT


@receiver(setting_changed)
def update_settings(setting, value, **kwargs):
    if setting.startswith("SMART_LOG"):
        globals()[setting] = value
