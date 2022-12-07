import pyvisa
import time
import pandas as pd
import signal
import sys
from functions.configManager import setup
from functions.configManager import saveConfig
from functions.flags import flags

def main():
    flags()
    def handler(signo, stack_frame):
        res = input("Ctrl-C was pressed. Do you really want to exit? [y/n]: ")
        if res == 'y':
            name = str(input("Enter the name of the file to save the measures: ") or "measures")
            meas.to_csv(f'data/{name}.csv', index=False)
            anritsu.close()
            rm.close()
            sys.exit(0)

    signal.signal(signal.SIGINT, handler)

    ip, port, centralFreq, freqUnits, span, spanUnits, sweepPoints, integrationBandwidth, integrationBandwidthUnits, sweepTime, sweepContinuously, preAmp, file = setup()
    
    try:
        rm = pyvisa.ResourceManager()
        anritsu = rm.open_resource(f'TCPIP0::{ip}::{port}::SOCKET')
        anritsu.read_termination = '\n'
        anritsu.write_termination = '\n'
        print("\n\n [✓] Conected to: " + anritsu.query("*IDN?"))

    except:
        print("\n\n[x] Error while connecting to instrument")
        sys.exit(1)

    print("\n\n[✓] Setting up instrument...")
    try:
        anritsu.write(f'FREQ:SPAN {span}{spanUnits}')
        print("- Instrument span set to: " + anritsu.query('FREQ:SPAN?'))
        anritsu.write(f'FREQ:CENT {centralFreq}{freqUnits}')
        print("- Instrument central frequency set to: " + anritsu.query('FREQ:CENT?'))
        anritsu.write(f'DISP:WIND:TRAC:Y:SCAL:RLEV -30')
        anritsu.write(f'CONFigure:CHPower')
        anritsu.write(f'TRACe1:TYPE AVER')
        if(preAmp == 'yes'):
            anritsu.write(f'POWer:RF:GAIN:STATe ON')
        else:
            anritsu.write(f'POWer:RF:GAIN:STATe OFF')
        print("- Instrument pre-amp set to: " + anritsu.query('POWer:RF:GAIN:STATe?'))
        anritsu.write(f'CHPower:BWIDth:INTegration {integrationBandwidth}{integrationBandwidthUnits}')
        print("- Instrument integration bandwidth set to: " + anritsu.query('CHPower:BWIDth:INTegration?'))
        if (sweepContinuously == 'yes'):
            anritsu.write(f'INIT:CONT ON')
        else:
            anritsu.write(f'INIT:CONT OFF')
        print("- Instrument sweep continuously set to: " + anritsu.query('INIT:CONT?'))
        anritsu.write(f'DISPlay:POINtcount {sweepPoints}')
        print("- Instrument sweep points set to: " + anritsu.query('DISPlay:POINtcount?'))

        print("\n\n [✓] Setup succesfull")

        saveConfig(ip, port, centralFreq, freqUnits, span, spanUnits, sweepPoints, integrationBandwidth, integrationBandwidthUnits, sweepTime, sweepContinuously, preAmp, file)


    except:
        print("\n\n[x] Error while setting up instrument")
        sys.exit(1)


    def measure():
        power = anritsu.query(f'FETCh:CHPower:CHPower?')
        gps = anritsu.query(f':FETCh:GPS:FULL?')
        gpsSplit = gps.split(',')
        status = gpsSplit[0]
        if (status == 'NO FIX'):
            return [power, status, None, None, None, None, None]
        else:
            dateTime = gpsSplit[1]
            latitude = gpsSplit[2]
            longitude = gpsSplit[3]
            altitude = gpsSplit[4]
            satellites = gpsSplit[5]
            return [power, status, dateTime, latitude, longitude, altitude, satellites]

    while True:
        option = input("1 - Start continuous measures\n2 - Single Measure\n3 - Exit\n")
        if option == '1':
            print("\n\n[✓] Starting continuous measures")
            data = []
            while True:
                [power, status, dateTime, latitude, longitude, altitude, satellites] = measure()
                print(f'Successful measure: Power: {power}, Datetime: {dateTime}, GPS Status: {status}')
                if (status == 'NO FIX'):
                    data.append([power, status, None, None, None, None, None])
                else:
                    data.append([power, status, dateTime, latitude, longitude, altitude, satellites])
                meas = pd.DataFrame(data, columns=['Power', 'Status', 'Date Time', 'Latitude', 'Longitude', 'Altitude', 'Satellites'])
                meas.to_csv('data/measures.csv', index=False)
                time.sleep(float(sweepTime))
        if option == '2':
            [power, status, dateTime, latitude, longitude, altitude, satellites] = measure()
            print(f'\n\n[✓] Successful measure: Power: {power}, Datetime: {dateTime}, GPS Status: {status}')
        if option == '3':
            anritsu.close()
            rm.close()
            sys.exit(0)

if __name__ == "__main__":
    main()