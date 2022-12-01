from collections.abc import Callable
from typing import Any, List
from typing_extensions import Self


class LogToOut:
    nested_depth: int = 0
    start_chr: str = ""
    pad_chr: str = " "
    indent_dup: int = 2
    func_in: str = "+"
    func_out: str = "-"

    @classmethod
    def get_padding(cls: Self) -> str:
        """
        Get padding according to depth.

        :return: Pad Character *  Nested Depth
        """
        return LogToOut.pad_chr * LogToOut.indent_dup * LogToOut.nested_depth

    @classmethod
    def unpack_kwargs(cls: Self, kwargs: dict) -> List[str]:
        """
        Converts kwargs to list of strings.

        :param kwargs: Function kwargs
        :return: List of "key=val" for every pair in kwargs
        """
        return [f"{attr}={val}" for attr, val in kwargs.items()]

    @classmethod
    def unpack_args(cls: Self, args: tuple) -> List[str]:
        return [f"{val}" for val in args]

    @classmethod
    def format_input(cls: Self, args: tuple, kwargs: dict):
        return ", ".join(LogToOut.unpack_args(args) + LogToOut.unpack_kwargs(kwargs))

    @classmethod
    def print_result(cls: Self, res: Any) -> str:
        if res:
            return f" -> {res}"
        else:
            return ""

    @classmethod
    def print_func_in(cls: Self, func: Callable, args: tuple, kwargs: dict) -> None:
        res = LogToOut.get_padding() \
              + f"{LogToOut.func_in} {func.__name__}( {LogToOut.format_input(args, kwargs)} )"
        LogToOut.nested_depth += 1
        print(res)

    @classmethod
    def print_func_out(cls: Self, func: Callable, result: Any) -> None:
        LogToOut.nested_depth -= 1
        res = LogToOut.get_padding() \
            + f"{LogToOut.func_out} {func.__name__}{LogToOut.print_result(result)}"
        print(res)

    @classmethod
    def log_function(cls: Self, func: Callable) -> Callable:
        def dec_func(*args, **kwargs):
            LogToOut.print_func_in(func, args, kwargs)
            res: Any = func(*args, **kwargs)
            LogToOut.print_func_out(func, res)
            return res

        return dec_func

    @classmethod
    def log_variable(cls: Self, var: Any, var_name: str = "") -> None:
        pad: str = LogToOut.get_padding()
        if var_name:
            log_msg = f"{var_name} = {var}"
        else:
            log_msg = f"{var}"
        print(pad + log_msg)


@LogToOut.log_function
def addition(a, b):
    LogToOut.log_variable(a, "a")
    LogToOut.log_variable(b, "b")
    return a + b


if __name__ == "__main__":
    addition(3, 50)
