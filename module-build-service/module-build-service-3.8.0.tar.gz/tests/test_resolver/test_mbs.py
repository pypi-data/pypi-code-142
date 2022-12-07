# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT
from __future__ import absolute_import

from mock import patch, PropertyMock, Mock
import os

import pytest

from module_build_service import app
from module_build_service.builder.MockModuleBuilder import load_local_builds
from module_build_service.common.errors import StreamNotXyz, UnprocessableEntity
import module_build_service.common.models
from module_build_service.common import conf
from module_build_service.common.utils import load_mmd, mmd_to_str
import module_build_service.resolver as mbs_resolver
from module_build_service.scheduler.db_session import db_session
import tests


def add_item(test_items, yaml_name=None, mmd=None, context=None, koji_tag='auto'):
    if mmd is None:
        modulemd = tests.read_staged_data(yaml_name)
        mmd = load_mmd(modulemd)

    if context:
        mmd = mmd.copy()
        mmd.set_context(context)

    item = {
        "name": mmd.get_module_name(),
        "stream": mmd.get_stream_name(),
        "version": str(mmd.get_version()),
        "context": mmd.get_context(),
        "modulemd": mmd_to_str(mmd),
        "_mmd": mmd,
    }

    if koji_tag == 'auto':
        koji_tag = "module-{name}-{stream}-{version}-{context}".format(**item)
    item["koji_tag"] = koji_tag

    test_items.append(item)


test_items = []
add_item(test_items, "formatted_testmodule")
add_item(test_items, "formatted_testmodule", context="c2c572ed")
add_item(test_items, "platform", koji_tag="module-f28-build")


ABSENT = object()


class FakeMBS(object):
    def __init__(self, session_mock):
        session_mock.get = self.get
        self.items = test_items
        self.request_count = 0
        self.required_params = {
            'order_desc_by': 'version',
            'state': ['ready'],
            'verbose': True,
            'per_page': 5,
        }

    def item_matches(self, item, params):
        for k in ("name", "stream", "version", "context", "koji_tag"):
            if k in params and item[k] != params[k]:
                return False

        return True

    def modify_item_mmd(self, nsvc, modify):
        old_items = self.items
        self.items = []
        for item in old_items:
            if item["_mmd"].get_nsvc() == 'testmodule:master:20180205135154:9c690d0e':
                item = dict(item)
                mmd = item["_mmd"].copy()

                modify(mmd)

                item["_mmd"] = mmd
                item["modulemd"] = mmd_to_str(mmd)

            self.items.append(item)

    def get(self, url, params={}):
        self.request_count += 1

        for k, v in self.required_params.items():
            if v == ABSENT:
                assert k not in params
            else:
                assert params[k] == v

        all_items = [i for i in self.items
                     if self.item_matches(i, params)]

        page = int(params.get('page', 1))
        per_page = int(params.get('per_page', 5))

        result_items = all_items[(page - 1) * per_page:page * per_page]
        if page * per_page < len(all_items):
            next_ = ("https://mbs.example.com/module-build-service/1/module-builds/"
                     "?per_page={}&page={}&verbose=1".format(per_page, page + 1))
        else:
            next_ = None

        mock_res = Mock()
        mock_res.json.return_value = {
            "items": result_items,
            "meta": {"next": next_},
        }

        return mock_res


