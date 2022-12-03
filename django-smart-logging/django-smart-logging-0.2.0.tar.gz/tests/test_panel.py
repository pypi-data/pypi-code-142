from unittest import mock

import pytest
import smart_logging.signals
from django.urls import reverse


@pytest.mark.django_db
def test_panel_no_online(app, settings, monkeypatch):
    monkeypatch.setattr("smart_logging.forms.conf.SMART_LOG_ONLINE", False)
    url = reverse("admin:smart_logging_panel")
    assert app.get(url)


@pytest.mark.django_db
def test_panel(app):
    url = reverse("admin:smart_logging_panel")
    res = app.get(url)
    res.forms["loggingConfig"]["form-2-level"] = "20"
    res.forms["loggingConfig"]["form-1-level"] = "20"
    res.forms["loggingConfig"]["form-2-propagate"] = True
    res.forms["loggingConfig"]["form-1-propagate"] = True
    res = res.forms["loggingConfig"].submit("config").follow()
    assert b"Configuration saved" in res.content


@pytest.mark.django_db
def test_panel_errors(app):
    from django.urls import reverse

    url = reverse("admin:smart_logging_panel")
    res = app.get(url)
    res.forms["loggingConfig"]["form-1-level"].force_value("-1")
    res = res.forms["loggingConfig"].submit("config")
    assert b"Fix errors below" in res.content


@pytest.mark.django_db
def test_panel_no_changes(app):
    from django.urls import reverse

    url = reverse("admin:smart_logging_panel")
    res = app.get(url)
    res = res.forms["loggingConfig"].submit("config").follow()
    assert b"No changes detected" in res.content


@pytest.mark.django_db
def test_panel_signal_called(app):
    url = reverse("admin:smart_logging_panel")
    res = app.get(url)
    res.forms["loggingConfig"]["form-0-level"] = "50"
    res.forms["loggingConfig"]["form-1-level"] = "50"
    with mock.patch.object(smart_logging.signals.logger_changed, "send") as m:
        res = res.forms["loggingConfig"].submit("config").follow()
        assert b"Configuration saved" in res.content
        assert m.called


@pytest.mark.django_db
def test_panel_online(app):
    url = reverse("admin:smart_logging_panel")
    assert app.get(f"{url}?page=online")


@pytest.mark.django_db
def test_panel_logs(app):
    url = reverse("admin:smart_logging_panel")
    assert app.get(f"{url}?page=logs")


@pytest.mark.django_db
def test_panel_debug(app):
    url = reverse("admin:smart_logging_panel")
    assert app.get(f"{url}?page=debug")


@pytest.mark.django_db
def test_panel_clear(app):
    url = reverse("admin:smart_logging_panel")
    assert app.get(f"{url}?page=clear")
