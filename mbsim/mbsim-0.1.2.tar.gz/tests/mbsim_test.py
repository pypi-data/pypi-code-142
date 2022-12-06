import logging
from argparse import Namespace

import pytest

from mbsim import mbsim


class MockEPs(object):
    """
    Mock object to mock entry points
    """

    def __init__(self, name):
        """
        init mock entry points object
        """
        self.name = name
        self._call = []
        self._select = []

    def __call__(self, *args, **kwargs):
        self._call.append((args, kwargs))
        return self

    def select(self, *args, **kwargs):
        self._select.append((args, kwargs))
        return (self,)

    def load(self):
        return self._load

    def _load(self, parser):
        args = parser(
            name="{}".format(self.name),
        )
        args.add_argument("a")
        return self


def test_main(monkeypatch):
    """
    Test the main function in mbsim
    """
    test = MockEPs("mock")
    monkeypatch.setattr(mbsim, "entry_points", test)
    mbsim.main(["mock", "hello"])
    assert test._call[0] == ((), {})
    assert test._select[0] == ((), {"group": "mbsim_command"})
    testns = test._call[1][0][0]
    assert isinstance(testns, Namespace)
    assert testns.cmd == "mock"
    assert testns.a == "hello"


@pytest.mark.parametrize("arg", ["-h", "--help"])
def test_help(arg):
    """
    Test if help is called with -h and --help
    """
    with pytest.raises(SystemExit):
        mbsim.main([arg])


@pytest.mark.parametrize("opt", ["-l", "--log"])
@pytest.mark.parametrize("log", ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"])
def test_setlog(opt, log, monkeypatch):
    """
    Test if set logging correctly
    """
    test = MockEPs("mock")
    monkeypatch.setattr(mbsim, "entry_points", test)
    mbsim.main([opt, log, "mock", "hello"])
    assert mbsim.log.isEnabledFor(getattr(logging, log))
