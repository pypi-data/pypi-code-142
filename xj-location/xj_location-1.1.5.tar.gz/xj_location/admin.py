from django.contrib import admin

from .models import Location, Boundary


class LocationManager(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'region_code', 'address', 'name', 'longitude', 'latitude', 'user_id', 'thread_id', 'created_time']
    fields = ['region_code', 'address', 'name', 'longitude', 'latitude', 'user_id', 'thread_id', 'created_time']


class BoundaryManager(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'name', 'created_at']
    search_fields = ['name']


admin.site.register(Location, LocationManager)
admin.site.register(Boundary, BoundaryManager)
