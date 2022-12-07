from .error_handeling import handle_error
from .typenames import get_arg_type_name
from typing import Callable, List


def check_type(arg, guarantee):
    if isinstance(arg, guarantee.guaranteed_type):
        return arg

    if guarantee.force_conversion:
        try:
            return guarantee.guaranteed_type(arg)
        except TypeError:
            pass
        except ValueError:
            pass

    # Type error occurred
    handle_error(
        where=guarantee.where,
        type_or_value="type",
        guarantee=guarantee,
        parameter_name=guarantee.parameter_name,
        what_dict={
            "should_type": get_arg_type_name(guarantee.guaranteed_type),
            "actual_type": get_arg_type_name(arg),
            "force_conversion": guarantee.force_conversion
        }
    )

    return arg   # in case of warnings_only


def enforce_check_functions(arg, guarantee) -> None:
    cf = guarantee.check_functions
    if cf is None:
        return

    descriptions = None
    error_indices = []

    if type(cf) is list and all(callable(f) for f in cf):
        error_indices = _find_errors(arg, cf)
    elif all(isinstance(k, str) for k in cf.keys()) \
            and all(callable(f) for f in cf.values()):
        descriptions = list(cf.keys())
        error_indices = _find_errors(arg, list(cf.values()))
    elif all(callable(f) for f in cf.keys()) \
            and all(isinstance(v, str) for v in cf.values()):
        descriptions = list(cf.values())
        error_indices = _find_errors(arg, list(cf.keys()))
    else:
        handle_error(
            where="internal",
            type_or_value="type",
            guarantee=guarantee,
            parameter_name=guarantee.parameter_name,
            what_dict={
                "should_type":
                    "List[Callable] or Dict[str, Callable] "
                    "or Dict[Callable, str]",
                "actual_type": f"{get_arg_type_name(arg)}"
            }
        )

    if error_indices:
        handle_error(
            where=guarantee.where,
            type_or_value="value",
            guarantee=guarantee,
            parameter_name=guarantee.parameter_name,
            what_dict=_get_what_dict(
                arg, guarantee, descriptions, error_indices)
        )


def _find_errors(
        arg,
        check_functions: List[Callable]
) -> list:
    errors = []
    for i, f in enumerate(check_functions):
        if not f(arg):
            errors.append(i)

    return errors


def _get_what_dict(
        arg,
        guarantee,
        descriptions: List[str],
        error_indices: list
):
    if not error_indices:
        return

    what_dict = {
        "error": f"violated {guarantee.guarantee_name}.check_functions",
        "violations": {},
        "arg": arg
    }

    for i, ind in enumerate(error_indices):
        err_msg = f"Check function at index {ind}"
        if descriptions:  # description only given in dict -> error_indies okay
            err_msg += f" - {descriptions[ind]}"

        what_dict["violations"][i] = err_msg

    return what_dict
