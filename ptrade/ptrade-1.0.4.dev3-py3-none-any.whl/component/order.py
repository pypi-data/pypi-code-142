from typing import Literal, Union
from ptrade import exception
from paux import order as _order


class Order():
    def __init__(self, accountMoney: Union[int, float]):
        self.currentOrderDatas = []  # 持仓订单
        self.historyOrderDatas = []  # 历史订单
        self.currentLongPosition = 0  # 持仓多单数量
        self.currentShortPosition = 0  # 持仓空单数量
        self.currentPosition = 0  # 总持仓数量
        self.accountMoney = accountMoney  # 账户余额

    # todo 部分参数有改变
    @staticmethod
    def get_empty_orderData():
        '''
        init需要更新的参数：
            orderType       订单类型 str
            instId          股票或数字货币 str
            toMode          交易模式 cross全仓，isolated逐仓 str
            posSide         方向 long做多，short做空 str
            lever           杠杆 int
            orderDatetime   订单开始的时间，%Y-m-%d %H:%M:% datetime
            buyLine         购买的价格 float
            buyCommissionRate   购买时候的手续费率
            tpLine          止盈的价格 float|None
            slLine          止损的价格 float|None
            smLine          爆仓的价格 float|None
            buyMoney        买入的金额 float
        close需要更新的参数：
            endType         订单终止的方式
            endDatetime     订单终止的时间，%Y-%m-%d %H:%M:%S datetime
            sellLine        卖出的价格 float
            sellCommissionRate  卖出时候的手续费率
            holdMinute      从订单开始到订单结束的时间，单位分钟 int
            sellMoney       卖出的金额（包含抛出） float
            commission      手续费 float
            profitRate      利润率 float
            profit          利润 float
        candle需要更新的参数：
            hh                  订单开始到订单终止的最大价格 float
            hhRate              订单开始到订单终止的最大涨幅 float
            ll                  订单开始到订单终止的最小价格 float
            llRate              订单开始到订单终止的最大跌幅 float
        辅助列：
            orderIndex
            endIndex
            orderTs
            endTs
        '''

        orderData = {
            # ---------------------------------------------
            # 订单类型 str
            'orderType': None,
            # 股票或数字货币 str
            'instId': None,
            # 交易模式 cross全仓，isolated逐仓 str
            'toMode': None,
            # 方向：long做多，short做空
            'posSide': None,
            # 杠杆 int
            'lever': None,
            # 订单开始的时间，%Y-m-%d %H:%M:%S datetime
            'orderDatetime': None,
            # 购买的价格 float
            'buyLine': None,
            # 买入的手续费率
            'buyCommissionRate': None,
            # 止盈的价格 float|None
            'tpLine': None,
            # 止损的价格 float|None
            'slLine': None,
            # 爆仓的价格 float | None
            'smLine': None,
            # 买入的金额 float
            'buyMoney': None,
            # --------------------------------------------
            # 订单终止的方式 str
            'endType': None,
            # 订单终止的时间，%Y-%m-%d %H:%M:%S datetime
            'endDatetime': None,
            # 卖出的价格 float
            'sellLine': None,
            # 卖出的手续费率
            'sellCommissionRate': None,
            # 从订单开始到订单结束的时间，单位分钟 int
            'holdMinute': None,
            # 卖出的金额（包含抛出） float
            'sellMoney': None,
            # 手续费 float
            'commission': None,
            # 利润率 float
            'profitRate': None,
            # 利润 float
            'profit': None,
            # ---------------------------------------------
            #  订单开始到订单终止的最大价格 float
            'hh': None,
            #  订单开始到订单终止的最大涨幅 float
            'hhRate': None,
            #  订单开始到订单终止的最小价格 float
            'll': None,
            # 订单开始到订单终止的最大跌幅 float
            'llRate': None,
        }

        return orderData

    # 开仓
    def start_orderData(
            self,
            instId: str,
            toMode: Literal['cross', 'isolated'],
            posSide: Literal['long', 'short'],
            lever: int,
            orderDatetime: object,
            buyLine: Union[int, float],
            buyCommissionRate: Union[int, float],
            buyMoney: Union[int, float],
            tpRate: Union[int, float, None] = None,
            tpLine: Union[int, float, None] = None,
            slRate: Union[int, float, None] = None,
            slLine: Union[int, float, None] = None,
            orderType: object = None,
            **kwargs
    ):
        '''
        创建订单
        :param instId:          股票或数字货币 (str)
        :param toMode:          交易模式 cross全仓，isolated逐仓 (str)
        :param posSide:         方向 long做多，short做空 (str)
        :param lever:           杠杆 (int)
        :param orderDatetime:   订单开始的时间，%Y-m-%d %H:%M:%S (datetime)
        :param buyLine:         购买的价格 (float)
        :param buyMoney:        买入的金额 (float)
        :param tpRate:          止盈率 (float|None)
        :param tpLine:          止赢价格 (float|None)
        :param slRate:          止损率 (float|None)
        :param slLine:          止损价格 (float|None)
        :param orderType:       订单类型（str)
        :param kwargs:          补充字段
        :return: orderData
        优先级：
            止盈线 > 止盈率   (止盈率仅当无止盈线时才生效）
            止损线 > 止损率   (止损率仅当无止损线时才生效）

        smLine(stock market): 强制平仓价格，仅逐仓使用，为逐仓亏损100%的标记价格，全仓不设置强制平仓价格
        '''
        # 获得一个初始化的订单
        orderData = self.get_empty_orderData()
        # 如果没有tpLine，则使用tpRate计算tpLine
        if not tpLine and tpRate:
            if posSide == 'long':
                tpLine = buyLine * (1 + abs(tpRate))
            elif posSide == 'short':
                tpLine = buyLine * (1 - abs(tpRate))
            else:
                raise exception.PosSideParamError(posSide)

        # 如果没有slLine，则使用slRate计算slLine
        if not slLine and slRate:
            if posSide == 'long':
                slLine = buyLine * (1 - abs(slRate))
            elif posSide == 'short':
                slLine = buyLine * (1 + abs(slRate))
            else:
                raise exception.PosSideParamError(posSide)
        # 计算smLine
        if toMode == 'isolated':
            if posSide == 'long':
                smLine = buyLine * (1 - 1 / lever)  # stock market
            elif posSide == 'short':
                smLine = buyLine * (1 + 1 / lever)  # stock market
            else:
                raise exception.PosSideParamError(posSide)
        elif toMode == 'cross':
            smLine = None
        else:
            raise exception.ToModeParamError(toMode)
        # 赋值
        orderData['orderType'] = orderType
        orderData['instId'] = instId
        orderData['toMode'] = toMode
        orderData['posSide'] = posSide
        orderData['lever'] = lever
        orderData['orderDatetime'] = orderDatetime
        orderData['buyLine'] = _order.round_simulate(buyLine)
        orderData['buyCommissionRate'] = buyCommissionRate
        # 保留位数
        orderData['tpLine'] = _order.round_simulate(tpLine) if tpLine != None else None
        orderData['slLine'] = _order.round_simulate(slLine) if slLine != None else None
        orderData['smLine'] = _order.round_simulate(smLine) if smLine != None else None
        orderData['buyMoney'] = buyMoney
        for key, value in kwargs.items():
            orderData[key] = value
        return orderData

    # 平仓
    def close_orderData(
            self,
            orderData: dict,
            sellLine: Union[int, float],
            sellCommissionRate: Union[int, float],
            endDatetime: object,
            endType: object = None,
            **kwargs
    ):
        '''
        关闭订单
        :param orderData: 关闭的订单(dict)
        :param sellLine: 卖出价格(float)
        :param endDatetime: 订单终止的时间，%Y-%m-%d %H:%M:%S (datetime)
        :param commission_rate: 手续费率(str)
        :param endType:订单终止的方式(str|None)
        :param kwargs: 补充字段
        :return:

        产生的数据：
            holdMinute      从订单开始到订单结束的时间，单位分钟 int
            sellMoney       卖出的金额（包含抛出） float
            commission      手续费 float
            profitRate      利润率 float
            profit          利润 float
        '''
        # 卖出价格
        sellLine = _order.round_simulate(sellLine)
        # 是否需要考虑爆仓
        if orderData['toMode'] == 'cross':
            pass
        elif orderData['toMode'] == 'isolated':
            # 多仓爆仓
            if orderData['posSide'] == 'long' and sellLine <= orderData['smLine']:
                sellLine = orderData['smLine']
                endType = 'SM'
            # 空仓爆仓
            elif orderData['posSide'] == 'short' and sellLine >= orderData['smLine']:
                sellLine = orderData['smLine']
                endType = 'SM'
        else:
            raise exception.ToModeParamError(orderData['toMode'])
        # 持仓时间（分钟）
        # holdMinute = int(
        #     (datetime.datetime.strptime(endDatetime, '%Y-%m-%d %H:%M:%S', ).timestamp() - datetime.datetime.strptime(
        #         orderData['orderDatetime'], '%Y-%m-%d %H:%M:%S').timestamp()) / 60)

        # 持仓时间（分钟）
        holdMinute = int(
            (orderData['endDatetime'].timestamp() - orderData['orderDatetime'].timestamp()) / 60
        )

        commission_data = _order.get_commission_data(
            posSide=orderData['posSide'],
            buyMoney=orderData['buyMoney'],
            buyLine=orderData['buyLine'],
            sellLine=sellLine,
            lever=orderData['lever'],
            buyCommissionRate=orderData['buyCommissionRate'],
            sellCommissionRate=sellCommissionRate
        )

        commission = commission_data['commission']
        sellMoney = commission_data['sellMoney']
        profitRate = commission_data['profitRate']
        profit = round(profitRate * orderData['buyMoney'], 4)

        # 赋值
        orderData['endType'] = endType
        orderData['endDatetime'] = endDatetime
        orderData['sellLine'] = sellLine
        orderData['holdMinute'] = holdMinute
        orderData['commission'] = commission
        orderData['sellMoney'] = sellMoney
        orderData['profitRate'] = profitRate
        orderData['profit'] = profit
        orderData['sellCommissionRate'] = sellCommissionRate
        # 补充字段
        for key, value in kwargs.items():
            orderData[key] = value
        return orderData

    # 进去历史交易数据
    def to_historyOrderDatas(self, orderDatas: Union[list, tuple, None]):
        '''
        从持仓中删除orderDatas，并添加到historyOrderDatas中
        维护：
            持有总订单数量     self.currentPosition
            持有多仓订单数量   self.currentLongPosition
            持有空仓订单数量   self.currentShortPosiiton
            账户余额          self.accountMoney
        账户金额如果出现负数，会报告异常
        :param orderDatas: 平仓订单对象
        '''
        if orderDatas:
            for orderData in orderDatas:
                # 删除持仓，可能这个订单已经被删除
                try:
                    self.currentOrderDatas.remove(orderData)
                except:
                    pass
                # 条件历史订单
                self.historyOrderDatas.append(orderData)
                # 维护账户余额
                self.accountMoney += orderData['sellMoney']
                if self.accountMoney < 0:
                    raise exception.OrderError('账户余额不能小于零')
                # 总仓位
                self.currentPosition -= 1
                # 多仓位
                if orderData['posSide'] == 'long':
                    self.currentLongPosition -= 1
                # 空仓位
                elif orderData['posSide'] == 'short':
                    self.currentShortPosition -= 1
                else:
                    raise exception.PosSideParamError(orderData['posSide'])

    # 进入持仓数据
    def to_currentOrderDatas(self, orderDatas: Union[list, tuple, None]):
        '''
        添加到currentOrderDatas中
        维护：
            持有总订单数量     self.currentPosition
            持有多仓订单数量   self.currentLongPosition
            持有空仓订单数量   self.currentShortPosiiton
            账户余额          self.accountMoney
        账户金额如果出现负数，会报告异常
        :param orderDatas: 开仓订单对象
        '''
        if orderDatas:
            for orderData in orderDatas:
                # 添加持仓
                self.currentOrderDatas.append(orderData)
                # 总仓位
                self.currentPosition += 1
                # 多仓位
                if orderData['posSide'] == 'long':
                    self.currentLongPosition += 1
                # 空仓位
                elif orderData['posSide'] == 'short':
                    self.currentShortPosition += 1
                else:
                    raise exception.PosSideParamError(orderData['posSide'])
                # 维护账户余额
                self.accountMoney -= orderData['buyMoney']
                if self.accountMoney < 0:
                    raise exception.OrderError('账户余额不能小于零')
