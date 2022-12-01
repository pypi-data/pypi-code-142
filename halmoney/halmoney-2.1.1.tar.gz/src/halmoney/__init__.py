# __init__.py
# Copyright (C) 2022 (sjpkorea@yahoo.com) and contributors
#

import inspect
import os
import sys

__version__ = '2.1.0'
real_path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
sys.path.append(real_path)

try:
    from halmoney import halmoney

except ImportError as e:
    print(e," Please re-check.")
    exit(1)

__all__ = [name for name, obj in locals().items()
    if not (name.startswith('_') or inspect.ismodule(obj))]