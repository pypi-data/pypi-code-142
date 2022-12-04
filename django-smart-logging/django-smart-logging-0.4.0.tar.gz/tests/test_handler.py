import logging

import pytest
from smart_logging.handlers import RedisLiveHandler


@pytest.fixture()
def handler():
    return RedisLiveHandler()


def test_emit(handler: RedisLiveHandler):
    message: logging.LogRecord = logging.LogRecord(
        "name",
        logging.ERROR,
        "pathname",
        lineno=10,
        msg="Test Message",
        args=None,
        exc_info=None,
    )
    handler.emit(message)


def test_retrieve(handler: RedisLiveHandler):
    handler.retrieve()
    handler.retrieve(True)


def test_clear(handler: RedisLiveHandler):
    handler.clear()