class TestMBSModule:
    def setup_method(self):
        mbs_resolver.MBSResolver.MBSResolver.region.invalidate()

    @pytest.fixture
    def fake_mbs(self):
        patcher = patch("module_build_service.resolver.MBSResolver.requests_session")
        session_mock = patcher.start()

        yield FakeMBS(session_mock)

        patcher.stop()

    @pytest.fixture
    def local_builds(self, require_empty_database):
        with patch("module_build_service.common.config.Config.system",
                   new_callable=PropertyMock,
                   return_value="test"):
            with patch("module_build_service.common.config.Config.mock_resultsdir",
                       new_callable=PropertyMock,
                       return_value=tests.staged_data_filename("local_builds")):
                yield

    @pytest.fixture
    def resolver(self):
        yield mbs_resolver.GenericResolver.create(db_session, conf, backend="mbs")

    def test_get_module_modulemds_nsvc(self, resolver, fake_mbs):
        """ Tests for querying a module from mbs """

        module_mmds = resolver.get_module_modulemds(
            "testmodule", "master", "20180205135154", "9c690d0e"
        )
        nsvcs = set(m.get_nsvc() for m in module_mmds)
        expected = {"testmodule:master:20180205135154:9c690d0e"}
        assert nsvcs == expected

    def test_get_module_modulemds_partial(
            self, resolver, fake_mbs, formatted_testmodule_mmd
    ):
        """ Test for querying MBS without the version of a module """

        fake_mbs.items = []

        # First page has version1.context[0..4]
        # Second page has version1.context5, version2.context[0..3]
        # Third page has version2.context[4..5]
        # We should only query the first two pages
        for i in range(0, 2):
            for context in range(0, 6):
                context_string = "{0:08d}".format(context)
                m = formatted_testmodule_mmd.copy()
                m.set_version(20180205135154 - i)
                m.set_context(context_string)
                add_item(fake_mbs.items, mmd=m)

        ret = resolver.get_module_modulemds("testmodule", "master")
        nsvcs = set(m.get_nsvc() for m in ret)
        expected = {
            "testmodule:master:20180205135154:00000000",
            "testmodule:master:20180205135154:00000001",
            "testmodule:master:20180205135154:00000002",
            "testmodule:master:20180205135154:00000003",
            "testmodule:master:20180205135154:00000004",
            "testmodule:master:20180205135154:00000005",
        }
        assert nsvcs == expected
        assert fake_mbs.request_count == 2

    def test_get_module_modulemds_cache(
            self, resolver, fake_mbs, formatted_testmodule_mmd
    ):
        """ Test that query results are cached """

        ret1 = resolver.get_module_modulemds("testmodule", "master")
        ret2 = resolver.get_module_modulemds("testmodule", "master")

        assert {m.get_nsvc() for m in ret1} == {m.get_nsvc() for m in ret2}
        assert fake_mbs.request_count == 1

    @pytest.mark.parametrize('strict', (False, True))
    def test_get_module_modulemds_not_found(self, resolver, fake_mbs, strict):
        def get_nonexistent():
            return resolver.get_module_modulemds("testmodule", "master", "0", strict=strict)

        if strict:
            with pytest.raises(UnprocessableEntity):
                get_nonexistent()
        else:
            assert get_nonexistent() == []

    @pytest.mark.parametrize('strict', (False, True))
    def test_get_module_modulemds_no_yaml(self, resolver, fake_mbs, strict):
        fake_mbs.items = [dict(i) for i in (fake_mbs.items)]
        for i in fake_mbs.items:
            i["modulemd"] = None

        def get_modulemds():
            return resolver.get_module_modulemds(
                "testmodule", "master", "20180205135154", strict=strict
            )

        if strict:
            with pytest.raises(UnprocessableEntity):
                get_modulemds()
        else:
            assert get_modulemds() == []

    def test_get_module_modulemds_local_module(self, resolver, fake_mbs, local_builds):
        load_local_builds(["platform:f30", "testmodule"])

        ret = resolver.get_module_modulemds("testmodule", "master")
        nsvcs = set(m.get_nsvc() for m in ret)
        expected = {"testmodule:master:20170816080816:321"}
        assert nsvcs == expected

    def test_get_module_build_dependencies(self, resolver, fake_mbs):
        expected = {"module-f28-build"}
        result = resolver.get_module_build_dependencies(
            "testmodule", "master", "20180205135154", "9c690d0e").keys()

        assert set(result) == expected

    def test_get_module_build_dependencies_from_mmd(
            self, resolver, fake_mbs, formatted_testmodule_mmd, platform_mmd
    ):
        loaded_platform_mmd = load_mmd(platform_mmd)

        fake_mbs.items = []
        add_item(
            fake_mbs.items,
            mmd=loaded_platform_mmd,
            koji_tag='module-f28-build'
        )
        # Test that duplicated koji tags are ignored
        add_item(
            fake_mbs.items,
            mmd=loaded_platform_mmd.copy('platform2', 'f28'),
            koji_tag='module-f28-build'
        )
        # Test that modules without koji tags (metadata modules) are ignored
        add_item(
            fake_mbs.items,
            mmd=loaded_platform_mmd.copy('metadata', 'f28'),
            koji_tag=None
        )

        mmd = formatted_testmodule_mmd.copy()
        xmd = mmd.get_xmd()
        xmd["mbs"]["buildrequires"].update({
            'platform2': {
                'name': 'platform2',
                'stream': 'f28',
                'version': '3',
                'context': '00000000',
            },
            'metadata': {
                'name': 'metadata',
                'stream': 'f28',
                'version': '3',
                'context': '00000000',
            },
        })
        mmd.set_xmd(xmd)

        add_item(fake_mbs.items, mmd=mmd, koji_tag=None)

        expected = {"module-f28-build"}
        result = resolver.get_module_build_dependencies(mmd=mmd)

        assert set(result) == expected

    def test_get_module_build_dependencies_local_module(
            self, resolver, fake_mbs, formatted_testmodule_mmd, local_builds
    ):
        load_local_builds(["platform:f28"])

        results = list(resolver.get_module_build_dependencies(mmd=formatted_testmodule_mmd).keys())
        assert len(results) == 1
        result = results[0]

        assert os.path.isabs(result)
        assert result.endswith('/staged_data/local_builds/module-platform-f28-3/results')

    def test_get_module_build_dependencies_missing_version(
            self, resolver, fake_mbs, formatted_testmodule_mmd
    ):
        with pytest.raises(RuntimeError,
                           match=r"The name, stream, version, and/or context weren't specified"):
            resolver.get_module_build_dependencies("testmodule", "master", None, "9c690d0e")

    def test_get_module_build_dependencies_bad_mmd(self, resolver, fake_mbs):
        fake_mbs.items = [dict(i) for i in (fake_mbs.items)]
        for i in fake_mbs.items:
            i["modulemd"] = None

        with pytest.raises(RuntimeError,
                           match=(r'The module "{.*}" did not contain its modulemd '
                                  r'or did not have its xmd attribute filled out in MBS')):
            resolver.get_module_build_dependencies(
                "testmodule", "master", "20180205135154", "9c690d0e")

    def test_get_module_build_dependencies_empty_buildrequires(
        self, resolver, fake_mbs, local_builds
    ):
        def modify(mmd):
            # Wipe out the dependencies
            for deps in mmd.get_dependencies():
                mmd.remove_dependencies(deps)
            xmd = mmd.get_xmd()
            xmd["mbs"]["buildrequires"] = {}
            mmd.set_xmd(xmd)

        fake_mbs.modify_item_mmd('testmodule:master:20180205135154:9c690d0e', modify)
        expected = set()

        resolver = mbs_resolver.GenericResolver.create(db_session, conf, backend="mbs")
        result = resolver.get_module_build_dependencies(
            "testmodule", "master", "20180205135154", "9c690d0e"
        ).keys()
        assert set(result) == expected

    def test_get_module_build_dependencies_no_context(
        self, resolver, fake_mbs, local_builds
    ):
        def modify(mmd):
            xmd = mmd.get_xmd()
            for name, details in xmd["mbs"]["buildrequires"].items():
                # Should be treated as 00000000
                del details["context"]
            mmd.set_xmd(xmd)

        fake_mbs.modify_item_mmd('testmodule:master:20180205135154:9c690d0e', modify)
        expected = {"module-f28-build"}

        resolver = mbs_resolver.GenericResolver.create(db_session, conf, backend="mbs")
        result = resolver.get_module_build_dependencies(
            "testmodule", "master", "20180205135154", "9c690d0e"
        ).keys()
        assert set(result) == expected

    def test_resolve_profiles(self, resolver, fake_mbs, formatted_testmodule_mmd):
        result = resolver.resolve_profiles(
            formatted_testmodule_mmd, ("buildroot", "srpm-buildroot")
        )
        expected = {
            "buildroot": {
                "unzip",
                "tar",
                "cpio",
                "gawk",
                "gcc",
                "xz",
                "sed",
                "findutils",
                "util-linux",
                "bash",
                "info",
                "bzip2",
                "grep",
                "redhat-rpm-config",
                "fedora-release",
                "diffutils",
                "make",
                "patch",
                "shadow-utils",
                "coreutils",
                "which",
                "rpm-build",
                "gzip",
                "gcc-c++",
            },
            "srpm-buildroot": {
                "shadow-utils",
                "redhat-rpm-config",
                "rpm-build",
                "fedora-release",
                "fedpkg-minimal",
                "gnupg2",
                "bash",
            },
        }

        assert result == expected

    def test_resolve_profiles_local_module(
            self, resolver, local_builds, formatted_testmodule_mmd
    ):
        load_local_builds(["platform:f28"])

        result = resolver.resolve_profiles(
            formatted_testmodule_mmd, ("buildroot", "srpm-buildroot"))
        expected = {"buildroot": {"foo"}, "srpm-buildroot": {"bar"}}
        assert result == expected

    def test_get_compatible_base_module_modulemds(
            self, resolver, fake_mbs, formatted_testmodule_mmd
    ):
        mmd = formatted_testmodule_mmd.copy('testmodule', 'f28.1.0')

        fake_mbs.required_params.update({
            'state': ['garbage', 'ready'],
            'stream_version_lte': 280100,
            'virtual_stream': ['f28'],
        })
        resolver.get_compatible_base_module_modulemds(mmd, True,
                                                      ['f28'], ['ready', 'garbage'])

    def test_get_compatible_base_module_modulemds_no_stream_version_lte(
            self, resolver, fake_mbs, formatted_testmodule_mmd
    ):
        mmd = formatted_testmodule_mmd.copy('testmodule', 'f28.1.0')

        fake_mbs.required_params.update({
            'state': ['garbage', 'ready'],
            'stream_version_lte': ABSENT,
            'virtual_stream': ['f28'],
        })
        resolver.get_compatible_base_module_modulemds(mmd, False,
                                                      ['f28'], ['ready', 'garbage'])

    @pytest.mark.parametrize('states,canonical_states', [
        ([module_build_service.common.models.BUILD_STATES['ready']], ['ready']),
        (None, ['ready']),
        (['ready', 'garbage'], ['garbage', 'ready']),
    ])
    def test_get_compatible_base_module_modulemds_canonicalize_state(
            self, resolver, fake_mbs, formatted_testmodule_mmd, states, canonical_states
    ):
        mmd = formatted_testmodule_mmd.copy('testmodule', 'f28.1.0')

        fake_mbs.required_params.update({
            'state': canonical_states,
            'stream_version_lte': 280100,
            'virtual_stream': ['f28'],
        })
        resolver.get_compatible_base_module_modulemds(mmd, True, ['f28'], states)

    def test_get_compatible_base_module_modulemds_no_virtual_stream(
            self, resolver, fake_mbs, formatted_testmodule_mmd
    ):
        mmd = formatted_testmodule_mmd.copy('testmodule', 'f28.1.0')
        with pytest.raises(RuntimeError, match=r"Virtual stream list must not be empty"):
            resolver.get_compatible_base_module_modulemds(mmd, True,
                                                          [], ['ready'])

    def test_get_compatible_base_module_modulemds_stream_not_xyz(
            self, resolver, fake_mbs, formatted_testmodule_mmd
    ):
        mmd = formatted_testmodule_mmd.copy('testmodule', 'f28')
        with pytest.raises(
                StreamNotXyz,
                match=(r"Cannot get compatible base modules, because stream "
                       r"of resolved base module testmodule:f28 is not in x\.y\.z format")
        ):
            resolver.get_compatible_base_module_modulemds(mmd, True,
                                                          ['f28'], ['ready'])

    def test_get_empty_buildrequired_modulemds(self, resolver, fake_mbs):
        platform = db_session.query(
            module_build_service.common.models.ModuleBuild).filter_by(id=1).one()
        result = resolver.get_buildrequired_modulemds("nodejs", "10", platform.mmd())
        assert [] == result

    @patch("module_build_service.resolver.MBSResolver.requests_session")
    def test_get_buildrequired_modulemds(self, mock_session):
        resolver = mbs_resolver.GenericResolver.create(db_session, conf, backend="mbs")
        mock_session.get.return_value = Mock(ok=True)
        mock_session.get.return_value.json.return_value = {
            "items": [
                {
                    "name": "nodejs",
                    "stream": "10",
                    "version": 1,
                    "context": "c1",
                    "modulemd": mmd_to_str(
                        tests.make_module("nodejs:10:1:c1"),
                    ),
                },
                {
                    "name": "nodejs",
                    "stream": "10",
                    "version": 2,
                    "context": "c1",
                    "modulemd": mmd_to_str(
                        tests.make_module("nodejs:10:2:c1"),
                    ),
                },
            ],
            "meta": {"next": None},
        }

        platform = db_session.query(
            module_build_service.common.models.ModuleBuild).filter_by(id=1).one()
        result = resolver.get_buildrequired_modulemds("nodejs", "10", platform.mmd())

        assert 1 == len(result)
        mmd = result[0]
        assert "nodejs" == mmd.get_module_name()
        assert "10" == mmd.get_stream_name()
        assert 1 == mmd.get_version()
        assert "c1" == mmd.get_context()

    @pytest.mark.parametrize('strict', (False, True))
    def test_get_module(self, resolver, fake_mbs, strict):
        module = resolver.get_module(
            "testmodule", "master", "20180205135154", "9c690d0e", strict=strict
        )
        assert module["version"] == "20180205135154"

        if strict:
            with pytest.raises(UnprocessableEntity):
                module = resolver.get_module(
                    "testmodule", "master", "12345", "9c690d0e", strict=strict
                )
        else:
            module = resolver.get_module(
                "testmodule", "master", "12345", "9c690d0e", strict=strict
            )
            assert module is None

    def test_get_module_cache(self, resolver, fake_mbs):
        for i in range(0, 2):
            resolver.get_module(
                "testmodule", "master", "20180205135154", "9c690d0e"
            )
        assert fake_mbs.request_count == 1

    def test_get_module_precache(self, resolver, fake_mbs):
        mmd = resolver.get_module_modulemds("testmodule", "master")[0]
        module = resolver.get_module(
            mmd.get_module_name(), mmd.get_stream_name(),
            mmd.get_version(), mmd.get_context()
        )
        assert int(module["version"]) == mmd.get_version()
        assert fake_mbs.request_count == 1

    @patch("module_build_service.resolver.MBSResolver.requests_session")
    def test_get_module_count(self, mock_session):
        mock_res = Mock()
        mock_res.json.return_value = {
            "items": [{"name": "platform", "stream": "f28", "version": "3", "context": "00000000"}],
            "meta": {"total": 5},
        }
        mock_session.get.return_value = mock_res

        resolver = mbs_resolver.GenericResolver.create(db_session, conf, backend="mbs")
        count = resolver.get_module_count(name="platform", stream="f28")

        assert count == 5
        mock_session.get.assert_called_once_with(
            "https://mbs.fedoraproject.org/module-build-service/1/module-builds/",
            params={"name": "platform", "page": 1, "per_page": 1, "short": True, "stream": "f28"},
        )

    @patch("module_build_service.resolver.MBSResolver.requests_session")
    def test_get_latest_with_virtual_stream(self, mock_session, platform_mmd):
        mock_res = Mock()
        mock_res.json.return_value = {
            "items": [
                {
                    "context": "00000000",
                    "modulemd": platform_mmd,
                    "name": "platform",
                    "stream": "f28",
                    "version": "3",
                }
            ],
            "meta": {"total": 5},
        }
        mock_session.get.return_value = mock_res

        resolver = mbs_resolver.GenericResolver.create(db_session, conf, backend="mbs")
        mmd = resolver.get_latest_with_virtual_stream("platform", "virtualf28")

        assert mmd.get_module_name() == "platform"
        mock_session.get.assert_called_once_with(
            "https://mbs.fedoraproject.org/module-build-service/1/module-builds/",
            params={
                "name": "platform",
                "order_desc_by": ["stream_version", "version"],
                "page": 1,
                "per_page": 1,
                "verbose": True,
                "virtual_stream": "virtualf28",
            },
        )

    def test_get_buildrequired_modulemds_local_builds(self, local_builds):
        with app.app_context():
            load_local_builds(["testmodule"])

            resolver = mbs_resolver.GenericResolver.create(db_session, conf, backend="mbs")
            result = resolver.get_buildrequired_modulemds(
                "testmodule", "master", "platform:f28:1:00000000")
            assert 1 == len(result)
            mmd = result[0]
            assert "testmodule" == mmd.get_module_name()
            assert "master" == mmd.get_stream_name()
            assert 20170816080816 == mmd.get_version()
            assert "321" == mmd.get_context()

    @patch("module_build_service.resolver.MBSResolver.requests_session")
    def test_get_buildrequired_modulemds_kojiresolver(self, mock_session):
        """
        Test that MBSResolver uses KojiResolver as input when KojiResolver is enabled for
        the base module.
        """
        mock_session.get.return_value = Mock(ok=True)
        mock_session.get.return_value.json.return_value = {
            "items": [
                {
                    "name": "nodejs",
                    "stream": "10",
                    "version": 2,
                    "context": "c1",
                    "modulemd": mmd_to_str(
                        tests.make_module("nodejs:10:2:c1"),
                    ),
                },
            ],
            "meta": {"next": None},
        }

        resolver = mbs_resolver.GenericResolver.create(db_session, conf, backend="mbs")

        platform = db_session.query(
            module_build_service.common.models.ModuleBuild).filter_by(id=1).one()
        platform_mmd = platform.mmd()
        platform_xmd = platform_mmd.get_xmd()
        platform_xmd["mbs"]["koji_tag_with_modules"] = "module-f29-build"
        platform_mmd.set_xmd(platform_xmd)

        with patch.object(
                resolver, "get_buildrequired_koji_builds") as get_buildrequired_koji_builds:
            get_buildrequired_koji_builds.return_value = [{
                "build_id": 124, "name": "nodejs", "version": "10",
                "release": "2.c1", "tag_name": "foo-test"}]
            result = resolver.get_buildrequired_modulemds("nodejs", "10", platform_mmd)
            get_buildrequired_koji_builds.assert_called_once()

        assert 1 == len(result)
        mmd = result[0]
        assert "nodejs" == mmd.get_module_name()
        assert "10" == mmd.get_stream_name()
        assert 2 == mmd.get_version()
        assert "c1" == mmd.get_context()

    def test_resolve_requires(self, resolver, fake_mbs):
        result = resolver.resolve_requires(["platform:f28:3:00000000", "testmodule:master"])
        result_skeleton = {
            k: "{stream}:{version}:{context}".format(**v) for k, v in result.items()
        }

        assert result_skeleton == {
            "platform": "f28:3:00000000",
            "testmodule": "master:20180205135154:9c690d0e",
        }

    def test_resolve_requires_bad_nsvc(self, resolver, fake_mbs):
        with pytest.raises(
                ValueError,
                match=r"Only N:S or N:S:V:C is accepted by resolve_requires, got platform"):
            resolver.resolve_requires(["platform"])

    def test_resolve_requires_no_commit_hash(self, resolver, fake_mbs):
        def modify(mmd):
            xmd = mmd.get_xmd()
            del xmd["mbs"]["commit"]
            mmd.set_xmd(xmd)

        fake_mbs.modify_item_mmd('testmodule:master:20180205135154:9c690d0e', modify)

        with pytest.raises(
                RuntimeError,
                match=(r"The module \"testmodule\" didn't contain "
                       r"both a commit hash and a version in MBS")):
            resolver.resolve_requires(["testmodule:master"])

    def test_resolve_requires_local_builds(self, resolver, local_builds, fake_mbs):
        load_local_builds(["platform:f30", "testmodule"])

        result = resolver.resolve_requires(["testmodule:master"])
        result_skeleton = {
            k: "{stream}:{version}:{context}".format(**v) for k, v in result.items()
        }

        assert result_skeleton == {
            "testmodule": "master:20170816080816:321"
        }

    def test_get_modulemd_by_koji_tag(self, resolver, fake_mbs):
        fake_mbs.required_params = {
            'verbose': True
        }
        mmd = resolver.get_modulemd_by_koji_tag("module-testmodule-master-20180205135154-9c690d0e")
        assert mmd.get_nsvc() == "testmodule:master:20180205135154:9c690d0e"

        mmd = resolver.get_modulemd_by_koji_tag("module-testmodule-master-1-1")
        assert mmd is None
