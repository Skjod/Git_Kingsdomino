import cv2 as cv

class SimplePreprocessor:

    # image preprocessor that resizes the image, ignoring the aspect ratio
	def __init__(self, width, height, inter=cv.INTER_AREA):
		self.width = width
		self.height = height
		self.inter = inter
	def preprocess(self, image):
		return cv.resize(image, (self.width, self.height),
			interpolation=self.inter)