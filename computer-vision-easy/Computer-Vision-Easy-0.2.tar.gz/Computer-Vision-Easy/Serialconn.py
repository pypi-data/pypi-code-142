import serial
import time
import logging
import serial.tools.list_ports

class Serial_object:
    def __init__(self,  port=None, baud=9600):
        self.port = port
        self.baud = baud
        connected = False
        if self.port is None:
            ports = list(serial.tools.list_ports.comports())
            for p in ports:
                
                print(f'{p.description} Connected')
                self.ser = serial.Serial(p.device)
                self.ser.baudrate = baud
                connected = True
            if not connected:
                logging.warning("Please enter COM Port Number.")

        else:
            try:
                self.ser = serial.Serial(self.port, self.baud)
                print("Serial Device Connected")
            except:
                logging.warning("Serial Device Not Connected")
def main():
    arduino = Serial_object()
   

if __name__ == "__main__":
    main()
