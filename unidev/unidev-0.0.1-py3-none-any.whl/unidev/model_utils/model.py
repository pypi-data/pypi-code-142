import json


class Model:
	data = None

	data_file = None
	data_dump = None

	def __init__(self, path=None):
		if path is not None:
			self.data_file = open(path, 'r+')
		else:
			self.data = None
			return

		try:
			self.data_dump = json.load(self.data_file)
		except json.decoder.JSONDecodeError:
			self.data = None
			return

		self.data = {}

		if info := self.data_dump.get("info"):
			self.data.update(info)
		if config := self.data_dump.get("config"):
			self.data.update(config)
		if params := self.data_dump.get("params"):
			self.data["params"] = params
		if procedure := self.data_dump.get("procedure_list"):
			self.data["procedure_list"] = procedure

	def update(self, category, name, value):
		self.data_dump[category][name] = value

		self.data_file.seek(0)
		json.dump(self.data_dump, self.data_file, indent=4)
		self.data_file.truncate()

	def get(self, param_name):
		if self.data is None:
			return None

		return self.data.get(param_name)

	def set(self, param_name, value):
		if self.data is not None:
			self.data[param_name] = value

	def get_data(self):
		return self.data

