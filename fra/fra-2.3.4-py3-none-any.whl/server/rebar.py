# -*- coding: utf-8 -*-
"""Application rebar registry."""
from __future__ import unicode_literals

from flask_rebar import Rebar
from flask_rebar import SwaggerV3Generator

rebar = Rebar()
registry = rebar.create_handler_registry(
    prefix="/api",
    swagger_generator=SwaggerV3Generator(
        title="Content Generator API",
        description="OpenAPI docs for recommendations generator based on content-based algorithm",
        version="2.3.4",
    ),
)
