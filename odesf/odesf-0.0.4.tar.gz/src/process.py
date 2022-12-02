import re
import types
from math import *

def __func_from_string(func_str):
    module_code = compile(func_str, '', 'exec')
    function_code = [c for c in module_code.co_consts if isinstance(c, types.CodeType)][0]
    func = types.FunctionType(function_code, globals())
    return func

def __process_const_str(co_ls):
    
    # post-process constant strings
    __sup_semicolon(co_ls)

    # join all constant strings
    return "".join(co_ls)

def __c_process_const_str(co_ls):
    
    # post-process constant strings
    __c_sup_semicolon(co_ls)

    # join all constant strings
    return "".join(co_ls)

def __process_eq_str(eq_ls):

    # split lhs and rhs
    __lhs_ls, __rhs_ls = __hs_ls(eq_ls)

    # parse lhs to get/replace derivative variable
    dep_dict, indep_dict = __lhs_parse(eq_ls, __lhs_ls)

    # replace derivative at rhs
    __rhs_replace(eq_ls, dep_dict, indep_dict, __rhs_ls)

    # post-process equation strings
    __sup_semicolon(eq_ls)

    # join all equation strings
    return "".join(eq_ls)


def __lhs_parse(eq_ls, lhs_ls):
    dep_dict = dict()
    indep_dict = dict()
    # rhs_ls = []
    for i in range(len(eq_ls)):

        eq_ls[i] = eq_ls[i].replace(lhs_ls[i], "_f_[{}]".format(i))

        dep_pattern = re.compile("^d([\D]*\w*)/") # get "d<>/"
        indep_pattern = re.compile("/d([\D]*\w*)")
        dep_var = dep_pattern.findall(lhs_ls[i])[0]
        indep_var = indep_pattern.findall(lhs_ls[i])[0]
        if dep_var:
            dep_dict['_y_[{}]'.format(i)] = dep_var
        if indep_var:
            indep_dict[indep_var] = "_x_"

    # rhs_ls.append(rhs)
    return dep_dict, indep_dict

def __rhs_replace(eq_ls, dep_dict, indep_dict, rhs):

    for i in range(len(rhs)):
        for k, v in dep_dict.items():
            # print(k, v)
            p = re.compile(r'(^|[\W])({})([\W]|$)'.format(v)) # (A: start or anything not \w - digits, letters and _)(B: target)(C: end or anything not \w - digits, letters and _)
            eq_ls[i] = re.sub(p, r'\1{}\3'.format(k), eq_ls[i]) # refer and keep (A:...) and (C:...), relplace (B:...)
            # print(eq_ls[i])

        for k, v in indep_dict.items():
            p = re.compile(r'(^|[\W])({})([W]|$)'.format(k))
            eq_ls[i] = re.sub(p, r'\1{}\3'.format(v), eq_ls[i])


def __hs(s):
    s = s.split("=")
    return s[0].strip(), s[1].strip()

def __hs_ls(s):
    __lhs_ls = []
    __rhs_ls = []
    for i in range(len(s)):
        __lhs, __rhs = __hs(s[i])
        __lhs_ls.append(__lhs)
        __rhs_ls.append(__rhs)
    return __lhs_ls, __rhs_ls


def __sup_semicolon(ls):
    for i in range(len(ls)):
        ls[i] = ls[i] + "; "

def __c_sup_semicolon(ls):
    for i in range(len(ls)):
        ls[i] = "double " + ls[i] + "; "

