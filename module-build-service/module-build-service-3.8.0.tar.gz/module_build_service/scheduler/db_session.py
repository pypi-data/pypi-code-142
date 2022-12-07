# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT
from __future__ import absolute_import

import sqlalchemy.event
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import scoped_session, sessionmaker, Session

from module_build_service.common.config import conf
from module_build_service.common.models import (
    session_before_flush_handlers, send_message_after_module_build_state_change
)

__all__ = ("db_session",)


def _setup_event_listeners(db_session):
    """
    Starts listening for events related to the database session.
    """
    event_hooks = (
        ("before_flush", session_before_flush_handlers),
        ("after_commit", send_message_after_module_build_state_change),
    )

    for event, handler in event_hooks:
        if not sqlalchemy.event.contains(Session, event, handler):
            sqlalchemy.event.listen(Session, event, handler)

    # initialize DB event listeners from the monitor module
    from module_build_service.common.monitor import db_hook_event_listeners

    db_hook_event_listeners(db_session.bind.engine)


def apply_engine_options(conf):
    options = {
        "configuration": {"sqlalchemy.url": conf.sqlalchemy_database_uri},
    }
    if conf.sqlalchemy_database_uri.startswith("sqlite://"):
        options.update({
            # Both local module build and running tests requires a file-based
            # SQLite database, we do not use a connection pool for these two
            # scenarios.
            "poolclass": NullPool,
        })
    else:
        # TODO - we could use ZopeTransactionExtension() here some day for
        # improved safety on the backend.
        pool_options = {}

        # Apply pool options SQLALCHEMY_* set in MBS config.
        # Abbrev sa stands for SQLAlchemy.
        def apply_mbs_option(mbs_config_key, sa_config_key):
            value = getattr(conf, mbs_config_key, None)
            if value is not None:
                pool_options[sa_config_key] = value

        apply_mbs_option("sqlalchemy_pool_size", "pool_size")
        apply_mbs_option("sqlalchemy_pool_timeout", "pool_timeout")
        apply_mbs_option("sqlalchemy_pool_recycle", "pool_recycle")
        apply_mbs_option("sqlalchemy_max_overflow", "max_overflow")
        apply_mbs_option("sqlalchemy_connect_args", "connect_args")

        options.update(pool_options)

    return options


engine_opts = apply_engine_options(conf)
engine = sqlalchemy.engine_from_config(**engine_opts)
session_factory = sessionmaker(bind=engine)

# This is the global, singleton database Session that could be used to operate
# database queries.
db_session = scoped_session(session_factory)
_setup_event_listeners(db_session)
