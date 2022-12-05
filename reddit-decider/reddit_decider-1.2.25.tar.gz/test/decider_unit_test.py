#!/usr/bin/env python
import os

from contextlib import contextmanager
from unittest import TestCase

from rust_decider import Decider
from rust_decider import DeciderException
from rust_decider import DeciderFeatureNotFoundException
from rust_decider import DeciderInitException
from utils import create_temp_config_file

TEST_DIR = os.path.dirname(os.path.abspath(__file__))


def setup_decider_class(cfg_path):
    return Decider(cfg_path)


class TestDecider(TestCase):
    def setUp(self):
        self.valid_ctx_dict = {
            "user_id": "795244",
            "device_id": "1234",
            "canonical_url": "www.reddit.com",
            "locale": "us_en",
            "user_is_employee": True,
            "logged_in": None,
            "app_name": "ios",
            "build_number": 1234,
            "country_code": "UA",
            "origin_service": "oss",
            "oauth_client_id": "test",
            "cookie_created_timestamp": 1648859753,
        }

        self.variants = [
            {"range_start": 0.0, "range_end": 0.2, "name": "control_1"},
            {"range_start": 0.2, "range_end": 0.4, "name": "variant_2"},
            {"range_start": 0.4, "range_end": 0.6, "name": "variant_3"},
            {"range_start": 0.6, "range_end": 0.8, "name": "variant_4"},
            {"range_start": 0.8, "range_end": 1.0, "name": "variant_5"},
        ]

        self.device_id_exp = {
            "genexp_device_id": {
                "id": 6222,
                "name": "genexp_device_id",
                "enabled": True,
                "owner": "test",
                "version": "5",
                "type": "range_variant",
                "start_ts": 0,
                "stop_ts": 2147483648,
                "emit_event": True,
                "experiment": {
                    "variants": self.variants,
                    "experiment_version": 5,
                    "shuffle_version": 91,
                    "bucket_val": "device_id",
                    "log_bucketing": False,
                },
            }
        }

        self.canonical_url_exp = {
            "genexp_canonical_url": {
                "id": 6233,
                "name": "genexp_canonical_url",
                "enabled": True,
                "owner": "test",
                "version": "5",
                "type": "range_variant",
                "start_ts": 0,
                "stop_ts": 2147483648,
                "emit_event": True,
                "experiment": {
                    "variants": self.variants,
                    "experiment_version": 5,
                    "shuffle_version": 91,
                    "bucket_val": "canonical_url",
                    "log_bucketing": False,
                },
            }
        }

        self.genexp_0_cfg = {
            "genexp_0": {
                "id": 6299,
                "name": "genexp_0",
                "enabled": True,
                "owner": "test",
                "version": "5",
                "emit_event": True,
                "type": "range_variant",
                "start_ts": 0,
                "stop_ts": 2147483648,
                "experiment": {
                    "variants": self.variants,
                    "experiment_version": 5,
                    "shuffle_version": 91,
                    "bucket_val": "user_id",
                    "log_bucketing": False,
                },
            },
        }
        super().setUp()

    def test_init(self):
        # handles full cfg.json file
        decider = setup_decider_class(f"{TEST_DIR}/../../cfg.json")
        self.assertEqual(decider.get_decider().err(), None)

    def test_init_missing_cfg_file(self):
        with self.assertRaises(DeciderInitException) as e:
            setup_decider_class("foo")
        self.assertEqual(
            str(e.exception),
            'rust_decider.init() has error: Decider initialization failed: Std io error: "No such file or directory (os error 2)".',
        )

    def test_init_bad_cfg(self):
        # an experiment's id is string instead of int
        cfg = {
            "exp_0": {
                "id": "3248",
                "name": "exp_0",
                "enabled": True,
                "owner": "test",
                "version": "2",
                "type": "range_variant",
                "start_ts": 37173982,
                "stop_ts": 2147483648,
                "experiment": {
                    "variants": [],
                    "experiment_version": 2,
                    "shuffle_version": 91,
                    "bucket_val": "user_id",
                    "log_bucketing": False,
                },
            }
        }

        with create_temp_config_file(cfg) as f:
            with self.assertRaises(DeciderInitException) as e:
                setup_decider_class(f.name)

            self.assertEqual(
                str(e.exception),
                'rust_decider.init() has error: Decider initialization failed: Json error: "invalid type: string \\"3248\\", expected u32".',
            )

    def test_choose(self):
        with create_temp_config_file(self.genexp_0_cfg) as f:
            decider = setup_decider_class(f.name)

            choice = decider.choose("genexp_0", self.valid_ctx_dict)

            self.assertEqual(
                dict(choice),
                {
                    "variant": "variant_5",
                    "value": None,
                    "feature_id": 6299,
                    "feature_name": "genexp_0",
                    "feature_version": 5,
                    "events": [
                        "0::::6299::::genexp_0::::5::::variant_5::::795244::::user_id::::0::::2147483648::::test"
                    ],
                },
            )

    def test_choose_without_variant(self):
        cfg = self.genexp_0_cfg.copy()
        variants = [
            {"name": "enabled", "size": 0, "range_end": 0, "range_start": 0},
            {"name": "control_1", "size": 0, "range_end": 0, "range_start": 0},
        ]
        cfg["genexp_0"]["experiment"]["variants"] = variants

        with create_temp_config_file(cfg) as f:
            decider = setup_decider_class(f.name)

            choice = decider.choose("genexp_0", self.valid_ctx_dict)

            self.assertEqual(
                dict(choice),
                {
                    "variant": None,
                    "value": None,
                    "feature_id": 6299,
                    "feature_name": "genexp_0",
                    "feature_version": 5,
                    "events": [],
                },
            )

    def test_choose_bucket_val_device_id(self):
        with create_temp_config_file(self.device_id_exp) as f:
            decider = setup_decider_class(f.name)

            choice = decider.choose("genexp_device_id", self.valid_ctx_dict)

            self.assertEqual(
                dict(choice),
                {
                    "variant": "variant_5",
                    "value": None,
                    "feature_id": 6222,
                    "feature_name": "genexp_device_id",
                    "feature_version": 5,
                    "events": [
                        "0::::6222::::genexp_device_id::::5::::variant_5::::1234::::device_id::::0::::2147483648::::test"
                    ],
                },
            )

    def test_choose_bucket_val_device_id_missing_identifier(self):
        with create_temp_config_file(self.device_id_exp) as f:
            decider = setup_decider_class(f.name)
            ctx = self.valid_ctx_dict.copy()
            del ctx["device_id"]

            with self.assertRaises(DeciderException) as e:
                decider.choose("genexp_device_id", ctx)

            self.assertEqual(
                str(e.exception),
                'Missing field "device_id" in context for bucket_val = device_id',
            )

    def test_choose_bucket_val_canonical_url(self):
        with create_temp_config_file(self.canonical_url_exp) as f:
            decider = setup_decider_class(f.name)

            choice = decider.choose("genexp_canonical_url", self.valid_ctx_dict)

            self.assertEqual(
                dict(choice),
                {
                    "variant": "control_1",
                    "value": None,
                    "feature_id": 6233,
                    "feature_name": "genexp_canonical_url",
                    "feature_version": 5,
                    "events": [
                        "0::::6233::::genexp_canonical_url::::5::::control_1::::www.reddit.com::::canonical_url::::0::::2147483648::::test"
                    ],
                },
            )

    def test_choose_bucket_val_canonical_url_missing_ctx_field(self):
        with create_temp_config_file(self.canonical_url_exp) as f:
            decider = setup_decider_class(f.name)
            ctx = self.valid_ctx_dict.copy()
            del ctx["canonical_url"]

            with self.assertRaises(DeciderException) as e:
                decider.choose("genexp_canonical_url", ctx)
            self.assertEqual(
                str(e.exception),
                'Missing field "canonical_url" in context for bucket_val = canonical_url',
            )

    def test_choose_with_other_fields_for_targeting(self):
        cfg = self.genexp_0_cfg.copy()
        cfg["genexp_0"]["experiment"].update(
            {"targeting": {"ALL": [{"EQ": {"field": "foo", "values": ["bar"]}}]}}
        )

        with create_temp_config_file(cfg) as f:
            decider = setup_decider_class(f.name)
            ctx = self.valid_ctx_dict.copy()

            # targeting matches
            ctx.update({"other_fields": {"foo": "bar"}})

            choice = decider.choose("genexp_0", ctx)

            self.assertEqual(
                dict(choice),
                {
                    "variant": "variant_5",
                    "value": None,
                    "feature_id": 6299,
                    "feature_name": "genexp_0",
                    "feature_version": 5,
                    "events": [
                        "0::::6299::::genexp_0::::5::::variant_5::::795244::::user_id::::0::::2147483648::::test"
                    ],
                },
            )

            # targeting doesn't match
            ctx.update({"other_fields": {"foo": "huh"}})

            choice = decider.choose("genexp_0", ctx)
            self.assertEqual(
                dict(choice),
                {
                    "variant": None,
                    "value": None,
                    "feature_id": 6299,
                    "feature_name": "genexp_0",
                    "feature_version": 5,
                    "events": [],
                },
            )

    @contextmanager
    def test_feature_not_found(self):
        with create_temp_config_file({}) as f:
            decider = setup_decider_class(f.name)
            yield decider

    def test_choose_feature_not_found(self):
        with self.test_feature_not_found() as d:
            with self.assertRaises(DeciderFeatureNotFoundException) as e:
                d.choose("any", self.valid_ctx_dict)

            self.assertEqual(
                str(e.exception),
                'Feature "any" not found.',
            )

    def test_choose_with_a_value(self):
        cfg = {
            "dc_bool": {
                "id": 3393,
                "value": True,
                "type": "dynamic_config",
                "version": "2",
                "enabled": True,
                "owner": "test",
                "name": "dc_bool",
                "value_type": "Boolean",
                "experiment": {"experiment_version": 2},
            }
        }
        with create_temp_config_file(cfg) as f:
            decider = setup_decider_class(f.name)

            choice = decider.choose("dc_bool", self.valid_ctx_dict)

            self.assertEqual(
                dict(choice),
                {
                    "variant": None,
                    "value": True,
                    "feature_id": 3393,
                    "feature_name": "dc_bool",
                    "feature_version": 2,
                    "events": [],
                },
            )
