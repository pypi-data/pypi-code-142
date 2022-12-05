from neurosdk.__utils import raise_exception_if

from neurosdk.__cmn_types import *
from neurosdk.cmn_types import SensorInfo, SensorFamily
from neurosdk.sensor import Sensor

import platform
import pathlib
import sys

if sys.platform == "win32":
    arc = platform.architecture()
    if arc[0].__contains__("64"):
        _libname = pathlib.Path(__file__).parent.resolve() / "libs" / "neurosdk2-x64.dll"
    else:
        _libname = pathlib.Path(__file__).parent.resolve() / "libs" / "neurosdk2-x32.dll"
elif sys.platform.startswith("linux"):
    print('Add linux lib')
elif sys.platform == "darwin":
    print('Add macos lib')
else:
    raise Exception("This platform (%s) is currently not supported by pyneurosdk." % sys.platform)

_neuro_lib = CDLL(str(_libname))


class Scanner:
    def __init__(self, filters):
        """
        :param filters:
            List of device types

        :raises BaseException:
            If an internal error occurred while creating scanner
        """
        _neuro_lib.createScanner.argtypes = [POINTER(c_ubyte), c_uint, POINTER(OpStatus)]
        _neuro_lib.createScanner.restype = SensorScannerPointer
        _neuro_lib.freeScanner.argtypes = [SensorScannerPointer]
        _neuro_lib.freeScanner.restype = c_void_p
        _neuro_lib.startScanner.argtypes = [SensorScannerPointer]
        _neuro_lib.startScanner.restype = OpStatus
        _neuro_lib.stopScanner.argtypes = [SensorScannerPointer]
        _neuro_lib.stopScanner.restype = OpStatus
        _neuro_lib.sensorsScanner.argtypes = [SensorScannerPointer, POINTER(NativeSensorInfo), POINTER(c_int32)]
        _neuro_lib.sensorsScanner.restype = OpStatus
        _neuro_lib.addSensorsCallbackScanner.argtypes = [SensorScannerPointer, SensorCallbackScanner, c_void_p,
                                                         ctypes.py_object]
        _neuro_lib.addSensorsCallbackScanner.restype = OpStatus
        _neuro_lib.removeSensorsCallbackScanner.argtypes = [SensorsListenerHandle]
        _neuro_lib.removeSensorsCallbackScanner.restype = c_void_p
        _neuro_lib.createSensor.argtypes = [SensorScannerPointer, NativeSensorInfo, POINTER(OpStatus)]
        _neuro_lib.createSensor.restype = SensorPointer

        self.__create_scanner(filters)
        self.__add_sensors_callback_scanner()
        self.sensorsChanged = None

        self.__closed = False

    def __del__(self):
        try:
            if not self.__closed:
                self.__closed = True
                self.sensorsChanged = None
                _neuro_lib.removeSensorsCallbackScanner(self.__sensorsCallbackHandle)
                _neuro_lib.freeScanner(self.__ptr)
                self.__ptr = None
        except:
            pass

    def __create_scanner(self, filters: list):
        filters_len = len(filters)
        status = OpStatus()
        filters_values = (c_ubyte * filters_len)(*[filters[i].value for i in range(filters_len)])
        self.__ptr = _neuro_lib.createScanner(filters_values, filters_len, byref(status))
        raise_exception_if(status)

    def __add_sensors_callback_scanner(self):
        def __py_sensor_callback_scanner(ptr, sensors_ptr, sz_sensors, user_data):
            sensors = [SensorInfo(SensFamily=SensorFamily(sensors_ptr[i].SensFamily),
                                  SensModel=sensors_ptr[i].SensModel,
                                  Name=''.join([chr(c) for c in sensors_ptr[i].Name]).rstrip('\x00'),
                                  Address=''.join([chr(c) for c in sensors_ptr[i].Address]).rstrip('\x00'),
                                  SerialNumber=''.join([chr(c) for c in sensors_ptr[i].SerialNumber]).rstrip('\x00'),
                                  PairingRequired=bool(int(sensors_ptr[i].PairingRequired))) for i in range(sz_sensors)]
            if user_data.sensorsChanged is not None:
                user_data.sensorsChanged(user_data, sensors)

        self.__sensorsCallback = SensorCallbackScanner(__py_sensor_callback_scanner)
        self.__sensorsCallbackHandle = SensorsListenerHandle()
        raise_exception_if(_neuro_lib.addSensorsCallbackScanner(self.__ptr, self.__sensorsCallback,
                                                                byref(self.__sensorsCallbackHandle), py_object(self)))

    def Sensors(self) -> [SensorInfo]:
        """
        The method requests all found and valid devices in the current search session

        :return:
            List of founded devices

        :raises BaseException:
            If an internal error occurred while getting sensors list
        """
        sz_sensors_in_out = SizeType(c_int32(64))
        SIP = POINTER(NativeSensorInfo)
        sensors = SIP(NativeSensorInfo())
        raise_exception_if(_neuro_lib.sensorsScanner(self.__ptr, sensors, sz_sensors_in_out))
        infos = []
        for i in range(sz_sensors_in_out.contents.value):
            infos.append(SensorInfo(SensFamily=SensorFamily(sensors[i].SensFamily),
                                    SensModel=sensors[i].SensModel,
                                    Name=''.join([chr(c) for c in sensors[i].Name]).rstrip('\x00'),
                                    Address=''.join([chr(c) for c in sensors[i].Address]).rstrip('\x00'),
                                    SerialNumber=''.join([chr(c) for c in sensors[i].SerialNumber]).rstrip('\x00'),
                                    PairingRequired=bool(int(sensors[i].PairingRequired))))
        return infos

    def Start(self):
        """
        Starts the process of searching for devices according to the specified parameters. If the device is found,
        sensorsChanged callback will be called. If the device leaves the scope for any reason, it will disappear from the list of
        found devices after 12 seconds

        :raises BaseException:
            If an internal error occurred while starting search
        """
        raise_exception_if(_neuro_lib.startScanner(self.__ptr))

    def Stop(self):
        """
        Stops the process of searching for devices

        :raises BaseException:
            If an internal error occurred while stopping search
        """
        raise_exception_if(_neuro_lib.stopScanner(self.__ptr))

    def CreateSensor(self, sensor_info: SensorInfo) -> Sensor:
        """
        Creates an instance of the device according to the information received, and automatically connects to it. The
        connection callback will not be called. If the connection is successful, a Sensor instance will be returned,
        otherwise an exception will be thrown

        :param sensor_info: SensorInfo
            Info about device.
        :return: Sensor
            Connected device object
        :raises BaseException:
            If an internal error occurred while creating device

        """
        status = OpStatus()
        si = NativeSensorInfo()
        si.SensFamily = sensor_info.SensFamily.value
        si.SensorModel = sensor_info.SensModel
        si.Name = sensor_info.Name.encode('utf-8')
        si.Address = sensor_info.Address.encode('utf-8')
        si.SerialNumber = sensor_info.SerialNumber.encode('utf-8')
        si.PairingRequired = int(sensor_info.PairingRequired)

        sensor_ptr = _neuro_lib.createSensor(self.__ptr, si, byref(status))
        raise_exception_if(status)
        return Sensor(sensor_ptr)
