import cv2 as cv
import numpy as np

rows = 5
cols = 5

plane = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)
    plane.append(row)

for i in range(rows):
    for j in range(cols):
        print(plane[i][j], end=" ")
    print()


