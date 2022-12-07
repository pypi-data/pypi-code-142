import warnings
from typing import Union
from ptrade import component
import paux.process


# 执行多个产品的模拟交易
class SimulateMultiply():
    def __init__(
            self,
            Simulate,
            candle_map,
            rule: component.RuleChinaStock,
    ):
        self.simulate_map = {}
        for instId, candle in candle_map.items():
            self.simulate_map[instId] = Simulate(
                candle=candle,
                instId=instId,
                rule=rule,
            )

    def run(
            self,
            start_date: Union[str, None] = None,
            end_date: Union[str, None] = None,
            clear: bool = True,
            p_num=1,
            skip_exception=False,
    ):
        if p_num <= 1:
            historyOrderDatas = []
            for instId, simulate in self.simulate_map.items():
                simulate.run(start_date=start_date, end_date=end_date, clear=clear)
                historyOrderDatas += simulate.historyOrderDatas
            self.analysis = component.Analysis(historyOrderDatas=historyOrderDatas)
        else:
            warnings.warn('p_num应该为1，异步执行存在安全性问题，下个版本会更新')
            params = []
            index_to_instId = {}
            for index, (instId, simulate) in enumerate(self.simulate_map.items()):
                index_to_instId[index] = instId
                params.append(
                    {
                        'func': simulate.run,
                        'start_date': start_date,
                        'end_date': end_date,
                        'clear': clear,
                        'return_data': True,
                    }
                )
            results = paux.process.pool_worker(
                params=params,
                p_num=p_num,
                skip_exception=skip_exception
            )
            self.historyOrderDatas = []
            self.currentOrderDatas = []
            for index, result in results:
                instId = index_to_instId[index]
                self.simulate_map[instId].historyOrderDatas = result['historyOrderDatas']
                self.simulate_map[instId].currentOrderDatas = result['currentOrderDatas']
                self.historyOrderDatas += result['historyOrderDatas']
                self.historyOrderDatas += result['currentOrderDatas']
            self.analysis = component.Analysis(historyOrderDatas=self.historyOrderDatas)
