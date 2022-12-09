from lib2to3.pgen2.literals import simple_escapes
import os
import sys
import time
from types import SimpleNamespace

try:
    import private

except ImportError:
    private = None

try:
    from rich.pretty import pretty_repr

    pformat = pretty_repr

except ImportError:
    from pprint import pformat

from tensorfn import distributed as dist
from tensorfn.checker.backend import Local
from tensorfn.util import base36encode, base36decode


class Checker2:
    def __init__(self, storages=None, reporters=None):
        self.storages = SimpleNamespace()
        self.reporters = SimpleNamespace()

        if storages is not None:
            for storage in storages:
                setattr(self.storages, storage._keyname, storage)

        if reporters is not None:
            for reporter in reporters:
                setattr(self.reporters, reporter._keyname, reporter)

        ms = time.time_ns() // 1_000_000
        self.set_name(base36encode(ms))

    def set_name(self, name):
        for storage in self.storages.__dict__.values():
            storage.set_name(name)

    def catalog(self, conf):
        if not dist.is_primary():
            return

        if not isinstance(conf, dict):
            conf = conf.dict()

        conf = pformat(conf)

        argvs = " ".join([os.path.basename(sys.executable)] + sys.argv)

        template = f"""{argvs}

{conf}"""
        template = template.encode("utf-8")

        for storage in self.storages.__dict__.values():
            storage.save(template, "catalog.txt")

    def save(self, data, name):
        if dist.is_primary():
            for storage in self.storages.__dict__.values():
                storage.save(data, name)

    def checkpoint(self, obj, name):
        if dist.is_primary():
            for storage in self.storages.__dict__.values():
                storage.checkpoint(obj, name)

    def log(self, step=None, **kwargs):
        if dist.is_primary():
            for reporter in self.reporters.__dict__.values():
                reporter.log(step, **kwargs)
