
# This will load everything into package namespace to allow
# skipping of submodule namespace e.g. from fake.load import func
# you can use from fake import func
from . import *

# We can put some package info here that can be accessed
# with package.__func__ syntax
__name__ = "JoeZiminski"
__version__ = "0.0.0.1"  # though nowe we have setuptools_scm


