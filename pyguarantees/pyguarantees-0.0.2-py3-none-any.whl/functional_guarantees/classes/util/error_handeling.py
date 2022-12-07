import warnings
from typing import Union

from pyguarantees.functional_guarantees.classes import TypeGuarantee
from pyguarantees.functional_guarantees.exceptions import \
    ParameterGuaranteesTypeError, ParameterGuaranteesValueError, \
    ReturnGuaranteesValueError, ReturnGuaranteesTypeError, \
    FunctionalGuaranteesUserTypeError, FunctionalGuaranteesUserValueError

from pyguarantees import severity


def choose_exception(
        where: str,
        type_or_value: str
) -> Union[
    ParameterGuaranteesTypeError,
    ParameterGuaranteesValueError,
    ReturnGuaranteesValueError,
    ReturnGuaranteesTypeError,
    FunctionalGuaranteesUserTypeError,
    FunctionalGuaranteesUserValueError
]:
    exception_dict = {
        "parameter": {
            "type": ParameterGuaranteesTypeError,
            "value": ParameterGuaranteesValueError
        },
        "return": {
            "type": ReturnGuaranteesTypeError,
            "value": ReturnGuaranteesValueError
        },
        "internal": {
            "type": FunctionalGuaranteesUserTypeError,
            "value": FunctionalGuaranteesUserValueError
        }
    }

    return exception_dict[where][type_or_value]


def make_exception(
        where: str,
        type_or_value: str,
        qualname: str,
        module: str,
        guarantee_name: str,
        parameter_name: str,
        error_severity: int,
        what_dict: dict
) -> Union[
    ParameterGuaranteesTypeError,
    ParameterGuaranteesValueError,
    ReturnGuaranteesValueError,
    ReturnGuaranteesTypeError,
    FunctionalGuaranteesUserTypeError,
    FunctionalGuaranteesUserValueError
]:
    exception = choose_exception(where, type_or_value)
    return exception(
        qualname=qualname,
        module=module,
        guarantee_name=guarantee_name,
        parameter_name=parameter_name,
        error_severity=error_severity,
        what_dict=what_dict
    )


def raise_warning_or_exception(
        exception: Union[
            ParameterGuaranteesTypeError,
            ParameterGuaranteesValueError,
            ReturnGuaranteesValueError,
            ReturnGuaranteesTypeError,
            FunctionalGuaranteesUserTypeError,
            FunctionalGuaranteesUserValueError
        ],
        type_guarantee: TypeGuarantee
):
    if type_guarantee.error_severity <= severity.WARN:
        warnings.warn(exception.err_str + "\t**Ignoring** \n")
    else:
        raise exception


def output_exception(
        exception: Union[
            ParameterGuaranteesTypeError,
            ParameterGuaranteesValueError,
            ReturnGuaranteesValueError,
            ReturnGuaranteesTypeError,
            FunctionalGuaranteesUserTypeError,
            FunctionalGuaranteesUserValueError
        ],
        guarantee: TypeGuarantee
):
    def esc(code):
        return f'\033[{code}m'

    if guarantee is None:
        raise exception

    if guarantee.error_severity == severity.DEBUG:
        print(esc(32) + exception.err_str + esc(0))     # green
    elif guarantee.error_severity == severity.INFO:
        print(exception.err_str)                        # default
    elif guarantee.error_severity == severity.WARN:
        print(esc(31) + exception.err_str + esc(0))     # red
    else:
        raise exception


def handle_error(
        where: str,
        type_or_value: str,
        guarantee: TypeGuarantee,
        parameter_name: str,
        what_dict: dict
) -> None:
    """
    Call this function when an error occurred.

    Creates the appropriate exception. If there is an `error_callback`,
    `handle_error` will call it with the exception. Else, it will handle it
    with the appropriate severity (printing for severity up to `severity.WARN`,
    raising the exception from there).

    Parameters
    __________

    where:  "parameter", "return", or "internal".
            Independent of the `guarantee` parameter, because that one can only
            include one of the first two options and `handle_error` should be
            usable for internal errors as well.

    type_or_value: "type" or "value".

    guarantee: The guarantee.

    parameter_name: The name of the parameter. Independent of `guarantee`
                    to make it usable for internal errors.

    what_dict:  A dictionary for all other information.
    """
    exception = make_exception(
        where=where,
        type_or_value=type_or_value,
        qualname=guarantee.qualname,
        module=guarantee.module,
        guarantee_name=guarantee.guarantee_name,
        parameter_name=parameter_name,
        error_severity=guarantee.error_severity,
        what_dict=what_dict
    )

    if guarantee is not None and guarantee.error_callback is not None:
        guarantee.error_callback(exception)
    else:
        output_exception(exception, guarantee)


def raise_type_warning_or_exception(
        err_msg: str,
        type_guarantee: TypeGuarantee
) -> None:
    if type_guarantee.error_severity <= severity.WARN:
        warnings.warn(err_msg + "\t **Ignoring** \n")
    else:
        raise TypeError(err_msg)


def raise_value_warning_or_exception(
        err_msg: str,
        type_guarantee: TypeGuarantee
) -> None:
    if type_guarantee.error_severity <= severity.WARN:
        warnings.warn(err_msg + "\t **Ignoring** \n")
    else:
        raise ValueError(err_msg)
