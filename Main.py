import cv2 as cv
import numpy as np

img = cv.imread("ImageFiles/CroppedBoards/1.jpg")
template = cv.imread("ImageFiles/Templates/Krone.png")

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#templated = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)

mask = cv.inRange(hsv, (36, 25, 25), (70, 255,255))

imask = mask>0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

cv.imwrite("green.png", green)


cv.imshow("green img", green)
cv.waitKey(0)