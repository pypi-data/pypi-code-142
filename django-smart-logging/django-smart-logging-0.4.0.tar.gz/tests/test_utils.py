import logging
from unittest import mock
from unittest.mock import Mock

import pytest
from smart_logging.utils import fqn, get_ip


def test_fqn():
    assert fqn(logging.Handler) == "logging.Handler"
    assert fqn(logging.Handler()) == "logging.Handler"
    assert fqn("logging.Handler") == "logging.Handler"
    assert fqn(logging.getLevelName) == "logging.getLevelName"
    with pytest.raises(ValueError):
        assert fqn(2) == "logging.getLevelName"
    assert fqn(2, silent=True) is None


def test_get_ip():
    assert get_ip()
    get_ip.cache_clear()

    with mock.patch("socket.socket") as m:
        m.return_value.getsockname.side_effect = Mock(side_effect=Exception())
        assert get_ip() == "127.0.0.1"
