

from banchi.objects import convertible_pb2, stock_pb2, yield_curve_pb2, fx_rate_pb2, \
  credit_data_pb2, ticker_pb2, warrant_pb2, market_pb2, calendar_pb2, currency_pb2

def deserialize_binary(binary_data, type_str):
  obj = None
  if (type_str == "Calendar"):
    obj = calendar_pb2.Calendar()
  elif (type_str == "ConvertibleBond"):
    obj = convertible_pb2.ConvertibleData()
  elif (type_str == "CreditData"):
    obj = credit_data_pb2.CreditData()
  elif (type_str == "Currency"):
    obj = currency_pb2.Currency()
  elif (type_str == "DailyTicker"):
    obj = ticker_pb2.DailyTicker()
  elif (type_str == "FXRate"):
    obj = fx_rate_pb2.FXRate()
  elif (type_str == "Region"):
    obj = market_pb2.Region()
  elif (type_str == "Sector"):
    obj = market_pb2.Sector()
  elif (type_str == "Stock"):
    obj = stock_pb2.Stock()
  elif (type_str == "Warrant"):
    obj = warrant_pb2.WarrantData()
  elif (type_str == "YieldCurve"):
    obj = yield_curve_pb2.YieldCurve()
  else:
    raise Exception # todo, more specific
  obj.ParseFromString(binary_data)
  return obj