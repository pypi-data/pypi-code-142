import ctypes
import os, sys

banchi_home = os.getenv('BANCHILIB_HOME', default='.')

if sys.platform.startswith('linux'):
    BANCHI_C = ctypes.CDLL(banchi_home + "/lib/libbanchi_c.so")
else:
    BANCHI_C = ctypes.CDLL(banchi_home + "/bin/banchi_c")


def schema_version():
    return BANCHI_C.SchemaVersion()
    
def version_string():
    return str(BANCHI_C.MajorVersion()) + "." + str(BANCHI_C.SchemaVersion())

def calc_yield_curve(curve_calc):
    ycCalcData = curve_calc.SerializeToString()
    out_handle = ctypes.c_void_p(0)
    out_size_handle = ctypes.c_int(0)
    BANCHI_C.CalcYieldCurve(ycCalcData, len(ycCalcData), ctypes.byref(out_handle), ctypes.byref(out_size_handle))
    curve_calc.outputs.ParseFromString(ctypes.string_at(out_handle, out_size_handle))
    BANCHI_C.DeleteBuffer(out_handle)

def calc_convertible(calc):
    calc_data = calc.SerializeToString()
    out_handle = ctypes.c_void_p(0)
    out_size_handle = ctypes.c_int(0)
    BANCHI_C.CalcConvertible(calc_data, len(calc_data), ctypes.byref(out_handle), ctypes.byref(out_size_handle))
    calc.outputs.ParseFromString(ctypes.string_at(out_handle, out_size_handle))
    BANCHI_C.DeleteBuffer(out_handle)