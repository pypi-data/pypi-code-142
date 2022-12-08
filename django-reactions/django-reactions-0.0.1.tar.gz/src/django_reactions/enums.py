from django.db import models

from django_reactions.conf import get_settings

Settings = get_settings()

class ReactionTypes(models.TextChoices):
    LOVE = 'LOVE', 'Love'
    HATE = 'HATE', 'Hate'
    WOW = 'WOW', 'Wow'
    COOL = 'COOL', 'Cool'
    THUMBS_UP = 'THUMBS_UP', 'Thumbs Up'
    THUMBS_DOWN = 'THUMBS_DOWN', 'Thumbs Down'

    @classmethod
    def get_default(cls):
        _default = Settings.DJANGO_REACTION_DEFAULT_TYPE
        if _default not in cls.values:
            err_msg = f"""
            DJANGO_REACTION_DEFAULT_TYPE must be one of the following values:
            {cls.values}
            {_default} is invalid.
            """
            raise ValueError(err_msg)
        return getattr(cls, _default)


class ReactionStatus(models.TextChoices):
    ACTIVE = 1, 'Active'
    INACTIVE = 0, 'Inactive'