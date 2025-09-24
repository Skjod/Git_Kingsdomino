import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("ImageFiles/CroppedBoards/2.jpg")

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img)

brightness = 1
contrast = 1.5
img2 = cv.addWeighted(img, contrast, np.zeros(img.shape, img.dtype), 0, brightness)

hsv = cv.cvtColor(img2, cv.COLOR_BGR2HSV)


mask = cv.inRange(hsv, (36, 25, 25), (70, 255,120))

imask = mask>0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

cv.imshow("Brightness", green)
cv.imshow("Contrast", img2)
cv.imshow("Original", img)
cv.waitKey(0)