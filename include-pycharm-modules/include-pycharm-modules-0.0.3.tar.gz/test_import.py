import importlib
from unittest import TestCase

from include_pycharm_modules import import_source_folders


class TestImportModule(TestCase):

    def test_path(self):
        import_source_folders(".")
        tm = importlib.import_module('test_module')
        self.assertTrue(tm.test_function())
