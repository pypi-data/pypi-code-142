from django.contrib import admin
from .models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ["user", "token", "created_at"]
    search_fields = ("user__username", "token")
    autocomplete_fields = ["user"]
