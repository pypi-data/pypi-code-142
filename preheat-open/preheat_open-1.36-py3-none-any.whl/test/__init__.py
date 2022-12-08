"""
Sub-package containing all test routines to be run with Pytest (parameterized with 'conftest.py')
"""
import os
import warnings

import pytest

import preheat_open
from preheat_open import ENV_VAR_TRACK_MISSING_DATA_FIELD, running_in_test_mode

# Setting up a test API key, which is only valid for a dummy test installation
TEST_LOCATION_ID = 2756
API_KEY = "KVkIdWLKac5XFLCs2loKb7GUitkTL4uJXoSyUFIZkVgWuCk8Uj"
ANONYMISED_API_KEY = "3xa0SeGXa4WlkrB68qGR9NoDAzVvGdiG3XAabKu6n7n5qQTDkL"

# Warning the user that this module is not meant to be used for non test-related activities
if running_in_test_mode() is False:
    warnings.warn(
        """

The module 'preheat_open.test' is not meant to be imported and actively used, 
unless you are specifically carrying out a test.

    """
    )

SHORT_TEST_PERIOD = ("2021-05-01T00:00+02:00", "2021-05-02T00:00+02:00", "hour")
MEDIUM_TEST_PERIOD = ("2021-05-01T00:00+02:00", "2021-05-02T00:00+02:00", "hour")


class PreheatTest:
    @pytest.fixture()
    def bypass_api_key(self):
        preheat_open.api.set_api_key(None)
        yield None
        preheat_open.api.set_api_key(API_KEY)


def mark_pytest_package_test():
    preheat_open.helpers.DISPLAY_DEVELOPER_WARNING.cache_clear()
    os.environ[ENV_VAR_TRACK_MISSING_DATA_FIELD] = "true"
