# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
from baitoolkit.param.param_validator import RequiredValidator, TypeValidator, ChoiceValidator, RangeValidator
from baitoolkit.common import type_util
from baitoolkit.common.type_util import ValueObj
from baitoolkit.exception.errors import ExistingError, InvalidError, RequiredError

"""Similar to argparse"""


class ParamDeclare(object):
    """Parameter Declare Object"""

    def __init__(self, name: str, default=None, name_to=None, required: bool = False, type_=None, range_: tuple = None,
                 choices: tuple = None, validators=None):
        self._name = name
        self._default = default
        self._name_to = name_to
        self._validators = list()
        self._required = required
        if required:
            self._validators.append(RequiredValidator())
        if type_ is not None:
            self._validators.append(TypeValidator(type_))
        if range_ is not None:
            self._validators.append(RangeValidator(range_[0], range_[1]))
        if choices is not None:
            self._validators.append(ChoiceValidator(choices=choices))
        if validators:
            self._validators.extend(validators)

    @property
    def name_to(self):
        return self._name_to if self._name_to is not None else self._name

    def check_value(self, value, label=None):
        if self._required and value is None and self._default is not None:
            return self._default
        for validator in self._validators:
            value = validator.validate(value, self._name if label is None else label)
        return value


class ParameterParser(object):
    """Similar  to argparser.ArgumentParser"""

    def __init__(self, ignore_unknown=False):
        """
        @param bool ignore_unknown: if True, raise Exception when unknown arguments is found during parsing."""
        self._arg_decs: [str, ParamDeclare] = dict()
        self._ignore_unknown = ignore_unknown

    def add_parameter(self, name: str, default=None, name_to=None, required: bool = False, type_=str,
                      range_: tuple = None,
                      choices: tuple = None, validators=None) -> bool:
        if name in self._arg_decs:
            raise ExistingError(f'{name}')
        self._arg_decs[name] = ParamDeclare(name, default=default, name_to=name_to,
                                            required=required, type_=type_, range_=range_, choices=choices,
                                            validators=validators)

    def parse_parameters(self, **kwargs) -> ValueObj:
        """parse parameters"""
        parsed_args = ValueObj()
        if not self._ignore_unknown:
            unknown_keys = set(kwargs.keys()) - set(self._arg_decs.keys())
            if unknown_keys:
                raise InvalidError(f'{unknown_keys}')
        for name, arg_dec in self._arg_decs.items():
            if '.' in name:
                names = name.split('.')
                parent_names = names[0:-1]
                inside_name = names[-1]
                tmp = kwargs
                for tmp_name in parent_names:
                    tmp = kwargs[tmp_name]
                inside_value = arg_dec.check_value(tmp[inside_name])
                tmp[arg_dec.name_to] = inside_value
                del tmp[inside_name]
            else:
                value = arg_dec.check_value(kwargs.get(name))
                parsed_args[arg_dec.name_to] = value
        return parsed_args

    def parse_json_str(self, json_str) -> ValueObj:
        """parse json str"""
        kwargs = type_util.json_to_object(json_str)
        return self.parse_parameters(**kwargs)
