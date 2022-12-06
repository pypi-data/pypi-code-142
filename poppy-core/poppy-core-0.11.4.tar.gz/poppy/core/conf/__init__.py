#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['settings']

from poppy.core.generic.metaclasses import Singleton
from . import default_settings as default_settings


class Settings(object, metaclass=Singleton):

    def __init__(self):
        # since this class is a singleton, the init method will only be called once
        self.configure(default_settings)

    def configure(self, settings_obj):
        """
        Update the settings using a settings module or dict
        """
        if isinstance(settings_obj, dict):
            self.from_dict(settings_obj)
        else:
            self.from_module(settings_obj)

    def from_module(self, settings_module):
        # update this dict from settings module (but only for ALL_CAPS settings)
        for setting in dir(settings_module):
            if setting.isupper():
                setattr(self, setting, getattr(settings_module, setting))

    def from_dict(self, settings_dict):
        # update this dict from settings module (but only for ALL_CAPS settings)
        for key, setting in settings_dict.items():
            if key.isupper():
                setattr(self, key, setting)
            else:
                raise Exception(f'The keys of a settings dictionary have to be in upper case (found: {key})')


settings = Settings()
