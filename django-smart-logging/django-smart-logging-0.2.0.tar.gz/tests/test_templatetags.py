from datetime import date

from smart_logging.templatetags.smart_logging import pretty_json, render


def test_pretty_json():
    assert pretty_json({"date": date.today()})


def test_render():
    assert render({"a": {}}, "a")
