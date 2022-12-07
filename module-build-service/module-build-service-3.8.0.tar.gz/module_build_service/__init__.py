# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT
"""The module build orchestrator for Modularity.

The orchestrator coordinates module builds and is responsible
for a number of tasks:

- Providing an interface for module client-side tooling via
  which module build submission and build state queries are
  possible.
- Verifying the input data (modulemd, RPM SPEC files and others)
  is available and correct.
- Preparing the build environment in the supported build systems,
  such as koji.
- Scheduling and building of the module components and tracking
  the build state.
- Emitting bus messages about all state changes so that other
  infrastructure services can pick up the work.
"""

from __future__ import absolute_import

import pkg_resources

from flask import Flask, has_app_context, url_for
from flask_sqlalchemy import SQLAlchemy

# Filter out warnings we don't want from external modules
import module_build_service.log_workaround  # noqa: F401
from module_build_service.common.config import config_section
from module_build_service.web.proxy import ReverseProxy

try:
    version = pkg_resources.get_distribution("module-build-service").version
except pkg_resources.DistributionNotFound:
    version = "unknown"
api_version = 2

app = Flask(__name__)
app.wsgi_app = ReverseProxy(app.wsgi_app)
app.config.from_object(config_section)


db = SQLAlchemy(app)


def get_url_for(*args, **kwargs):
    """
    flask.url_for wrapper which creates the app_context on-the-fly.
    """
    if has_app_context():
        return url_for(*args, **kwargs)

    # Localhost is right URL only when the scheduler runs on the same
    # system as the web views.
    app.config["SERVER_NAME"] = "localhost"
    with app.app_context():
        from module_build_service.common import log
        log.debug(
            "WARNING: get_url_for() has been called without the Flask "
            "app_context. That can lead to SQLAlchemy errors caused by "
            "multiple session being used in the same time."
        )
        return url_for(*args, **kwargs)


def load_views():
    from module_build_service.web import views

    assert views


load_views()
