import argparse
import cv2
import numpy as np
from matplotlib import image as Image
import os

def parser():
	parse = argparse.ArgumentParser()
	parse.add_argument("--output-dir", "-o", help="images | videos output directory", type=str)
	parse.add_argument("--accuracy", "-ac", help="motions accuracy", type=str)
	

	return parse.parse_args()

def imgsToVideos():
	frameSize = (640, 480)

	out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, frameSize)

	nb_images = 10000
	start = 60000

	for i in range(start, start + nb_images):
		try:
			img = Image.imread(f"/home/ridoineel/Dev/motion_detector/dist/images/capture{i + 1}.jpg")
			out.write(img.astype("uint8"))

			os.system("clear")
			print(i+1)
		except KeyboardInterrupt:
			print("Save")

		i += 1


	out.release()