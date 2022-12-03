import os
import sys
from pathlib import Path

import pytest as pytest
from django.conf import settings
from django.urls import reverse

test_dir = Path(__file__).parent


def pytest_configure(config):
    sys.path.insert(0, str((test_dir / "../src").absolute()))
    sys.path.insert(0, str((test_dir / "demo").absolute()))
    os.environ["DJANGO_SETTINGS_MODULE"] = "demo.settings"


@pytest.fixture()
def app(db, django_app):
    res = django_app.get(reverse("admin:login"))
    res.form["username"] = "sax"
    res.form["password"] = "123"
    res.form.submit()
    return django_app


@pytest.fixture()
def manager():
    import logging.config

    from smart_logging.manager import manager

    logging.config.dictConfig(settings.LOGGING)
    manager.set_config(settings.LOGGING)
    manager.init()
    manager.online_handler.clear()
    return manager
