# Create your models here.
from django.conf import settings
from django.contrib.sites.models import Site
from django.db.models import CASCADE, ImageField, Model, OneToOneField
from django.utils.translation import gettext_lazy as _


def image_directory_path(instance, filename):
    return "{}/images/django_site/{}/{}".format(
        getattr(settings, "MEDIA_ROOT", "media"),
        getattr(instance, "id", "config"),
        filename,
    )


class Config(Model):
    """Config model is OneToOne related to Site model."""

    site = OneToOneField(
        Site,
        on_delete=CASCADE,
        primary_key=True,
        related_name="config",
        verbose_name=_("Site"),
    )

    favicon = ImageField(
        _("Favicon of site"),
        blank=True,
        null=True,
        upload_to=image_directory_path,
    )
    logo = ImageField(
        _("Logo of site"),
        blank=True,
        null=True,
        upload_to=image_directory_path,
    )
    dark_logo = ImageField(
        _("Dark Logo of site"),
        blank=True,
        null=True,
        upload_to=image_directory_path,
    )
    small_logo = ImageField(
        _("Small Logo of site"),
        blank=True,
        null=True,
        upload_to=image_directory_path,
    )
    mobile_logo = ImageField(
        _("Mobile logo of site"),
        blank=True,
        null=True,
        upload_to=image_directory_path,
    )

    class Meta:
        app_label = "sites"
        verbose_name = _("Site Config")
        verbose_name_plural = _("Site Configs")
        db_table = "django_site_config"

    def __str__(self):
        return self.site.name

    @property
    def favicon_url(self):
        """Return logo url"""
        return (
            settings.IMAGE_SETTINGS["ICON_DISPLAY"]
            if not self.favicon
            else getattr(self.favicon, "url")
        )

    @property
    def logo_url(self):
        """Return logo url"""
        return (
            settings.IMAGE_SETTINGS["LOGO_DISPLAY"]
            if not self.logo
            else getattr(self.logo, "url")
        )

    @property
    def dark_logo_url(self):
        """Return logo url"""
        return (
            settings.IMAGE_SETTINGS["LOGO_DISPLAY"]
            if not self.dark_logo
            else getattr(self.dark_logo, "url")
        )

    @property
    def small_logo_url(self):
        """Return logo url"""
        return (
            settings.IMAGE_SETTINGS["LOGO_DISPLAY"]
            if not self.small_logo
            else getattr(self.small_logo, "url")
        )

    @property
    def mobile_logo_url(self):
        """Return mobile_logo url"""
        return (
            settings.IMAGE_SETTINGS["LOGO_DISPLAY"]
            if not self.mobile_logo
            else getattr(self.mobile_logo, "url")
        )
