from neurosdk.__utils import raise_exception_if
from neurosdk.__cmn_types import *
from neurosdk.cmn_types import *

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
    raise Exception("This platform (%s) is currently not supported by py_neurosdk." % sys.platform)

_neuro_lib = CDLL(str(_libname))


class Sensor:
    def __init__(self, ptr):
        """
        Don't use it to creation device

        -----------
        :param ptr:
            Inner pointer to Sensor object
        """
        _neuro_lib.freeSensor.argtypes = [SensorPointer]
        _neuro_lib.freeSensor.restype = c_void_p
        _neuro_lib.connectSensor.argtypes = [SensorPointer]
        _neuro_lib.connectSensor.restype = OpStatus
        _neuro_lib.disconnectSensor.argtypes = [SensorPointer]
        _neuro_lib.disconnectSensor.restype = OpStatus
        _neuro_lib.getFeaturesCountSensor.argtypes = [SensorPointer]
        _neuro_lib.getFeaturesCountSensor.restype = c_int32
        _neuro_lib.getFeaturesSensor.argtypes = [SensorPointer, POINTER(c_int8), POINTER(c_int32)]
        _neuro_lib.getFeaturesSensor.restype = OpStatus
        _neuro_lib.isSupportedFeatureSensor.argtypes = [SensorPointer, c_int8]
        _neuro_lib.isSupportedFeatureSensor.restype = c_int8
        _neuro_lib.getCommandsCountSensor.argtypes = [SensorPointer]
        _neuro_lib.getCommandsCountSensor.restype = c_int32
        _neuro_lib.getCommandsSensor.argtypes = [SensorPointer, POINTER(c_int8), POINTER(c_int32)]
        _neuro_lib.getCommandsSensor.restype = OpStatus
        _neuro_lib.isSupportedCommandSensor.argtypes = [SensorPointer, c_int8]
        _neuro_lib.isSupportedCommandSensor.restype = c_int8
        _neuro_lib.getParametersCountSensor.argtypes = [SensorPointer]
        _neuro_lib.getParametersCountSensor.restype = c_int32
        _neuro_lib.getParametersSensor.argtypes = [SensorPointer, POINTER(NativeParameterInfo), POINTER(c_int32)]
        _neuro_lib.getParametersSensor.restype = OpStatus
        _neuro_lib.isSupportedParameterSensor.argtypes = [SensorPointer, c_int8]
        _neuro_lib.isSupportedParameterSensor.restype = c_int8
        _neuro_lib.getChannelsCountSensor.argtypes = [SensorPointer]
        _neuro_lib.getChannelsCountSensor.restype = c_int32
        _neuro_lib.execCommandSensor.argtypes = [SensorPointer, c_int8]
        _neuro_lib.execCommandSensor.restype = OpStatus
        _neuro_lib.getFamilySensor.argtypes = [SensorPointer]
        _neuro_lib.getFamilySensor.restype = c_int8
        _neuro_lib.readNameSensor.argtypes = [SensorPointer, c_char_p, c_int32]
        _neuro_lib.readNameSensor.restype = OpStatus
        _neuro_lib.writeNameSensor.argtypes = [SensorPointer, c_char_p, c_int32]
        _neuro_lib.writeNameSensor.restype = OpStatus
        _neuro_lib.readStateSensor.argtypes = [SensorPointer, POINTER(c_int8)]
        _neuro_lib.readStateSensor.restype = OpStatus
        _neuro_lib.readAddressSensor.argtypes = [SensorPointer, c_char_p, c_int32]
        _neuro_lib.readAddressSensor.restype = OpStatus
        _neuro_lib.readSerialNumberSensor.argtypes = [SensorPointer, c_char_p, c_int32]
        _neuro_lib.readSerialNumberSensor.restype = OpStatus
        _neuro_lib.writeSerialNumberSensor.argtypes = [SensorPointer, c_char_p, c_int32]
        _neuro_lib.writeSerialNumberSensor.restype = OpStatus
        _neuro_lib.readBattPowerSensor.argtypes = [SensorPointer, POINTER(c_int32)]
        _neuro_lib.readBattPowerSensor.restype = OpStatus
        _neuro_lib.readHardwareFiltersSensor.argtypes = [SensorPointer, POINTER(c_int8), POINTER(c_int32)]
        _neuro_lib.readHardwareFiltersSensor.restype = OpStatus
        _neuro_lib.writeHardwareFiltersSensor.argtypes = [SensorPointer, POINTER(c_int8), c_int32]
        _neuro_lib.writeHardwareFiltersSensor.restype = OpStatus
        _neuro_lib.readSamplingFrequencySensor.argtypes = [SensorPointer, POINTER(c_int8)]
        _neuro_lib.readSamplingFrequencySensor.restype = OpStatus
        _neuro_lib.writeSamplingFrequencySensor.argtypes = [SensorPointer, c_int8]
        _neuro_lib.writeSamplingFrequencySensor.restype = OpStatus
        _neuro_lib.readGainSensor.argtypes = [SensorPointer, POINTER(c_int8)]
        _neuro_lib.readGainSensor.restype = OpStatus
        _neuro_lib.writeGainSensor.argtypes = [SensorPointer, c_int8]
        _neuro_lib.writeGainSensor.arestype = OpStatus
        _neuro_lib.readDataOffsetSensor.argtypes = [SensorPointer, POINTER(c_uint8)]
        _neuro_lib.readDataOffsetSensor.restype = OpStatus
        _neuro_lib.writeDataOffsetSensor.argtypes = [SensorPointer, c_uint8]
        _neuro_lib.writeDataOffsetSensor.restype = OpStatus
        _neuro_lib.readExternalSwitchSensor.argtypes = [SensorPointer, POINTER(c_int8)]
        _neuro_lib.readExternalSwitchSensor.restype = OpStatus
        _neuro_lib.writeExternalSwitchSensor.argtypes = [SensorPointer, c_int8]
        _neuro_lib.writeExternalSwitchSensor.restype = OpStatus
        _neuro_lib.readADCInputSensor.argtypes = [SensorPointer, POINTER(c_int8)]
        _neuro_lib.readADCInputSensor.restype = OpStatus
        _neuro_lib.writeADCInputSensor.argtypes = [SensorPointer, c_int8]
        _neuro_lib.writeADCInputSensor.restype = OpStatus
        _neuro_lib.readAccelerometerSensSensor.argtypes = [SensorPointer, POINTER(c_int8)]
        _neuro_lib.readAccelerometerSensSensor.restype = OpStatus
        _neuro_lib.writeAccelerometerSensSensor.argtypes = [SensorPointer, c_int8]
        _neuro_lib.writeAccelerometerSensSensor.restype = OpStatus
        _neuro_lib.readGyroscopeSensSensor.argtypes = [SensorPointer, POINTER(c_int8)]
        _neuro_lib.readGyroscopeSensSensor.restype = OpStatus
        _neuro_lib.writeGyroscopeSensSensor.argtypes = [SensorPointer, c_int8]
        _neuro_lib.writeGyroscopeSensSensor.restype = OpStatus
        _neuro_lib.readFirmwareModeSensor.argtypes = [SensorPointer, POINTER(c_int8)]
        _neuro_lib.readFirmwareModeSensor.restype = OpStatus
        _neuro_lib.writeFirmwareModeSensor.argtypes = [SensorPointer, c_int8]
        _neuro_lib.writeFirmwareModeSensor.restype = OpStatus
        _neuro_lib.readVersionSensor.argtypes = [SensorPointer, POINTER(NativeSensorVersion)]
        _neuro_lib.readVersionSensor.restype = OpStatus
        _neuro_lib.readSamplingFrequencyFPGSensor.argtypes = [SensorPointer, POINTER(c_int8)]
        _neuro_lib.readSamplingFrequencyFPGSensor.restype = OpStatus
        _neuro_lib.readSamplingFrequencyMEMSSensor.argtypes = [SensorPointer, POINTER(c_int8)]
        _neuro_lib.readSamplingFrequencyMEMSSensor.restype = OpStatus
        _neuro_lib.readSamplingFrequencyResistSensor.argtypes = [SensorPointer, POINTER(c_int8)]
        _neuro_lib.readSamplingFrequencyResistSensor.restype = OpStatus
        _neuro_lib.readSamplingFrequencyRespSensor.argtypes = [SensorPointer, POINTER(c_int8)]
        _neuro_lib.readSamplingFrequencyRespSensor.restype = OpStatus
        _neuro_lib.readAmpMode.argtypes = [SensorPointer, POINTER(c_uint8)]
        _neuro_lib.readAmpMode.restype = OpStatus
        _neuro_lib.readStimulatorAndMAStateCallibri.argtypes = [SensorPointer, POINTER(NativeCallibriStimulatorMAState)]
        _neuro_lib.readStimulatorAndMAStateCallibri.restype = OpStatus
        _neuro_lib.readStimulatorParamCallibri.argtypes = [SensorPointer, POINTER(NativeCallibriStimulationParams)]
        _neuro_lib.readStimulatorParamCallibri.restype = OpStatus
        _neuro_lib.writeStimulatorParamCallibri.argtypes = [SensorPointer, NativeCallibriStimulationParams]
        _neuro_lib.writeStimulatorParamCallibri.restype = OpStatus
        _neuro_lib.readMotionAssistantParamCallibri.argtypes = [SensorPointer,
                                                                POINTER(NativeCallibriMotionAssistantParams)]
        _neuro_lib.readMotionAssistantParamCallibri.restype = OpStatus
        _neuro_lib.writeMotionAssistantParamCallibri.argtypes = [SensorPointer, NativeCallibriMotionAssistantParams]
        _neuro_lib.writeMotionAssistantParamCallibri.restype = OpStatus
        _neuro_lib.readMotionCounterParamCallibri.argtypes = [SensorPointer, POINTER(NativeCallibriMotionCounterParam)]
        _neuro_lib.readMotionCounterParamCallibri.restype = OpStatus
        _neuro_lib.writeMotionCounterParamCallibri.argtypes = [SensorPointer, NativeCallibriMotionCounterParam]
        _neuro_lib.writeMotionCounterParamCallibri.restype = OpStatus
        _neuro_lib.readMotionCounterCallibri.argtypes = [SensorPointer, POINTER(c_uint32)]
        _neuro_lib.readMotionCounterCallibri.restype = OpStatus
        _neuro_lib.readColorCallibri.argtypes = [SensorPointer, POINTER(c_int)]
        _neuro_lib.readIrAmplitudeHeadband.argtypes = [SensorPointer, POINTER(c_uint8)]
        _neuro_lib.readIrAmplitudeHeadband.restype = OpStatus
        _neuro_lib.writeIrAmplitudeHeadband.argtypes = [SensorPointer, c_int8]
        _neuro_lib.writeIrAmplitudeHeadband.restype = OpStatus
        _neuro_lib.readRedAmplitudeHeadband.argtypes = [SensorPointer, POINTER(c_uint8)]
        _neuro_lib.readRedAmplitudeHeadband.restype = OpStatus
        _neuro_lib.writeRedAmplitudeHeadband.argtypes = [SensorPointer, c_uint8]
        _neuro_lib.writeRedAmplitudeHeadband.restype = OpStatus
        _neuro_lib.pingNeuroSmart.argtypes = [SensorPointer, c_uint8]
        _neuro_lib.pingNeuroSmart.restype = OpStatus
        _neuro_lib.readStimulatorParamCompactNeuro.argtypes = [SensorPointer, POINTER(NativeCompactNeuroStimulParam)]
        _neuro_lib.readStimulatorParamCompactNeuro.restype = OpStatus
        _neuro_lib.writeStimulatorParamCompactNeuro.argtypes = [SensorPointer, NativeCompactNeuroStimulParam]
        _neuro_lib.writeStimulatorParamCompactNeuro.restype = OpStatus
        _neuro_lib.readSupportedChannelsCompactNeuro.argtypes = [SensorPointer, POINTER(NativeEEGChannelInfo),
                                                                 POINTER(c_int32)]
        _neuro_lib.readSupportedChannelsCompactNeuro.restype = OpStatus
        _neuro_lib.addBatteryCallback.argtypes = [SensorPointer, BatteryCallback, c_void_p, ctypes.py_object]
        _neuro_lib.addBatteryCallback.restype = OpStatus
        _neuro_lib.removeBatteryCallback.argtypes = [BattPowerListenerHandle]
        _neuro_lib.removeBatteryCallback.restype = c_void_p
        _neuro_lib.addMEMSDataCallback.argtypes = [SensorPointer, MEMSDataCallback, c_void_p, ctypes.py_object]
        _neuro_lib.addMEMSDataCallback.restype = OpStatus
        _neuro_lib.removeMEMSDataCallback.argtypes = [MEMSDataListenerHandle]
        _neuro_lib.removeMEMSDataCallback.restype = c_void_p
        _neuro_lib.addQuaternionDataCallback.argtypes = [SensorPointer, QuaternionDataCallback, c_void_p,
                                                         ctypes.py_object]
        _neuro_lib.addQuaternionDataCallback.restype = OpStatus
        _neuro_lib.removeQuaternionDataCallback.argtypes = [QuaternionDataListenerHandle]
        _neuro_lib.removeQuaternionDataCallback.restype = c_void_p
        _neuro_lib.addConnectionStateCallback.argtypes = [SensorPointer, ConnectionStateCallback, c_void_p,
                                                          ctypes.py_object]
        _neuro_lib.addConnectionStateCallback.restype = OpStatus
        _neuro_lib.removeConnectionStateCallback.argtypes = [SensorStateListenerHandle]
        _neuro_lib.removeConnectionStateCallback.restype = c_void_p
        _neuro_lib.addAmpModeCallback.argtypes = [SensorPointer, AmpModeCallback, c_void_p, ctypes.py_object]
        _neuro_lib.addAmpModeCallback.restype = OpStatus
        _neuro_lib.removeAmpModeCallback.argtypes = [AmpModeListenerHandle]
        _neuro_lib.removeAmpModeCallback.restype = c_void_p
        _neuro_lib.addSignalCallbackCallibri.argtypes = [SensorPointer, SignalCallbackCallibri, c_void_p,
                                                         ctypes.py_object]
        _neuro_lib.addSignalCallbackCallibri.restype = OpStatus
        _neuro_lib.removeSignalCallbackCallibri.argtypes = [CallibriSignalDataListenerHandle]
        _neuro_lib.removeSignalCallbackCallibri.restype = c_void_p
        _neuro_lib.addRespirationCallbackCallibri.argtypes = [SensorPointer, RespirationCallbackCallibri, c_void_p,
                                                              ctypes.py_object]
        _neuro_lib.addRespirationCallbackCallibri.restype = OpStatus
        _neuro_lib.removeRespirationCallbackCallibri.argtypes = [CallibriRespirationDataListenerHandle]
        _neuro_lib.removeRespirationCallbackCallibri.restype = c_void_p
        _neuro_lib.addElectrodeStateCallbackCallibri.argtypes = [SensorPointer, ElectrodeStateCallbackCallibri,
                                                                 c_void_p, ctypes.py_object]
        _neuro_lib.addElectrodeStateCallbackCallibri.restype = OpStatus
        _neuro_lib.removeElectrodeStateCallbackCallibri.argtypes = [CallibriElectrodeStateListenerHandle]
        _neuro_lib.removeElectrodeStateCallbackCallibri.restype = c_void_p
        _neuro_lib.addEnvelopeDataCallbackCallibri.argtypes = [SensorPointer, EnvelopeDataCallbackCallibri, c_void_p,
                                                               ctypes.py_object]
        _neuro_lib.addEnvelopeDataCallbackCallibri.restype = OpStatus
        _neuro_lib.removeEnvelopeDataCallbackCallibri.argtypes = [CallibriEnvelopeDataListenerHandle]
        _neuro_lib.removeEnvelopeDataCallbackCallibri.restype = c_void_p
        _neuro_lib.addFPGDataCallbackNeuroSmart.argtypes = [SensorPointer, FPGDataCallbackNeuroSmart, c_void_p,
                                                            ctypes.py_object]
        _neuro_lib.addFPGDataCallbackNeuroSmart.restype = OpStatus
        _neuro_lib.removeFPGDataCallbackNeuroSmart.argtypes = [FPGDataListenerHandle]
        _neuro_lib.removeFPGDataCallbackNeuroSmart.restype = c_void_p
        _neuro_lib.addResistCallbackBrainBit.argtypes = [SensorPointer, ResistCallbackBrainBit, c_void_p,
                                                         ctypes.py_object]
        _neuro_lib.addResistCallbackBrainBit.restype = OpStatus
        _neuro_lib.removeResistCallbackBrainBit.argtypes = [BrainBitResistDataListenerHandle]
        _neuro_lib.removeResistCallbackBrainBit.restype = c_void_p
        _neuro_lib.addSignalDataCallbackBrainBit.argtypes = [SensorPointer, SignalDataCallbackBrainBit, c_void_p,
                                                             ctypes.py_object]
        _neuro_lib.addSignalDataCallbackBrainBit.restype = OpStatus
        _neuro_lib.removeSignalDataCallbackBrainBit.argtypes = [BrainBitSignalDataListenerHandle]
        _neuro_lib.removeSignalDataCallbackBrainBit.restype = c_void_p
        _neuro_lib.addResistCallbackHeadband.argtypes = [SensorPointer, ResistCallbackHeadband, c_void_p,
                                                         ctypes.py_object]
        _neuro_lib.addResistCallbackHeadband.restype = OpStatus
        _neuro_lib.removeResistCallbackHeadband.argtypes = [HeadbandResistDataListenerHandle]
        _neuro_lib.removeResistCallbackHeadband.restype = c_void_p
        _neuro_lib.addSignalDataCallbackHeadband.argtypes = [SensorPointer, SignalDataCallbackHeadband, c_void_p,
                                                             ctypes.py_object]
        _neuro_lib.addSignalDataCallbackHeadband.restype = OpStatus
        _neuro_lib.removeSignalDataCallbackHeadband.argtypes = [HeadbandSignalDataListenerHandle]
        _neuro_lib.removeSignalDataCallbackHeadband.restype = c_void_p
        _neuro_lib.readAmplifierParamHeadphones.argtypes = [SensorPointer, POINTER(NativeHeadphonesAmplifierParam)]
        _neuro_lib.readAmplifierParamHeadphones.restype = OpStatus
        _neuro_lib.writeAmplifierParamHeadphones.argtypes = [SensorPointer, NativeHeadphonesAmplifierParam]
        _neuro_lib.writeAmplifierParamHeadphones.restype = OpStatus
        _neuro_lib.addResistCallbackHeadphones.argtypes = [SensorPointer, ResistCallbackHeadphones, c_void_p,
                                                           ctypes.py_object]
        _neuro_lib.addResistCallbackHeadphones.restype = OpStatus
        _neuro_lib.removeResistCallbackHeadphones.argtypes = [HeadphonesResistDataListenerHandle]
        _neuro_lib.removeResistCallbackHeadphones.restype = c_void_p
        _neuro_lib.addSignalDataCallbackHeadphones.argtypes = [SensorPointer, SignalDataCallbackHeadphones, c_void_p,
                                                               ctypes.py_object]
        _neuro_lib.addSignalDataCallbackHeadphones.restype = OpStatus
        _neuro_lib.removeSignalDataCallbackHeadphones.argtypes = [HeadphonesSignalDataListenerHandle]
        _neuro_lib.removeSignalDataCallbackHeadphones.restype = c_void_p

        _neuro_lib.readAmplifierParamHeadphones2.argtypes = [SensorPointer, POINTER(NativeHeadphones2AmplifierParam)]
        _neuro_lib.readAmplifierParamHeadphones2.restype = OpStatus
        _neuro_lib.writeAmplifierParamHeadphones2.argtypes = [SensorPointer, NativeHeadphones2AmplifierParam]
        _neuro_lib.writeAmplifierParamHeadphones2.restype = OpStatus
        _neuro_lib.addResistCallbackHeadphones2.argtypes = [SensorPointer, ResistCallbackHeadphones2, c_void_p,
                                                            ctypes.py_object]
        _neuro_lib.addResistCallbackHeadphones2.restype = OpStatus
        _neuro_lib.removeResistCallbackHeadphones2.argtypes = [Headphones2ResistDataListenerHandle]
        _neuro_lib.removeResistCallbackHeadphones2.restype = c_void_p
        _neuro_lib.addSignalDataCallbackHeadphones2.argtypes = [SensorPointer, SignalDataCallbackHeadphones2, c_void_p,
                                                                ctypes.py_object]
        _neuro_lib.addSignalDataCallbackHeadphones2.restype = OpStatus
        _neuro_lib.removeSignalDataCallbackHeadphones2.argtypes = [Headphones2SignalDataListenerHandle]
        _neuro_lib.removeSignalDataCallbackHeadphones2.restype = c_void_p

        _neuro_lib.addResistCallbackCompactNeuro.argtypes = [SensorPointer, ResistCallbackCompactNeuro, c_void_p,
                                                             ctypes.py_object]
        _neuro_lib.addResistCallbackCompactNeuro.restype = OpStatus
        _neuro_lib.removeResistCallbackCompactNeuro.argtypes = [CompactNeuroResistDataListenerHandle]
        _neuro_lib.removeResistCallbackCompactNeuro.restype = c_void_p
        _neuro_lib.addSignalDataCallbackCompactNeuro.argtypes = [SensorPointer, SignalDataCallbackCompactNeuro,
                                                                 c_void_p, ctypes.py_object]
        _neuro_lib.addSignalDataCallbackCompactNeuro.restype = OpStatus
        _neuro_lib.removeSignalDataCallbackCompactNeuro.argtypes = [CompactNeuroSignalDataListenerHandle]
        _neuro_lib.removeSignalDataCallbackCompactNeuro.restype = c_void_p

        self.__ptr = ptr

        if self.IsSupportedParameter(SensorParameter.ParameterBattPower):
            self.batteryChanged = None
            self.__add_battery_callback()

        s_family = self.SensFamily
        if self.IsSupportedFeature(SensorFeature.FeatureMEMS):
            self.memsDataReceived = None
            self.__add_mems_data_callback()
            if s_family == SensorFamily.SensorLECallibri or s_family == SensorFamily.SensorLEKolibri:
                self.quaternionDataReceived = None
                self.__add_quaternion_data_callback()
        self.sensorStateChanged = None
        self.__add_connection_state_callback()
        if s_family == SensorFamily.SensorLECallibri or s_family == SensorFamily.SensorLEKolibri:
            self.callibriSignalDataReceived = None
            self.__add_signal_callback_callibri()
            if self.IsSupportedFeature(SensorFeature.FeatureRespiration):
                self.callibriRespirationDataReceived = None
                self.__add_respiration_callback_callibri()
            self.callibriElectrodeStateChanged = None
            self.__add_electrode_state_callback_callibri()
            if self.IsSupportedFeature(SensorFeature.FeatureEnvelope):
                self.callibriEnvelopeDataReceived = None
                self.__add_envelope_data_callback_callibri()
        elif s_family == SensorFamily.SensorLEBrainBit or s_family == SensorFamily.SensorLEBrainBitBlack or s_family == SensorFamily.SensorLEHeadband:
            if s_family == SensorFamily.SensorLEBrainBitBlack or s_family == SensorFamily.SensorLEHeadband:
                self.sensorAmpModeChanged = None
                self.__add_amp_mode_callback()
            if self.IsSupportedFeature(SensorFeature.FeatureFPG):
                self.fpgDataReceived = None
                self.__add_FPG_data_callback_neuro_smart()
            if s_family == SensorFamily.SensorLEHeadband:
                if self.IsSupportedFeature(SensorFeature.FeatureResist):
                    self.headbandResistDataReceived = None
                    self.__add_resist_callback_headband()
                if self.IsSupportedFeature(SensorFeature.FeatureSignal):
                    self.headbandSignalDataReceived = None
                    self.__add_signal_data_callback_headband()
            else:
                if self.IsSupportedFeature(SensorFeature.FeatureResist):
                    self.brainBitResistDataReceived = None
                    self.__add_resist_callback_brain_bit()
                if self.IsSupportedFeature(SensorFeature.FeatureSignal):
                    self.brainBitSignalDataReceived = None
                    self.__add_signal_data_callback_brain_bit()
        elif s_family == SensorFamily.SensorLEHeadPhones:
            self.headphonesResistDataReceived = None
            self.__add_resist_callback_headphones()
            self.headphonesSignalDataReceived = None
            self.__add_signal_data_callback_headphones()
        elif s_family == SensorFamily.SensorLEHeadPhones2:
            self.headphones2ResistDataReceived = None
            self.__add_resist_callback_headphones2()
            self.headphones2SignalDataReceived = None
            self.__add_signal_data_callback_headphones2()
        elif s_family == SensorFamily.SensorSPCompactNeuro:
            self.compactNeuroResistDataReceived = None
            self.__add_resist_callback_compact_neuro()
            self.compactNeuroSignalDataReceived = None
            self.__add_signal_data_callback_compact_neuro()
        self.__closed = False

    def __del__(self):
        try:
            if not self.__closed:
                self.__closed = True

                self.batteryChanged = None
                self.memsDataReceived = None
                self.quaternionDataReceived = None
                self.sensorStateChanged = None
                self.callibriSignalDataReceived = None
                self.callibriRespirationDataReceived = None
                self.callibriEnvelopeDataReceived = None
                self.sensorAmpModeChanged = None
                self.fpgDataReceived = None
                self.headbandResistDataReceived = None
                self.headbandSignalDataReceived = None
                self.brainBitResistDataReceived = None
                self.brainBitSignalDataReceived = None
                self.headphonesResistDataReceived = None
                self.headphonesSignalDataReceived = None
                self.headphones2ResistDataReceived = None
                self.headphones2SignalDataReceived = None
                self.compactNeuroResistDataReceived = None
                self.compactNeuroSignalDataReceived = None

                _neuro_lib.removeBatteryCallback(self.__batteryCallbackHandle)
                _neuro_lib.removeConnectionStateCallback(self.__connectionStateCallbackHandle)
                _neuro_lib.removeResistCallbackBrainBit(self.__resistCallbackBrainBitHandle)
                _neuro_lib.removeSignalDataCallbackBrainBit(self.__signalDataCallbackBrainBitHandle)
                _neuro_lib.removeMEMSDataCallback(self.__memsDataCallbackHandle)
                _neuro_lib.removeQuaternionDataCallback(self.__quaternionDataCallbackHandle)
                _neuro_lib.removeAmpModeCallback(self.__ampModeCallbackHandle)
                _neuro_lib.removeSignalCallbackCallibri(self.__signalCallbackCallibriHandle)
                _neuro_lib.removeRespirationCallbackCallibri(self.__respirationCallbackCallibriHandle)
                _neuro_lib.removeElectrodeStateCallbackCallibri(self.__electrodeStateCallbackCallibriHandle)
                _neuro_lib.removeEnvelopeDataCallbackCallibri(self.__envelopeDataCallbackCallibriHandle)
                _neuro_lib.removeFPGDataCallbackNeuroSmart(self.__fpgDataCallbackNeuroSmartHandle)
                _neuro_lib.removeResistCallbackHeadband(self.__resistCallbackHeadbandHandle)
                _neuro_lib.removeSignalDataCallbackHeadband(self.__signalDataCallbackHeadbandHandle)
                _neuro_lib.removeResistCallbackHeadphones(self.__resistCallbackHeadphonesHandle)
                _neuro_lib.removeSignalDataCallbackHeadphones(self.__signalDataCallbackHeadphonesHandle)
                _neuro_lib.removeResistCallbackHeadphones2(self.__resistCallbackHeadphones2Handle)
                _neuro_lib.removeSignalDataCallbackHeadphones2(self.__signalDataCallbackHeadphones2Handle)
                _neuro_lib.removeResistCallbackCompactNeuro(self.__resistCallbackCompactNeuroHandle)
                _neuro_lib.removeSignalDataCallbackCompactNeuro(self.__signalDataCallbackCompactNeuroHandle)

                _neuro_lib.freeSensor(self.__ptr)
                self.__ptr = None
        except:
            pass

    def __add_mems_data_callback(self):
        def __py_mems_data_callback(ptr, data, sz_data, user_data):
            mems_data = [MEMSData(PackNum=int(data[i].PackNum),
                                  Accelerometer=Point3D(X=data[i].Accelerometer.X,
                                                        Y=data[i].Accelerometer.Y,
                                                        Z=data[i].Accelerometer.Z),
                                  Gyroscope=Point3D(X=data[i].Gyroscope.X,
                                                    Y=data[i].Gyroscope.Y,
                                                    Z=data[i].Gyroscope.Z)) for i in range(sz_data)]
            if user_data.memsDataRecived is not None:
                user_data.memsDataRecived(user_data, mems_data)

        self.__memsDataCallback = MEMSDataCallback(__py_mems_data_callback)
        self.__memsDataCallbackHandle = MEMSDataListenerHandle()
        raise_exception_if(
            _neuro_lib.addMEMSDataCallback(self.__ptr, self.__memsDataCallback, byref(self.__memsDataCallbackHandle),
                                           py_object(self)))

    def __add_quaternion_data_callback(self):
        def __py_quaternion_data_callback(ptr, data, sz_data, user_data):
            qa_data = [QuaternionData(PackNum=int(data[i].PackNum),
                                      W=data[i].W,
                                      X=data[i].X,
                                      Y=data[i].Y,
                                      Z=data[i].Z) for i in range(sz_data)]
            if user_data.quaternionDataRecived is not None:
                user_data.quaternionDataRecived(user_data, qa_data)

        self.__quaternionDataCallback = QuaternionDataCallback(__py_quaternion_data_callback)
        self.__quaternionDataCallbackHandle = QuaternionDataListenerHandle()
        raise_exception_if(
            _neuro_lib.addQuaternionDataCallback(self.__ptr, self.__quaternionDataCallback,
                                                 byref(self.__quaternionDataCallbackHandle),
                                                 py_object(self)))

    def __add_signal_callback_callibri(self):
        def __py_signal_callback_callibri(ptr, data, sz_data, user_data):
            signal_data = [CallibriSignalData(PackNum=int(data[i].PackNum),
                                              Samples=[float(data[i].Samples[j]) for j in range(data[i].SzSamples)])
                           for i in range(sz_data)]
            if user_data.callibriSignalDataReceived is not None:
                user_data.callibriSignalDataReceived(user_data, signal_data)

        self.__signalCallbackCallibri = SignalCallbackCallibri(__py_signal_callback_callibri)
        self.__signalCallbackCallibriHandle = CallibriSignalDataListenerHandle()
        raise_exception_if(
            _neuro_lib.addSignalCallbackCallibri(self.__ptr, self.__signalCallbackCallibri,
                                                 byref(self.__signalCallbackCallibriHandle),
                                                 py_object(self)))

    def __add_respiration_callback_callibri(self):
        def __py_respiration_callback_callibri(ptr, data, sz_data, user_data):
            resp_data = [CallibriRespirationData(PackNum=int(data[i].PackNum),
                                                 Samples=[float(data[i].Samples[j]) for j in range(data[i].SzSamples)])
                         for i in range(sz_data)]
            if user_data.callibriRespirationDataReceived is not None:
                user_data.callibriRespirationDataReceived(user_data, resp_data)

        self.__respirationCallbackCallibri = RespirationCallbackCallibri(__py_respiration_callback_callibri)
        self.__respirationCallbackCallibriHandle = CallibriRespirationDataListenerHandle()
        raise_exception_if(
            _neuro_lib.addRespirationCallbackCallibri(self.__ptr, self.__respirationCallbackCallibri,
                                                      byref(self.__respirationCallbackCallibriHandle),
                                                      py_object(self)))

    def __add_electrode_state_callback_callibri(self):
        def __py_electrode_state_callback_callibri(ptr, state, user_data):
            if user_data.callibriElectrodeStateChanged is not None:
                user_data.callibriElectrodeStateChanged(user_data, CallibriElectrodeState(state))

        self.__electrodeStateCallbackCallibri = ElectrodeStateCallbackCallibri(__py_electrode_state_callback_callibri)
        self.__electrodeStateCallbackCallibriHandle = CallibriElectrodeStateListenerHandle()
        raise_exception_if(
            _neuro_lib.addElectrodeStateCallbackCallibri(self.__ptr, self.__electrodeStateCallbackCallibri,
                                                         byref(self.__electrodeStateCallbackCallibriHandle),
                                                         py_object(self)))

    def __add_envelope_data_callback_callibri(self):
        def __py_envelope_data_callback_callibri(ptr, data, sz_data, user_data):
            env_data = [CallibriEnvelopeData(PackNum=int(data[i].PackNum),
                                             Sample=float(data[i].Samples))
                        for i in range(sz_data)]
            if user_data.callibriEnvelopeDataReceived is not None:
                user_data.callibriEnvelopeDataReceived(user_data, env_data)

        self.__envelopeDataCallbackCallibri = EnvelopeDataCallbackCallibri(__py_envelope_data_callback_callibri)
        self.__envelopeDataCallbackCallibriHandle = CallibriEnvelopeDataListenerHandle()
        raise_exception_if(
            _neuro_lib.addEnvelopeDataCallbackCallibri(self.__ptr, self.__envelopeDataCallbackCallibri,
                                                       byref(self.__envelopeDataCallbackCallibriHandle),
                                                       py_object(self)))

    def __add_amp_mode_callback(self):
        def __py_amp_mode_callback(ptr, mode, user_data):
            if user_data.sensorAmpModeChanged is not None:
                user_data.sensorAmpModeChanged(user_data, SensorAmpMode(mode))

        self.__ampModeCallback = AmpModeCallback(__py_amp_mode_callback)
        self.__ampModeCallbackHandle = AmpModeListenerHandle()
        raise_exception_if(
            _neuro_lib.addAmpModeCallback(self.__ptr, self.__ampModeCallback,
                                          byref(self.__ampModeCallbackHandle),
                                          py_object(self)))

    def __add_FPG_data_callback_neuro_smart(self):
        def __py_FPG_data_callback_neuro_smart(ptr, data, sz_data, user_data):
            fpg_data = [FPGData(PackNum=int(data[i].PackNum),
                                IrAmplitude=float(data[i].IrAmplitude),
                                RedAmplitude=float(data[i].RedAmplitude))
                        for i in range(sz_data)]

            if user_data.fpgDataReceived is not None:
                user_data.fpgDataReceived(user_data, fpg_data)

        self.__fpgDataCallbackNeuroSmart = FPGDataCallbackNeuroSmart(__py_FPG_data_callback_neuro_smart)
        self.__fpgDataCallbackNeuroSmartHandle = FPGDataListenerHandle()
        raise_exception_if(
            _neuro_lib.addFPGDataCallbackNeuroSmart(self.__ptr, self.__fpgDataCallbackNeuroSmart,
                                                    byref(self.__fpgDataCallbackNeuroSmartHandle),
                                                    py_object(self)))

    def __add_resist_callback_headband(self):
        def __py_resist_callback_headband(ptr, data, user_data):
            resist = HeadbandResistData(O1=float(data.O1),
                                        O2=float(data.O2),
                                        T3=float(data.T3),
                                        T4=float(data.T4))
            if user_data.headbandResistDataReceived is not None:
                user_data.headbandResistDataReceived(user_data, resist)

        self.__resistCallbackHeadband = ResistCallbackHeadband(__py_resist_callback_headband)
        self.__resistCallbackHeadbandHandle = HeadbandResistDataListenerHandle()
        raise_exception_if(_neuro_lib.addResistCallbackHeadband(self.__ptr, self.__resistCallbackHeadband,
                                                                byref(self.__resistCallbackHeadbandHandle),
                                                                py_object(self)))

    def __add_signal_data_callback_headband(self):
        def __py_signal_data_callback_headband(ptr, data, sz_data, user_data):
            signal_data = [HeadbandSignalData(PackNum=int(data[i].PackNum),
                                              Marker=int(data[i].Marker),
                                              O1=float(data[i].O1),
                                              O2=float(data[i].O2),
                                              T3=float(data[i].T3),
                                              T4=float(data[i].T4)) for i in range(sz_data)]
            if user_data.headbandSignalDataReceived is not None:
                user_data.headbandSignalDataReceived(user_data, signal_data)

        self.__signalDataCallbackHeadband = SignalDataCallbackHeadband(__py_signal_data_callback_headband)
        self.__signalDataCallbackHeadbandHandle = HeadbandSignalDataListenerHandle()
        raise_exception_if(_neuro_lib.addSignalDataCallbackHeadband(self.__ptr, self.__signalDataCallbackHeadband,
                                                                    byref(self.__signalDataCallbackHeadbandHandle),
                                                                    py_object(self)))

    def __add_battery_callback(self):
        def __py_battery_callback(ptr, battery, user_data):
            if user_data.batteryChanged is not None:
                user_data.batteryChanged(user_data, int(battery))

        self.__batteryCallback = BatteryCallback(__py_battery_callback)
        self.__batteryCallbackHandle = BattPowerListenerHandle()
        raise_exception_if(
            _neuro_lib.addBatteryCallback(self.__ptr, self.__batteryCallback, byref(self.__batteryCallbackHandle),
                                          py_object(self)))

    def __add_connection_state_callback(self):
        def __py_connection_state_callback(ptr, state, user_data):
            if user_data.sensorStateChanged is not None:
                user_data.sensorStateChanged(user_data, SensorState(state))

        self.__connectionStateCallback = ConnectionStateCallback(__py_connection_state_callback)
        self.__connectionStateCallbackHandle = SensorStateListenerHandle()
        raise_exception_if(_neuro_lib.addConnectionStateCallback(self.__ptr, self.__connectionStateCallback,
                                                                 byref(self.__connectionStateCallbackHandle),
                                                                 py_object(self)))

    def __add_resist_callback_brain_bit(self):
        def __py_resist_callback_brain_bit(ptr, data, user_data):
            resist = BrainBitResistData(O1=float(data.O1),
                                        O2=float(data.O2),
                                        T3=float(data.T3),
                                        T4=float(data.T4))
            if user_data.brainBitResistDataReceived is not None:
                user_data.brainBitResistDataReceived(user_data, resist)

        self.__resistCallbackBrainBit = ResistCallbackBrainBit(__py_resist_callback_brain_bit)
        self.__resistCallbackBrainBitHandle = BrainBitResistDataListenerHandle()
        raise_exception_if(_neuro_lib.addResistCallbackBrainBit(self.__ptr, self.__resistCallbackBrainBit,
                                                                byref(self.__resistCallbackBrainBitHandle),
                                                                py_object(self)))

    def __add_resist_callback_headphones(self):
        def __py_resist_callback_headphones(ptr, data, sz_data, user_data):
            resist_data = [HeadphonesResistData(PackNum=int(data[i].PackNum),
                                                Ch1=float(data[i].Ch1),
                                                Ch2=float(data[i].Ch2),
                                                Ch3=float(data[i].Ch3),
                                                Ch4=float(data[i].Ch4),
                                                Ch5=float(data[i].Ch5),
                                                Ch6=float(data[i].Ch6),
                                                Ch7=float(data[i].Ch7)) for i in range(sz_data)]
            if user_data.headphonesResistDataReceived is not None:
                user_data.headphonesResistDataReceived(user_data, resist_data)

        self.__resistCallbackHeadphones = ResistCallbackHeadphones(__py_resist_callback_headphones)
        self.__resistCallbackHeadphonesHandle = HeadphonesResistDataListenerHandle()
        raise_exception_if(_neuro_lib.addResistCallbackHeadphones(self.__ptr, self.__resistCallbackHeadphones,
                                                                  byref(self.__resistCallbackHeadphonesHandle),
                                                                  py_object(self)))

    def __add_resist_callback_headphones2(self):
        def __py_resist_callback_headphones2(ptr, data, sz_data, user_data):
            resist_data = [Headphones2ResistData(PackNum=int(data[i].PackNum),
                                                 Ch1=float(data[i].Ch1),
                                                 Ch2=float(data[i].Ch2),
                                                 Ch3=float(data[i].Ch3),
                                                 Ch4=float(data[i].Ch4)) for i in range(sz_data)]
            if user_data.headphones2ResistDataReceived is not None:
                user_data.headphones2ResistDataReceived(user_data, resist_data)

        self.__resistCallbackHeadphones2 = ResistCallbackHeadphones2(__py_resist_callback_headphones2)
        self.__resistCallbackHeadphones2Handle = Headphones2ResistDataListenerHandle()
        raise_exception_if(_neuro_lib.addResistCallbackHeadphones2(self.__ptr, self.__resistCallbackHeadphones2,
                                                                   byref(self.__resistCallbackHeadphones2Handle),
                                                                   py_object(self)))

    def __add_signal_data_callback_brain_bit(self):
        def __py_signal_data_callback_brain_bit(ptr, data, sz_data, user_data):
            signal_data = [BrainBitSignalData(PackNum=int(data[i].PackNum),
                                              Marker=int(data[i].Marker),
                                              O1=float(data[i].O1),
                                              O2=float(data[i].O2),
                                              T3=float(data[i].T3),
                                              T4=float(data[i].T4)) for i in range(sz_data)]
            if user_data.brainBitSignalDataReceived is not None:
                user_data.brainBitSignalDataReceived(user_data, signal_data)

        self.__signalDataCallbackBrainBit = SignalDataCallbackBrainBit(__py_signal_data_callback_brain_bit)
        self.__signalDataCallbackBrainBitHandle = BrainBitSignalDataListenerHandle()
        raise_exception_if(_neuro_lib.addSignalDataCallbackBrainBit(self.__ptr, self.__signalDataCallbackBrainBit,
                                                                    byref(self.__signalDataCallbackBrainBitHandle),
                                                                    py_object(self)))

    def __add_signal_data_callback_headphones(self):
        def __py_signal_data_callback_headphones(ptr, data, sz_data, user_data):
            signal_data = [HeadphonesSignalData(PackNum=int(data[i].PackNum),
                                                Marker=int(data[i].Marker),
                                                Ch1=float(data[i].Ch1),
                                                Ch2=float(data[i].Ch2),
                                                Ch3=float(data[i].Ch3),
                                                Ch4=float(data[i].Ch4),
                                                Ch5=float(data[i].Ch5),
                                                Ch6=float(data[i].Ch6),
                                                Ch7=float(data[i].Ch7)) for i in range(sz_data)]
            if user_data.headphonesSignalDataReceived is not None:
                user_data.headphonesSignalDataReceived(user_data, signal_data)

        self.__signalDataCallbackHeadphones = SignalDataCallbackHeadphones(__py_signal_data_callback_headphones)
        self.__signalDataCallbackHeadphonesHandle = HeadphonesSignalDataListenerHandle()
        raise_exception_if(_neuro_lib.addSignalDataCallbackHeadphones(self.__ptr, self.__signalDataCallbackHeadphones,
                                                                      byref(self.__signalDataCallbackHeadphonesHandle),
                                                                      py_object(self)))

    def __add_signal_data_callback_headphones2(self):
        def __py_signal_data_callback_headphones2(ptr, data, sz_data, user_data):
            signal_data = [Headphones2SignalData(PackNum=int(data[i].PackNum),
                                                 Marker=int(data[i].Marker),
                                                 Ch1=float(data[i].Ch1),
                                                 Ch2=float(data[i].Ch2),
                                                 Ch3=float(data[i].Ch3),
                                                 Ch4=float(data[i].Ch4)) for i in range(sz_data)]
            if user_data.headphones2SignalDataReceived is not None:
                user_data.headphones2SignalDataReceived(user_data, signal_data)

        self.__signalDataCallbackHeadphones2 = SignalDataCallbackHeadphones2(__py_signal_data_callback_headphones2)
        self.__signalDataCallbackHeadphones2Handle = Headphones2SignalDataListenerHandle()
        raise_exception_if(_neuro_lib.addSignalDataCallbackHeadphones2(self.__ptr, self.__signalDataCallbackHeadphones2,
                                                                       byref(
                                                                           self.__signalDataCallbackHeadphones2Handle),
                                                                       py_object(self)))

    def __add_resist_callback_compact_neuro(self):
        def __py_resist_callback_compact_neuro(ptr, data, sz_data, user_data):
            resist_data = [CompactNeuroResistData(O1=float(data[i].O1),
                                                  P3=float(data[i].P3),
                                                  C3=float(data[i].C3),
                                                  F3=float(data[i].F3),
                                                  Fp1=float(data[i].Fp1),
                                                  T5=float(data[i].T5),
                                                  T3=float(data[i].T3),
                                                  F7=float(data[i].F7),
                                                  F8=float(data[i].F8),
                                                  T4=float(data[i].T4),
                                                  T6=float(data[i].T6),
                                                  Fp2=float(data[i].Fp2),
                                                  F4=float(data[i].F4),
                                                  C4=float(data[i].C4),
                                                  P4=float(data[i].P4),
                                                  O2=float(data[i].O2),
                                                  D1=float(data[i].D1),
                                                  D2=float(data[i].D2),
                                                  OZ=float(data[i].OZ),
                                                  PZ=float(data[i].PZ),
                                                  CZ=float(data[i].CZ),
                                                  FZ=float(data[i].FZ),
                                                  FpZ=float(data[i].FpZ),
                                                  D3=float(data[i].D3)) for i in range(sz_data)]
            if user_data.compactNeuroSignalDataReceived is not None:
                user_data.compactNeuroSignalDataReceived(user_data, resist_data)

        self.__resistCallbackCompactNeuro = ResistCallbackCompactNeuro(__py_resist_callback_compact_neuro)
        self.__resistCallbackCompactNeuroHandle = CompactNeuroResistDataListenerHandle()
        raise_exception_if(_neuro_lib.addResistCallbackCompactNeuro(self.__ptr, self.__resistCallbackCompactNeuro,
                                                                    byref(self.__resistCallbackCompactNeuroHandle),
                                                                    py_object(self)))

    def __add_signal_data_callback_compact_neuro(self):
        def __py_signal_data_callback_compact_neuro(ptr, data, sz_data, user_data):
            signal_data = [CompactNeuroSignalData(PackNum=int(data[i].PackNum),
                                                  Marker=int(data[i].Marker),
                                                  O1=float(data[i].O1),
                                                  P3=float(data[i].P3),
                                                  C3=float(data[i].C3),
                                                  F3=float(data[i].F3),
                                                  Fp1=float(data[i].Fp1),
                                                  T5=float(data[i].T5),
                                                  T3=float(data[i].T3),
                                                  F7=float(data[i].F7),
                                                  F8=float(data[i].F8),
                                                  T4=float(data[i].T4),
                                                  T6=float(data[i].T6),
                                                  Fp2=float(data[i].Fp2),
                                                  F4=float(data[i].F4),
                                                  C4=float(data[i].C4),
                                                  P4=float(data[i].P4),
                                                  O2=float(data[i].O2),
                                                  D1=float(data[i].D1),
                                                  D2=float(data[i].D2),
                                                  OZ=float(data[i].OZ),
                                                  PZ=float(data[i].PZ),
                                                  CZ=float(data[i].CZ),
                                                  FZ=float(data[i].FZ),
                                                  FpZ=float(data[i].FpZ),
                                                  D3=float(data[i].D3)) for i in range(sz_data)]
            if user_data.compactNeuroSignalDataReceived is not None:
                user_data.compactNeuroSignalDataReceived(user_data, signal_data)

        self.__signalDataCallbackCompactNeuro = SignalDataCallbackCompactNeuro(__py_signal_data_callback_compact_neuro)
        self.__signalDataCallbackCompactNeuroHandle = CompactNeuroSignalDataListenerHandle()
        raise_exception_if(
            _neuro_lib.addSignalDataCallbackCompactNeuro(self.__ptr, self.__signalDataCallbackCompactNeuro,
                                                         byref(self.__signalDataCallbackCompactNeuroHandle),
                                                         py_object(self)))

    @property
    def SensFamily(self) -> SensorFamily:
        family = _neuro_lib.getFamilySensor(self.__ptr)
        return SensorFamily(family)

    @property
    def Features(self) -> [SensorFeature]:
        sz = _neuro_lib.getFeaturesCountSensor(self.__ptr)
        sz_sensor_feature_in_out = SizeType(c_int32(sz))
        features_val = EnumType(c_int8(sz))
        raise_exception_if(_neuro_lib.getFeaturesSensor(self.__ptr, features_val, sz_sensor_feature_in_out))
        return [SensorFeature(features_val[i]) for i in range(sz_sensor_feature_in_out.contents.value)]

    @property
    def Commands(self) -> [SensorCommand]:
        sz = _neuro_lib.getCommandsCountSensor(self.__ptr)
        sz_sensor_commands_in_out = SizeType(c_int32(sz))
        commands_val = EnumType(c_int8())
        raise_exception_if(_neuro_lib.getCommandsSensor(self.__ptr, commands_val, sz_sensor_commands_in_out))
        return [SensorCommand(commands_val[i]) for i in range(sz_sensor_commands_in_out.contents.value)]

    @property
    def Parameters(self) -> [ParameterInfo]:
        sz = _neuro_lib.getParametersCountSensor(self.__ptr)
        szSensorParametersInOut = SizeType(c_int32(sz))
        parametersVal = (NativeParameterInfo * sz)()
        raise_exception_if(_neuro_lib.getParametersSensor(self.__ptr, parametersVal, szSensorParametersInOut))
        return [ParameterInfo(Param=SensorParameter(parametersVal[i].Param),
                              ParamAccess=SensorParamAccess(parametersVal[i].ParamAccess)) for i in
                range(szSensorParametersInOut.contents.value)]

    @property
    def Name(self) -> str:
        name_out = ctypes.create_string_buffer(SENSOR_NAME_LEN)
        raise_exception_if(_neuro_lib.readNameSensor(self.__ptr, name_out, SENSOR_NAME_LEN))
        return ''.join([chr(c) for c in name_out.value]).rstrip('\x00')

    @Name.setter
    def Name(self, value: str):
        raise_exception_if(_neuro_lib.writeNameSensor(self.__ptr, value.encode('utf-8'), len(value)))

    @property
    def State(self) -> SensorState:
        state_val = EnumType(c_int8(1))
        raise_exception_if(_neuro_lib.readStateSensor(self.__ptr, state_val))
        return SensorState(state_val.contents.value)

    @property
    def Address(self) -> str:
        address_out = ctypes.create_string_buffer(SENSOR_ADR_LEN)
        raise_exception_if(_neuro_lib.readAddressSensor(self.__ptr, address_out, SENSOR_ADR_LEN))
        return ''.join([chr(c) for c in address_out.value]).rstrip('\x00')

    @property
    def SerialNumber(self) -> str:
        serial_number_out = ctypes.create_string_buffer(SENSOR_SN_LEN)
        raise_exception_if(_neuro_lib.readSerialNumberSensor(self.__ptr, serial_number_out, SENSOR_SN_LEN))
        return ''.join([chr(c) for c in serial_number_out.value]).rstrip('\x00')

    @SerialNumber.setter
    def SerialNumber(self, sn: str):
        raise_exception_if(_neuro_lib.writeSerialNumberSensor(self.__ptr, sn.encode('utf-8'), len(sn)))

    @property
    def BattPower(self) -> int:
        power = SizeType(c_int32(1))
        raise_exception_if(_neuro_lib.readBattPowerSensor(self.__ptr, power))
        return int(power.contents.value)

    @property
    def HardwareFilters(self) -> [SensorFilter]:
        filters_out = EnumType(c_int8())
        sz_filters_in_out = SizeType(c_int32(64))
        raise_exception_if(_neuro_lib.readHardwareFiltersSensor(self.__ptr, filters_out, sz_filters_in_out))
        return [SensorFilter(filters_out[i]) for i in range(sz_filters_in_out.contents.value)]

    @HardwareFilters.setter
    def HardwareFilters(self, filters: list):
        filters_len = len(filters)
        filters_values = (c_ubyte * filters_len)(*[filters[i].value for i in range(filters_len)])
        raise_exception_if(_neuro_lib.writeHardwareFiltersSensor(self.__ptr, filters_values, filters_len))

    @property
    def SamplingFrequency(self) -> SensorSamplingFrequency:
        sf_val = EnumType(c_int8(1))
        raise_exception_if(_neuro_lib.readSamplingFrequencySensor(self.__ptr, sf_val))
        return SensorSamplingFrequency(sf_val.contents.value)

    @SamplingFrequency.setter
    def SamplingFrequency(self, sf: SensorSamplingFrequency):
        raise_exception_if(_neuro_lib.writeSamplingFrequencySensor(self.__ptr, sf.value))

    @property
    def Gain(self) -> SensorGain:
        gain_val = EnumType(c_int8(1))
        raise_exception_if(_neuro_lib.readGainSensor(self.__ptr, gain_val))
        return SensorGain(gain_val.contents.value)

    @Gain.setter
    def Gain(self, gain: SensorGain):
        raise_exception_if(_neuro_lib.writeGainSensor(self.__ptr, gain.value))

    @property
    def DataOffset(self) -> SensorDataOffset:
        CP = POINTER(c_uint8)
        data_offset_val = CP(c_uint8(1))
        raise_exception_if(_neuro_lib.readDataOffsetSensor(self.__ptr, data_offset_val))
        return SensorDataOffset(data_offset_val.contents.value)

    @DataOffset.setter
    def DataOffset(self, do: SensorDataOffset):
        raise_exception_if(_neuro_lib.writeDataOffsetSensor(self.__ptr, do.value))

    @property
    def ExtSwInput(self) -> SensorExternalSwitchInput:
        ext_sw_input_val = EnumType(c_int8(1))
        raise_exception_if(_neuro_lib.readExternalSwitchSensor(self.__ptr, ext_sw_input_val))
        return SensorExternalSwitchInput(ext_sw_input_val.contents.value)

    @ExtSwInput.setter
    def ExtSwInput(self, ext_sw_inp: SensorExternalSwitchInput):
        raise_exception_if(_neuro_lib.writeDataOffsetSensor(self.__ptr, ext_sw_inp.value))

    @property
    def ADCInput(self) -> SensorADCInput:
        adc_input_val = EnumType(c_int8(1))
        raise_exception_if(_neuro_lib.readADCInputSensor(self.__ptr, adc_input_val))
        return SensorADCInput(adc_input_val.contents.value)

    @ADCInput.setter
    def ADCInput(self, adc_inp: SensorADCInput):
        raise_exception_if(_neuro_lib.writeExternalSwitchSensor(self.__ptr, adc_inp.value))

    @property
    def AccSens(self) -> SensorAccelerometerSensitivity:
        acc_sens_val = EnumType(c_int8(1))
        raise_exception_if(_neuro_lib.readAccelerometerSensSensor(self.__ptr, acc_sens_val))
        return SensorAccelerometerSensitivity(acc_sens_val.contents.value)

    @AccSens.setter
    def AccSens(self, acc_sens: SensorAccelerometerSensitivity):
        raise_exception_if(_neuro_lib.writeADCInputSensor(self.__ptr, acc_sens.value))

    @property
    def GyroSens(self) -> SensorGyroscopeSensitivity:
        gyro_sens_val = EnumType(c_int8(1))
        raise_exception_if(_neuro_lib.readGyroscopeSensSensor(self.__ptr, gyro_sens_val))
        return SensorGyroscopeSensitivity(gyro_sens_val.contents.value)

    @GyroSens.setter
    def GyroSens(self, gyro_sens: SensorGyroscopeSensitivity):
        raise_exception_if(_neuro_lib.writeGyroscopeSensSensor(self.__ptr, gyro_sens.value))

    @property
    def FirmwareMode(self) -> SensorFirmwareMode:
        firmware_mode_val = EnumType(c_int8(1))
        raise_exception_if(_neuro_lib.readFirmwareModeSensor(self.__ptr, firmware_mode_val))
        return SensorFirmwareMode(firmware_mode_val.contents.value)

    @FirmwareMode.setter
    def FirmwareMode(self, mode: SensorFirmwareMode):
        raise_exception_if(_neuro_lib.writeFirmwareModeSensor(self.__ptr, mode.value))

    @property
    def Version(self) -> SensorVersion:
        SVP = POINTER(NativeSensorVersion)
        version = SVP(NativeSensorVersion())
        raise_exception_if(_neuro_lib.readVersionSensor(self.__ptr, version))
        return SensorVersion(FwMajor=int(version.contents.FwMajor),
                             FwMinor=int(version.contents.FwMinor),
                             FwPatch=int(version.contents.FwPatch),
                             HwMajor=int(version.contents.HwMajor),
                             HwMinor=int(version.contents.HwMinor),
                             HwPatch=int(version.contents.HwPatch),
                             ExtMajor=int(version.contents.ExtMajor))

    @property
    def SamplingFrequencyResist(self) -> SensorSamplingFrequency:
        sampling_frequency_out = EnumType(c_int8(1))
        raise_exception_if(_neuro_lib.readSamplingFrequencyResistSensor(self.__ptr, sampling_frequency_out))
        return SensorSamplingFrequency(sampling_frequency_out.contents.value)

    @property
    def SamplingFrequencyMEMS(self) -> SensorSamplingFrequency:
        sampling_frequency_out = EnumType(c_int8(1))
        raise_exception_if(_neuro_lib.readSamplingFrequencyMEMSSensor(self.__ptr, sampling_frequency_out))
        return SensorSamplingFrequency(sampling_frequency_out.contents.value)

    @property
    def SamplingFrequencyFPG(self) -> SensorSamplingFrequency:
        sampling_frequency_out = EnumType(c_int8(1))
        raise_exception_if(_neuro_lib.readSamplingFrequencyFPGSensor(self.__ptr, sampling_frequency_out))
        return SensorSamplingFrequency(sampling_frequency_out.contents.value)

    @property
    def SamplingFrequencyResp(self) -> SensorSamplingFrequency:
        sampling_frequency_out = EnumType(c_int8(1))
        raise_exception_if(_neuro_lib.readSamplingFrequencyRespSensor(self.__ptr, sampling_frequency_out))
        return SensorSamplingFrequency(sampling_frequency_out.contents.value)

    @property
    def StimulatorMAStateCallibri(self) -> CallibriStimulatorMAState:
        CSMAS = POINTER(NativeCallibriStimulatorMAState)
        ma_state = CSMAS(NativeCallibriStimulatorMAState())
        raise_exception_if(_neuro_lib.readStimulatorAndMAStateCallibri(self.__ptr, ma_state))
        return CallibriStimulatorMAState(StimulatorState=CallibriStimulatorState(ma_state.contents.StimulatorState),
                                         MAState=CallibriStimulatorState(ma_state.contents.MAState))

    @property
    def StimulatorParamCallibri(self) -> CallibriStimulationParams:
        CSP = POINTER(NativeCallibriStimulationParams)
        stimulation_params_out = CSP(NativeCallibriStimulationParams())
        raise_exception_if(_neuro_lib.readStimulatorParamCallibri(self.__ptr, stimulation_params_out))
        return CallibriStimulationParams(Current=int(stimulation_params_out.contents.Current),
                                         PulseWidth=int(stimulation_params_out.contents.PulseWidth),
                                         Frequency=int(stimulation_params_out.contents.Frequency),
                                         StimulusDuration=int(stimulation_params_out.contents.StimulusDuration))

    @StimulatorParamCallibri.setter
    def StimulatorParamCallibri(self, params: CallibriStimulationParams):
        stim_params = NativeCallibriStimulationParams()
        stim_params.Current = params.Current
        stim_params.PulseWidth = params.PulseWidth
        stim_params.Frequency = params.Frequency
        stim_params.StimulusDuration = params.StimulusDuration
        raise_exception_if(_neuro_lib.writeStimulatorParamCallibri(self.__ptr, stim_params))

    @property
    def MotionAssistantParamCallibri(self) -> CallibriMotionAssistantParams:
        CMAP = POINTER(NativeCallibriMotionAssistantParams)
        motion_assistant_params_out = CMAP(NativeCallibriMotionAssistantParams())
        raise_exception_if(_neuro_lib.readMotionAssistantParamCallibri(self.__ptr, motion_assistant_params_out))
        return CallibriMotionAssistantParams(GyroStart=motion_assistant_params_out.contents.GyroStart,
                                             GyroStop=motion_assistant_params_out.contents.GyroStop,
                                             Limb=motion_assistant_params_out.contents.Limb,
                                             MinPauseMs=motion_assistant_params_out.contents.MinPauseMs)

    @MotionAssistantParamCallibri.setter
    def MotionAssistantParamCallibri(self, params: CallibriMotionAssistantParams):
        stimulation_params = NativeCallibriMotionAssistantParams()
        stimulation_params.GyroStart = params.GyroStart
        stimulation_params.GyroStop = params.GyroStop
        stimulation_params.Limb = params.Limb
        stimulation_params.MinPauseMs = params.MinPauseMs
        raise_exception_if(_neuro_lib.writeStimulatorParamCallibri(self.__ptr, stimulation_params))

    @property
    def MotionCounterParamCallibri(self) -> CallibriMotionCounterParam:
        CMCP = POINTER(NativeCallibriMotionCounterParam)
        motion_counter_param_out = CMCP(NativeCallibriMotionCounterParam())
        raise_exception_if(_neuro_lib.readMotionCounterParamCallibri(self.__ptr, motion_counter_param_out))
        return CallibriMotionCounterParam(InsenseThresholdMG=motion_counter_param_out.contents.InsenseThresholdMG,
                                          InsenseThresholdSample=motion_counter_param_out.contents.InsenseThresholdSample)

    @MotionCounterParamCallibri.setter
    def MotionCounterParamCallibri(self, params: CallibriMotionCounterParam):
        motion_counter_param = NativeCallibriMotionCounterParam()
        motion_counter_param.InsenseThresholdMG = params.InsenseThresholdMG
        motion_counter_param.InsenseThresholdSample = params.InsenseThresholdSample
        raise_exception_if(_neuro_lib.writeMotionCounterParamCallibri(self.__ptr, motion_counter_param))

    @property
    def MotionCounterCallibri(self) -> int:
        EnumType = POINTER(c_uint32)
        motion_counter_out = EnumType(c_uint32(1))
        raise_exception_if(_neuro_lib.readMotionCounterCallibri(self.__ptr, motion_counter_out))
        return int(motion_counter_out.contents.value)

    @property
    def ColorCallibri(self) -> CallibriColorType:
        callibri_color_out = EnumType(c_uint8(1))
        raise_exception_if(_neuro_lib.readColorCallibri(self.__ptr, callibri_color_out))
        return CallibriColorType(callibri_color_out.contents.value)

    @property
    def IrAmplitudeHeadband(self) -> IrAmplitude:
        EnumType = POINTER(c_uint8)
        amplitude_out = EnumType(c_uint8(1))
        raise_exception_if(_neuro_lib.readIrAmplitudeHeadband(self.__ptr, amplitude_out))
        return IrAmplitude(amplitude_out.contents.value)

    @IrAmplitudeHeadband.setter
    def IrAmplitudeHeadband(self, amplitude: IrAmplitude):
        raise_exception_if(_neuro_lib.writeIrAmplitudeHeadband(self.__ptr, amplitude.value))

    @property
    def RedAmplitudeHeadband(self) -> RedAmplitude:
        EnumType = POINTER(c_uint8)
        amplitude_out = EnumType(c_uint8(1))
        raise_exception_if(_neuro_lib.readRedAmplitudeHeadband(self.__ptr, amplitude_out))
        return RedAmplitude(amplitude_out.contents.value)

    @RedAmplitudeHeadband.setter
    def RedAmplitudeHeadband(self, amplitude: RedAmplitude):
        raise_exception_if(_neuro_lib.writeRedAmplitudeHeadband(self.__ptr, amplitude.value))

    @property
    def AmpMode(self) -> SensorAmpMode:
        EnumType = POINTER(c_uint8)
        mode_out = EnumType(c_uint8(1))
        raise_exception_if(_neuro_lib.readAmpMode(self.__ptr, mode_out))
        return SensorAmpMode(mode_out.contents.value)

    @property
    def AmplifierParamHeadphones(self) -> HeadphonesAmplifierParam:
        HAP = POINTER(NativeHeadphonesAmplifierParam)
        amp_param_out = HAP(NativeHeadphonesAmplifierParam())
        raise_exception_if(_neuro_lib.readAmplifierParamHeadphones(self.__ptr, amp_param_out))
        return HeadphonesAmplifierParam(ChSignalUse1=amp_param_out.contents.ChSignalUse1,
                                        ChSignalUse2=amp_param_out.contents.ChSignalUse2,
                                        ChSignalUse3=amp_param_out.contents.ChSignalUse3,
                                        ChSignalUse4=amp_param_out.contents.ChSignalUse4,
                                        ChSignalUse5=amp_param_out.contents.ChSignalUse5,
                                        ChSignalUse6=amp_param_out.contents.ChSignalUse6,
                                        ChSignalUse7=amp_param_out.contents.ChSignalUse7,
                                        ChResistUse1=amp_param_out.contents.ChResistUse1,
                                        ChResistUse2=amp_param_out.contents.ChResistUse2,
                                        ChResistUse3=amp_param_out.contents.ChResistUse3,
                                        ChResistUse4=amp_param_out.contents.ChResistUse4,
                                        ChResistUse5=amp_param_out.contents.ChResistUse5,
                                        ChResistUse6=amp_param_out.contents.ChResistUse6,
                                        ChResistUse7=amp_param_out.contents.ChResistUse7,
                                        ChGain1=SensorGain(amp_param_out.contents.ChGain1),
                                        ChGain2=SensorGain(amp_param_out.contents.ChGain2),
                                        ChGain3=SensorGain(amp_param_out.contents.ChGain3),
                                        ChGain4=SensorGain(amp_param_out.contents.ChGain4),
                                        ChGain5=SensorGain(amp_param_out.contents.ChGain5),
                                        ChGain6=SensorGain(amp_param_out.contents.ChGain6),
                                        ChGain7=SensorGain(amp_param_out.contents.ChGain7),
                                        Current=GenCurrent(amp_param_out.contents.Current))

    @AmplifierParamHeadphones.setter
    def AmplifierParamHeadphones(self, amplitude: HeadphonesAmplifierParam):
        amp_param = NativeHeadphonesAmplifierParam()
        amp_param.ChSignalUse1 = amplitude.ChSignalUse1
        amp_param.ChSignalUse2 = amplitude.ChSignalUse2
        amp_param.ChSignalUse3 = amplitude.ChSignalUse3
        amp_param.ChSignalUse4 = amplitude.ChSignalUse4
        amp_param.ChSignalUse5 = amplitude.ChSignalUse5
        amp_param.ChSignalUse6 = amplitude.ChSignalUse6
        amp_param.ChSignalUse7 = amplitude.ChSignalUse7

        amp_param.ChResistUse1 = amplitude.ChResistUse1
        amp_param.ChResistUse2 = amplitude.ChResistUse2
        amp_param.ChResistUse3 = amplitude.ChResistUse3
        amp_param.ChResistUse4 = amplitude.ChResistUse4
        amp_param.ChResistUse5 = amplitude.ChResistUse5
        amp_param.ChResistUse6 = amplitude.ChResistUse6
        amp_param.ChResistUse7 = amplitude.ChResistUse7

        amp_param.ChGain1 = amplitude.ChGain1.value
        amp_param.ChGain2 = amplitude.ChGain2.value
        amp_param.ChGain3 = amplitude.ChGain3.value
        amp_param.ChGain4 = amplitude.ChGain4.value
        amp_param.ChGain5 = amplitude.ChGain5.value
        amp_param.ChGain6 = amplitude.ChGain6.value
        amp_param.ChGain7 = amplitude.ChGain7.value

        amp_param.Current = amplitude.Current.value
        raise_exception_if(_neuro_lib.writeAmplifierParamHeadphones(self.__ptr, amp_param))

    @property
    def AmplifierParamHeadphones2(self) -> Headphones2AmplifierParam:
        HAP = POINTER(NativeHeadphones2AmplifierParam)
        amp_param_out = HAP(NativeHeadphones2AmplifierParam())
        raise_exception_if(_neuro_lib.readAmplifierParamHeadphones2(self.__ptr, amp_param_out))
        return Headphones2AmplifierParam(ChSignalUse1=amp_param_out.contents.ChSignalUse1,
                                        ChSignalUse2=amp_param_out.contents.ChSignalUse2,
                                        ChSignalUse3=amp_param_out.contents.ChSignalUse3,
                                        ChSignalUse4=amp_param_out.contents.ChSignalUse4,
                                        ChResistUse1=amp_param_out.contents.ChResistUse1,
                                        ChResistUse2=amp_param_out.contents.ChResistUse2,
                                        ChResistUse3=amp_param_out.contents.ChResistUse3,
                                        ChResistUse4=amp_param_out.contents.ChResistUse4,
                                        ChGain1=SensorGain(amp_param_out.contents.ChGain1),
                                        ChGain2=SensorGain(amp_param_out.contents.ChGain2),
                                        ChGain3=SensorGain(amp_param_out.contents.ChGain3),
                                        ChGain4=SensorGain(amp_param_out.contents.ChGain4),
                                        Current=GenCurrent(amp_param_out.contents.Current))

    @AmplifierParamHeadphones2.setter
    def AmplifierParamHeadphones2(self, amplitude: Headphones2AmplifierParam):
        amp_param = NativeHeadphonesAmplifierParam()
        amp_param.ChSignalUse1 = amplitude.ChSignalUse1
        amp_param.ChSignalUse2 = amplitude.ChSignalUse2
        amp_param.ChSignalUse3 = amplitude.ChSignalUse3
        amp_param.ChSignalUse4 = amplitude.ChSignalUse4

        amp_param.ChResistUse1 = amplitude.ChResistUse1
        amp_param.ChResistUse2 = amplitude.ChResistUse2
        amp_param.ChResistUse3 = amplitude.ChResistUse3
        amp_param.ChResistUse4 = amplitude.ChResistUse4

        amp_param.ChGain1 = amplitude.ChGain1.value
        amp_param.ChGain2 = amplitude.ChGain2.value
        amp_param.ChGain3 = amplitude.ChGain3.value
        amp_param.ChGain4 = amplitude.ChGain4.value

        amp_param.Current = amplitude.Current.value
        raise_exception_if(_neuro_lib.writeAmplifierParamHeadphones2(self.__ptr, amp_param))

    @property
    def StimulatorParamCompactNeuro(self) -> CompactNeuroStimulParam:
        CNSP = POINTER(NativeCompactNeuroStimulParam)
        stimulation_params_out = CNSP(NativeCompactNeuroStimulParam())
        raise_exception_if(_neuro_lib.readStimulatorParamCompactNeuro(self.__ptr, stimulation_params_out))
        return CompactNeuroStimulParam(Freq=stimulation_params_out.contents.Freq,
                                       PulseWidthMs=stimulation_params_out.contents.PulseWidthMs,
                                       FillingFreq=stimulation_params_out.contents.FillingFreq,
                                       Power=stimulation_params_out.contents.Power,
                                       Count=stimulation_params_out.contents.Count)

    @StimulatorParamCompactNeuro.setter
    def StimulatorParamCompactNeuro(self, amplitude: CompactNeuroStimulParam):
        stimulationParams = NativeCompactNeuroStimulParam()
        stimulationParams.Freq = amplitude.Freq
        stimulationParams.PulseWidthMs = amplitude.PulseWidthMs
        stimulationParams.FillingFreq = amplitude.FillingFreq
        stimulationParams.Power = amplitude.Power
        stimulationParams.Count = amplitude.Count
        raise_exception_if(_neuro_lib.writeStimulatorParamCompactNeuro(self.__ptr, stimulationParams))

    @property
    def SupportedChannelsCompactNeuro(self) -> [EEGChannelInfo]:
        sz = _neuro_lib.getChannelsCountSensor(self.__ptr)
        sz_channels_in_out = SizeType(c_int32(sz))
        channels_out = (NativeEEGChannelInfo * sz)()
        raise_exception_if(_neuro_lib.readSupportedChannelsCompactNeuro(self.__ptr, channels_out, sz_channels_in_out))
        return [EEGChannelInfo(Id=EEGChannelId(channels_out[i].Id),
                               ChType=EEGChannelType(channels_out[i].ChType),
                               Name=''.join([chr(c) for c in channels_out[i].Name]).rstrip('\x00'),
                               Num=int(channels_out[i].Num)) for i in range(sz_channels_in_out.contents.value)]

    def Connect(self):
        """
        Device connections. After a successful connection, the sensorStateChanged callback will be called. It is a
        blocking method.

        :raises BaseException:
            If an internal error occurred while connecting.
        """
        raise_exception_if(_neuro_lib.connectSensor(self.__ptr))

    def Disconnect(self):
        """
        Disconnect from the device. After a successful shutdown, the sensorStateChanged callback will be called

        :raises BaseException:
            If an internal error occurred while disconnecting.
        """
        raise_exception_if(_neuro_lib.disconnectSensor(self.__ptr))

    def IsSupportedFeature(self, future: SensorFeature) -> bool:
        """
        Checks if a feature is supported

        :param future:
            Feature to be checked for support
        :return: bool
            Is the feature supported or not
        """
        supported = _neuro_lib.isSupportedFeatureSensor(self.__ptr, future.value)
        return bool(int(supported))

    def IsSupportedCommand(self, sensor_command: SensorCommand) -> bool:
        """
        Checks if a command is supported

        :param sensor_command:
            Command to be checked for support
        :return:
            Is the command supported or not
        """
        supported = _neuro_lib.isSupportedCommandSensor(self.__ptr, sensor_command.value)
        return bool(int(supported))

    def IsSupportedParameter(self, sensor_parameter: SensorParameter) -> bool:
        """
        Checks if a parameter is supported

        :param sensor_parameter:
            Parameter to be checked for support
        :return:
            Is the parameter supported or not
        """
        supported = _neuro_lib.isSupportedParameterSensor(self.__ptr, sensor_parameter.value)
        return bool(int(supported))

    def ExecCommand(self, sensor_command: SensorCommand):
        """
        Sends a specific command to the device.It is a blocking method.

        :param sensor_command: SensorCommand
            Command to execute

        :raises BaseException:
            If an internal error occurred while executing command.
        """
        raise_exception_if(_neuro_lib.execCommandSensor(self.__ptr, sensor_command.value))

    def PingNeuroSmart(self, marker: int):
        """
        Allows the user to send a flag to the device, which will then be returned to the data packet as the value of
        the token. Not supported by all devices

        :param marker: int
            Byte marker

        :raises BaseException:
            If an internal error occurred while executing command.
        """
        raise_exception_if(_neuro_lib.pingNeuroSmart(self.__ptr, c_uint8(marker)))
        pass
