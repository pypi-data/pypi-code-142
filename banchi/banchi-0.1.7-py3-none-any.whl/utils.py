from banchi.objects.date_pb2 import Date
from datetime import datetime, date, timedelta

serial_number_ref_date = date(1899, 12, 30)

def to_pydate(banchi_date):
  if (banchi_date.serial_number == 0):
    return None
  py_date = serial_number_ref_date
  py_date += timedelta(days=banchi_date.serial_number)
  return py_date

def from_pydate(py_date):
  banchi_date = Date()
  if (py_date != None):
    banchi_date.serial_number = (py_date - serial_number_ref_date).days
  return banchi_date