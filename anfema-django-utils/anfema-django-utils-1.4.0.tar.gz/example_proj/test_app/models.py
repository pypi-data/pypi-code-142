from django.db import models

from anfema_django_utils.db.triggers import DenyFieldUpdateTrigger


class RelatedModel(models.Model):
    content = models.TextField(default="default content")


class DenyFieldUpdateTriggerTestModel(models.Model):
    set_once_flag = models.BooleanField()
    related_model = models.ForeignKey(RelatedModel, on_delete=models.PROTECT)
    content = models.TextField(default="default content")

    class Meta:
        constraints = (
            DenyFieldUpdateTrigger('set_once_flag', name='test_deny_set_once_flag_update'),
            DenyFieldUpdateTrigger('related_model_id', name='test_deny_related_model_id_update'),
        )
