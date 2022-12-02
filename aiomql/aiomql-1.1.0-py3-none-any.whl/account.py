from .core.meta_trader import MetaTrader
from .core.models import AccountInfo


class Account(AccountInfo):
    """
    Properties and methods of the current trading account. Subclass of AccountInfo

    Args:
        mt5 (MetaTrader): The Meta trader object for connecting to the terminal. Default Keyword Argument
        kwargs: Arguments for AccountInfo attributes

    Attributes:
        risk (float): Percentage of account to risk
        risk_to_reward (float): ratio of risk to reward
        connected (float):

    Notes:
        Other Account properties are defined in the AccountInfo Object
        Since bot can only use one account at a time use the account class as a module style singleton object by importing the account object declared
        in this module instead of creating a new object.
    """
    risk: float = 0.05
    risk_to_reward: float = 2
    connected: bool

    def __init__(self, mt5: MetaTrader = MetaTrader(), **kwargs):
        self.mt5 = mt5
        super().__init__(**kwargs)

    async def refresh(self):
        """
        Update the account info object with latest values from the terminal
        Returns:
            Account: The Account Object with updated properties

        """
        account_info = await self.mt5.account_info()
        acc = account_info._asdict()
        acc['account_number'] = acc['login']
        del acc['login']
        self.set_attributes(**acc)

    async def login(self):
        """
        Make sure account_number, password and server attributes have been initialized
        Returns: True if login was successful else False

        """
        self.connected = await self.mt5.login(login=self.account_number, password=self.password, server=self.server)
        if self.connected:
            await self.refresh()
        return self.connected


account = Account()
