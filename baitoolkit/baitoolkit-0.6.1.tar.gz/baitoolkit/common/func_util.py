# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import base64
import functools
import hashlib
import inspect

import six

from baitoolkit. import exception
from baitoolkit.exception.errors import InternalError

"""
    Function Utility.
"""


def wrap_func(func, *args, **kwargs):
    wrapper = functools.partial(func, *args, **kwargs)
    try:
        functools.update_wrapper(wrapper, func)
    except AttributeError:
        # func already wrapped by functools.partial won't have
        # __name__, __module__ or __doc__ and the update_wrapper()
        # call will fail.
        pass
    return wrapper


def import_string(obj_path: str):
    """
        import module from string
        :param obj_path:str: the string of absolute path a module,
        eg: utility.error.TypeGeneratorError or utility.error.TypeGeneratorError:method_abc
    """

    def import_(mod_path):
        try:
            if "." in mod_path:
                pkg_path, hcls = mod_path.rsplit('.', 1)
                mod = __import__(pkg_path, None, None, [''])
                mod = getattr(mod, hcls)
            else:
                mod = __import__(mod_path, None, None, [''])
        except BaseException:
            raise InternalError('could not import module due to error resolving %s: ' % mod_path)
        return mod

    if ':' not in obj_path:
        return import_(obj_path)

    module_name, rest = obj_path.split(':', 1)
    obj = import_(module_name)
    try:
        for name in rest.split('.'):
            obj = getattr(obj, name)
        return obj
    except BaseException:
        raise InternalError('could not import module due to error resolving %s: ' % obj_path)


def get_function_path(func, bound_to=None):
    """
        Get received func path (as string), to import func later with `import_string`.
    """
    if isinstance(func, six.string_types):
        return func

    # static and class methods
    if hasattr(func, '__func__'):
        real_func = func.__func__
    elif callable(func):
        real_func = func
    else:
        return func

    func_path = []

    module = getattr(real_func, '__module__', '__main__')
    if module:
        func_path.append(module)

    if not bound_to:
        try:
            bound_to = six.get_method_self(func)
        except AttributeError:
            pass

    if bound_to:
        if isinstance(bound_to, six.class_types):
            func_path.append(bound_to.__name__)
        else:
            func_path.append(bound_to.__class__.__name__)

    func_path.append(real_func.__name__)
    return '.'.join(func_path)


def get_function_args(func):
    """
        Return FullArgSpec(args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations)
    """
    return inspect.getfullargspec(func)


def eval_script(script, **kwargs):
    """
        Execute a python script.
    """
    if script == '':
        return True
    if type(script) != str:
        return script(**kwargs)
    else:
        return eval(script, kwargs)


def get_function(obj, name):
    """Get function of object
    :param object obj: one instance of class
    :param str name: the function name to be get
    :return function: None if no found.
    """
    if hasattr(obj, name):
        return getattr(obj, name)
    else:
        raise exception.NoFoundError('function', name, str(obj))


def sign_function(f, *args, **kwargs):
    """Calculate a hash value of a function and its arguments."""

    def inspect_args():
        new_args = []
        arg_num = 0
        argspec = inspect.getfullargspec(f)

        args_len = len(argspec.args)
        for i in range(args_len):
            if i == 0 and argspec.args[i] in ('self', 'cls'):
                arg = repr(args[0])
                arg_num += 1
            elif argspec.args[i] in kwargs:
                arg = '%s:%s' % (argspec.args[i], kwargs[argspec.args[i]])
            elif arg_num < len(args):
                arg = args[arg_num]
                arg_num += 1
            elif abs(i - args_len) <= len(argspec.defaults):
                arg = argspec.defaults[i - args_len]
                arg_num += 1
            else:
                arg = None
                arg_num += 1
            new_args.append(arg)
        return new_args

    fullargs = inspect_args()
    updated = "{0}".format(fullargs)

    signature = hashlib.md5()
    signature.update(updated.encode('utf-8'))
    signature = base64.b64encode(signature.digest())[:16]
    signature = signature.decode('utf-8')
    f_sig = '%s.%s' % (f.__module__, f.__name__)
    signature = '%s:%s' % (f_sig, signature)
    return signature
