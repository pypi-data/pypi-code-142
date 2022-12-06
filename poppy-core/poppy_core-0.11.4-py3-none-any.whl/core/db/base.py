#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from poppy.core.db.database import Database
from poppy.core.conf import settings

__all__ = ["Base"]

# create a base declarative class for all models
Base = Database.bases_manager.get(settings.MAIN_DATABASE)

