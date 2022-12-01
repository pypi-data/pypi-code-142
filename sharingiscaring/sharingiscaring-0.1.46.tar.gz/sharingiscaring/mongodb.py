import os

import dateutil
from .mongodb_queries._search_transfers import Mixin as _search_transfers
from .mongodb_queries._subscriptions import Mixin as _subscriptions
from pymongo import MongoClient
from rich.console import Console
from sharingiscaring.tooter import Tooter, TooterType, TooterChannel
console = Console()

class TestMongo:
    def __init__(self):
        pass

class MongoDB(
    _search_transfers,
    _subscriptions
    ):

    def __init__(self, mongo_config, tooter: Tooter):
        self.tooter: Tooter = tooter
        try:
            con = MongoClient(f'mongodb://admin:{mongo_config["MONGODB_PASSWORD"]}@{mongo_config["MONGO_IP"]}:{mongo_config["MONGO_PORT"]}')
            self.db                          = con.concordium
            self.collection_blocks           = self.db['blocks']
            self.collection_transactions     = self.db['transactions']
            self.collection_messages         = self.db['bot_messages']
            console.log(con.server_info()['version'])
        except Exception as e:
            tooter.send(channel=TooterChannel.NOTIFIER, message=f'BOT ERROR! Cannot connect to MongoDB, with error: {e}', notifier_type=TooterType.MONGODB_ERROR)
            