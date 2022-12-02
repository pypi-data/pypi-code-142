from process import __process_eq_str, __process_const_str, __c_process_const_str, __func_from_string


def eq_to_pyfunc(equations, constants=None, with_return=False):
    eqs_str = __process_eq_str(equations)

    if constants and not with_return:
        cons_str = __process_const_str(constants)
        return __func_from_string(f"def func(_x_, _y_, _f_): {cons_str} {eqs_str}")

    elif constants and with_return:
        cons_str = __process_const_str(constants)
        return __func_from_string(f"def func(_x_, _y_, _f_): {cons_str} {eqs_str} return _f_ ")

    elif constants is None and not with_return:
        return __func_from_string(f"def func(_x_, _y_, _f_): {eqs_str}")

    elif constants is None and with_return:
        return __func_from_string(f"def func(_x_, _y_, _f_): {eqs_str} return _f_ ")

def eq_to_pyfunc_string(equations, constants=None, with_return=False):
    eqs_str = __process_eq_str(equations)

    if constants and not with_return:
        cons_str = __process_const_str(constants)
        return f"def func(_x_, _y_, _f_): {cons_str} {eqs_str}"

    elif constants and with_return:
        cons_str = __process_const_str(constants)
        return f"def func(_x_, _y_, _f_): {cons_str} {eqs_str} return _f_ "

    elif constants is None and not with_return:
        return f"def func(_x_, _y_, _f_): {eqs_str}"

    elif constants is None and with_return:
        return f"def func(_x_, _y_, _f_): {eqs_str} return _f_ "


def eq_to_cfunc_string(equations, constants=None, with_return=False):

    eqs_str = __process_eq_str(equations)

    if constants and not with_return:
        cons_str = __c_process_const_str(constants)
        return "void template_func(double _x_, double _y_[], double _f_[])" + " { " + f"{cons_str} {eqs_str}" + "}", "void template_func(double _x_, double _y_[], double _f_[]);"
    
    elif constants and with_return:
        cons_str = __c_process_const_str(constants)
        return "double** template_func(double _x_, double _y_[], double _f_[])" + " { " + f"{cons_str} {eqs_str}" + " return _f_ }", "double** template_func(double _x_, double _y_[], double _f_[]);"

    elif constants is None and not with_return:
        return "void template_func(double _x_, double _y_[], double _f_[])" + " { " + f"{eqs_str}" + "}", "void template_func(double _x_, double _y_[], double _f_[]);"

    elif constants is None and with_return:
        return "double** template_func(double _x_, double _y_[], double _f_[])" + " { " + f"{eqs_str}" + " return _f_ }", "double** template_func(double _x_, double _y_[], double _f_[]);"