import subprocess

class App:
	def __init__(self, url, runtime):
		self.url = url
		self.activities = {}

	def register_activity(self, activity, activity_name):
		# get current file name
		print("inside register_activity")
		print("registering activity: " + activity_name)
		print("running the activity function that was passed")
		activity()
		self.activities["activity_name"] = activity

		p = subprocess.Popen("ls -lh", stdout=subprocess.PIPE, shell=True)
		print(p.communicate())

	def start(self):
		print("starting app")


	# private functions that we don't need to expose
	# create docker files
	# options for runtimes:
	# https://github.com/openfaas/templates
	