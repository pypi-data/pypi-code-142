import numpy as np
import pandas as pd
import datetime
from typing import Literal
from copy import deepcopy
from ptrade import exception


# 分析模块
class Analysis():
    # 默认展示的DataFrame字段
    DETAIL_COLUMNS = [
        'orderType',
        'posSide',
        'instId',
        'toMode',
        'lever',
        'orderDatetime',
        'endDatetime',
        'holdMinute',
        'endType',
        'buyLine',
        'sellLine',
        'tpLine',
        'slLine',
        'smLine',
        'buyMoney',
        'sellMoney',
        'commission',
        'profit',
        'profitRate',
        'hh',
        'hhRate',
        'll',
        'llRate',
    ]
    # 过程数据中展示的字段
    INFO_COLUMNS = [
        'period',
        'profit_sum',
        'profit_mean',
        'profit_peak',
        'profit_valley',
        'dprofit',
        'dloss',
        'order_num',
        'account_money',
        'account_money_peak',
        'account_money_valley',
    ]

    def __init__(self, historyOrderDatas):
        self.historyOrderDatas = historyOrderDatas

    # 获得DataFrame对象
    def get_df(self, historyOrderDatas=[], **kwargs):
        if hasattr(self, 'df'):
            return self.df
        if not historyOrderDatas:
            historyOrderDatas = self.historyOrderDatas
        df_columns = deepcopy(self.DETAIL_COLUMNS)
        # 自定义控制字段的显示
        for column, show in kwargs.items():
            if show == True and column not in df_columns:
                df_columns.append(column)
                continue
            if show == False and column in df_columns:
                df_columns.remove(column)
                continue
        if not historyOrderDatas:
            df = pd.DataFrame([], columns=df_columns)
            return df

        df = pd.DataFrame(historyOrderDatas)[df_columns].sort_values(by='orderDatetime').reset_index(drop=True)
        self.df = df
        return self.df

    # 按照仓位计算交易过程DataFrame
    def get_df_by_position(self, position: int = None, longPosition: int = None, shortPosition: int = None,
                           historyOrderDatas=[], df=None):
        if historyOrderDatas:
            df = self.get_df(historyOrderDatas=historyOrderDatas)
        elif type(df).__name__ != 'NoneType':
            df = df
        else:
            if hasattr(self, 'df'):
                df = self.df
            else:
                df = self.get_df()
        if df.shape[0] == 0:
            return df
        # 如果需要过滤仓位
        if position or longPosition or shortPosition:
            if not position:
                position = 9999 * 9999
            if not longPosition:
                longPosition = 9999 * 9999
            if not shortPosition:
                shortPosition = 9999 * 9999
            currentLongOrderDatas = []
            currentShortOrderDatas = []
            currentOrderDatas = []
            historyOrderDatas = []
            for i in df.index:
                # 本次的订单
                thisOrderData = df.loc[i].to_dict()
                # 卖出之前的订单
                removeLongOrderDatas = []
                removeShortOrderDatas = []
                removeOrderDatas = []
                for orderData in currentOrderDatas:
                    if orderData['endDatetime'] <= thisOrderData['orderDatetime']:
                        removeOrderDatas.append(orderData)
                        if orderData['posSide'] == 'long':
                            removeLongOrderDatas.append(orderData)
                        elif orderData['posSide'] == 'short':
                            removeShortOrderDatas.append(orderData)

                for orderData in removeOrderDatas:
                    historyOrderDatas.append(orderData)
                    currentOrderDatas.remove(orderData)

                for orderData in removeLongOrderDatas:
                    currentLongOrderDatas.remove(orderData)
                for orderData in removeShortOrderDatas:
                    currentShortOrderDatas.remove(orderData)
                longPositionLeft = min(
                    position - len(currentOrderDatas),
                    longPosition - len(currentLongOrderDatas),
                )
                shortPositionLeft = min(
                    position - len(currentOrderDatas),
                    shortPosition - len(currentShortOrderDatas),
                )

                if thisOrderData['posSide'] == 'long':
                    if longPositionLeft > 0:
                        currentLongOrderDatas.append(thisOrderData)
                        currentOrderDatas.append(thisOrderData)
                elif thisOrderData['posSide'] == 'short':
                    if shortPositionLeft > 0:
                        currentShortOrderDatas.append(thisOrderData)
                        currentOrderDatas.append(thisOrderData)
            historyOrderDatas += currentOrderDatas
            df = pd.DataFrame(historyOrderDatas)
        return df

    # 计算等比连续投资的DataFrame
    def get_df_sequential_investment(
            self,
            account_money,
            invest_percentage=0.1,
            historyOrderDatas=[],
            df=None,
            position: int = None,
            longPosition: int = None,
            shortPosition: int = None,
    ):

        df = self.get_df_by_position(
            position=position,
            longPosition=longPosition, shortPosition=shortPosition,
            historyOrderDatas=historyOrderDatas, df=df,
        )
        if not df.shape[0]:
            return df

        currentOrderDatas = []
        historyOrderDatas = []
        df = df.sort_values(by='orderDatetime').reset_index(drop=True)
        for i in df.index:
            if position != None and len(currentOrderDatas) > position:
                print(i, len(currentOrderDatas))
            # 本次的订单
            thisOrderData = df.loc[i].to_dict()
            # 卖出之前的订单
            removeOrderDatas = []
            for orderData in currentOrderDatas:
                if orderData['endDatetime'] <= thisOrderData['orderDatetime']:
                    removeOrderDatas.append(orderData)

            for orderData in removeOrderDatas:
                account_money += orderData['profit']
                historyOrderDatas.append(orderData)
                currentOrderDatas.remove(orderData)

            if account_money > 0:
                buyMoney = min(
                    account_money,
                    (account_money + sum([
                        orderData['buyMoney'] for orderData in currentOrderDatas
                    ])) * invest_percentage
                )
                alter_rate = buyMoney / thisOrderData['buyMoney']
                thisOrderData['buyMoney'] = round(alter_rate * thisOrderData['buyMoney'], 4)
                thisOrderData['sellMoney'] = round(alter_rate * thisOrderData['sellMoney'], 4)
                thisOrderData['commission'] = round(alter_rate * thisOrderData['commission'], 8)
                thisOrderData['profit'] = round(alter_rate * thisOrderData['profit'], 4)
                currentOrderDatas.append(thisOrderData)
        historyOrderDatas += currentOrderDatas
        if historyOrderDatas:
            df_sequential_investment = pd.DataFrame(historyOrderDatas)
        else:
            df_sequential_investment = pd.DataFrame([], columns=self.DETAIL_COLUMNS)
        return df_sequential_investment

    # 获取交易过程中的分析数据
    def get_df_process_info(
            self,
            account_money,
            period: Literal['day', 'week', 'month', 'year', 'all'],
            historyOrderDatas=[],
            df=None,
            position: int = None,
            longPosition: int = None,
            shortPosition: int = None,
    ):
        df = self.get_df_by_position(
            position=position,
            longPosition=longPosition,
            shortPosition=shortPosition,
            historyOrderDatas=historyOrderDatas,
            df=df
        )
        if not df.shape[0]:
            return pd.DataFrame([], columns=self.INFO_COLUMNS)

        if period == 'day':
            df[period] = df['endDatetime'].apply(lambda d: d[0:10])
        elif period == 'week':
            df[period] = df['endDatetime'].apply(
                lambda d: '~'.join(
                    datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S').isocalendar()[0:2]
                )
            )
        elif period == 'month':
            df[period] = df['endDatetime'].apply(lambda d: d[0:7])
        elif period == 'year':
            df[period] = df['endDatetime'].apply(lambda d: d[0:4])
        elif period == 'all':
            df[period] = '{start_date}~{end_date}'.format(
                # start_date=df['orderDatetime'].min().[0:10],
                # end_date=df['endDatetime'].min()[0:10],
                start_date=df['orderDatetime'].min().strftime('%Y-%m-%d %H:%M:%S')[0:10],
                end_date=df['endDatetime'].min().strftime('%Y-%m-%d %H:%M:%S')[0:10],
            )
        else:
            msg = f'period = f{period}，period must in ["day","week","month","year","all"]'
            raise exception.ParamError(msg)
        info_datas = []
        endTypes = df['endType'].unique().tolist()
        for this_period, df_gb in df.groupby(period):
            # profit
            profit_sum = round(df_gb['profit'].sum(), 4)
            profit_mean = round(df_gb['profit'].mean(), 4)
            dprofit = 0
            dloss = 0
            profits = df_gb['profit'].values
            cum_profits = np.cumsum(profits)
            profit_peak = cum_profits.max()
            profit_valley = cum_profits.min()
            for i in range(df_gb.shape[0]):
                cum_profits = np.cumsum(profits[i:])
                dprofit = max(dprofit, np.max(cum_profits))
                dloss = min(dloss, np.min(cum_profits))
            order_num = df_gb.shape[0]
            account_money_peak = account_money + profit_peak
            account_money_valley = account_money + profit_valley
            account_money = account_money + profit_sum

            this_data = {
                'period': period,
                period: this_period,
                'profit_sum': profit_sum,
                'profit_mean': profit_mean,
                'profit_peak': profit_peak,
                'profit_valley': profit_valley,
                'dprofit': dprofit,
                'dloss': dloss,
                'order_num': order_num,
                'account_money': account_money,
                'account_money_peak': account_money_peak,
                'account_money_valley': account_money_valley,

            }
            for endType in endTypes:
                this_data[endType] = df_gb.query('endType==@endType').shape[0]
            info_datas.append(this_data)
        return pd.DataFrame(info_datas)


if __name__ == '__main__':
    pass
