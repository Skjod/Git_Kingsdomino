import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PointCounterLaura import PointCounter_fun_laura
from Classifier import Classifier_fun
from CrownDetection import Crown_fun



image = cv.imread("ImageFiles/TestBilleder/73.jpg")

labels = ["forest", "grasslands", "wheat", "swamp", "mine", "lake"]
crowns = Crown_fun(image)
tiles = Classifier_fun(image)

points = PointCounter_fun_laura(tiles, crowns, labels, board_image=image, board_idx=73)

print(points)



#print(Classifier_method(image))