from scanner import Scanner
from cmn_types import *

import concurrent.futures
from time import sleep


def sensor_found(scanner, sensors):
    for i in range(len(sensors)):
        print('Sensor found: %s' % sensors[i])


def on_sensor_state_changed(sensor, state):
    print('Sensor {0} is {1}'.format(sensor.Name, state))


def on_battery_changed(sensor, battery):
    print('Battery: {0}'.format(battery))


def on_brain_bit_signal_data_received(sensor, data):
    print(data)


def on_brain_bit_resist_data_received(sensor, data):
    print(data)


def on_callibri_signal_data_received(sensor, data):
    print(data)


def on_callibri_electrodes_state_changed(sensor, data):
    print(data)


def on_callibri_envelope_received(sensor, data):
    print(data)


def on_callibri_respiration_data_received(sensor, data):
    print(data)


try:
    scanner = Scanner([SensorFamily.SensorLEBrainBitBlack, SensorFamily.SensorLEHeadband, SensorFamily.SensorLEBrainBit,
                   SensorFamily.SensorLECallibri])

    scanner.sensorsChanged = sensor_found
    scanner.Start()
    print("Starting search for 30 sek...")
    sleep(10)
    scanner.Stop()

    sensInfos = scanner.Sensors()
    for i in range(len(sensInfos)):
        sensor_info = sensInfos[i]
        print(sensInfos[i])

        def device_connection(sensor_info):
            return scanner.CreateSensor(sensor_info)


        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(device_connection, sensor_info)
            sensor = future.result()
            print("Device connected")

        sensor.sensorStateChanged = on_sensor_state_changed
        sensor.batteryChanged = on_battery_changed

        sensFamily = sensor.SensFamily

        print(sensFamily)
        print(sensor.Features)
        print(sensor.Commands)
        print(sensor.Parameters)
        print(sensor.Name)
        print(sensor.State)
        print(sensor.Address)
        print(sensor.SerialNumber)
        print(sensor.BattPower)
        print(sensor.SamplingFrequency)
        print(sensor.Gain)
        print(sensor.DataOffset)
        print(sensor.Version)

        if sensFamily == SensorFamily.SensorLEBrainBit or sensFamily == SensorFamily.SensorLEBrainBitBlack:
            sensor.brainBitSignalDataReceived = on_brain_bit_signal_data_received
            sensor.brainBitResistDataReceived = on_brain_bit_resist_data_received

        if sensFamily == SensorFamily.SensorLECallibri:
            if sensor.IsSupportedFeature(SensorFeature.FeatureSignal):
                sensor.callibriSignalDataReceived = on_callibri_signal_data_received
                sensor.callibriElectrodeStateChanged = on_callibri_electrodes_state_changed
            if sensor.IsSupportedFeature(SensorFeature.FeatureEnvelope):
                sensor.callibriEnvelopeDataReceived = on_callibri_envelope_received
            if sensor.IsSupportedFeature(SensorFeature.FeatureRespiration):
                sensor.callibriRespirationDataReceived = on_callibri_respiration_data_received

        if sensor.IsSupportedCommand(SensorCommand.CommandStartSignal):
            sensor.ExecCommand(SensorCommand.CommandStartSignal)
            print("Start signal")
            sleep(10)
            sensor.ExecCommand(SensorCommand.CommandStopSignal)
            print("Stop signal")

        if sensor.IsSupportedCommand(SensorCommand.CommandStopResist):
            sensor.ExecCommand(SensorCommand.CommandStartResist)
            print("Start resist")
            sleep(10)
            print("Timer end")
            sensor.ExecCommand(SensorCommand.CommandStopResist)
            print("Stop resist")

        if sensor.IsSupportedCommand(SensorCommand.CommandStartEnvelope):
            sensor.ExecCommand(SensorCommand.CommandStartEnvelope)
            print("Start envelope")
            sleep(10)
            sensor.ExecCommand(SensorCommand.CommandStopEnvelope)
            print("Stop envelope")

        if sensor.IsSupportedCommand(SensorCommand.CommandStartRespiration):
            sensor.ExecCommand(SensorCommand.CommandStartRespiration)
            print("Start respiration")
            sleep(10)
            sensor.ExecCommand(SensorCommand.CommandStopRespiration)
            print("Stop respiration")

        if sensor.IsSupportedFeature(SensorFeature.FeatureCurrentStimulator):
            sensor.ExecCommand(SensorCommand.CommandStartCurrentStimulation)
            print("Start CurrentStimulation")
            sleep(10)
            sensor.ExecCommand(SensorCommand.CommandStopCurrentStimulation)
            print("Stop CurrentStimulation")

        sensor.Disconnect()
        print("Disconnect from sensor")
        del sensor

    del scanner
    print('Remove scanner')
except Exception as err:
        print(err)
