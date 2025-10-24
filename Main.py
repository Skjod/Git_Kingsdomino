import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PointCounter import seperateTiles

#importer billede
img = cv.imread("ImageFiles/CroppedBoards/56.jpg")

#øg kontrasten
#plt.subplot(1,2,1)

#brightness = 1
#contrast = 1.5

#conImg = cv.addWeighted(img, contrast, np.zeros(img.shape, img.dtype), 0, brightness)

#lav et grid med 5 rækker og 5 kolonner
ROWS, COLS = 5, 5
cell_height = img.shape[0] // ROWS
cell_width  = img.shape[1] // COLS

#lav tom matrix
board = []

#gennemgå hvert enkelt felt og crop det
for y in range(ROWS):
    row = []
    for x in range(COLS):
        # Klip ét felt ud
        cell = img[y*cell_height:(y+1)*cell_height,
                   x*cell_width:(x+1)*cell_width]
        row.append(cell)
    board.append(row)

terrain_hsv = {
    "forest":  ((35, 15, 0), (85, 255, 70)),
    "Grasslands":  ((35, 50, 70), (85, 255, 255)),
    "Wheat fields":  ((20, 100, 150), (35, 255, 255)),
    "Swamps": ((20, 50, 70), (50, 200, 180)),
    "Mines": ((0, 0, 0), (180, 100, 255)),
    "Lakes":   ((90, 50, 50), (140, 255, 255))
}

for y in range(ROWS):
    for x in range(COLS):
        cell = board [y][x]
        hsv_cell = cv.cvtColor(cell, cv.COLOR_BGR2HSV)

        terrain_found = None
        for terrain, (lower, upper) in terrain_hsv.items():
            mask = cv.inRange(hsv_cell, np.array(lower), np.array(upper))
            if cv.countNonZero(mask) > 0.3 * mask.size:  # mere end 50% af pixels matcher
                terrain_found = terrain
                break

        if terrain_found is None:
            terrain_found = "unknown"  # fallback

                # Gem terræntypen i matrixen
        board[y][x] = {"terrain": terrain_found, "crowns": 0}

for r, row in enumerate(board):
        for c, cell in enumerate(row):
            print(f"Felt ({r},{c}): {cell['terrain']}, {cell['crowns']} kroner")


            # Vis feltet i et vindue
        #window_name = f"Felt {y},{x}"
        #cv.imshow(window_name, cell)



#cv.imshow("felt", cells[1][0])
#cv.waitKey(0)
#cv.destroyAllWindows()
''''template = cv.imread("ImageFiles/Templates/")

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#templated = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)

mask = cv.inRange(hsv, (36, 25, 25), (70, 255,100))

imask = mask>0
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

cv.imshow("green img", green)
cv.waitKey(0)'''