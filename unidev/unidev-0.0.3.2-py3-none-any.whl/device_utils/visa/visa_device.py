import pyvisa

from time import sleep
from unidev.device_utils.device import Device


class VisaDevice(Device):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.resource_manager = pyvisa.ResourceManager()
		self.instrument = None

	def connect(self):
		try:
			if self.address is not None:
				self.instrument = self.resource_manager.open_resource(self.address)
				self.instrument.timeout = self.timeout
				self.instrument.read_termination = self.termination
				self.instrument.write_termination = self.termination

				self.connected = True

		except pyvisa.Error:
			self.connected = False

		return self.connected

	def disconnect(self):
		self.instrument.close()
		self.connected = False

	def is_connected(self):
		return self.connected

	def wait(self):
		while True:
			opc = self.opc()

			if opc() != "+1" and opc != "1":
				sleep(0.01)
			else:
				return

	def check_error(self):
		err = self.instrument.query(":SYST:ERR?")

		if "No error" not in err:
			return err
		else:
			return 0

	def send(self, cmd):
		self.wait()

		if "?" in cmd:
			out = self.instrument.query(cmd)
			self.instrument.write("*OPC")

			return out
		else:
			self.instrument.write(cmd)
			self.instrument.write("*OPC")

	def idn(self):
		answer = self.instrument.query("*IDN?")
		return answer

	def opc(self):
		answer = self.instrument.query("*OPC?")
		return answer
