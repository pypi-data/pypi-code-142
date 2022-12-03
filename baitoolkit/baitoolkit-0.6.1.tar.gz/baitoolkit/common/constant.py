# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""

from baitoolkit.common import type_util


class ConstBase(object):
    """The basic class of constant."""

    @classmethod
    def get(cls, key):
        return cls.__dict__.get(key)

    @classmethod
    def keys(cls):
        consts = list()
        for k, v in cls.__dict__.items():
            if k.startswith('_') or isinstance(v, (classmethod, staticmethod)):
                continue
            consts.append(k)
        return consts

    @classmethod
    def values(cls):
        consts = list()
        for k, v in cls.__dict__.items():
            if k.startswith('_') or isinstance(v, (classmethod, staticmethod)):
                continue
            consts.append(v)
        return consts

    @classmethod
    def items(cls, qualifier=False) -> dict:
        """Return all key-values."""
        consts = dict()
        for k, v in cls.__dict__.items():
            if k.startswith('_') or isinstance(v, (classmethod, staticmethod)):
                continue
            if qualifier:
                k = '{}-{}'.format(cls.__name__, k)
            consts[k] = v
        return consts

    @classmethod
    def localized_items(cls):
        from baitoolkit.common.localization import gettext
        cls._localized_items(gettext)

    @classmethod
    def _localized_items(cls, t_) -> dict:
        """If showing in UI, should override this method in sub-class."""
        return cls.items(qualifier=False)



def fetch_all_consts(qualifier=False):
    """fetch all constants.
    :param bool qualifier: attaching the complete class name to CONSTANT NAME or not.
    """
    constants = dict()
    for clazz in ConstBase.sub_classes():
        consts = clazz.items(qualifier=qualifier)
        type_util.dict_merge(constants, consts)
    return constants


class YesNo(ConstBase):
    Yes = 'Y'
    No = 'N'

    @classmethod
    def _localized_items(cls, t_) -> dict:
        return {
            cls.Yes: t_('是'),
            cls.No: t_('否')
        }
