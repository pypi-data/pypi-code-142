# -*- encoding:utf-8 -*-
import six as six
from abc import ABCMeta, abstractmethod
from hermes.kdutils.lazy import LazyFunc
from hermes.kdutils.base import ParamBase, FreezeAttrMixin


class LongCallMixin(FreezeAttrMixin):
    """
        混入类，混入代表多头，不完全是期权中buy call的概念，
    """

    @LazyFunc
    def long_type_str(self):
        """用来区别多头类型unique 值为call"""
        return "long"

    @LazyFunc
    def expect_direction(self):
        """期望收益方向，1.0即正向期望"""
        return 1.0


class ShortMixin(FreezeAttrMixin):
    """
        混入类，混入代表空头，应用场景在于期权，期货策略中，
        不完全是期权中buy put的概念，只代看跌反向操作，
        即期望买入后交易目标价格下跌，下跌带来收益
    """

    @LazyFunc
    def short_type_str(self):
        """用来区别买入类型unique 值为put"""
        return "short"

    @LazyFunc
    def expect_direction(self):
        """期望收益方向，1.0即反向期望"""
        return -1.0


class FactorBase(six.with_metaclass(ABCMeta, ParamBase)):

    def __init__(self, **kwargs):
        # 子类继续完成自有的构造
        self._init_self(**kwargs)

    @abstractmethod
    def _init_self(self, **kwargs):
        """子类因子针对可扩展参数的初始化"""
        pass

    def _format(self, data, name):
        data = data.stack()
        data.name = name
        data.category = self.category
        return data

    def factors_list(self):
        return list(
            filter(
                lambda x: not x.startswith('_') and not x.islower() and
                callable(getattr(self, x)), dir(self)))
