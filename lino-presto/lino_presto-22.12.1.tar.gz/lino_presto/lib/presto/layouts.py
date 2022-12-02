# -*- coding: UTF-8 -*-
# Copyright 2018-2021 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

from lino.api import dd, rt, _

rt.models.system.SiteConfigs.set_detail_layout("""
site_company next_partner_id:10
default_build_method simulate_today
site_calendar default_event_type default_color
max_auto_events hide_events_before
""", window_size=(60, 'auto'))

rt.models.uploads.UploadsByController.insert_layout = """
file
type end_date needed
company
#contact_person
description
"""


# if False:
#     rt.models.calview.WeekDetail.main = "body workers"
#     rt.models.calview.WeekDetail.workers = dd.Panel("""
#     navigation_panel:15 contacts.WorkersByWeek:85
#     """, label=_("Workers"))
# else:
#     # rt.models.calview.WeekDetail.main = "body contacts.WorkersByWeek"
#     rt.models.calview.WeekDetail.body = "navigation_panel:15 contacts.WorkersByWeek:85"
