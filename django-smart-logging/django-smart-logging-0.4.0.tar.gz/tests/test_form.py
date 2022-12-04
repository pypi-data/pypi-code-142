import pytest
from smart_logging.forms import LoggerConfigForm


@pytest.fixture()
def initial_data(manager):
    dummy_cfg = {
        "logger": "log1",
        "level": 10,
        "handlers": ["console"],
        "propagate": False,
    }
    return dummy_cfg


def test_form_no_changes(initial_data, rf):
    request = rf.post("/submit/", initial_data)
    frm = LoggerConfigForm(request.POST, initial=initial_data)
    frm.is_valid()
    frm.save()


@pytest.mark.parametrize(
    "field,value",
    [
        ("propagate", True),
        ("level", 20),
        ("handlers", ["console1"]),
    ],
)
def test_form(initial_data, field, value, manager, rf):
    post_data = dict(initial_data)
    post_data[field] = value
    request = rf.post("/submit/", post_data)
    frm = LoggerConfigForm(request.POST, initial=initial_data)
    frm.is_valid()
    frm.save()
    manager.refresh()
    assert manager.loggers[post_data["logger"]].propagate == post_data["propagate"]
