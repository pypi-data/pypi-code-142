# This all runs automatically when the package is imported

from setuptools_scm import get_version

__author__ = "Rob Campbell"
__version__ = get_version()

"""
Bad practice to put actual code in here because it's run on import and maybe you
don't want that
"""


# We can make imports easier here by doing, e.g.
# from . import some_module
#
# So functions inside some_module can be imported as
# packagename.FUNCTION_IN_SOME_MODULE
#
# For example, see numpy's __init__.py
