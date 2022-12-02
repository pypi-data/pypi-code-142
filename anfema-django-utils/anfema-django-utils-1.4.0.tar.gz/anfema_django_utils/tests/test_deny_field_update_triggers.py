from unittest import SkipTest

from django.db import InternalError, connections
from django.test import TestCase

from anfema_django_utils.db.triggers import DenyFieldUpdateTrigger
from example_proj.test_app.forms import DenyFieldUpdateTriggerModelForm
from example_proj.test_app.models import DenyFieldUpdateTriggerTestModel, RelatedModel


class TestDenyFieldUpdateTrigger(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        db_vendor = connections['default'].vendor
        # TODO: make tests compatible with `mysql` (different exception on trigger violation)
        if db_vendor not in ('postgresql',):
            raise SkipTest(f"DenyFieldUpdateTrigger does not support the {db_vendor} db backend")
        super().setUpClass()

    @classmethod
    def setUpTestData(cls) -> None:
        cls.model_with_triggers = DenyFieldUpdateTriggerTestModel.objects.create(
            set_once_flag=True, related_model=RelatedModel.objects.create()
        )
        cls.model_form = DenyFieldUpdateTriggerModelForm()

    def test_save_changed_unrelated_field_succeeds(self):
        self.model_with_triggers.content = "new content"
        self.model_with_triggers.save()

    def test_save_changed_set_once_flag_fails(self):
        self.model_with_triggers.set_once_flag = False
        with self.assertRaisesMessage(InternalError, "Direct update of “set_once_flag” is forbidden."):
            self.model_with_triggers.save()

    def test_update_changed_set_once_flag_fails(self):
        with self.assertRaisesMessage(InternalError, "Direct update of “set_once_flag” is forbidden."):
            DenyFieldUpdateTriggerTestModel.objects.update(set_once_flag=False)

    def test_save_changed_related_model_fails(self):
        self.model_with_triggers.related_model = RelatedModel.objects.create()
        with self.assertRaisesMessage(InternalError, "Direct update of “related_model_id” is forbidden."):
            self.model_with_triggers.save()

    def test_update_changed_related_model_fails(self):
        new_related_model = RelatedModel.objects.create()
        with self.assertRaisesMessage(InternalError, "Direct update of “related_model_id” is forbidden."):
            DenyFieldUpdateTriggerTestModel.objects.update(related_model=new_related_model)

    def test_form_validation(self):
        model_form = DenyFieldUpdateTriggerModelForm(
            {
                'set_once_flag': False,  # invalid change
                'content': 'content',
                'related_model': self.model_with_triggers.related_model_id,
            },
            instance=self.model_with_triggers,
        )
        error_msg = DenyFieldUpdateTrigger.default_violation_error_message % {'name': 'test_deny_set_once_flag_update'}
        self.assertFormError(model_form, field=None, errors=[error_msg])
