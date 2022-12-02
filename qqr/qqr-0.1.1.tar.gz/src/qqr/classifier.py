from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from pathlib import Path


def Classifier(filepath, verbose=False):
	"""Classify an image as blurred or skewed.

	Args:
		filepath (string): Path to file
		verbose (bool): Enable verbose logging

	Returns:
		type (string): Type of image
	"""

	model = load_model(f"{Path(__file__).parent.absolute()}/cv_vgg_model.h5")
	img = image.load_img(filepath, target_size=(290, 290))
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	images = np.vstack([x])
	pred = model.predict(images, batch_size=1, verbose=(1 if verbose else 0))
	if pred[0][0] > 0.5:
		category = "Blurred"
	elif pred[0][1] > 0.5:
		category = "Original"
	elif pred[0][2] > 0.5:
		category = "Skewed"
	return category
