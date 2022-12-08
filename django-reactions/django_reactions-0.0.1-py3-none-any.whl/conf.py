from __future__ import annotations

from django.conf import settings


class Settings:
    """
    Shadow Django's settings with a little logic
    """
    @property
    def DJANGO_REACTION_USER_MODEL(self) -> str:
        return getattr(settings, "DJANGO_REACTION_USER_MODEL", settings.AUTH_USER_MODEL)
    
    @property
    def DJANGO_REACTION_MAX_CHARS(self) -> int:
        return getattr(settings, "DJANGO_REACTION_MAX_CHARS", 20)
    
    @property
    def DJANGO_REACTION_TYPES(self) -> str:
        return getattr(settings, "DJANGO_REACTION_TYPES", "django_reactions.enums.ReactionTypes")

    @property
    def DJANGO_REACTION_STATUS(self) -> str:
        return getattr(settings, "DJANGO_REACTION_STATUS", "django_reactions.enums.ReactionStatus")
    
    @property
    def DJANGO_REACTION_DEFAULT_TYPE(self) -> str:
        return getattr(settings, "DJANGO_REACTION_DEFAULT_TYPE", "LOVE")

    # DJANGO_REACTION_USER_MODEL = getattr(settings, 'DJANGO_REACTION_USER_MODEL', settings.AUTH_USER_MODEL)
    # DJANGO_REACTION_MAX_CHARS = getattr(settings, 'DJANGO_REACTION_TYPES', 20)
    # DJANGO_REACTION_TYPES = getattr(settings, 'DJANGO_REACTION_TYPES', None)
    # DJANGO_REACTION_DEFAULT_TYPE = getattr(settings, 'DJANGO_REACTION_DEFAULT_TYPE', 'LOVE')

def get_settings() -> Settings:
    return Settings()