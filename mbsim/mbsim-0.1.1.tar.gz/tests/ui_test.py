import argparse

import pytest

from mbsim import ui
from mbsim.mbsim import EntryPoints


class MockUI(object):
    """
    Mock an ui entrypoint
    """

    def __init__(self, name):
        """
        init ui
        """
        self.name = name


class Test_getargs(object):
    """
    Test getargs function
    """

    def test_noep(self, monkeypatch):
        """
        Test no entry points for ui
        """
        monkeypatch.setattr(ui, "_eps", EntryPoints({}))
        assert ui.getargs(123) is None

    @pytest.mark.parametrize(
        "arg",
        [
            "a",
            "b",
            "c",
        ],
    )
    def test_args(self, arg, monkeypatch):
        """
        Test if args are as expected
        """
        monkeypatch.setattr(ui, "_eps", EntryPoints({"mbsim_ui": [MockUI("a"), MockUI("b"), MockUI("c")]}))
        parser = argparse.ArgumentParser()
        mock = parser.add_subparsers(
            dest="cmd",
        )
        assert ui.getargs(mock.add_parser) is ui.run
        args = parser.parse_args(["ui", arg])
        assert hasattr(args, "UI")
        assert getattr(args, "UI") == arg


class Mockeps(object):
    """
    Mock eps function
    """

    def __init__(self):
        """
        init mock object
        """
        self.call = False
        self._load = False
        self.sel = []

    def __call__(self):
        """
        Mock call
        """
        if self.call:
            raise RuntimeError("All ready called")
        self.call = True

    def load(self):
        """
        Mock call
        """
        if self._load:
            raise RuntimeError("All ready loaded")
        self._load = True
        return self

    def select(self, *args, **kwargs):
        """
        Mock select function
        """
        self.sel.append((args, kwargs))
        return self


class Mockargs(object):
    """
    Mock args
    """

    def __init__(self, **kwargs):
        """
        Init args
        """
        for key, val in kwargs.items():
            setattr(self, key, val)


class Test_run(object):
    """
    Test run function
    """

    def test_run(self, monkeypatch):
        """
        Test run function
        """
        eps = Mockeps()
        monkeypatch.setattr(ui, "_eps", eps)
        ui.run(Mockargs(UI="web"))
        assert eps.call
        assert eps._load
        assert eps.sel == [((), {"name": "web"})]
