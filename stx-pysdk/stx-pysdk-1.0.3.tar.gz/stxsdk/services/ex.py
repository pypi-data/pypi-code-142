from stxsdk import Selection

return_fields = {
    'archived': 'Boolean', 'closedAt': 'String', 'position': 'String', 'price': 'Float',
    'description': 'String', 'detailedEventBrief': 'String', 'eventBrief': 'String', 'eventId': 'rID',
    'eventStart': 'String', 'eventStatus': 'String', 'eventType': 'String',
    'homeCategory': 'String', 'lastProbabilityAt': 'DateTime', 'lastTradedPrice': 'Int',
    'manualProbability': 'Boolean', 'marketId': 'rID', 'maxPrice': 'Int', 'status': 'String',
    'priceChange24h': 'Int', 'probability': 'Float', 'question': 'String', 'symbol': 'String',
    'result': 'String', 'rulesSpecifier': 'String', 'shortTitle': 'String', 'specifier': 'String',
    'timestamp': 'String', 'timestampInt': 'Int', 'title': 'String', 'volume24h': 'Int',
    'orderPriceRules': {'from': 'Int', 'inc': 'Int', 'to': 'Int'},
    'offers': {'price': 'Int', 'quantity': 'Int'},
    'bids': {'price': 'Int', 'quantity': {"t1": "str", "t2": "str"}},
    'filters': {'category': 'String', 'manual': 'Boolean', 'section': 'String', 'subcategory': 'String'},
    'tradingFilters': {'category': 'String', 'manual': 'Boolean', 'section': 'String', 'subcategory': 'String'},
    'recentTrades': {'liquidityTaker': 'String', 'price': 'Int', 'quantity': 'Int', 'timestamp': 'String', 'timestampInt': 'Int'},
}


def get_selections(fields):
    values, nested = [], {}
    for field_name, field_value in fields.items():
        if isinstance(field_value, str):
            values.append(field_name)
        else:
            nested[field_name] = get_selections(field_value)
    return Selection(*values, **nested)


selections = get_selections(return_fields)
print()
