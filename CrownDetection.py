import cv2
import numpy as np

image = cv2.imread("ImageFiles/Test data/67.jpg")

def Crown_fun(img):

    temp = cv2.imread("ImageFiles/Templates/crown3.png")
    temp90 = cv2.imread("ImageFiles/Templates/crown90.png")
    temp180 = cv2.imread("ImageFiles/Templates/crown180.png")
    temp270 = cv2.imread("ImageFiles/Templates/crown270.png")

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

    crown_counts = np.zeros((ROWS, COLS), dtype=int)

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
            total = 0
            for t in [threshTemp, threshTemp90, threshTemp180, threshTemp270]:
                t = (t > 0).astype(np.uint8) * 255
                num_labels, labels = cv2.connectedComponents(t)
                total += num_labels - 1  # træk baggrund fra

            crown_counts[y, x] = total

    return crown_counts
    #print("Kroner pr. felt:")
    #print(crown_counts)




