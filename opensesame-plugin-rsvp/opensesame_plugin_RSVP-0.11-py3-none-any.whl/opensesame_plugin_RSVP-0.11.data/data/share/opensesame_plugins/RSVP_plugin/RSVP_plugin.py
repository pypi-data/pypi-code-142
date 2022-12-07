#-*- coding:utf-8 -*-

"""
author:

Robbert van der Mijn
robbertmijn@gmail.com

"""

from libopensesame.py3compat import *
from libopensesame.item import item
from libqtopensesame.items.qtautoplugin import qtautoplugin
from openexp.canvas import canvas
import numpy as np
import random

class RSVP_plugin(item):

	"""
	This class (the class with the same name as the module) handles the basic
	functionality of the item. It does not deal with GUI stuff.
	"""

	# Provide an informative description for your plug-in.
	description = u'Add an RSVP to your experiment'

	def reset(self):

		"""
		desc:
			Resets plug-in to initial values.
		"""
		self.var._mode = "text"
		self.var._targets = u'4;8'
		self.var._ntargets = 2
		self.var._targets_shuffle = u'no'
		self.var._distractors = u'q;w;e;r;t;y;u;i;o;p;a;s;d;f;g;h;j;k;l;z;x;c;v;b;n;m'
		self.var._ndistractors = 15
		self.var._distractors_shuffle = u'no'
		self.var._target_positions = u'5;7'
		self.var._stimdur = 300

	def prepare(self):

		# Call the parent constructor.
		item.prepare(self)

		# get target positions from GUI
		target_positions = [int(x) - 1 for x in self.var._target_positions.split(';')]
		
		# get target/distractor identities from text file, or from the GUI directly
		if ".txt" in self.var._targets:
			with open(self.experiment.pool[self.var._targets]) as f:
				targets = f.read()
				targets = targets.split('\n')
		else:
			targets = self.var._targets.split(';')

		if ".txt" in self.var._distractors:
			with open(self.experiment.pool[self.var._distractors]) as f:
				distractors = f.read()
				distractors = distractors.split('\n')
		else:
			distractors = self.var._distractors.split(';')

		# populate a list with canvasses
		self.cnvs_stream = {}

		# for each stimulus in the stream, we check if it needs to be a target of a distractor
		for i in range(self.var._ndistractors + self.var._ntargets):
			if i in target_positions:
				# pop a random target from the list or take the first element
				if self.var._targets_shuffle == "yes":
					t = targets.pop(random.randint(0,len(targets)-1))
				else:
					t = targets.pop(0)

				# create empty canvas
				self.cnvs_stream[str(i)] = canvas(self.experiment)

				# Add text or image from file to canvas
				# TODO: build in checks and warnings here
				if self.var._mode == "text":
					# TODO: allow control of how text is formatted (maybe use skecthpad functionality?)
					self.cnvs_stream[str(i)].text(
					"<span style='color:rgba(0,0,0,.01)'>gb</span>{}<span style='color:rgba(0,0,0,.01)'>gb</span>".format(t),
					font_size=48,
					color=u'rgb(190,190,190)',
					x=0,
					y=0
					)
				else:
					self.cnvs_stream[str(i)].image(self.experiment.pool[t])
					
				self.var.set('stim_%d' % i, t)

			else:
				# pop a random distractor from the list or take the first element
				if self.var._distractors_shuffle == "yes":
					d = distractors.pop(random.randint(0,len(distractors)-1))
				else:
					d = distractors.pop(0)

				# create empty canvas
				self.cnvs_stream[str(i)] = canvas(self.experiment)
				if self.var._mode == "text":

					self.cnvs_stream[str(i)].text(
					"<span style='color:rgba(0,0,0,.01)'>gb</span>{}<span style='color:rgba(0,0,0,.01)'>gb</span>".format(d),
					font_size=48,
					color=u'rgb(190,190,190)',
					x=0,
					y=0
					)
				else:
					self.cnvs_stream[str(i)].image(self.experiment.pool[d])

				self.var.set('stim_%d' % i, d)

		# create fixation canvas	
		self.cnvs_fix = canvas(self.experiment)

	def run(self):

		for i in range(self.var._ndistractors + self.var._ntargets):
			t = self.cnvs_stream[str(i)].show()
			self.sleep(self.var._stimdur)


class qtRSVP_plugin(RSVP_plugin, qtautoplugin):

	"""
	This class handles the GUI aspect of the plug-in. By using qtautoplugin, we
	usually need to do hardly anything, because the GUI is defined in info.json.
	"""

	def __init__(self, name, experiment, script=None):

		"""
		Constructor.

		Arguments:
		name		--	The name of the plug-in.
		experiment	--	The experiment object.

		Keyword arguments:
		script		--	A definition script. (default=None)
		"""

		# We don't need to do anything here, except call the parent
		# constructors.
		RSVP_plugin.__init__(self, name, experiment, script)
		qtautoplugin.__init__(self, __file__)