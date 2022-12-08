from django.db import models
from djangoldp.models import Model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from ..views.needle_activity import create_welcome_needle_activity


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_user(sender, instance, created, **kwargs):
    print(sender)
    print("USERPROFILE1: {0} with id {1}".format(instance, instance.pk))
    if created and not Model.is_external(instance):
        create_welcome_needle_activity(instance);
