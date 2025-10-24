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

planeCrowns = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)
    planeCrowns.append(row)
planeCrowns[0][1] = 1
planeCrowns[1][1] = 2
# match = "water"

### spit function
dq = deque([])
blob = 0 #information stored in current blob
blobs = [] #collected information about blobs
points = []
crownCount = 0

def spit(i, j, matrix, blobNum, blob, crownCount, match, crowns):
    if matrix[i][j] != "burnt":
        blob += 1
        crownCount += crowns[i][j]

    if dq:
        dq.popleft()
        dq.popleft()

    if matrix[i][j+1] == match:
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

    matrix[i][j] = "burnt"
    if dq:
        spit(dq[0], dq[1], matrix, blobNum, blob, crownCount, match, crowns)
    else:
        blobs.append(blob)
        points.append(blobs[blobNum] * crownCount)


### call this method when calculating points; takes 2 matrices and 1 list
def seperateTiles(matrix, crowns, tileTypes):
    blobNum = 0
    for match in tileTypes:
        print(match)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == match:
                    print("blob detected")
                    print(i, j)
                    spit(i, j, matrix, blobNum, blob, crownCount, match, crowns)
                    blobNum += 1
    print(blobs)
    print(points)


for i in range(rows):
    for j in range(cols):
        print(plane[i][j], end=" ")
    print()

seperateTiles(plane, planeCrowns, tileElements)