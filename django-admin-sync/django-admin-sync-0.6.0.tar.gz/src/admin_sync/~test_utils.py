import json
from unittest.mock import Mock, patch

from django.test import TestCase, RequestFactory

from admin_sync.utils import SyncResponse, is_logged_to_remote


class AuthRequestFactory(RequestFactory):
    def request(self, **request):
        req = super().request(**request)
        from django.contrib.sessions.backends.base import SessionBase
        from django.contrib.messages.storage.fallback import FallbackStorage
        req.session = SessionBase()
        req._messages = FallbackStorage(req)
        req.user = Mock(is_authenticated=True)
        return req


class AbstractTests:
    class AdminSyncTestCase(TestCase):
        def setUp(self):
            from django.contrib.admin import site
            model = [key for key, value in site._registry.items() if value.__class__ == self.target]
            self.model_admin = site._registry[model[0]]

        def tearDown(self):
            # Clean up run after every test method.
            pass

        # def test_get_sync_data(self):
        #     request = AuthRequestFactory().post("/")
        #     data = self.model_admin.get_sync_data(request,
        #                                           self.model_admin.get_queryset(request)
        #                                           )
        #     assert json.loads(data)[0]['id'] == self.model_admin.id

        def test_contract(self):
            pass

        def test_receive(self):
            request = AuthRequestFactory().post("/")
            with patch('admin_sync.mixin.is_logged_to_remote', lambda *a: True):
                r = self.model_admin.get_qs_from_remote(self.model_admin,
                                                        request)
                assert r.content == ''

        def test_dump(self):
            request = AuthRequestFactory().get("/")
            response = self.model_admin.dumpdata_qs(self.model_admin, request)
            assert isinstance(response, SyncResponse)
            assert response.content
            assert response.json() is not None
