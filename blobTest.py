import cv2
import numpy as np

# Load image
image = cv2.imread("ImageFiles/CroppedBoards/3.jpg", cv2.IMREAD_GRAYSCALE)
thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY)[1]

# Setup SimpleBlobDetector parameters
params = cv2.SimpleBlobDetector_Params()

# Thresholds for binarization
params.minThreshold = 10
params.maxThreshold = 200

# Color filter
params.filterByColor = True
params.blobColor = 0

# Filter by Area
params.filterByArea = True
params.minArea = 123
params.maxArea = 400

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1
params.maxCircularity = 1.5

# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.8

# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.01

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect(thresh)

# Draw blobs as red circles
output = cv2.drawKeypoints(thresh, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show the output
cv2.imshow("Blobs Detected", output)
cv2.waitKey(0)