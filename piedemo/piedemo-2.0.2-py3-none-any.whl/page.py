import os
import copy

from .fields.outputs.base import OutputField


class Page(object):
    def __init__(self):
        super(Page, self).__init__()

    def get_content(self, **kwargs):
        raise NotImplementedError()

    def process(self, **data) -> str:
        raise NotImplementedError()

    def fill(self, fields, data,
             inplace=False,
             generate=True,
             hook=lambda a, b: None):
        if not inplace:
            fields = copy.deepcopy(fields)
        name2field = {f.name: f for f in fields.children() if isinstance(f, OutputField)}
        for key in data.keys():
            if key in name2field:
                name2field[key].set_output(data[key])
        hook(fields, data)
        if generate:
            return fields.generate()
        return fields

    def parse(self, fields, data):
        key2field = {f.name: f for f in fields.children()}
        for k in list(data.keys()):
            if k not in key2field:
                del data[k]
                continue
            data[k] = key2field[k].parse(data[k])
        return data
