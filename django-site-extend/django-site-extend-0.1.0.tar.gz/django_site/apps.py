from django.apps import AppConfig
from django.db.models.signals import post_migrate

from django_site import APP_LABEL


def create_default_site_config(sender, **kwargs):
    """after migrations"""
    from django.contrib.sites.models import Site

    from django_site.models import Config

    sites = Site.objects.all()
    for site in sites:
        if not Config.objects.filter(site=site).exists():
            Config.objects.create(site=site)


class DjangoSiteConfig(AppConfig):
    name = "django_site"
    verbose_name = APP_LABEL

    def ready(self):
        post_migrate.connect(create_default_site_config, sender=self)
        try:
            import django_site.signals  # noqa F401
        except ImportError:
            pass
