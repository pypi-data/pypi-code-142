import serial
import serial.tools.list_ports as list_ports

from unidev.device_utils.device import Device


def get_connected_devices():
	ports = serial.tools.list_ports.comports()
	devices = []

	for port, desc, hwid in sorted(ports):
		devices.append(port)

	return devices


class SerialDevice(Device):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		if baud_rate := kwargs.get("baud_rate"):
			self.baud_rate = baud_rate

		self.device = None

	def connect(self):
		self.device = serial.Serial(
			self.address,
			self.baud_rate,
			timeout=self.timeout)

		self.connected = True

		return self.connected

	def write(self, data):
		if type(data) != bytes:
			encoded_data = data.encode()
			self.device.write(encoded_data)
		else:
			self.device.write(data)

	def writeln(self, data):
		self.write(data + "\n")

	def read_line(self):
		data = self.device.readline()

		return data

	def read(self, byte_count=0):
		if byte_count == 0:
			return self.read_line()
		else:
			data = self.device.read(size=byte_count)

			return data

