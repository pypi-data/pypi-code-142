# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
from flask import Flask
from flask_login import LoginManager, current_user

from baitoolkit.auth import auth_constant
from baitoolkit.auth.user_token import AnonymousUser
from baitoolkit.common import logger_factory, security
from baitoolkit.exception.errors import BaseError
from baitoolkit.web import blueprint, req_util

__logger = logger_factory.get_logger(__name__)


class AuthorizationError(BaseError):
    def __init__(self, it):
        super(AuthorizationError, self).__init__(it=it)

    @staticmethod
    def template():
        return "You don't have permission to access {{it}}."


def load_user(user_id):
    """Load User from request or session"""
    # first, try to login using Basic Auth
    api_key = req_util.get_request_head(auth_constant.AUTH_HEAD_NAME)
    if api_key is None:
        user = AnonymousUser()
        return user
    # next, try to login using the session
    # finally, return None if both methods did not login the user
    return None


def __generate_salt(key):
    """generate salt"""
    value = security.str_to_sha1_hex(key)
    value += '@#$6￥%^$2d*x&.;1'
    return security.str_to_sha256_hex(value)


def unpack_authorization(secret_key, max_age=auth_constant.AUTH_MAX_AGE):
    """
    Return authorization from request head.
    :param str secret_key: the secret to un-sign object.
    :param int max_age: the alive period. unit: second.
    """

    authorization = blueprint.get_request_head(auth_constant.AUTH_HEAD_NAME)
    if authorization is None:
        return None
    try:
        authorization = security.unsign_object(secret_key, authorization, max_age=max_age,
                                               salt=__generate_salt(secret_key))
    except BaseException as e:
        logger.error('Failed to un-sign object due to %s' % str(e))
        authorization = None
    return authorization


def generate_authorization(secret_key, data):
    """
    Generate authorization.
    :param str secret_key:
    :param object data: the object that can be jsonified.
    """
    return security.sign_object(secret_key, data, salt=__generate_salt(secret_key))


def init_login_manager(app: Flask):
    """init login manager function"""
    login_manager = LoginManager()
    login_manager.request_loader(load_user)
    login_manager.session_protection = "strong"
    login_manager.init_app(app)
    return login_manager


def current_user_token():
    """Return current user."""
    return current_user


def current_user_id():
    """Return current user id."""
    return current_user_token().user_id
