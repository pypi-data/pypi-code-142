
import sqlite3
from banchi.objects import convertible_pb2, stock_pb2, fx_rate_pb2
from banchi import serialization

from enum import Enum

class MarshallSubObjects(Enum):
  NONE = 1
  ALL = 2

class DataService:

  local_file = ""
  local_con = None


  def __init__(self,*,local_file):
    self.local_file = local_file
    self.local_con = sqlite3.connect(self.local_file)
  
  def marshall_sub_objects(self, obj, marshall_sub_objs):
    if(marshall_sub_objs != MarshallSubObjects.NONE):
      if (isinstance(obj, convertible_pb2.ConvertibleData)):
        obj.stock.CopyFrom(self.get_object(obj.stock.object.id, marshall_sub_objs, obj.stock))
        obj.instrument_risk_free_curve.CopyFrom(self.get_object(obj.instrument_risk_free_curve.object.id, \
          marshall_sub_objs, obj.instrument_risk_free_curve))
        obj.instrument_credit_data.CopyFrom(self.get_object(obj.instrument_credit_data.object.id, \
          marshall_sub_objs, obj.instrument_credit_data))
        obj.info.region.CopyFrom(self.get_object(obj.info.region.object.id, marshall_sub_objs, obj.info.region))
        obj.fx_rate.CopyFrom(self.get_object(obj.fx_rate.object.id, marshall_sub_objs, obj.fx_rate))
        obj.instrument_calendar.CopyFrom(self.get_object(obj.instrument_calendar.object.id, marshall_sub_objs, obj.instrument_calendar))
        obj.instrument.currency.CopyFrom(self.get_object(obj.instrument.currency.object.id, marshall_sub_objs, obj.instrument.currency))
      if (isinstance(obj, stock_pb2.Stock)):
        obj.time_series.close_prices.CopyFrom(self.get_object(obj.time_series.close_prices.object.id, \
          marshall_sub_objs, obj.time_series.close_prices))
        obj.time_series.open_prices.CopyFrom(self.get_object(obj.time_series.open_prices.object.id, \
          marshall_sub_objs, obj.time_series.open_prices))
        obj.time_series.high_prices.CopyFrom(self.get_object(obj.time_series.high_prices.object.id, \
          marshall_sub_objs, obj.time_series.high_prices))
        obj.time_series.low_prices.CopyFrom(self.get_object(obj.time_series.low_prices.object.id, \
          marshall_sub_objs, obj.time_series.low_prices))
        obj.time_series.vwaps.CopyFrom(self.get_object(obj.time_series.vwaps.object.id, \
          marshall_sub_objs, obj.time_series.vwaps))
        obj.calendar.CopyFrom(self.get_object(obj.calendar.object.id, marshall_sub_objs, obj.calendar))
        obj.info.region.CopyFrom(self.get_object(obj.info.region.object.id, marshall_sub_objs, obj.info.region))
        obj.info.sector.CopyFrom(self.get_object(obj.info.sector.object.id, marshall_sub_objs, obj.info.sector))
        obj.currency.CopyFrom(self.get_object(obj.currency.object.id, marshall_sub_objs, obj.currency))
      if (isinstance(obj, fx_rate_pb2.FXRate)):
        obj.time_series.close_rates.CopyFrom(self.get_object(obj.time_series.close_rates.object.id, \
          marshall_sub_objs, obj.time_series.close_rates))
        obj.time_series.open_rates.CopyFrom(self.get_object(obj.time_series.open_rates.object.id, \
          marshall_sub_objs, obj.time_series.open_rates))
        obj.time_series.high_rates.CopyFrom(self.get_object(obj.time_series.high_rates.object.id, \
          marshall_sub_objs, obj.time_series.high_rates))
        obj.time_series.low_rates.CopyFrom(self.get_object(obj.time_series.low_rates.object.id, \
          marshall_sub_objs, obj.time_series.low_rates))
    return obj

  def get_object(self, id, marshall_sub_objs=MarshallSubObjects.NONE, obj=None):
    if (id == ""):
      return obj
    id_split = id.split(':', 2)
    type_str = id_split[0]
    cur = self.local_con.cursor()
    res = cur.execute("SELECT Data FROM {} WHERE Id='{}'".format(type_str, id))
    binary_data = res.fetchone()[0]
    
    obj = serialization.deserialize_binary(binary_data, type_str)
    obj = self.marshall_sub_objects(obj, marshall_sub_objs)
    return obj


  def get_objects_of_type(self, type_str, marshall_sub_objs=MarshallSubObjects.NONE):
    cur = self.local_con.cursor()
    res = cur.execute("SELECT Data FROM {}".format(type_str))
    all_data = res.fetchall()
    binary_data = all_data[0]
    objs = []
    for data in all_data:
      binary_data = data[0]
      obj = serialization.deserialize_binary(binary_data, type_str)
      obj = self.marshall_sub_objects(obj, marshall_sub_objs)
      objs.append(obj)
    return objs