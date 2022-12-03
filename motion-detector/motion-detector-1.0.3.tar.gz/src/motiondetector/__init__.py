import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sg
from PIL import Image, ImageFilter
from os.path import join, dirname

try:
	from utils.Class import Color, Style
except:
	from .utils.Class import Color, Style

class Kernel:
	blur = np.ones((3, 3))/9
	edges1 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

class MotionDetector:
	def __init__(self, outputDirectory):
		self.outputDirectory = outputDirectory
		self.MAX_IMGS_MATCH_DIST = 1850

	def run(self):
		# define a video capture object
		vid = cv2.VideoCapture(0)

		cur_frame = None
		prev_frame = None

		i = 0
		while True:
			ret, cur_frame = vid.read()

			if prev_frame is not None and self.moving(cur_frame, prev_frame):
					print(Color.primary(f"[MOTION_DETECTOR]: motion {i + 1} detected"))
					
					# save the image
					self.saveCurrentFrame(cur_frame, f'capture{i}.jpg', self.outputDirectory)
					i += 1

			prev_frame = cur_frame

			# the 'q' button is set as the
			# quitting button
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		vid.release()

	def moving(self, img1, img2, accuracy=1):
		if len(img1.shape) not in [1, 3] or len(img2.shape) not in [1, 3]:
			return

		if img1.shape != img2.shape:
			return

		img1 = self.prepareImage(img1)
		img2 = self.prepareImage(img2)

		# euclidian distance between img1 and img2
		dist = np.linalg.norm(img1 - img2)

		return dist >= self.MAX_IMGS_MATCH_DIST * accuracy

	def saveCurrentFrame(self, frame, filename, target_dir):
		# save current frame {frame} as an image

		cv2.imwrite(join(target_dir, filename), frame)


	def prepareImage(self, img):
		if len(img.shape) == 3: #rgb
			img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		img = sg.convolve2d(img, Kernel.blur, mode="same", boundary="fill")

		return img