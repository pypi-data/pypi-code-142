from admin_sync.test_utils import AbstractTests
from django.contrib.auth.models import User

from demoapp.admin import SyncUserAdmin


class aaaa(AbstractTests.AdminSyncTestCase):
    target = SyncUserAdmin

    def setUp(self):
        self.model_instance = User.objects.create(username="u2", is_staff=1, is_superuser=1)
        super().setUp()

