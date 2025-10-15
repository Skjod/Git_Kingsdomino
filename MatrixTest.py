import numpy as np
import cv2 as cv
from collections import deque

### create example matrix
rows = 5
cols = 5
tileElements = ["forest", "grass", "water", "desert"]
plane = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(tileElements[0])
    plane.append(row)
plane[1][1] = tileElements[2]
plane[1][2] = tileElements[2]
plane[3][3] = tileElements[2]
# match = "water"

### spit function
dq = deque([])
# blob = [] #information stored in current blob
# blobs = [] #collected information about blobs

def spit(i, j, matrix, blobNum, blob, blobs, match):
    blob += 1
    print(i, ", ", j, matrix[i][j])
    if dq:
        dq.popleft()
        dq.popleft()

    if matrix[i][j+1] != None and matrix[i][j+1] == match:
        dq.append(i)
        dq.append(j+1)
    if matrix[i+1][j] == match:
        dq.append(i+1)
        dq.append(j)
    if matrix[i-1][j] == match:
        dq.append(i-1)
        dq.append(j)
    if matrix[i][j-1] == match:
        dq.append(i)
        dq.append(j-1)

    # if dq[1] == "burnt":
    #     while "burnt" in dq:
    #         deque.remove("burnt")
    if dq:
        spit(dq[0], dq[1], matrix, blobNum, blob, blobs, match)
    else:
        blobs.append(blob)


def seperateTiles(matrix, tileTypes):
    blobNum = 0
    blob = 0
    blobs = []
    match = ""
    for type in tileTypes:
        match = type
        print(match)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == match:
                    print("blob detected")
                    print(i, j)
                    spit(i, j, matrix, blobNum, blob, blobs, match)
                    blobNum += 1
    print(blobs)


for i in range(rows):
    for j in range(cols):
        print(plane[i][j], end=" ")
    print()

seperateTiles(plane, tileElements)