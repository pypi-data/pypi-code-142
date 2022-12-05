from typing import Callable

from poetry_git_version_plugin import config


class PluginException(RuntimeError):
    def __str__(self) -> str:
        return f'{config.PLUGIN_NAME}: {self.args[0]}'


def plugin_exception_wrapper(func: Callable):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except PluginException as ex:
            raise ex

        except BaseException as ex:
            raise PluginException(ex) from ex

    return wrapper
