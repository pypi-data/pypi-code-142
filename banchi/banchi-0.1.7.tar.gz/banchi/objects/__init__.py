import sys
import os
import importlib
generated_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(generated_dir) # needed so that proto generated python modules can locate their dependencies

# idea for importing dynamically, not currently working
#for module in os.listdir(generated_dir):
#    if module != '__init__.py' and module[-6:] == '_pb2.py':
#        module_name = module[:-3]
#        as_module_name = module[:-5]
#        globals()[as_module_name] = importlib.import_module(module_name, "banchi.objects")

import banchi.objects.bond_pb2 as bond
import banchi.objects.calendar_pb2 as calendar
import banchi.objects.cashflows_pb2 as cashflows
import banchi.objects.conversion_pb2 as conversion
import banchi.objects.convertible_calc_pb2 as convertible_calc
import banchi.objects.convertible_call_schedule_pb2 as convertible_call_schedule
import banchi.objects.convertible_pb2 as convertible
import banchi.objects.date_pb2 as date
import banchi.objects.dividend_protection_pb2 as dividend_protection
import banchi.objects.enums_pb2 as enums
import banchi.objects.fx_rate_pb2 as fx_rate
import banchi.objects.interest_rate_index_pb2 as interest_rate_index
import banchi.objects.make_whole_pb2 as make_whole
import banchi.objects.market_pb2 as market
import banchi.objects.matrix_pb2 as matrix
import banchi.objects.model_parameters_pb2 as model_parameters
import banchi.objects.object_info_pb2 as object_info
import banchi.objects.offset_pb2 as offset
import banchi.objects.output_pb2 as output
import banchi.objects.put_schedule_pb2 as put_schedule
import banchi.objects.stock_pb2 as stock
import banchi.objects.ticker_pb2 as ticker
import banchi.objects.trigger_pb2 as trigger
import banchi.objects.warrant_call_schedule_pb2 as warrant_call_schedule
import banchi.objects.warrant_pb2 as warrant
import banchi.objects.yield_curve_pb2 as yield_curve