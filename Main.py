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
#print(Classifier_method(image))

'''import cv2 as cv
import numpy as np
import os
from PointCounterLaura import PointCounter_fun_laura
from Classifier import Classifier_fun
from CrownDetection import Crown_fun

# Mappen med billeder
image_folder = "ImageFiles/Test data"

# Tile labels
labels = ["forest", "grasslands", "wheat", "swamp", "mine", "lake"]

# Loop over alle billeder
for idx, file in enumerate(os.listdir(image_folder)):
    full_path = os.path.join(image_folder, file)
    image = cv.imread(full_path)
    if image is None:
        print(f"Could not load image: {full_path}")
        continue

    print(f"\nProcessing board {idx}: {file}")

    # Kør klassificering og crowns detection
    tiles = Classifier_fun(image)
    crowns = Crown_fun(image)

    # Kør point counter og gem tiles til confusion matrix
    points = PointCounter_fun_laura(tiles, crowns, labels, board_idx=idx)

    print(f"Board {idx} ({file}) score: {points}")'''