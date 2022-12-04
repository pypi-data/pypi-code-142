def use_par(par):
    """
    Wrapper set self argument as first function argument.
    """

    def wrap(fun):
        def INNER(*args, **kwargs):
            return fun(par, *args, **kwargs)

        INNER.__name__ = fun.__name__
        return INNER

    return wrap


def use_pars(*pars):
    """
    Wrapper set self arguments as first function arguments.
    """

    def wrap(fun):
        def INNER(*args, **kwargs):
            return fun(*pars, *args, **kwargs)

        INNER.__name__ = fun.__name__
        return INNER

    return wrap
