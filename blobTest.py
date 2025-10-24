import cv2
import numpy as np
import glob, os

# Load image
imageMatch = cv2.imread("ImageFiles/CroppedBoards/1.jpg")
img = cv2.imread("ImageFiles/CroppedBoards/1.jpg", cv2.IMREAD_GRAYSCALE)
temp = cv2.imread("ImageFiles/Templates/crown3.png")
temp90 = cv2.imread("ImageFiles/Templates/crown90.png")
temp180 = cv2.imread("ImageFiles/Templates/crown180.png")
temp270 = cv2.imread("ImageFiles/Templates/crown270.png")
match = cv2.matchTemplate(imageMatch, temp, cv2.TM_CCOEFF_NORMED)
match90 = cv2.matchTemplate(imageMatch, temp90, cv2.TM_CCOEFF_NORMED)
match180 = cv2.matchTemplate(imageMatch, temp180, cv2.TM_CCOEFF_NORMED)
match270 = cv2.matchTemplate(imageMatch, temp270, cv2.TM_CCOEFF_NORMED)
threshTemp = cv2.threshold(match, 0.55, 255, cv2.THRESH_BINARY)[1]
threshTemp90 = cv2.threshold(match90, 0.55, 255, cv2.THRESH_BINARY)[1]
threshTemp180 = cv2.threshold(match180, 0.55, 255, cv2.THRESH_BINARY)[1]
threshTemp270 = cv2.threshold(match270, 0.55, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)[1]


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
cv2.imshow("image", imageMatch)
cv2.imshow("thresh", thresh)
cv2.imshow("match", match)
cv2.imshow("thresh", threshTemp)
cv2.imshow("thresh90", threshTemp90)
cv2.imshow("thresh180", threshTemp180)
cv2.imshow("thresh270", threshTemp270)
cv2.waitKey(0)