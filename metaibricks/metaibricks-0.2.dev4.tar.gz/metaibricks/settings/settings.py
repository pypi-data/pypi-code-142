import os

from pydantic import BaseSettings

from metaibricks.settings.logger import Logger

_env_prefix = "met_ai_"


class Settings(BaseSettings):
    netrc_filename: str = os.path.join(os.environ.get("HOME", ""), ".netrc")
    log_level: str = "WARNING"
    log_file_name: str = None
    log_file_level: str = "WARNING"

    class Config:
        env_prefix = _env_prefix

    @classmethod
    def set(cls, **kwargs):
        """Class method for setting everything in the os environ"""
        settings_obj = cls()
        for key, value in kwargs.items():
            if hasattr(settings_obj, key) and value is not None:
                os.environ[f"{_env_prefix}{key}"] = str(value)

        Logger.set_config(
            json_file=kwargs.get("log_file_name", None),
            json_minimal_level=kwargs.get("log_file_level", "WARNING"),
            minimal_level=kwargs.get("log_level", "WARNING"),
        )

    @classmethod
    def clean(cls):
        """Class method for cleaning the os.environ of the lib attributes."""
        for key in os.environ:
            if key.startswith(_env_prefix):
                del os.environ[key]
