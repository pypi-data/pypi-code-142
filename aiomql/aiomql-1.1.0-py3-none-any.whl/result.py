import datetime
from functools import cache
import csv
import asyncio
from logging import getLogger

from .core.models import OrderSendResult
from .order import Order
from .config import Config

logger = getLogger()


class TradeResult:
    """
    Save result of trades made by a strategy to a csv file.
    Args:
        result (OrderSendResult): OrderSendResult object of an executed trade
        request (Order | dict): Order object or a dict of trade order request properties
        parameters (dict): The parameters of the strategy placing the trade
        time (float): Timestamp of when order was placed
        name: Name  of strategy or any desired name for the result csv file
    Attributes:
        config: The configuration object
        result (dict): Trade result as a dict
        request (dict): Trade order as a dict
        parameters (dict): The parameters of the strategy placing the trade
        time: Timestamp
        time (float): Timestamp of when order was placed
        name: Name  of strategy or any desired name for the result csv file

    Notes:
        To enable saving trades as csv file. Make sure that config.record_trades is True
    """
    def __init__(self, *, result: OrderSendResult | dict, request: Order | dict, parameters: dict, time: float = datetime.datetime.utcnow().timestamp(),
                 name: str = ""):
        self.config = Config()
        self.result: dict = result.dict if not isinstance(request, dict) else request
        self.request: dict = request.get_dict(include={'action', 'symbol', 'sl', 'tp', 'type'}) if not isinstance(request, dict) else request
        self.parameters = parameters
        self.time = time
        self.name = name or self.parameters.get('name', datetime.datetime.today().strftime('%a %M %b %Y'))

        if self.config.record_trades:
            loop = asyncio.get_running_loop()
            asyncio.run_coroutine_threadsafe(self.to_csv(), loop)

    @property
    @cache
    def data(self) -> dict:
        """
        A dict representing data to be saved in the csv file. It is a combination of the strategy parameters, the order result properties, the trade
        request properties, actual profit made from trade, timestamp of when trade was placed, closed to indicate if trade has been closed and win to
        indicate if trade was successful or not
        Returns (dict): A dict of data to be saved
        """
        data = self.parameters | self.result | self.request | {'actual_profit': 0, 'time': self.time, 'closed': False, 'win': False}
        return data

    async def to_csv(self):
        """
        Saves to csv file format
        Returns:

        """
        try:
            file = self.config.records_dir / f"{self.name}.csv"
            exists = file.exists()
            self.data.pop('name')
            self.data['date'] = datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M")
            with open(file, 'a', newline='') as fh:
                writer = csv.DictWriter(fh, fieldnames=sorted(list(self.data.keys())), extrasaction='ignore', restval=None)
                if not exists:
                    writer.writeheader()
                writer.writerow(self.data)
        except Exception as err:
            logger.error(err)
