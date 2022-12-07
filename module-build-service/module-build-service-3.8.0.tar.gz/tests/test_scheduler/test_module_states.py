# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT
from __future__ import absolute_import
import os

import mock
from mock import patch
import pytest

from module_build_service.common import build_logs, conf, models
import module_build_service.resolver
from module_build_service.scheduler.db_session import db_session
import module_build_service.scheduler.handlers.modules
from tests import scheduler_init_data, clean_database

base_dir = os.path.dirname(os.path.dirname(__file__))


class TestModuleStateChecks:
    def setup_method(self, test_method):
        clean_database()
        self.config = conf
        self.session = mock.Mock()
        conf.strict_module_state_transitions = True

    def teardown_method(self, test_method):
        try:
            path = build_logs.path(db_session, 1)
            os.remove(path)
        except Exception:
            pass

    @pytest.mark.parametrize(
        "bad_state",
        ["build", "done", "failed", "ready", "garbage"],
    )
    @patch("module_build_service.builder.GenericBuilder.create_from_module")
    def test_wait_state_validation(self, create_builder, bad_state):
        scheduler_init_data(module_state=bad_state)
        build = models.ModuleBuild.get_by_id(db_session, 2)
        # make sure we have the right build
        assert build.state == models.BUILD_STATES[bad_state]
        assert build.version == "20170109091357"
        with patch("module_build_service.resolver.GenericResolver.create"):
            module_build_service.scheduler.handlers.modules.wait(
                msg_id="msg-id-1",
                module_build_id=build.id,
                module_build_state=models.BUILD_STATES["wait"])

        # the handler should exit early for these bad states
        create_builder.assert_not_called()

        # build state should not be changed
        build = models.ModuleBuild.get_by_id(db_session, build.id)
        assert build.state == models.BUILD_STATES[bad_state]

    @pytest.mark.parametrize(
        "bad_state",
        ["done", "ready", "garbage"],
    )
    @patch("module_build_service.builder.GenericBuilder.create_from_module")
    def test_failed_state_validation(self, create_builder, bad_state):
        scheduler_init_data(module_state=bad_state)
        build = models.ModuleBuild.get_by_id(db_session, 2)
        # make sure we have the right build
        assert build.state == models.BUILD_STATES[bad_state]
        assert build.version == "20170109091357"
        with patch("module_build_service.resolver.GenericResolver.create"):
            module_build_service.scheduler.handlers.modules.failed(
                msg_id="msg-id-1",
                module_build_id=build.id,
                module_build_state=models.BUILD_STATES["wait"])

        # the handler should exit early for these bad states
        create_builder.assert_not_called()

        # build state should not be changed
        build = models.ModuleBuild.get_by_id(db_session, build.id)
        assert build.state == models.BUILD_STATES[bad_state]

    @pytest.mark.parametrize(
        "bad_state",
        ["init", "wait", "failed", "ready", "garbage"],
    )
    @patch("module_build_service.builder.GenericBuilder.clear_cache")
    def test_done_state_validation(self, clear_cache, bad_state):
        scheduler_init_data(module_state=bad_state)
        build = models.ModuleBuild.get_by_id(db_session, 2)
        # make sure we have the right build
        assert build.state == models.BUILD_STATES[bad_state]
        assert build.version == "20170109091357"
        with patch("module_build_service.resolver.GenericResolver.create"):
            module_build_service.scheduler.handlers.modules.done(
                msg_id="msg-id-1",
                module_build_id=build.id,
                module_build_state=models.BUILD_STATES["done"])

        # the handler should exit early for these bad states
        clear_cache.assert_not_called()

        # build state should not be changed
        build = models.ModuleBuild.get_by_id(db_session, build.id)
        assert build.state == models.BUILD_STATES[bad_state]
