import importlib
from functools import lru_cache

from django.db import models

from django_reactions.conf import get_settings

Settings = get_settings()


class Loader:
    @classmethod
    def get_reaction_type(cls):
        DJANGO_REACTION_TYPES = Settings.DJANGO_REACTION_TYPES
        if DJANGO_REACTION_TYPES is None:
            err_msg = f"""
            DJANGO_REACTION_TYPES cannot be set as None be set in your settings.
            """
            raise ValueError(err_msg)
        if isinstance(DJANGO_REACTION_TYPES, models.TextChoices):
            err_msg = f"""
            DJANGO_REACTION_TYPES must be a path to a subclass models.TextChoices.
            {DJANGO_REACTION_TYPES} is invalid.
            """
            raise ValueError(err_msg)
        module, class_name = DJANGO_REACTION_TYPES.rsplit(".", 1)
        return getattr(importlib.import_module(module), class_name)

    @classmethod
    def get_reaction_status(cls):
        DJANGO_REACTION_STATUS = Settings.DJANGO_REACTION_STATUS
        if DJANGO_REACTION_STATUS is None:
            err_msg = f"""
            DJANGO_REACTION_STATUS cannot be set as None be set in your settings.
            """
            raise ValueError(err_msg)
        if isinstance(DJANGO_REACTION_STATUS, models.TextChoices):
            err_msg = f"""
            DJANGO_REACTION_STATUS must be a path to a subclass models.Text
            {DJANGO_REACTION_STATUS} is invalid.
            """
            raise ValueError(err_msg)
        module, class_name = DJANGO_REACTION_STATUS.rsplit(".", 1)
        return getattr(importlib.import_module(module), class_name)


ReactionStatus = Loader.get_reaction_status()
ReactionType = Loader.get_reaction_type()