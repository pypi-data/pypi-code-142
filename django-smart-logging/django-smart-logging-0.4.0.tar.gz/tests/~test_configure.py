import logging
import logging.config

import pytest
from logging_dbconfig.processor import Processor


@pytest.fixture()
def processor():
    return Processor()


@pytest.fixture()
def logger():
    logger = logging.getLogger("test_logger")
    logger.handlers = [logging.StreamHandler()]
    logger.propagate = True
    logger.setLevel('NOTSET')
    return logger


def test_pacth_level(processor, logger, caplog):
    message = {"data": '{"action": "patch", "data": {"loggers": {"test_logger": {"level": "CRITICAL"}}}}'}
    caplog.set_level('NOTSET')
    logger.debug("DEBUG-1")
    logger.info("INFO-1")
    logger.warning("WARNING-1")
    logger.error("ERROR-1")
    logger.critical("CRITICAL-1")

    assert caplog.messages == ['DEBUG-1', 'INFO-1', 'WARNING-1', 'ERROR-1', 'CRITICAL-1']
    processor.process(message)
    # logger.setLevel('CRITICAL')
    assert logger.getEffectiveLevel() == logging.CRITICAL
    logger.info("INFO-2")
    logger.debug("DEBUG-2")
    logger.warning("WARNING-2")
    logger.error("ERROR-2")
    logger.critical("CRITICAL-2")
    assert 'CRITICAL-2' in caplog.messages
    assert 'ERROR-2' not in caplog.messages


def test_set_level(processor, logger, caplog):
    message = {"data": '{"action": "set", "data": {"loggers": {"test_logger": {"level": "CRITICAL"}}}}'}
    caplog.set_level('NOTSET')
    logger.debug("DEBUG-1")
    logger.info("INFO-1")
    logger.warning("WARNING-1")
    logger.error("ERROR-1")
    logger.critical("CRITICAL-1")

    assert caplog.messages == ['DEBUG-1', 'INFO-1', 'WARNING-1', 'ERROR-1', 'CRITICAL-1']
    processor.process(message)
    # logger.setLevel('CRITICAL')
    assert logger.getEffectiveLevel() == logging.CRITICAL
    logger.info("INFO-2")
    logger.debug("DEBUG-2")
    logger.warning("WARNING-2")
    logger.error("ERROR-2")
    logger.critical("CRITICAL-2")
    assert 'CRITICAL-2' in caplog.messages
    assert 'ERROR-2' not in caplog.messages

    config = processor.get_config({"action": "get", "data": {'target': 'test_logger'}})
    assert config == {'handlers': [], 'level': 'CRITICAL', 'propagate': True}


def test_wrong_config(processor):
    message = {"data": '{"action": "set", "data": "error"}'}
    processor.process(message)


def test_config_reset(processor):
    message = {"data": '{"action": "reset", "data": "error"}'}
    processor.process(message)


def test_wrong_action_config(processor):
    message = {"data": '{"action": "error", "data": "error"}'}
    processor.process(message)
