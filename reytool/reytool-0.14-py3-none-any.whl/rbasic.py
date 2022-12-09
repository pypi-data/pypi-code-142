# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
══════════════════════════════
@Time    : 2022/12/05 14:09:42
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Rey"s basic methods
══════════════════════════════
'''


from varname import nameof


def check_parm(value: "object", *args: "object | type", print_var_name: "bool"=True) -> "None":
    """
    Check the content or type of the value.
    """

    if type(value) in args:
        return
    args_id = [id(element) for element in args]
    if id(value) in args_id:
        return
    if print_var_name:
        try:
            var_name = nameof(value, frame=2)
            var_name = " '%s'" % var_name
        except:
            var_name = ""
    else:
        var_name = ""
    include_str = ", ".join([repr(element) for element in args])
    error_text = "parameter%s the value content or type must in [%s], now: %s" % (var_name, include_str, repr(value))
    error = ValueError(error_text)
    raise error
    
def check_parm_least_one(*args: "object") -> "None":
    """
    Check that at least one of multiple values is not None.

    Parameters
    ----------
    *args : object
        Check values.
    """

    for value in args:
        if value != None:
            return
    try:
        vars_name = nameof(*args, frame=2)
    except:
        vars_name = None
    if vars_name:
        vars_name_str = " " + " and ".join(["\"%s\"" % var_name for var_name in vars_name])
    else:
        vars_name_str = ""
    error_text = "at least one of parameters%s is not None" % vars_name_str
    error = ValueError(error_text)
    raise error

def check_parm_only_one(*args: "object") -> "None":
    """
    Check that at most one of multiple values is not None.

    Parameters
    ----------
    *args : object
        Check values.
    """

    none_count = 0
    for value in args:
        if value != None:
            none_count += 1
    if none_count > 1:
        try:
            vars_name = nameof(*args, frame=2)
        except:
            vars_name = None
        if vars_name:
            vars_name_str = " " + " and ".join(["\"%s\"" % var_name for var_name in vars_name])
        else:
            vars_name_str = ""
        error_text = "at most one of parameters%s is not None" % vars_name_str
        error = ValueError(error_text)
        raise error

def if_iterable(obj: "object", exclude_type: "list"=[str, bytes]) -> "bool":
    """
    Judge if iterable.
    """

    check_parm(exclude_type, list)

    obj_type = type(obj)
    if obj_type in exclude_type:
        return False
    try:
        obj_dir = obj.__dir__()
    except TypeError:
        return False
    if "__iter__" in obj_dir:
        return True
    else:
        return False

def get_first_notnull(*args: "object", default: "object"=None, exclude: "list"=[]) -> object:
    """
    Get first notnull element.
    """

    check_parm(exclude, list)
    
    for element in args:
        if element not in [None, *exclude]:
            return element
    return default

def error(throw: "object"=True, info: "object"=None, error_type: "BaseException"= AssertionError) -> "object":
    """
    Throw error or return information.

    Parameters
    ----------
    judge : object
        whether throw error.
    info : object
        Error information or return information.
    error_type : BaseException
        Error type.

    Returns
    -------
    object
        Throw error or return information.
    """

    if throw:
        if info == None:
            error = error_type
        else:
            error = error_type(info)
        raise error
    else:
        return info