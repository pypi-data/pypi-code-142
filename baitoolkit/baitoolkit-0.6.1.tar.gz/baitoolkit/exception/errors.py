# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""

import re
import traceback

"""
Error Definition
"""


class BaseError(Exception):
    def __init__(self, **kwargs):
        self.__kwargs = kwargs

    @property
    def code(self):
        return error_code(self)

    @staticmethod
    def template():
        raise NotImplementedError("Error.template is not implemented by sub-class.")

    @property
    def message(self):
        message = self.template()

        if message is not None and (self.__kwargs is not None and len(self.__kwargs) > 0):
            for key, value in self.__kwargs.items():
                message = message.replace("{{%s}}" % key, str(value))
        return message

    @property
    def arguments(self):
        return self.__kwargs

    def get_argument(self, key):
        return self.arguments[key]

    @property
    def data(self):
        return self.arguments['data'] if self.arguments is not None and 'data' in self.arguments else None

    def __str__(self):
        return self.message

    @staticmethod
    def sub_classes():
        scs = []
        for sc in BaseError.__subclasses__():
            scs.append(sc)
        return scs


def error_code(error_class_or_inst):
    """Return code of exception."""
    e_code = error_class_or_inst.__class__.__name__ if isinstance(error_class_or_inst,
                                                                  BaseException) else error_class_or_inst.__name__
    e_code = re.sub('[A-Z]', lambda x: "_" + x.group(0), e_code)
    return e_code[1:].upper()


def get_error(code):
    for err in BaseError.sub_classes():
        if err.code == code:
            return err
    return None


class InternalError(BaseError):
    """
        Internal Error.
    """

    def __init__(self, message=None, data=None, **kwargs):
        super(InternalError, self).__init__(message=message, data=data, **kwargs)

    @staticmethod
    def template():
        return "{{message}}"


class ExternalError(BaseError):
    """
        External Error.
    """

    def __init__(self, message=None, data=None, **kwargs):
        super(ExternalError, self).__init__(message=message, data=data, **kwargs)

    @staticmethod
    def template():
        return "{{message}}"


class NoDoError(ExternalError):
    def __init__(self, action, what, data=None):
        super(NoDoError, self).__init__(action=action, what=what, data=data)

    @staticmethod
    def template():
        return "No support to {{action}} {{what}}."


class NoFoundError(ExternalError):
    def __init__(self, it, something, where=None, data=None):
        super(NoFoundError, self).__init__(it=str(it),
                                           something=str(something), where=str(where), data=data)

    @staticmethod
    def template():
        return "{{it}} {{something}} is not found in {{where}}."


class ReferredError(ExternalError):
    def __init__(self, it, referred, data=None):
        super(ReferredError, self).__init__(it=it, referred=referred, data=data)

    @staticmethod
    def template():
        return "{{it}} is referred by {{referred}}."


class InvalidError(ExternalError):
    def __init__(self, something, why=None, data=None):
        if why is not None:
            super(InvalidError, self).__init__(
                something=str(something), why=str(why), data=data)
        else:
            super(InvalidError, self).__init__(
                something=str(something), data=data)

    @staticmethod
    def template():
        return "{{something}} is not valid because {{why}}."


class RequiredError(ExternalError):
    def __init__(self, label, data=None):
        super(RequiredError, self).__init__(label=label, data=data)

    @staticmethod
    def template():
        return "{{label}} is required."


class ChoiceError(ExternalError):
    def __init__(self, label, choices, data=None):
        super(ChoiceError, self).__init__(label=label,
                                          choices=",".join(map(str, choices)), data=data)

    @staticmethod
    def template():
        return "{{label}}'s value `{{data}}` is not one of {{choices}}."


class LengthError(ExternalError):
    def __init__(self, label, minlength, maxlength, data=None):
        super(LengthError, self).__init__(label=label, minlength=minlength, maxlength=maxlength, data=data)

    @staticmethod
    def template():
        return "{{label}}'s length must between {{minlength}} and {{maxlength}}."


class RangeError(ExternalError):
    def __init__(self, label, mininum, maximum, data=None):
        super(RangeError, self).__init__(
            label=label, mininum=mininum, maximum=maximum, data=data)

    @staticmethod
    def template():
        return "{{label}}'s value `{{data}}` is out of {{mininum}} and {{maximum}}."


class CompareError(ExternalError):
    def __init__(self, label, operator, limitlabel, limit, data=None):
        super(CompareError, self).__init__(
            label=label, operator=operator, limit=limit, limitlabel=limitlabel,
            data=data)

    @staticmethod
    def template():
        return "{{label}}'s value `{{data}}` should be {{operator}} {{limitlabel}} {{limit}}."


class TypeInvalidError(ExternalError):
    def __init__(self, type_name, label, data=None):
        super(TypeInvalidError, self).__init__(type_name=type_name, label=label, data=data)

    @staticmethod
    def template():
        return "{{label}}'s type is not {{type_name}}."


class FormInvalidError(ExternalError):
    def __init__(self, it, data=None):
        super(FormInvalidError, self).__init__(it=it, data=data)

    @staticmethod
    def template():
        return "{{it}} Some field value is invalid."


class ExistingError(ExternalError):
    def __init__(self, it, data=None):
        super(ExistingError, self).__init__(it=it, data=data)

    @staticmethod
    def template():
        return "{{it}} has existed."


class RpcError(InternalError):
    def __init__(self, app_id, path, message, code=None, data=None):
        code = code if code is not None else RpcError.code()
        super(RpcError, self).__init__(app_id=app_id, path=path, message=message, code=code, data=data)

    @staticmethod
    def template():
        return "Failed to call {{app_id}}:{{path}} due to {{code}}-{{message}}."


class IllegalWordError(ExternalError):
    def __init__(self, label, illegal_word):
        super(IllegalWordError, self).__init__(label=label, illegal_word=illegal_word)

    @staticmethod
    def template():
        return "{{label}} includes the illegal word {{illegal_word}}"


class UniqueError(ExternalError):
    def __init__(self, label, value):
        super(UniqueError, self).__init__(label=label, value=value)

    @staticmethod
    def template():
        return "The value {{value}} of {{label}} has existed."


class CreationError(InternalError):
    def __init__(self, label):
        super(CreationError, self).__init__(label=label)

    @staticmethod
    def template():
        return "Failed to create record to {{label}}."


class UpdateError(InternalError):
    def __init__(self, label):
        super(UpdateError, self).__init__(label=label)

    @staticmethod
    def template():
        return "Failed to update record to {{label}}."


class DeleteError(InternalError):
    def __init__(self, label):
        super(DeleteError, self).__init__(label=label)

    @staticmethod
    def template():
        return "Failed to delete record to {{label}}."


def format_exc_info(exc_info):
    error_class = exc_info[1]
    tb_message = format_traceback(exc_info[2])
    return "%s\n%s" % (str(error_class), tb_message)


def format_traceback(traceback1=None):
    if traceback1 is not None:
        return "".join(traceback.format_tb(traceback1))
    return traceback.format_exc()
