"""
SPDX-FileCopyrightText: 2022. Thomas Mahe <contact@tmahe.dev>
SPDX-License-Identifier: MIT

This work is licensed under the terms of the MIT license.
For a copy, see <https://opensource.org/licenses/MIT>.
"""

import sys
from unittest.mock import patch


def with_arguments(*args):
    arguments = list(args)

    def decorator_with_arguments(func):
        arguments.insert(0, str(func).split(' ')[1])

        def inner(*args, **kwargs):
            with patch.object(sys, 'argv', arguments):
                return func(*args, **kwargs)

        return inner

    return decorator_with_arguments
