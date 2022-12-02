# -*- coding: UTF-8 -*-
# Copyright 2018-2019 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""The :ref:`presto` extension of :mod:`lino_xl.lib.invoicing`.

This adds a new field :attr:`order
<lino_voga.lib.invoicing.models.Plan.order>` to the invoicing plan
and a "basket" button to the Order model.

.. autosummary::
   :toctree:

    fixtures.demo_bookings


"""

raise Excption("User lino_xl.lib.invoicing.order_model instead")


from lino_xl.lib.invoicing import Plugin, _


class Plugin(Plugin):

    extends_models = ['Plan']
