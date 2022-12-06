# -*- coding: utf-8 -*-
"""
    atom
    ~~~~

    A atom Plugin for FlaskBB.

    :copyright: (c) 2022 by exelotl.
    :license: MIT License, see LICENSE for more details.
"""
import os

from pluggy import HookimplMarker

from flaskbb.forum.models import Forum
from flaskbb.utils.forms import SettingValueType
from flaskbb.utils.helpers import render_template

from .views import atom_bp

__version__ = "0.2.0"


hookimpl = HookimplMarker("flaskbb")


# connect the hooks
@hookimpl
def flaskbb_load_migrations():
    return os.path.join(os.path.dirname(__file__), "migrations")


@hookimpl
def flaskbb_load_translations():
    return os.path.join(os.path.dirname(__file__), "translations")


@hookimpl
def flaskbb_load_blueprints(app):
    app.register_blueprint(atom_bp, url_prefix="/atom")


@hookimpl
def flaskbb_tpl_before_navigation():
    return render_template("atom_navlink.html")


# plugin settings
SETTINGS = {
    "limit": {
        "value": 15,
        "value_type": SettingValueType.integer,
        "name": "Feed limit",
        "description": "The max number of posts to show in the feed.",
        "extra": {"min": 1},
    },
    "output_html": {
        "value": True,
        "value_type": SettingValueType.boolean,
        "name": "Output html?",
        "description": "If disabled, content in the feed will be rendered as plain text.",
        "extra": {},
    },
}
