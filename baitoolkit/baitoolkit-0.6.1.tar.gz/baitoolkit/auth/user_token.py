# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
from flask_login import AnonymousUserMixin, UserMixin


class UserToken(UserMixin):

    def __init__(self, user_id, account=None, preferred_language=None, preferred_timezone=None):
        self._user_id = user_id
        self._account = account if account is not None else user_id
        self._preferred_language = preferred_language
        self._preferred_timezone = preferred_timezone

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self._user_id

    @property
    def preferred_language(self):
        return self._preferred_language

    @property
    def preferred_timezone(self):
        return self._preferred_timezone


class AnonymousUser(UserToken, AnonymousUserMixin):

    def __init__(self, preferred_language=None, preferred_timezone=None):
        super(AnonymousUser, self).__init__('anonymous', account='anonymous',
                                            preferred_language=preferred_language,
                                            preferred_timezone=preferred_timezone)
