import pytest

pytest.register_assert_rewrite("zyfra_check.check")

from zyfra_check.check_methods import *  # noqa: F401, F402, F403