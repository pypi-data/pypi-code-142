from unidev.device_utils.visa.visa_device import VisaDevice


class VisaModelDevice(VisaDevice):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def exec(self, **kwargs):
		out = []
		cmd_list = self.procedure_list.get(kwargs.get("procedure_name"))

		for cmd_item in cmd_list:
			if "cmd" in cmd_item:
				cmd = cmd_item.get("cmd")
				if arg_list := cmd_item.get("args"):
					args = []
					for arg_name in arg_list:
						arg = kwargs.get(arg_name)
						args.append(arg)

					if "{0}" in cmd:
						tmp = self.send(cmd.format(*args))
					else:
						tmp = self.send(cmd % tuple(args))
				else:
					tmp = self.send(cmd)

				if tmp is not None:
					out.append(tmp)

		if len(out) == 1:
			return out[0]
		else:
			return out
