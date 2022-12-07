import datetime
import warnings
import numpy as np
from typing import Union, Literal
from ptrade import component
from ptrade import exception
import paux.order
import paux.date
import paux.candle.transform


class Simulate():
    def __init__(
            self,
            candle,
            rule: component.RuleChinaStock,
            instId=None,
    ):
        # 参数与内置模块
        self.candle = candle  # K线数据
        self.rule = rule  # 规则
        self.instId = instId  # 标底
        self._order = component.Order(accountMoney=rule.ACCOUNT_MONEY)  # 订单模块
        # 当前K线单位时间内
        self.index = np.nan  # 被遍历的candle行索引
        self.open = np.nan  # 开盘价
        self.low = np.nan  # 最低价
        self.high = np.nan  # 最高价
        self.close = np.nan  # 收盘价
        self.ts = np.nan  # 开盘时刻的毫秒级时间戳
        # 当前时刻
        self.datetime = None
        self.date = None
        self.time = None
        # 前一天的数据
        self.last_day_open = np.nan  # 昨日开盘价
        self.last_day_high = np.nan  # 昨日最高价
        self.last_day_low = np.nan  # 昨日最低价
        self.last_day_close = np.nan  # 昨日收盘价

        self.setup()

    # 用户重写 --------------------------------------------------------------------------------------------
    def setup(self):
        # do something
        pass

    def sell(self):
        # do something
        pass

    def buy(self):
        # do something
        pass

    # 属性 ------------------------------------------------------------------------------------------------
    '''
    1. 账户金额预估
    2. 
    '''

    # 余额 ------------------------------------------------------------------------------------------------
    # 账户可用余额
    @property
    def accountMoney(self):
        return self._order.accountMoney

    @accountMoney.setter
    def accountMoney(self, value):
        self._order.accountMoney = value

    # 持仓余额估计
    @property
    def positionAccountMoney(self):
        accountMoney_in_position = 0
        for orderData in self._order.currentOrderDatas:
            sellMoney = paux.order.get_commission_data(
                posSide=orderData['posSide'],
                buyMoney=orderData['buyMoney'],
                buyLine=orderData['buyLine'],
                sellLine=orderData['sellLine'],
                lever=orderData['lever'],
                buyCommissionRate=self.rule.BUY_COMMISSION_RATE,
                sellCommissionRate=self.rule.SELL_COMMISSION_RATE,
            )['sellMoney']
            accountMoney_in_position += sellMoney
        return accountMoney_in_position

    # 多单持仓余额估计
    @property
    def longPositionAccountMoney(self):
        accountMoney_in_position = 0
        for orderData in self._order.currentOrderDatas:
            if orderData['posSide'] != 'long':
                continue
            sellMoney = paux.order.get_commission_data(
                posSide=orderData['posSide'],
                buyMoney=orderData['buyMoney'],
                buyLine=orderData['buyLine'],
                sellLine=orderData['sellLine'],
                lever=orderData['lever'],
                buyCommissionRate=self.rule.BUY_COMMISSION_RATE,
                sellCommissionRate=self.rule.SELL_COMMISSION_RATE,
            )['sellMoney']
            accountMoney_in_position += sellMoney
        return accountMoney_in_position

    # 空单持仓余额估计
    @property
    def shortPositionAccountMoney(self):
        accountMoney_in_position = 0
        for orderData in self._order.currentOrderDatas:
            if orderData['posSide'] != 'short':
                continue
            sellMoney = paux.order.get_commission_data(
                posSide=orderData['posSide'],
                buyMoney=orderData['buyMoney'],
                buyLine=orderData['buyLine'],
                sellLine=orderData['sellLine'],
                lever=orderData['lever'],
                buyCommissionRate=self.rule.BUY_COMMISSION_RATE,
                sellCommissionRate=self.rule.SELL_COMMISSION_RATE,
            )['sellMoney']
            accountMoney_in_position += sellMoney
        return accountMoney_in_position

    # 订单数据---------------------------------------------------------------------------------------------

    # 持仓订单数据
    @property
    def currentOrderDatas(self):
        return self._order.currentOrderDatas

    @currentOrderDatas.setter
    def currentOrderDatas(self, value):
        self._order.currentOrderDatas = value

    # 持仓多单数据
    @property
    def currentLongOrderDatas(self):
        return [
            orderData for orderData in self._order.currentOrderDatas if orderData['posSide'] == 'long'
        ]

    # 持仓空单数据
    @property
    def currentShortOrderDatas(self):
        return [
            orderData for orderData in self._order.currentOrderDatas if orderData['posSide'] == 'short'
        ]

    @property
    def currentOrderDatasCanBeTraded(self):
        if self.rule.T == 0:
            return self.currentOrderDatas
        dateCanBeTrade = self.date + datetime.timedelta(days=self.rule.T)

        orderDatas = []
        for orderData in self.currentOrderDatas:
            if dateCanBeTrade >= orderData['orderDatetime'].date():
                orderDatas.append(orderData)
        return orderDatas

    @property
    def currentLongOrderDatasCanBeTraded(self):
        return [
            orderData for orderData in self.currentOrderDatasCanBeTraded if orderData['posSide'] == 'long'
        ]

    @property
    def currentShortOrderDatasCanBeTraded(self):
        return [
            orderData for orderData in self.currentOrderDatasCanBeTraded if orderData['posSide'] == 'short'
        ]

    # 历史订单数据
    @property
    def historyOrderDatas(self):
        return self._order.historyOrderDatas

    @historyOrderDatas.setter
    def historyOrderDatas(self, value):
        self._order.historyOrderDatas = value

    # 历史多单数据
    @property
    def historyLongOrderDatas(self):
        return [
            orderData for orderData in self._order.historyOrderDatas if orderData['posSide'] == 'long'
        ]

    # 历史空单数据
    @property
    def historyShortOrderDatas(self):
        return [
            orderData for orderData in self._order.historyOrderDatas if orderData['posSide'] == 'short'
        ]

    # 仓位数量---------------------------------------------------------------------------------------------
    # 当前仓位总数
    @property
    def currentPosition(self):
        '''
        获得持仓的总订单数量
        :return:int
        '''
        return self._order.currentPosition

    # 当前多仓数量
    @property
    def currentLongPosition(self):
        '''
        获得持仓的多单数量
        :return:int
        '''
        return self._order.currentLongPosition

    # 当前空仓数量
    @property
    def currentShortPosition(self):
        '''
        获得持仓的空单数量
        :return:int
        '''
        return self._order.currentShortPosition

    # 剩余多仓数量
    @property
    def longPositionLeft(self):
        longPositionLeft = min(
            self.rule.LONG_POSITION - self.currentLongPosition,
            self.rule.POSITION - self.currentPosition,
        )
        return longPositionLeft

    # 剩余空仓数量
    @property
    def shortPositionLeft(self):
        # 剩余仓位数量
        shortPositionLeft = min(
            self.rule.SHORT_POSITION - self.currentShortPosition,
            self.rule.POSITION - self.currentPosition,
        )
        return shortPositionLeft

    # 记录数据---------------------------------------------------------------------------------------------
    def record(self):
        '''
        更新:
        1. 每个时刻的价格数据
        2. 每日开盘价
        3. 昨日的开盘、最高、最低与收盘价
        '''
        # 当前颗粒度中的数据
        self.ts = self.candle[self.index, 0]  # 开盘时刻毫秒级时间戳
        self.open = self.candle[self.index, 1]  # 开盘价格
        self.high = self.candle[self.index, 2]  # 最高价格
        self.low = self.candle[self.index, 3]  # 最低价格
        self.close = self.candle[self.index, 4]  # 收盘价格
        self.volume = self.candle[self.index, 5]  # 交易数量
        self.datetime = paux.date.to_datetime(
            date=self.ts,
            timezone=self.rule.TIMEZONE,
        )

        self.date = self.datetime.date()
        self.time = self.datetime.time()

        if not hasattr(self, 'last_date'):
            self.__last_date = self.date
            self.last_date = None
            self.last_day_open = np.nan  # 昨日开盘价
            self.last_day_high = np.nan  # 昨日最高价
            self.last_day_low = np.nan  # 昨日最低价
            self.last_day_close = np.nan  # 昨日收盘价
            self.last_day_volume = np.nan  # 昨日成交额

        if self.date != self.__last_date:
            self.last_date = self.__last_date
            self.__last_date = self.date
            self.this_day_open = self.open  # 今日开盘价
            last_day_open_ts = paux.date.to_ts(
                date=self.last_date,
                timezone=self.rule.TIMEZONE,
            )
            last_day_close_ts = last_day_open_ts + 1000 * 60 * 60 * 24

            last_day_candle = self.candle[
                (self.candle[:, 0] >= last_day_open_ts) & (self.candle[:, 0] < last_day_close_ts)
                ]
            self.last_day_open = last_day_candle[0, 1]  # 昨日开盘价
            self.last_day_high = last_day_candle[:, 2].max()  # 昨日最高价
            self.last_day_low = last_day_candle[:, 3].min()  # 昨日最低价
            self.last_day_close = last_day_candle[:, 4]  # 昨日收盘价

    # 开仓订单---------------------------------------------------------------------------------------------
    def start_orderData(
            self,
            buyLine: Union[int, float],
            buyMoney: Union[int, float],
            posSide: Literal['long', 'short'],
            buyCommissionRate: Union[int, float, Literal['rule']] = 'rule',
            lever: Union[int, Literal['rule']] = 'rule',
            tpRate: Union[int, float, Literal['rule']] = 'rule',
            tpLine: Union[int, float, None] = None,
            slRate: Union[int, float, Literal['rule']] = 'rule',
            slLine: Union[int, float, None] = None,
            orderType: object = None,
            toMode: Literal['isolated', 'cross'] = 'isolated',
            priority=100,
            **kwargs
    ):
        '''
        发起订单
        :param posSide:持仓方向
            posSide='long'  多单
            posSide='short' 空单
        :param lever:杠杆
        :param buyLine:购买价格
        :param buyMoney:购买金额
        :param tpRate:止盈率，
            tpRate='rule'   使用rule中的止盈率
            tpRate=0.5      止盈率为50%
        :param tpLine:止赢价格，相当于挂单价格
            止赢优先级：  tpLine > tpRate
                        tpLine=None，使用tpRate
                        tpLine!=None,不适用tpRate
        :param slRate:
            slRate='rule'   使用rule中的止损率
            slRate=-0.5     止损率为50%
        :param slLine:止损价格
            止赢优先级：  slLine > slRate
                        slLine=None，使用slRate
                        slLine!=None,不适用slRate
        :param orderType:订单类型
        :param toMode:
            toMode = 'isolated' 逐仓
            toMode = 'cross'    全仓
        :param kwargs:补充参数
        注意：
        1. 止盈与止损
            如果止盈卖出，多单的卖出价格一定不会低于止盈价格，空单的卖出价格一定不会高于止盈价格
            如果止损卖出，亏损率一定不会低于止损率
        2. 全仓与逐仓
            逐仓有强制平仓价格，全仓没有
        3. 补充的辅助字段有：
            1. orderIndex
            2. orderTs
            3. smLine(stock market): 强制平仓价格，仅逐仓使用，为逐仓亏损100%的标记价格，全仓不设置强制平仓价格
        :return:
        '''
        # 杠杆
        if lever == 'rule':
            if posSide == 'long':
                lever = self.rule.LONG_LEVER
            elif posSide == 'short':
                lever = self.rule.SHORT_LEVER
            else:
                raise exception.PosSideParamError(posSide)
        # 止盈率
        if tpRate == 'rule':
            if posSide == 'long':
                tpRate = self.rule.LONG_TP_RATE
            elif posSide == 'short':
                tpRate = self.rule.SHORT_TP_RATE
        # 止损率
        if slRate == 'rule':
            if posSide == 'long':
                slRate = self.rule.LONG_SL_RATE
            elif posSide == 'short':
                slRate = self.rule.SHORT_SL_RATE
        # 当前订单的candle行索引
        orderIndex = self.index
        buyLine = paux.order.round_simulate(np.clip(buyLine, self.low, self.high))

        if buyCommissionRate == 'rule':
            buyCommissionRate = self.rule.BUY_COMMISSION_RATE
        return self._order.start_orderData(
            orderType=orderType,
            instId=self.instId,
            lever=lever,
            toMode=toMode,
            posSide=posSide,
            buyMoney=buyMoney,
            # orderDatetime=self.datetime.strftime('%Y-%m-%d %H:%M:%S'),
            orderDatetime=self.datetime,
            buyLine=buyLine,
            buyCommissionRate=buyCommissionRate,
            tpLine=tpLine,
            tpRate=tpRate,
            slLine=slLine,
            slRate=slRate,
            orderTs=self.ts,  # 补充字段
            orderIndex=orderIndex,  # 补充字段
            priority=priority,  # 优先级
            **kwargs,
        )

    # 平仓订单---------------------------------------------------------------------------------------------
    def close_orderData(
            self,
            orderData: dict,
            sellLine: Union[int, float],
            sellCommissionRate: Union[int, float, Literal['rule']] = 'rule',
            endType: object = None,
            priority=50,
            **kwargs
    ):
        '''
        结束订单
        :param orderData:订单对象
        :param sellLine:卖出价格
        :param commissionRate:手续费率
            commissionRate = 'rule'    使用rule中的手续费率
            commissionRate = 0.001     手续费为交易价格的0.1%
        :param endType:结束类型
        :param kwargs:补充参数
        辅助字段：
            endIndex
            endTs
        通过计算产生的字段：
            commission  手续费 float
            holdMinute  从订单开始到订单结束的时间，单位分钟 int
            sellMoney   卖出的金额（包含抛出） float
            profitRate  利润率 float
            profit      利润 float
        补充的过程数据：
            hh          订单开始到订单终止的最大价格 float
            hhRate      订单开始到订单终止的最大涨幅 float
            ll          订单开始到订单终止的最小价格 float
            llRate      订单开始到订单终止的最大跌幅 float
        '''
        # 手续费
        if sellCommissionRate == 'rule':
            sellCommissionRate = self.rule.SELL_COMMISSION_RATE
        # 开始与终止索引
        endIndex = self.index
        orderIndex = orderData['orderIndex']
        # 过程中的最高价与最低价
        if orderIndex != endIndex:
            hh = self.candle[orderIndex:endIndex, 2].max()
            ll = self.candle[orderIndex:endIndex, 3].min()
        else:
            hh = self.candle[endIndex, 2]
            ll = self.candle[endIndex, 3]
        hhRate = round((hh - orderData['buyLine']) / orderData['buyLine'], 4)
        llRate = round((ll - orderData['buyLine']) / orderData['buyLine'], 4)
        return self._order.close_orderData(
            orderData=orderData,
            sellLine=sellLine,
            # endDatetime=self.datetime.strftime('%Y-%m-%d %H:%M:%S'),
            endDatetime=self.datetime,
            sellCommissionRate=sellCommissionRate,
            endType=endType,
            # 补充的字段
            endIndex=endIndex,
            endTs=self.ts,
            hh=hh,
            hhRate=hhRate,
            ll=ll,
            llRate=llRate,
            priority=priority,
            **kwargs
        )

    # 多种平仓方式---------------------------------------------------------------------------------------------
    # 止盈止损卖出
    def tpSell_and_slThrow(self):
        '''
        止盈卖出与止损抛出
            悲观策略：如果单位时间内价格剧烈波动，同时达到止盈与止损条件，以止损价格抛出
            止盈价格与止损价格并不一定是实际的卖出价格
            止盈卖出：endType = 'TP'
            止损抛出：endType = 'SL'
        '''
        priority = 50  # 优先级
        if not paux.date.is_period_allowed(
                date=self.time,
                periods=self.rule.SELL_PERIODS,
                timezone=self.rule.TIMEZONE,
        ):
            return None
        # 止盈卖出与止损抛出
        for orderData in self.currentOrderDatasCanBeTraded:
            posSide = orderData['posSide']
            # 如果达到了止损条件
            # 多单：最小价<=止损价格；空单：最大价格>=止损价格
            if orderData['slLine'] and (
                    (posSide == 'long' and self.low <= orderData['slLine']) or
                    (posSide == 'short' and self.high >= orderData['slLine'])):
                # 多单实际止损价格
                if posSide == 'long':
                    realSlLine = min(self.open, orderData['slLine'])
                # 空单实际止损价格
                elif posSide == 'short':
                    realSlLine = max(self.open, orderData['slLine'])
                else:
                    raise exception.PosSideParamError(posSide)
                # 平仓
                orderData = self.close_orderData(
                    orderData=orderData,
                    sellLine=realSlLine,
                    endType='SL',
                    priority=priority,
                )
                yield orderData
                continue
            # 未达成止损条件，观测是否达到止盈条件
            # 多单：最高价>=止盈价格；空单：最低价<=止盈价格
            if orderData['tpLine'] and ((posSide == 'long' and self.high >= orderData['tpLine']) or
                                        (posSide == 'short' and self.low <= orderData['tpLine'])):
                # 多单实际止盈价格
                if posSide == 'long':
                    realTpLine = max(self.open, orderData['tpLine'])
                # 空单实际止盈价格
                elif posSide == 'short':
                    realTpLine = min(self.open, orderData['tpLine'])
                else:
                    raise exception.PosSideParamError(posSide)
                # 平仓
                orderData = self.close_orderData(
                    orderData=orderData,
                    sellLine=realTpLine,
                    endType='TP',
                    priority=priority,
                )
                yield orderData
                continue

    # 爆仓
    def smThrow(self):
        '''
        逐仓爆仓，仅逐仓可以爆仓，逐仓isolated在start_orderData时会创建smLine，全仓cross的smLine=np.nan
        爆仓不受rule中的SELL_PERIOD影响
        endType = 'SM'
        '''
        priority = 50
        for orderData in self.currentOrderDatasCanBeTraded:
            if orderData['toMode'] == 'isolated':
                if (orderData['posSide'] == 'long' and self.low <= orderData['smLine'] or
                        orderData['posSide'] == 'short' and self.high >= orderData['smLine']):
                    yield self.close_orderData(
                        orderData=orderData,
                        sellLine=orderData['smLine'],
                        endType='SM',
                        priority=priority,
                    )

    # 在抛出时间段卖出
    def periodThrow(self):
        '''
        时间段满足要求，则全部平仓
        endType = 'PT'
        '''
        priority = 200
        # 是否满足时间段要求
        if not paux.date.is_period_allowed(
                date=self.time,
                periods=self.rule.THROW_PERIODS,
                timezone=self.rule.TIMEZONE,
        ):
            return None
        # 全部持仓以市价平掉
        for orderData in self.currentOrderDatasCanBeTraded:
            orderData = self.close_orderData(
                orderData=orderData,
                sellLine=self.open,
                endType='PT',
                priority=priority,
            )
            yield orderData

    # 超过最大持仓时间卖出
    def timeoutThrow(self):
        '''
        持仓时间超时，以市价平仓
        endType = 'TT'
        '''
        # 时间段是否允许卖出
        priority = 200
        if not paux.date.is_period_allowed(
                date=self.time,
                periods=self.rule.SELL_PERIODS,
                timezone=self.rule.TIMEZONE,
        ):
            return None
        if not self.rule.MAX_HOLD_ORDER_MINUTE:
            return None
        # 便利全部持仓订单
        for orderData in self.currentOrderDatasCanBeTraded:
            # 持仓时间超过了预设最大时间
            if ((self.ts - orderData['orderTs']) / 60000) >= self.rule.MAX_HOLD_ORDER_MINUTE:
                orderData = self.close_orderData(
                    orderData=orderData,
                    sellLine=self.open,
                    endType='TT',
                    priority=priority,
                )
                yield orderData

    # 以市场价卖出
    def marketThrow(self, orderDatas):
        '''
        :param orderDatas:市价抛出的订单
        以市场价抛出订单，endType = 'MT'
        '''
        priority = 0
        if orderDatas:
            for orderData in orderDatas:
                orderData = self.close_orderData(
                    orderData=orderData,
                    sellLine=self.close,
                    endType='MT',
                    priority=priority,
                )
                yield orderData

    # 运行计算---------------------------------------------------------------------------------------------
    def run(
            self,
            start_date: Union[str, None] = None,
            end_date: Union[str, None] = None,
            clear: bool = True,
            return_data=False,
    ):
        '''
        :param start_date:
        :param end_date:
        :param clear: 是否在遍历后的最后时刻卖出全部仓位
        :param buyLocked:
            buyLocked = True    卖出与买入不能发生在同一时刻
            buyLocked = False   可以先卖出后再买入
        优先级：periodThrow > timeoutThrow > smThrow >  slThrow > tpSell > sell > buy_long > buy_short
        '''

        # 起始索引与终止索引
        start_index = paux.candle.transform.get_candle_index_by_date(
            candle=self.candle,
            date=start_date,
            default=0
        )
        # 终止索引
        end_index = paux.candle.transform.get_candle_index_by_date(
            candle=self.candle,
            date=end_date,
            default=self.candle.shape[0]
        )

        '''
        买卖的优先级，越大越优先
        # periodThrow:200
        # timeoutThrow:200
        # smThrow:50
        # tpSell_and_slThrow:50
        # sell:50
        # buy:100
        '''
        for index in range(start_index, end_index):
            # 更新数据
            self.index = index
            self.record()
            # 时间段抛出
            periodThrow = self.periodThrow()
            periodThrowDatas = [orderData for orderData in periodThrow if periodThrow]
            # 超时抛出
            timeoutThrow = self.timeoutThrow()
            timeoutThrowDatas = [orderData for orderData in timeoutThrow if timeoutThrow]
            # 爆仓强平
            smThrow = self.smThrow()
            smThrowDatas = [orderData for orderData in smThrow if smThrow]
            # 止盈卖出与止损抛出
            tpSell_and_slThrow = self.tpSell_and_slThrow()
            tpSell_and_slThrowDatas = [orderData for orderData in tpSell_and_slThrow if tpSell_and_slThrow]

            # 自定义卖出
            if paux.date.is_period_allowed(
                    date=self.time,
                    periods=self.rule.SELL_PERIODS,
                    timezone=self.rule.TIMEZONE,
            ):
                sell = self.sell()
                if sell:
                    sellDatas = [orderData for orderData in sell if sell]
                else:
                    sellDatas = []
            else:
                sellDatas = []
            # 自定义买入
            if paux.date.is_period_allowed(
                    date=self.time,
                    periods=self.rule.BUY_PERIODS,
                    timezone=self.rule.TIMEZONE,
            ) and not paux.date.is_period_allowed(
                date=self.time,
                periods=self.rule.THROW_PERIODS,
                timezone=self.rule.TIMEZONE
            ):
                buy = self.buy()
                if buy:
                    buyDatas = [orderData for orderData in buy]
                else:
                    buyDatas = []
            else:
                buyDatas = []
            totalOrderDatas = periodThrowDatas + timeoutThrowDatas + smThrowDatas + tpSell_and_slThrowDatas + sellDatas + buyDatas
            totalOrderDatas = sorted(totalOrderDatas, key=lambda d: d['priority'], reverse=True)

            for orderData in totalOrderDatas:
                # 购买订单
                if orderData['sellLine'] == None:
                    self.__to_currentOrderDatas(orderData)
                else:
                    self._order.to_historyOrderDatas(orderDatas=[orderData, ])
        # 未成交订单强平
        if clear:
            marketThrow = self.marketThrow(orderDatas=self._order.currentOrderDatas)
            if marketThrow:
                marketThrowOrderDatas = [orderData for orderData in marketThrow]
            else:
                marketThrowOrderDatas = []

            self._order.to_historyOrderDatas(
                marketThrowOrderDatas
                # self.marketThrow(orderDatas=self._order.currentOrderDatas)
            )
        self.analysis = component.Analysis(historyOrderDatas=self.historyOrderDatas)
        if return_data:
            return {'historyOrderDatas': self.historyOrderDatas, 'currentOrderDatas': self.currentOrderDatas}

    # 根据条件判断是否满足进入持仓
    def __to_currentOrderDatas(self, orderData):

        if self.longPositionLeft == 0 and self.shortPositionLeft == 0:
            return None
        if self.longPositionLeft < 0 or self.shortPositionLeft < 0:
            msg = f'longPositionLeft = {self.longPositionLeft},shortPositionLeft={self.shortPositionLeft}'
            raise exception.TraderError(msg=msg)
        if orderData['posSide'] == 'long':
            if self.longPositionLeft > 0:
                self._order.to_currentOrderDatas(orderDatas=[orderData, ])
            else:
                msg = '多仓仓位不足，orderData无法开仓,orderData={orderData}'.format(orderData=str(orderData))
                warnings.warn(msg)
        elif orderData['posSide'] == 'short':
            if self.shortPositionLeft > 0:
                self._order.to_currentOrderDatas(orderDatas=[orderData, ])
            else:
                msg = '空仓仓位不足，orderData无法开仓,orderData={orderData}'.format(orderData=str(orderData))
                warnings.warn(msg)
