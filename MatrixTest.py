import numpy as np
import cv2 as cv
from collections import deque

rows = 5
cols = 5

tileType = ["forest", "grass", "water", "desert"]
plane = []


for i in range(rows):
    row = []
    for j in range(cols):
        row.append(tileType[0])
    plane.append(row)

plane[1][1] = tileType[2]
plane[1][2] = tileType[2]
plane[3][3] = tileType[2]
match = "water"
noOfMatches = 0

dq = deque([])
blob = []
blobs = []


def spit(i, j, blobNum):
    blob.append(i)
    blob.append(j)
    if dq:
        dq.popleft()
        dq.popleft()

    if plane[i][j+1] == match:
        dq.append(i)
        dq.append(j+1)
    if plane[i+1][j] == match:
        dq.append(i+1)
        dq.append(j)
    if plane[i-1][j] == match:
        dq.append(i-1)
        dq.append(j)
    if plane[i][j-1] == match:
        dq.append(i)
        dq.append(j-1)

    plane[i][j] = "burnt"
    if dq:
        spit(dq[0], dq[1], blobNum)
    else:
        blobs.append(blob.copy())
        blob.clear()


# for i in range(rows):
#     for j in range(cols):
#         print(plane[i][j], end=" ")
#     print()


for i in range(rows):
    for j in range(cols):
        if plane[i][j] == match:
            spit(i, j, noOfMatches)
            noOfMatches += 1
            print("blob detected")
            print(i, j)

print(blobs)