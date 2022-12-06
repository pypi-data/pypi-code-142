import json
import os
import re

import numpy as np
from _ctypes import PyObj_FromPtr  # see https://stackoverflow.com/a/15012814/355230
from tabulate import tabulate

# class NoIndent(object):
# 	""" Value wrapper. """
# 	def __init__(self, value):
# 		if not isinstance(value, (list, tuple)):
# 			raise TypeError('Only lists and tuples can be wrapped')
# 		self.value = value


class MyEncoder(json.JSONEncoder):
    FORMAT_SPEC = "@@{}@@"  # Unique string pattern of NoIndent object ids.
    regex = re.compile(FORMAT_SPEC.format(r"(\d+)"))  # compile(r'@@(\d+)@@')

    def __init__(self, **kwargs):
        # Keyword arguments to ignore when encoding NoIndent wrapped values.
        ignore = {"cls", "indent"}

        # Save copy of any keyword argument values needed for use here.
        self._kwargs = {k: v for k, v in kwargs.items() if k not in ignore}
        super().__init__(**kwargs)

    def default(self, obj):
        # return (self.FORMAT_SPEC.format(id(obj)) if isinstance(obj, NoIndent)
        return (
            self.FORMAT_SPEC.format(id(obj))
            if isinstance(obj, list)
            else super().default(obj)
        )

    def iterencode(self, obj, **kwargs):
        format_spec = self.FORMAT_SPEC  # Local var to expedite access.

        # Replace any marked-up NoIndent wrapped values in the JSON repr
        # with the json.dumps() of the corresponding wrapped Python object.
        for encoded in super().iterencode(obj, **kwargs):
            match = self.regex.search(encoded)
            if match:
                id = int(match.group(1))
                no_indent = PyObj_FromPtr(id)
                json_repr = json.dumps(no_indent.value, **self._kwargs)
                # Replace the matched id string with json formatted representation
                # of the corresponding Python object.
                encoded = encoded.replace(f'"{format_spec.format(id)}"', json_repr)

            yield encoded


def load_json(path):
    with open(path) as serialized:
        _dict = json.load(serialized)
    df = qcDataFrame(_dict=_dict)
    return df


class qcDataFrame:
    """
    The QC data frame which stores meta data and task data.
    """

    def __init__(self, columns=None, units=None, x=None, _dict=None):
        self._identifiers = {}
        self._meta_data = {}
        self._data = {}
        if _dict:
            self.from_dict(_dict)
            return

        columns = columns or []

        for i, column in enumerate(columns):
            self._data[column] = {
                "X": x[i] if x else False,
                "Unit": units[i] if units else None,
                "Values": [],
            }

    def add_meta_data(self, key, value):
        self._meta_data[key] = value

    def add_identifier(self, key, value):
        self._identifiers[key] = value

    def add_data(self, data):
        for key, value in data.items():
            self._data[key]["Values"] += list(value)

    def add_column(self, column, unit=False, x=False, data=None):
        data = data or []
        if column in self._data:
            print(f"Warning: column {column} already exists! Will overwrite.")
        self._data[column] = {"X": x, "Unit": unit, "Values": list(data)}

    def __getitem__(self, column):
        return np.array(self._data[column]["Values"])

    def set_unit(self, column, unit):
        self._data[column]["Unit"] = unit

    def get_unit(self, column):
        return self._data[column]["Unit"]

    def set_x(self, column, x):
        self._data[column]["X"] = x

    def get_x(self, column):
        return self._data[column]["X"]

    def __len__(self):
        return max(len(value["Values"]) for value in self._data.values())

    def sort_values(self, by, reverse=False):
        for key, value in self._data.items():
            if key == by:
                continue
            value["Values"] = list(
                next(
                    zip(
                        *sorted(
                            zip(value["Values"], self._data[by]["Values"]),
                            key=lambda x: x[1],
                            reverse=reverse,
                        )
                    )
                )
            )
        self._data[by]["Values"].sort(reverse=reverse)

    def __str__(self):
        text = "Identifiers:\n"
        text += str(json.dumps(self._identifiers, cls=MyEncoder, indent=4))
        text += "\n"
        # text += "Meta data:\n"
        # text += str(json.dumps(self._meta_data, cls=MyEncoder, indent=4))
        # text += "\n"
        table = []
        for key, value in self._data.items():
            table.append(
                [key + (f" [{value['Unit']}]" if value["Unit"] else "")]
                + value["Values"]
            )
        text += tabulate(table, floatfmt=".3f")
        return text

    def to_dict(self):
        _dict = {
            "Identifiers": self._identifiers,
            "Measurements": self._data,
            "Metadata": self._meta_data,
        }
        return _dict

    def from_dict(self, _dict):
        self._identifiers = _dict["Identifiers"]
        self._meta_data = _dict["Metadata"]
        self._data = _dict["Measurements"]

    def to_json(self):
        _dict = self.to_dict()
        return json.dumps(_dict, cls=MyEncoder, indent=4)

    def save_json(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        _dict = self.to_dict()
        with open(path, "w") as fp:
            json.dump(_dict, fp, cls=MyEncoder, indent=4)
