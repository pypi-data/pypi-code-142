import os
import subprocess

from termcolor import cprint as print

from ...tools.hooksmanager import hooksManager
from ...tools.configuration import ConfigurationTool
from .ideploymentaction import IDeploymentAction
from ...enums import EnvironmentType, HookTypes


class ZappaDeployment(IDeploymentAction):
	""" Deployment through Zappa
	"""
	@classmethod
	def shouldExecute(cls):
		""" Check if the Action should be deployed
		"""
		# Check if there is an zappa folder
		return os.path.exists("zappa_settings.json")

	def start(self, environType, **kwargs):
		""" Start the deployment
		"""
		# Get the configs
		ConfigurationTool.readConfig()

		# Check if there is an template
		if os.path.exists("zappa_settings.json") is False:
			raise Exception("Cant find Zappa template: 'zappa_settings.json'")

		# Remember the environment type for later
		self.environment = environType

		# Check if it is the production environment
		if self.environment == EnvironmentType.PRODUCTION:
			# Check of we een stagename override hebben
			if ConfigurationTool.getExtraConfig("prod-zappa-stage") is not None:
				stageName = ConfigurationTool.getExtraConfig("prod-zappa-stage")
			else:
				stageName = "production"
		else:
			# Check of we een stagename override hebben
			if ConfigurationTool.getExtraConfig("dev-zappa-stage") is not None:
				stageName = ConfigurationTool.getExtraConfig("dev-zappa-stage")
			else:
				stageName = "dev"

		# Check of het een array is
		if isinstance(stageName, list) is True:
			for sName in stageName:
				# Deploy the stage
				self._deployStage(sName)

		else:
			# Deploy the stage
			self._deployStage(stageName)

	def _deployStage(self, stageName):
		""" Run the zappa command
		"""
		# Execute the PRE_COMPILE hooks
		hooksManager.executeHooks(self.environment, HookTypes.PRE_COMPILE)

		# Create a temporary directory
		print("Creating environment")
		self._createTempDir()

		# Execute the POST_COMPILE hooks
		hooksManager.executeHooks(self.environment, HookTypes.POST_COMPILE)

		# Execute the PRE_INSTALL hooks
		hooksManager.executeHooks(self.environment, HookTypes.PRE_INSTALL)

		# Check the dependencies
		print("Installing dependencies")
		self._checkDependencies()

		# Execute the POST_INSTALL hooks
		hooksManager.executeHooks(self.environment, HookTypes.POST_INSTALL)

		# Execute the PRE_DEPLOYMENT hooks
		hooksManager.executeHooks(self.environment, HookTypes.PRE_DEPLOYMENT)

		# Zapping it
		print("Zappa-ing: %s" % stageName)
		# Find how to run zappa
		zappaCommand = self._findZappa()

		# Check if we could find a zappa
		if zappaCommand is None:
			raise Exception("Could not find Zappa. Make sure it is installed.")

		# Run the deployment command
		try:
			subprocess.check_output("cd %s && %s deploy %s" % (self.location, zappaCommand, stageName), stderr=subprocess.STDOUT, shell=True)
		except subprocess.CalledProcessError as e:
			# Check if it was already deployed
			if b"did you mean to call update" in e.output:
				# Run the update command
				try:
					subprocess.check_output("cd %s && %s update %s" % (self.location, zappaCommand, stageName), stderr=subprocess.STDOUT, shell=True)
				except subprocess.CalledProcessError as e:
					print(e.output, "red")
					return False
			else:
				print("An error occured", "red")
				return False
		finally:
			# Execute the POST_DEPLOYMENT hooks
			hooksManager.executeHooks(self.environment, HookTypes.POST_DEPLOYMENT)

	def _findZappa(self):
		""" Search for Zappa
		"""
		# Check if zappa is available as a root level
		try:
			subprocess.check_output("zappa", shell=True)
		except subprocess.CalledProcessError:
			pass
		else:
			return "zappa"

		# Check if poetry is available
		if os.path.exists("poetry.lock") is True:
			# Try zappa in poetry
			try:
				subprocess.check_output("poetry run zappa", shell=True)
			except subprocess.CalledProcessError:
				pass
			else:
				return "poetry run zappa"

		return None
