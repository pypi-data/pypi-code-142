from django.contrib.sites.models import Site
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_site.models import Config


@receiver(post_save, sender=Site)
def create_or_update_site_config(sender, instance, **kwargs):
    """This signal creates/updates a Config object
    after creating/updating a Site object.
    """
    config, created = Config.objects.update_or_create(site=instance)
    if not created:
        config.save()
