# Register your models here.
from django.contrib import admin
from django.contrib.sites.models import Site

from django_site.models import Config

admin.site.unregister(Site)


class ConfigInline(admin.StackedInline):
    model = Config
    can_delete = False


class SiteAdmin(admin.ModelAdmin):
    list_display = ("domain", "name")
    search_fields = ("domain", "name")
    inlines = (ConfigInline,)
    list_filter = ("domain", "name")


admin.site.register(Site, SiteAdmin)
