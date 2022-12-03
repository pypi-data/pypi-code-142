# import logging
#
from json import JSONDecodeError

import pytest as pytest

# from django.conf import settings
from smart_logging.processor import Processor


#
#
@pytest.fixture()
def processor():
    return Processor()


def test_process(processor):
    msg = {"data": '{"config": {"logger": "root"}, "__sender__": "10"}'}
    assert processor.process(msg)


def test_wrong_logger(processor):
    msg = {"data": '{"config": {"logger": "---"}, "__sender__": "10"}'}
    assert processor.process(msg)


def test_errror(processor):
    msg = {"data": '{"config": {"logger: "---"}, "__sender__": "10"}'}
    with pytest.raises(JSONDecodeError):
        assert processor.process(msg)


#
# def test_update_config(processor):
#     updates = {"loggers": {"live_logging": {"level": "CRITICAL"}}}
#     new_config = processor.get_config({"action": "patch", "data": updates})
#     assert new_config['loggers']['live_logging']['level'] == 'CRITICAL'
#
#
# def test_get_config(processor):
#     config = processor.get_config({"action": "get", "data": {'target': 'live_logging'}})
#     assert config == {'handlers': [], 'level': 'DEBUG', 'propagate': True}
#
#
# def test_wrong_config(processor):
#     config = processor.get_config({"action": "get", "data": {'target': 'live_logging'}})
#     assert config == {'handlers': [], 'level': 'DEBUG', 'propagate': True}
#
#
# def test_config_reset(processor):
#     config = processor.get_config({"action": "reset", "data": {}})
#     assert config == settings.LOGGING
#
#
# def test_wrong_action_config(processor, caplog):
#     # from live_logging.processor import logger
#     # logger.setLevel(logging.INFO)
#     caplog.set_level(logging.ERROR)
#     # logger.propagate = True
#     with caplog.at_level(logging.ERROR):
#         config = processor.get_config({"action": "errored", "data": {'target': 'live_logging'}})
#     assert config is None
#     assert caplog.messages == ['Invalid action']
