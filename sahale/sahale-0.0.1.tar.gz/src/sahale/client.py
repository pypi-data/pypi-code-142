class Client:
	"""Client for accessing Sahale.

	"""
	def __init__(self, url):
		self.url = url

	def execute_activity(self, activity_name):
		# need to submit a request to the sahale backend to find the activity by name, and execute it
		print("executing activity: " + activity_name)
		return "some result"