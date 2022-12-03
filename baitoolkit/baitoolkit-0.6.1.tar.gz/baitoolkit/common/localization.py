# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import datetime

from flask import Flask
from flask_babel import lazy_gettext, gettext, Babel

from baitoolkit.common import type_util
from baitoolkit.auth import iam_client
from baitoolkit.common.context_manager import global_ctx

t_ = gettext
l_ = lazy_gettext

gettext = gettext
lazy_gettext = lazy_gettext


def init_babel(app: Flask):
    """init babel"""
    babel = Babel()
    from baitoolkit.auth import iam_client
    from baitoolkit.web import req_util

    def locale_selector():
        user_token = iam_client.current_user_token()
        return req_util.get_request_locale() if user_token is None else user_token.preferred_language

    babel.localeselector(locale_selector)
    babel.init_app(app)
    return babel


def to_datetime_of_user_preferred_tz(dt: datetime.datetime) -> str:
    """Format to the datetime user preferred timezone."""
    if dt is None:
        return ''

    user = iam_client.current_user()
    if user is None:
        timezone = global_ctx.get_web_config_value('BABEL_DEFAULT_TIMEZONE')
    else:
        timezone = user.preferred_timezone()
    return type_util.tz_utc_to_local(dt, timezone)
