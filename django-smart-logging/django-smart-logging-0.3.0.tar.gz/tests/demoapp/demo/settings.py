import os
import uuid
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parents[3]

ALLOWED_HOSTS = ["*"]
SECRET_KEY = "aaaaaaa"
DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "smart_logging.sqlite",
        "TEST": {
            "NAME": ":memory:",
        },
        "TEST_NAME": ":memory:",
        "HOST": "",
        "PORT": "",
        "ATOMIC_REQUESTS": True,
    }
}
AUTHENTICATION_BACKENDS = ("demo.backends.AnyUserAuthBackend",)
MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    # 'django.contrib.sites',
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_sysinfo",
    "adminactions",
    "adminfilters",
    "adminfilters.depot",
    "admin_extra_buttons",
    "smart_admin.apps.SmartLogsConfig",
    "smart_admin.apps.SmartTemplateConfig",
    "smart_admin.apps.SmartAuthConfig",
    "smart_admin.apps.SmartConfig",
    "smart_logging",
    "demo",
]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR / "tests" / "demoapp" / "demo" / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.messages.context_processors.messages",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
            ]
        },
    },
]

STATIC_URL = "/static/"
ROOT_URLCONF = "demo.urls"
SMART_LOG_INSPECT = True
SMART_LOG_PREFIX = uuid.uuid4()
SMART_LOG_CHANNEL = "demo_smart_log"
SMART_LOG_DEBUG = True
SMART_LOG_HANDLERS = 2
SMART_LOG_REDIS = os.environ.get("SMART_LOG_REDIS", "??")
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {"format": " %(levelname)s %(asctime)s %(module)s: %(message)s"},
        "simple1": {
            "format": "simple1 %(levelname)s %(asctime)s %(module)s: %(message)s"
        },
        "simple2": {
            "format": "simple2 %(levelname)s %(asctime)s %(module)s: %(message)s"
        },
    },
    "handlers": {
        "null": {"class": "logging.NullHandler"},
        "console": {"class": "logging.StreamHandler", "formatter": "verbose"},
        "console1": {
            "class": "logging.StreamHandler",
            "formatter": "simple1",
            "level": "ERROR",
        },
        "console2": {"class": "logging.StreamHandler", "formatter": "simple2"},
    },
    "loggers": {
        "log_null": {
            "handlers": ["null", "console"],
            "level": "ERROR",
            "propagate": True,
        },
        "log1": {
            "handlers": ["console1"],
            "level": "DEBUG",
            "propagate": False,
        },
        "log2": {
            "handlers": ["console2"],
            "level": "DEBUG",
            "propagate": True,
        },
        "log3": {
            "handlers": [],
            "level": "DEBUG",
            "propagate": True,
        },
    },
    "root": {
        "handlers": ["console"],
        # 'level': 0,
        "propagate": False,
    },
}
