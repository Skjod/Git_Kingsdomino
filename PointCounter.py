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

def PointCounter_fun(matrix,crowns,tileTypes):
    ### spit function
    dq = deque([])
    blob = 0 #information stored in current blob
    blobs = [] #collected information about blobs
    points = []
    crownCount = 0
    coordinates = ""

    def spit(i, j, matrix, blobNum, blob, crownCount, match, crowns):
        if matrix[i][j] != "burnt":
            blob += 1
            crownCount += crowns[i][j]

        if dq:
            dq.popleft()
            dq.popleft()
        if j + 1 < cols and matrix[i][j+1] == match:
            dq.append(i)
            dq.append(j+1)
        if i + 1 < rows and matrix[i+1][j] == match:
            dq.append(i+1)
            dq.append(j)
        if i - 1 >= 0 and matrix[i-1][j] == match:
            dq.append(i-1)
            dq.append(j)
        if j - 1 >= 0 and matrix[i][j-1] == match:
            dq.append(i)
            dq.append(j-1)

        matrix[i][j] = "burnt"
        if dq:
            spit(dq[0], dq[1], matrix, blobNum, blob, crownCount, match, crowns)
        else:
            blobs.append(blob)
            points.append(blobs[blobNum] * crownCount)


    blobNum = 0
    for match in tileTypes:
        #print(match)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == match:
                    #print("blob detected")
                    spit(i, j, matrix, blobNum, blob, crownCount, match, crowns)
                    coordinates += str(match) + " at: (" + str(i + 1) + ", " + str(j + 1) + "), with " + str(blobs[blobNum]) + " connected tiles\n"
                    blobNum += 1

    coordinates += "\ncrowns detected at: "
    for i in range(rows):
        for j in range(cols):
            if crowns[i][j] > 0:
                coordinates += "\n" + str(crowns[i][j]) + " crown(s) detected at: (" + str(i + 1) + ", " + str(j + 1) + ")"
    coordinates += "\n\ntotal points: " + str(sum(points))

    #print(points)
    return coordinates

    '''for i in range(rows):
        for j in range(cols):
            print(plane[i][j], end=" ")
        print()'''

    seperateTiles(plane, planeCrowns, tileElements)

print(PointCounter_fun(plane, planeCrowns, tileElements))