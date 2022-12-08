import traceback
from typing import Any, Callable, List

import mflog


class Logger:
    """Logger class wrapping created to dynamically create loggers
    it prevents fails when the mflog.set_config is changed during runtime
    after some logger have already been created.
    """

    def __init__(self, name: str, **bind_kwargs) -> Any:
        self._name = name
        self._bind_kwargs = bind_kwargs

    def _log(self, method: str, *args, **kwargs):
        """Default method triggering a logger creation and usage.

        Args:
            method (str): method to use. For instance, self._log("info", "toto")
                will display the INFO-level message "toto".
            *args: argument of the given method
            **kwargs: keyword arguments of the given method

        Returns:
            Any: returns the given method's return
        """
        logger = mflog.getLogger(self._name)
        logger = logger.bind(**self._bind_kwargs)
        return logger.__getattribute__(method)(*args, **kwargs)

    def debug(self, *args, **kwargs):
        return self._log("debug", *args, **kwargs)

    def info(self, *args, **kwargs):
        return self._log("info", *args, **kwargs)

    def warning(self, *args, **kwargs):
        return self._log("warning", *args, **kwargs)

    def error(self, *args, **kwargs):
        return self._log("error", *args, **kwargs)

    def exception(self, *args, **kwargs):
        return self._log("exception", *args, **kwargs)

    def critical(self, *args, **kwargs):
        return self._log("critical", *args, **kwargs)

    def bind(self, *args, **kwargs):
        self._bind_kwargs.update(kwargs)
        return self._log("bind", *args, **kwargs)

    def try_unbind(self, *args, **kwargs):
        for key in args:
            if key in self._bind_kwargs:
                self._bind_kwargs.pop(key)
        return self._log("try_unbind", *args, **kwargs)

    @classmethod
    def set_config(
        cls,
        minimal_level: str = None,
        json_minimal_level: str = None,
        json_file: str = None,
        override_files: List[str] = None,
        thread_local_context: bool = False,
        extra_context_func: Callable = None,
        json_only_keys: List[str] = None,
        override_dict: dict = {},
        syslog_address: str = None,
        syslog_format: str = None,
        fancy_output: bool = None,
        auto_dump_locals: bool = True,
    ):
        """Class method wrapper to the mflog.set_config"""
        return mflog.set_config(
            minimal_level=minimal_level,
            json_minimal_level=json_minimal_level,
            json_file=json_file,
            override_files=override_files,
            thread_local_context=thread_local_context,
            extra_context_func=extra_context_func,
            json_only_keys=json_only_keys,
            override_dict=override_dict,
            syslog_address=syslog_address,
            syslog_format=syslog_format,
            fancy_output=fancy_output,
            auto_dump_locals=auto_dump_locals,
        )


def log_error(excpt: Exception, log: Logger):
    """Function made for handling and logging exception raised in a
    asynchronous-multiprocess context.

    Args:
        excpt (Exception): Exception to log.
        log (Logger): Logger pass the exception to.
    """
    trace = traceback.format_exception(type(excpt), excpt, excpt.__traceback__)
    log.error(f"An error has been caught {repr(excpt)}.\n" + "".join(trace))
