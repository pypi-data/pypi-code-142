"""Top-level package for Py Cover Letters."""

__author__ = """Luis C. Berrocal"""
__email__ = 'luis.berrocal.1942@gmail.com'
__version__ = '0.3.0'

from py_cover_letters.config import ConfigurationManager

config_manager = ConfigurationManager()
if config_manager.is_valid():
    CURRENT_CONFIGURATION = config_manager.get_current()
else:
    CURRENT_CONFIGURATION = config_manager.get_sample_config()
    print(f'>>>>> Invalid configuration {config_manager.config_file}')
