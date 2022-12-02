import asyncio
from datetime import datetime
from typing import Iterable
from pathlib import Path
import csv

from .history import History
from .config import Config


class Records:
    """
    This utility class read trade records from csv files, and update them based on their closing positions

    Keyword Args:
        records_dir (Path): Path to directory containing record of placed trades.

    Attributes:
        config: Config object

        records_dir(Path): Path to directory containing record of placed trades, If not given takes the default from the config
    """

    def __init__(self, records_dir: Path = None):
        self.config = Config()
        self.records_dir = records_dir or self.config.records_dir

    async def get_records(self):
        """
        get trade records from records_dir folder
        Returns:

        """
        for file in self.records_dir.iterdir():
            if file.is_file() and file.name.endswith('.csv'):
                yield file

    async def read_record(self, file: Path):
        """
        Read and update trade records

        Args:
            file: Trade record file

        Returns:

        """
        with open(file, newline='') as fr:
            reader = csv.DictReader(fr)
            rows = (row for row in reader)
            rows = await self.update_record(rows)
            fr.close()
            if not all(rows):
                return
            fw = open(file, newline='', mode='w')
            writer = csv.DictWriter(fw, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
            fw.close()

    async def update_record(self, rows: Iterable) -> Iterable[dict]:
        """
        Get update of trades in the record file.
        Args:
            rows: rows of recorded trade in a particular file

        Returns: return rows of updated trades as an iterable of dicts

        """
        rows = {row['deal']: row for row in sorted((row for row in rows), key=lambda row: float(row['time']))}
        open_rows = [(key, value) for key, value in rows.items() if value.get('closed').title() == "False"]
        if len(open_rows) == 0:
            return [{}]

        start, end = datetime.fromtimestamp(float(open_rows[0][1]['time'])).replace(hour=0, minute=0, second=0), datetime.now()\
            .replace(hour=23, minute=59, second=59)

        history = History(date_from=start, date_to=end)
        await history.init(orders=False)
        deals = {str(deal.position_id): deal.profit for deal in history.deals}

        for el in open_rows:
            row = el[1]
            if row['order'] not in deals:
                continue
            profit = float(row['profit'])
            actual_profit = deals[row['order']]
            win = actual_profit / profit > self.config.win_percentage
            row.update(actual_profit=actual_profit, closed=True, win=win)
        return list(rows.values())

    async def update_trade_records(self):
        """
        Update trade records
        Returns:
        """
        records = [self.read_record(record) async for record in self.get_records()]
        await asyncio.gather(*records)

    async def update_trade_record(self, file: Path | str):
        """

        Returns:

        """
        await self.read_record(file)
