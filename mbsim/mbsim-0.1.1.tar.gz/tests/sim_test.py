import argparse

import pytest

from mbsim import sim

defaultargs = {
    "tcp": {"sim_address": "", "sim_port": 502},
    "udp": {"sim_address": "", "sim_port": 502},
    "rtu": {
        "path": "/dev/ttyS0",
        "sim_buad": 19200,
        "sim_byte": 8,
        "sim_stopbits": 1,
        "sim_parity": "N",
        "sim_timeout": 0,
        "sim_xonxoff": 0,
        "sim_rtscts": 0,
    },
}

altargs = {
    "tcp": {"sim_address": ["-a", "127.0.0.1"], "sim_port": ["-p", "5020"]},
    "udp": {"sim_address": ["--address", "127.0.0.1"], "sim_port": ["--port", "5020"]},
    "rtu": {
        "path": ["/dev/ttyS1"],
        "sim_buad": ["-b", "115200"],
        "sim_byte": ["--bytesize", "7"],
        "sim_stopbits": ["-s", "2"],
        "sim_parity": ["-p", "E"],
        "sim_timeout": ["-t", "3"],
        "sim_xonxoff": ["-x", "1"],
        "sim_rtscts": ["-r", "1"],
    },
}


class Test_getargs(object):
    """
    Test sim args parser
    """

    def test_getargsReturn(self):
        """
        test if returns
        """
        parser = argparse.ArgumentParser()
        mock = parser.add_subparsers(
            dest="cmd",
        )
        assert sim.getargs(mock.add_parser) is sim.run

    @pytest.mark.parametrize("proto", ["tcp", "udp", "rtu"])
    def test_defaultargs(self, proto):
        """
        Test default arguments for sim cmd
        """
        parser = argparse.ArgumentParser()
        mock = parser.add_subparsers(
            dest="cmd",
        )
        sim.getargs(mock.add_parser)
        args = parser.parse_args(["sim", proto])
        for key, val in defaultargs[proto].items():
            assert getattr(args, key) == val

    @pytest.mark.parametrize("proto,vals", [(key, val) for key, val in altargs.items()])
    def test_altargs(self, proto, vals):
        """
        This test adding alt values to argparse
        """
        parser = argparse.ArgumentParser()
        mock = parser.add_subparsers(
            dest="cmd",
        )
        sim.getargs(mock.add_parser)
        mockcmdargs = ["sim", proto]
        for val in vals.values():
            mockcmdargs += val
        args = parser.parse_args(mockcmdargs)
        for key, val in altargs[proto].items():
            test = getattr(args, key)
            if isinstance(test, int):
                assert test == int(val[-1])
            else:
                assert test == val[-1]


class Mockmb(object):
    """
    Mock mbsim-core moduel
    """

    def __init__(self):
        """
        init mock object
        """
        self._start = []

    def start(self, *args, **kwargs):
        """
        Start function
        """
        self._start.append((args, kwargs))


class Mockargs(object):
    """
    Mock args
    """

    def __init__(self, proto, **kwargs):
        """
        init mock object
        """
        self.sim_protocol = proto
        for key, val in kwargs.items():
            setattr(self, key, val)


class Test_run(object):
    """
    Test run function function
    """

    @pytest.mark.parametrize("proto", ["tcp", "udp", "rtu"])
    @pytest.mark.parametrize("vals", [defaultargs, altargs])
    def test_proto(self, proto, vals, monkeypatch):
        """
        Test the correct server is called
        """
        map = {
            "port": "path",
            "buadrate": "sim_buad",
            "bytesize": "sim_byte",
            "stopbits": "sim_stopbits",
            "parity": "sim_parity",
            "timeout": "sim_timeout",
            "xonxoff": "sim_xonxoff",
            "rtscts": "sim_rtscts",
        }
        test = Mockmb()
        args = Mockargs(proto, **vals[proto])
        monkeypatch.setattr(sim, "import_module", lambda x: test)
        sim.run(args)
        print(vals)
        assert len(test._start) == 1
        assert test._start[0][0][0] == proto
        print(test._start[0][1])
        for key, val in test._start[0][1].items():
            if key == "address":
                assert val == (vals[proto]["sim_address"], vals[proto]["sim_port"])
            else:
                assert val == vals[proto][map[key]]

    def test_unknownProto(self, monkeypatch):
        """
        Test if unknown protocol is used
        """
        with pytest.raises(RuntimeError, match="Did not find accepted protocol"):
            args = Mockargs("ohno", **defaultargs["rtu"])
            sim.run(args)
