import logging

import pytest as pytest
from django.conf import settings
from smart_logging.processor import Processor


@pytest.fixture()
def processor():
    return Processor()


def test_set_config(processor):
    assert processor.get_config({"action": "set", "data": settings.LOGGING}) == settings.LOGGING


def test_update_config(processor):
    updates = {"loggers": {"live_logging": {"level": "CRITICAL"}}}
    new_config = processor.get_config({"action": "patch", "data": updates})
    assert new_config['loggers']['live_logging']['level'] == 'CRITICAL'


def test_get_config(processor):
    config = processor.get_config({"action": "get", "data": {'target': 'live_logging'}})
    assert config == {'handlers': [], 'level': 'DEBUG', 'propagate': True}


def test_wrong_config(processor):
    config = processor.get_config({"action": "get", "data": {'target': 'live_logging'}})
    assert config == {'handlers': [], 'level': 'DEBUG', 'propagate': True}


def test_config_reset(processor):
    config = processor.get_config({"action": "reset", "data": {}})
    assert config == settings.LOGGING


def test_wrong_action_config(processor, caplog):
    # from live_logging.processor import logger
    # logger.setLevel(logging.INFO)
    caplog.set_level(logging.ERROR)
    # logger.propagate = True
    with caplog.at_level(logging.ERROR):
        config = processor.get_config({"action": "errored", "data": {'target': 'live_logging'}})
    assert config is None
    assert caplog.messages == ['Invalid action']
