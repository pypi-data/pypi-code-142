from stxsdk import StxClient, Selection

client = StxClient()
order_price_rules = Selection("from", "inc", "to")
selections = Selection(
    "closedAt",
    "description",
    "eventId",
    "marketId",
    "title",
    "status",
    orderPriceRules=order_price_rules,
    # inline selection object
    bids=Selection("price", "quantity"),
)
client.marketInfos()
