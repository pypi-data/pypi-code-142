# -*- coding: UTF-8 -*-
# Copyright 2012-2021 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""See :ref:`presto`.

.. autosummary::
   :toctree:

   lib
   projects


"""

from os.path import join, dirname

from .setup_info import SETUP_INFO

__version__ = SETUP_INFO['version']
intersphinx_urls = dict(
    docs="https://lino-framework.gitlab.io/presto/",
    dedocs="https://lino-framework.gitlab.io/presto/de/")
srcref_url = 'https://gitlab.com/lino-framework/presto/blob/master/%s'
