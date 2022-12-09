from datetime import datetime, timezone

from sxc_api_client import SxcApiClient
from sxc_api_client.constants import MarketHistoryIntervals

sxc = SxcApiClient()
# sxc = SxcApiClient(access_key="fYAIupmmewvGdOkuHWCOGrfkXTJwru",
#                    secret_key="KHXBqIEgcIwaufwmQmtCOUYjsMyvqBGOaJmOncDbQGATxmVgsr")
# sxc = SxcApiClient(access_key="AJMJPIpwkQQMbQdSCMizM5KdNd8ELz",
#                    secret_key="o2pxVTQPLrNx6Tb29rtG3qxMVOTgeJcROeYcpFDGpW6iCjf889")

# "fYAIupmmewvGdOkuHWCOGrfkXTJwru"
# "KHXBqIEgcIwaufwmQmtCOUYjsMyvqBGOaJmOncDbQGATxmVgsr"

# "AJMJPIpwkQQMbQdSCMizM5KdNd8ELz"
# "o2pxVTQPLrNx6Tb29rtG3qxMVOTgeJcROeYcpFDGpW6iCjf889"

# order = sxc.get_order('203765246')
# orders = sxc.list_orders_by_codes(['203750225', '203749636', '203749135', '203749089', '203748506', '203744284', '203743829', '203743794', '203742320', '203742305', '203742289', '203742280', '203742253', '203741214', '203738236', '203735710', '203735205', '203716975', '203705138', '203705123', '203705106', '203705098', '203705076', '203702892', '203702357', '203700291', '203686901', '203686332', '203682524', '203670927', '203665584', '203665563', '203665553', '203665542', '203665532', '203665491', '203662064', '203660217', '203645233', '203628424', '203628402', '203628389', '203628377', '203628369', '203628350', '203628332', '203624093', '203617822', '203617821', '203597561', '203595424', '203594919', '203592840', '203588009', '203587995', '203587969', '203587955', '203587929', '203587899', '203579724'])
# address = sxc.generate_new_address('USDT')
# addresses = sxc.list_addresses('USDT')
# invoice = sxc.generate_ln_invoice('BTC', 1)
# order_book = sxc.list_order_book('LTC', 'BTC')
price = sxc.get_price('LTC', 'BTC')
markets = sxc.list_markets()
market_history = []
for m in sxc.scroll_market_history_by_granularity('CRW', 'BTC', datetime(2022, 1, 1, tzinfo=timezone.utc).timestamp(),
                                                  datetime(2022, 11, 30, tzinfo=timezone.utc).timestamp(),
                                                  MarketHistoryIntervals.DAYS_1.value):
    market_history.extend(m)
sxc.withdraw('LTC', '123', 11, 1)
f = sxc.list_market_history('CRW', 'BTC',
                            datetime(2019, 1, 1, tzinfo=timezone.utc).timestamp(),
                            datetime(2022, 1, 1, tzinfo=timezone.utc).timestamp(),
                            MarketHistoryIntervals.DAYS_7.value)
pass
