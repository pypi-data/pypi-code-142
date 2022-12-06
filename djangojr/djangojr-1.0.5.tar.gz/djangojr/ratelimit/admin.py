from django.contrib import admin
from .models import RateLimit


@admin.register(RateLimit)
class RateLimitAdmin(admin.ModelAdmin):
    list_display = ["user", "ip", "count",
                    "blocked", "blocked_at", "created_at",]
    search_fields = ("user__username", "ip")
    autocomplete_fields = ["user"]
