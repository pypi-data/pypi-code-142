# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""

import base64
from hashlib import md5, sha1, sha256, sha512

from itsdangerous import URLSafeTimedSerializer
from werkzeug import security

from baitoolkit.common import type_util
from baitoolkit.exception import assert_util

"""
    Encrypt and decrypt utilities
"""


def str_to_md5_hex(content, salt=None):
    md = md5()
    content1 = type_util.unicode_bytes(content)
    md.update(content1)
    hd = md.hexdigest()
    if salt is not None:
        hd = str_to_md5_hex(hd+salt)
    return hd


def str_to_sha1_hex(content, salt=None):
    sha = sha1()
    content1 = type_util.unicode_bytes(content)
    sha.update(content1)
    sha = sha.hexdigest()
    if salt is not None:
        sha = str_to_sha1_hex(sha+salt)
    return sha


def str_to_sha256_hex(content, salt=None):
    sha = sha256()
    content1 = type_util.unicode_bytes(content)
    sha.update(content1)
    sha = sha.hexdigest()
    if salt is not None:
        sha = str_to_sha256_hex(sha+salt)
    return sha


def str_to_sha512_hex(content, salt=None):
    sha = sha512()
    content1 = type_util.unicode_bytes(content)
    sha.update(content1)
    sha = sha.hexdigest()
    if salt is not None:
        sha = str_to_sha512_hex(sha+salt)
    return sha


def file_to_md5_hex(file_path):
    md = md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md.update(chunk)
        f.close()
    md = md.hexdigest()
    return md


def file_to_sha1_hex(file_path):
    sha = sha1()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha.update(chunk)
        f.close()
    sha = sha.hexdigest()
    return sha


def file_to_sha256_hex(file_path):
    sha = sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha.update(chunk)
        f.close()
    sha = sha.hexdigest()
    return sha


def str_to_base64(value, urlsafe=True):
    """Encode string to base64"""
    value = type_util.unicode_bytes(value)
    val = base64.urlsafe_b64encode(value) if urlsafe else base64.encodebytes(value)
    val = type_util.unicode_str(val)
    return val


def base64_to_str(value, urlsafe=True):
    """Decode base64 string."""
    value = type_util.unicode_str(value)
    value = base64.urlsafe_b64decode(value) if urlsafe else base64.decodebytes(value)
    value = value.decode()
    return value


def sign_object(key, obj, salt=None):
    """
    Sign an object to a string.
    :param str key: the password to be used in the signature.
    :param object obj: the object can be json serialized.
    :param str salt: the salt to be used when sign.
    :return:
    """
    assert_util.assert_required(obj, 'object')
    assert_util.assert_range(len(key), 16, 64, 'key')
    string = type_util.obj_to_json(obj)
    string = type_util.str_compress(string)
    signer = URLSafeTimedSerializer(key, salt=salt)
    string1 = signer.dumps(string)
    return string1


def unsign_object(key, string, salt=None, max_age=5):
    """
    UnSign a string to an object.
    :param str key: the password to be used in the signature.
    :param str string: the string to be unsign.
    :param str salt: the salt to be used when un-sign.
    :param int max_age: ensure the signature is not older than this time in seconds.
    :return object:
    """
    assert_util.assert_required(string, 'string')
    assert_util.assert_range(len(key), 16, 64, 'key')
    signer = URLSafeTimedSerializer(key, salt=salt)
    string = signer.loads(string, max_age=max_age)
    string = type_util.str_decompress(string)
    obj = type_util.json_to_object(string)
    return obj


def hash_password(password):
    """
    Encrypt password
    :param str password:
    :return:
    """
    return security.generate_password_hash(password)


def check_password(pw_hash, password):
    """
    Check password is correct.
    :param str pw_hash:
    :param str password:
    :return:
    """
    return security.check_password_hash(pw_hash, password)

