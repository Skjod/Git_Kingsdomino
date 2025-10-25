import os
import cv2
import numpy as np
from collections import deque

def PointCounter_fun_laura(matrix, crowns, tileTypes, board_image, board_idx=0):
    """
    Gemmer hver tile som JPG med tile-type, crowns, position og board
    Gemmer det faktiske tile-billede, ikke en sort placeholder
    """
    dq = deque([])
    blob = 0
    blobs = []
    points = []
    crownCount = 0

    # Opret folder til dette board
    board_folder = f'Predictions/board_{board_idx}'
    os.makedirs(board_folder, exist_ok=True)

    ROWS, COLS = len(matrix), len(matrix[0])
    cell_height = board_image.shape[0] // ROWS
    cell_width = board_image.shape[1] // COLS

    def spit(i, j, matrix, blobNum, blob, crownCount, match, crowns_matrix):
        if matrix[i][j] != "burnt":
            blob += 1
            crownCount += crowns_matrix[i][j]

            # Udklip tile fra originalbilledet
            tile_img = board_image[i*cell_height:(i+1)*cell_height,
                                   j*cell_width:(j+1)*cell_width]

            # Gem tile som JPG med info i filnavn
            filename = f"tile_{i}_{j}_{match}_{crowns_matrix[i][j]}.jpg"
            cv2.imwrite(os.path.join(board_folder, filename), tile_img)

        if dq:
            dq.popleft()
            dq.popleft()
        if j + 1 < COLS and matrix[i][j+1] == match:
            dq.append(i)
            dq.append(j+1)
        if i + 1 < ROWS and matrix[i+1][j] == match:
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
            spit(dq[0], dq[1], matrix, blobNum, blob, crownCount, match, crowns_matrix)
        else:
            blobs.append(blob)
            points.append(blobs[blobNum] * crownCount)

    blobNum = 0
    for match in tileTypes:
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == match:
                    print(match, "at: ", i, j)
                    spit(i, j, matrix, blobNum, blob, crownCount, match, crowns)
                    blobNum += 1

    print(blobs)
    return sum(points)

'''import os
import csv
from collections import deque
import copy  # <-- til at gemme kopi af matrix

def PointCounter_fun_laura(matrix, crowns, tileTypes, board_idx=0, output_csv_folder="PredictionsCSV"):
    """
    Beregner points via blobs og crowns (som før)
    Samtidig gemmes CSV med hver tile (faktisk tile_type og crowns)
    """

    # Gem kopi af matrix til CSV, inden vi ændrer den til 'burnt'
    matrix_for_csv = copy.deepcopy(matrix)

    dq = deque([])
    blob = 0
    blobs = []
    points = []
    crownCount = 0

    ROWS, COLS = len(matrix), len(matrix[0])

    def spit(i, j, matrix, blobNum, blob, crownCount, match, crowns_matrix):
        if matrix[i][j] != "burnt":
            blob += 1
            crownCount += crowns_matrix[i][j]

        if dq:
            dq.popleft()
            dq.popleft()
        if j + 1 < COLS and matrix[i][j+1] == match:
            dq.append(i)
            dq.append(j+1)
        if i + 1 < ROWS and matrix[i+1][j] == match:
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
            spit(dq[0], dq[1], matrix, blobNum, blob, crownCount, match, crowns_matrix)
        else:
            blobs.append(blob)
            points.append(blobs[blobNum] * crownCount)

    blobNum = 0
    for match in tileTypes:
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == match:
                    spit(i, j, matrix, blobNum, blob, crownCount, match, crowns)
                    blobNum += 1

    # --- Gem CSV med hver tile ---
    os.makedirs(output_csv_folder, exist_ok=True)
    csv_path = os.path.join(output_csv_folder, f"board_{board_idx}_predictions.csv")
    with open(csv_path, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["board","tile_y","tile_x","tile_type","crowns"])
        for y in range(ROWS):
            for x in range(COLS):
                writer.writerow([f"board_{board_idx}", y, x, matrix_for_csv[y][x], crowns[y][x]])

    print(f"CSV gemt for board {board_idx}: {csv_path}")

    return sum(points)'''