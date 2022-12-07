# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['Enums',
 'MexcClient',
 'MexcClient.Enums',
 'MexcClient.Utils',
 'MexcClient.Utils.Signature']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'mexcapiclient',
    'version': '0.1.4',
    'description': '',
    'long_description': '# Client MEXC Exchange\n\nA simple python client for the [MEXC](https://www.mexc.com/) exchange. \nOpen, unofficial project, intended to consume all endpoints provided by Exchange \n[documentation](https://mxcdevelop.github.io/apidocs/spot_v3_en/#introduction).\n\n## Summary\n\n* [Pypi](#pypi)\n* [Dependencies](#dependencies)\n* [how to use](#how-to-use)\n* [functions implemented so far](#functions-implemented-so-far)\n* [Instalation](#installation)\n  * [Python version](#python-version)\n\n## Pypi\nsee the project on Pypi by accessing the [link](https://pypi.org/project/mexcapiclient/).\n\n## Dependencies\n\nThis project uses some libraries for its operation as well as tests and linter for code organization. Its dependencies are:\n\n* [Requests](https://requests.readthedocs.io/en/latest/)\n* [Black](https://github.com/psf/black)\n* [Pytest](https://docs.pytest.org/en/7.1.x/contents.html)\n\n## how to use \n\nA simple code example for client use is:\n\n    from MexcClient.client import MexcClient\n\n    client = MexcClient("API_KEY", "API_SECRET")\n    client.server_time()\n\n## functions implemented so far\n\n| Func                  | Method | Endpoint                 | Params                                                                                                                                                                    | Section               |\n|-----------------------|--------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|\n| check_connection      | GET    | /api/v3/ping             | None                                                                                                                                                                      | Market Data Endpoints |\n| server_time           | GET    | /api/v3/time             | None                                                                                                                                                                      | Market Data Endpoints |\n| exchange_info         | GET    | /api/v3/exchangeInfo     | None                                                                                                                                                                      | Market Data Endpoints |\n| order_book_of_symbol  | GET    | /api/v3/depth            | symbol: str, limit: int                                                                                                                                                   | Market Data Endpoints |\n| recent_trades_list    | GET    | /api/v3/trades           | symbol: str, limit: int                                                                                                                                                   | Market Data Endpoints |\n| old_trade_lookup      | GET    | /api/v3/historicalTrades | symbol: str, limit: int                                                                                                                                                   | Market Data Endpoints |\n| kline_data            | GET    | /api/v3/klines           | symbol: str, interval: EnumKlineInterval, start_time: int, end_time: int, limit: int = 500                                                                                | Market Data Endpoints |\n| current_average_price | GET    | /api/v3/avgPrice         | symbol: str                                                                                                                                                               | Market Data Endpoints |\n| create_order_test     | POST   | /api/v3/order/test       | symbol: str, side: EnumOrderSide, _type: EnumOrderType, timestamp: int, quantity: int, quote_order_quantity: str, price: str, new_client_order_id: str, recv_window: int  | Spot Account/Trade    |\n| create_new_order      | POST   | /api/v3/order            | symbol: str, side: EnumOrderSide, _type: EnumOrderType, timestamp: int, quantity: int, quote_order_quantity: str, price: str, new_client_order_id: str, recv_window: int  | Spot Account/Trade    |\n|                       |        |                          |                                                                                                                                                                           |                       |\n|                       |        |                          |                                                                                                                                                                           |                       |\n|                       |        |                          |                                                                                                                                                                           |                       |\n\n\n## installation\nTo install just run the following command:\n\n    pip install mexcapiclient\n\n\n### Python version\npython version used in this project was:\n\n* [Python3.9](https://www.python.org/)\n\n',
    'author': 'Carlos Eduardo',
    'author_email': 'suportebeloj@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/suportebeloj/client-mexc-exchange',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
