#! /usr/bin/env python3.8

from os.path import join, dirname, isdir

try:
	from __init__ import MotionDetector
	from utils.functions import parser
except:
	from .__init__ import MotionDetector
	from .utils.functions import parser

def main():
	data = parser()

	accuracy = data.accuracy
	outputDirectory = data.output_dir

	if not outputDirectory or not isdir(outputDirectory):
		# no output directory as input ?
		# or wrong output directory
		# set default output directory

		parent_dir = dirname(__file__)
		outputDirectory = join(parent_dir, "dist/images")

	motionDetector = MotionDetector(outputDirectory)
	motionDetector.run()

if __name__ == "__main__":
	main()
