import cv2 as cv
from PointCounter import PointCounter_fun
from Classifier import Classifier_fun
from CrownDetection import Crown_fun


image = cv.imread("ImageFiles/Test data/73.jpg")

labels = ["forest", "grasslands", "wheat", "swamp", "mine", "lake"]
crowns = Crown_fun(image)
tiles = Classifier_fun(image)

points = PointCounter_fun(tiles, crowns, labels)

print(points)
