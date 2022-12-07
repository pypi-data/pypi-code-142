# 美股的规则样例
import pendulum


class RuleAmericaStock():
    # -----------------------------------------------------------
    # 时区
    timezone = 'America/New_York'  # 美股时间 中国时间：Asia/Shanghai
    # -----------------------------------------------------------
    # 账户余额
    ACCOUNT_MONEY = 2000
    # -----------------------------------------------------------
    # todo 购买金额
    # 单次买入的金额为BUY_MONEY
    # 单次购买的金额为BUY_MONEY_RATE * ACCOUNT_MONEY
    # BUY_MONEY和BUY_MONEY_RATE同时出现，以BUY_MONEY_RATE为主
    BUY_MONEY = 100
    BUY_MONEY_RATE = 0.1
    # -----------------------------------------------------------
    # 止盈止损
    LONG_TP_RATE = None  # 多单止盈，挂单价格
    LONG_SL_RATE = None  # 多单止损，出发止损价格，以市价单平仓
    SHORT_TP_RATE = None  # 空单止盈，挂单价格
    SHORT_SL_RATE = None  # 空单止损，出发止损价格，以市价单平仓
    # -----------------------------------------------------------
    # 杠杆
    LONG_LEVER = 1  # 多单杠杆
    SHORT_LEVER = 1  # 空单杠杆
    # -----------------------------------------------------------
    # 仓位
    LONG_POSITION = 100  # 多单仓位
    SHORT_POSITION = 100  # 空单仓位
    POSITION = 100  # 总仓位
    # -----------------------------------------------------------
    # 交易时间
    # 运行购买的时间
    BUY_PERIODS = [
        ['00:00:00', '23:59:59']
    ]
    # 运行卖出的时间
    SELL_PERIODS = [
        ['00:00:00', '23:59:59']
    ]
    # 运行抛出的时间
    THROW_PERIODS = [
        # ['23:59:00', '23:59:00'],
    ]
    # -----------------------------------------------------------
    # 最长订单时间（分钟）
    MAX_HOLD_ORDER_MINUTE = 60 * 24
    # -----------------------------------------------------------
    # 手续费率
    BUY_COMMISSION_RATE = 0.0001
    SELL_COMMISSION_RATE = 0.0011
    # -----------------------------------------------------------
    # 开盘与收盘时刻
    OPEN_TIME = '00:00:00'  # 开盘的时刻
    CLOSE_TIME = '00:00:00'  # 收盘的时刻 todo 未使用


class RuleChinaStock():
    # 交易规则
    T = 0  # T0 T1 T2
    # -----------------------------------------------------------
    # 时区
    TIMEZONE = 'Asia/Shanghai'  # 美股时间 中国时间：Asia/Shanghai
    # -----------------------------------------------------------
    # 账户余额
    ACCOUNT_MONEY = 2000
    # -----------------------------------------------------------
    # todo 购买金额
    # 单次买入的金额为BUY_MONEY
    # 单次购买的金额为BUY_MONEY_RATE * ACCOUNT_MONEY
    # BUY_MONEY和BUY_MONEY_RATE同时出现，以BUY_MONEY_RATE为主
    BUY_MONEY = 100
    BUY_MONEY_RATE = 0.1
    # -----------------------------------------------------------
    # 止盈止损
    LONG_TP_RATE = None  # 多单止盈，挂单价格
    LONG_SL_RATE = None  # 多单止损，出发止损价格，以市价单平仓
    SHORT_TP_RATE = None  # 空单止盈，挂单价格
    SHORT_SL_RATE = None  # 空单止损，出发止损价格，以市价单平仓
    # -----------------------------------------------------------
    # 杠杆
    LONG_LEVER = 1  # 多单杠杆
    SHORT_LEVER = 1  # 空单杠杆
    # -----------------------------------------------------------
    # 仓位
    LONG_POSITION = 100  # 多单仓位
    SHORT_POSITION = 100  # 空单仓位
    POSITION = 100  # 总仓位
    # -----------------------------------------------------------
    # 交易时间
    # 运行购买的时间
    BUY_PERIODS = [
        ['00:00:00', '23:59:59']
    ]
    # 运行卖出的时间
    SELL_PERIODS = [
        ['00:00:00', '23:59:59']
    ]
    # 运行抛出的时间
    THROW_PERIODS = [
        # ['23:59:00', '23:59:00'],
    ]
    # -----------------------------------------------------------
    # 最长订单时间（分钟）
    MAX_HOLD_ORDER_MINUTE = None
    # -----------------------------------------------------------
    # 手续费率
    BUY_COMMISSION_RATE = 0.0001
    SELL_COMMISSION_RATE = 0.0011
    # -----------------------------------------------------------
    # 开盘与收盘时刻
    OPEN_TIME = '00:00:00'  # 开盘的时刻

    def __init__(self):
        for i in range(len(self.BUY_PERIODS)):
            for j in range(2):
                self.BUY_PERIODS[i][j] = pendulum.from_format(self.BUY_PERIODS[i][j], 'HH:mm:ss').time()

        for i in range(len(self.SELL_PERIODS)):
            for j in range(2):
                self.SELL_PERIODS[i][j] = pendulum.from_format(self.SELL_PERIODS[i][j], 'HH:mm:ss').time()

        for i in range(len(self.THROW_PERIODS)):
            for j in range(2):
                self.THROW_PERIODS[i][j] = pendulum.from_format(self.THROW_PERIODS[i][j], 'HH:mm:ss').time()


if __name__ == '__main__':
    rcs = RuleChinaStock()
    print(type(rcs.BUY_PERIODS[0][1]))
