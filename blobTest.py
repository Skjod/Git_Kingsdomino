import cv2
import numpy as np
import glob, os
from collections import deque

from cv2.gapi import combine

# Load image
img = cv2.imread("ImageFiles/CroppedBoards/1.jpg")
#img = cv2.imread("ImageFiles/CroppedBoards/1.jpg", cv2.IMREAD_GRAYSCALE)

temp = cv2.imread("ImageFiles/Templates/crown3.png")
temp90 = cv2.imread("ImageFiles/Templates/crown90.png")
temp180 = cv2.imread("ImageFiles/Templates/crown180.png")
temp270 = cv2.imread("ImageFiles/Templates/crown270.png")

dq = deque([])
blob = 0 #information stored in current blob
blobs = [] #collected information about blobs
points = []
crownCount = 0
blobNum = 0

def spit(i, j, matrix, blobNum):
    if dq:
        dq.popleft()
        dq.popleft()

    if matrix[i][j+1] == 1:
        dq.append(i)
        dq.append(j+1)
    if matrix[i+1][j] == 1:
        dq.append(i+1)
        dq.append(j)
    if matrix[i-1][j] == 1:
        dq.append(i-1)
        dq.append(j)
    if matrix[i][j-1] == 1:
        dq.append(i)
        dq.append(j-1)

    matrix[i][j] = "burnt"
    if dq:
        spit(dq[0], dq[1], matrix, blobNum)

ROWS, COLS = 5, 5
cell_height = img.shape[0] // ROWS
cell_width  = img.shape[1] // COLS

board = []

for y in range(ROWS):
    row = []
    for x in range(COLS):
        # Klip ét felt ud
        cell = img[y*cell_height:(y+1)*cell_height,
                   x*cell_width:(x+1)*cell_width]
        row.append(cell)
    board.append(row)

for y in range(ROWS):
    for x in range(COLS):
        cell = board[y][x]

        match = cv2.matchTemplate(cell, temp, cv2.TM_CCOEFF_NORMED)
        match90 = cv2.matchTemplate(cell, temp90, cv2.TM_CCOEFF_NORMED)
        match180 = cv2.matchTemplate(cell, temp180, cv2.TM_CCOEFF_NORMED)
        match270 = cv2.matchTemplate(cell, temp270, cv2.TM_CCOEFF_NORMED)
        threshTemp = cv2.threshold(match, 0.55, 255, cv2.THRESH_BINARY)[1]
        threshTemp90 = cv2.threshold(match90, 0.55, 255, cv2.THRESH_BINARY)[1]
        threshTemp180 = cv2.threshold(match180, 0.55, 255, cv2.THRESH_BINARY)[1]
        threshTemp270 = cv2.threshold(match270, 0.55, 255, cv2.THRESH_BINARY)[1]
        #thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
        print(threshTemp[0][0])
        if threshTemp[y][x] == 1:
            print("blob detected")
            # print(i, j)
            spit(100, 100, threshTemp)
            blobNum += 1

        window_name = f"Felt {y},{x}"
        cv2.imshow(window_name, threshTemp)

print(blobNum)

print(threshTemp)

# # Setup SimpleBlobDetector parameters
# params = cv2.SimpleBlobDetector_Params()
#
# # Thresholds for binarization
# params.minThreshold = 10
# params.maxThreshold = 200
#
# # Color filter
# params.filterByColor = True
# params.blobColor = 0
#
# # Filter by Area
# params.filterByArea = True
# params.minArea = 123
# params.maxArea = 400
#
# # Filter by Circularity
# params.filterByCircularity = True
# params.minCircularity = 0.1
# params.maxCircularity = 10
#
# # Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.3
#
# # Filter by Inertia
# params.filterByInertia = False
# params.minInertiaRatio = 0.01
#
# # Create a detector with the parameters
# detector = cv2.SimpleBlobDetector_create(params)

# # Detect blobs
# keypoints = detector.detect(thresh)
#
# # Draw blobs as red circles
# output = cv2.drawKeypoints(thresh, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show the output
# cv2.imshow("Blobs Detected", output)
cv2.imshow("image", img)
#cv2.imshow("thresh", thresh)
#cv2.imshow("match", match)
'''cv2.imshow("thresh", threshTemp)
cv2.imshow("thresh90", threshTemp90)
cv2.imshow("thresh180", threshTemp180)
cv2.imshow("thresh270", threshTemp270)'''
cv2.waitKey(0)
