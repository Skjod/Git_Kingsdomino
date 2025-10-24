'''import cv2
import os

fullBoards = []
croppedImages = []

def input_image_folder():
    imageDir = ("ImageFiles/Laura training data 0-30")

    if os.path.isdir(imageDir):
        for file in os.listdir(imageDir):
            full_path = os.path.join(imageDir, file)
            img = cv2.imread(full_path)
            if img is None:
                print(f"Could not load image: {full_path}")
            else:
                print(f"Image loaded successfully: {full_path}")
                fullBoards.append(img)
    else:
        print("This is not a funtional path!")
        input_image_folder()

input_image_folder()

label_keys = {
    ord('f'): 'forest',
    ord('g'): 'grasslands',
    ord('w'): 'wheat',
    ord('s'): 'swamp',
    ord('m'): 'mine',
    ord('l'): 'lake',
    ord('u'): 'unknown'
}

crown_keys = {
    ord('0'): 0,
    ord('1'): 1,
    ord('2'): 2,
    ord('3'): 3,
}

for img in fullBoards:
    ROWS, COLS = 5, 5
    cell_height = img.shape[0] // ROWS
    cell_width = img.shape[1] // COLS

    for y in range(ROWS):
        for x in range(COLS):
            tile = img[y*cell_height:(y+1)*cell_height, x*cell_width:(x+1)*cell_width]
            cv2.imshow("Label tile", tile)
            key = cv2.waitKey(0)
            if key in label_keys:
                label = label_keys[key]
                os.makedirs(f'dataset/{label}', exist_ok=True)
                cv2.imwrite(f'dataset/{label}/tile_{y}_{x}.jpg', tile)
                crowns = cv2.waitKey(0)
                if crowns in crown_keys:
                    with open(f"TrainingInfo//{label}.txt", "a") as f:
                        f.write(f"{crown_keys[crowns]}\n")

            elif key == 27:  # ESC for at stoppe
                break


cv2.destroyAllWindows()'''

import os
import cv2

fullBoards = []  # fyldes med billeder af boards

def input_image_folder():
    imageDir = "ImageFiles/Laura training data 0-30"
    if os.path.isdir(imageDir):
        for file in os.listdir(imageDir):
            full_path = os.path.join(imageDir, file)
            img = cv2.imread(full_path)
            if img is not None:
                fullBoards.append(img)
            else:
                print(f"Could not load image: {full_path}")
    else:
        print("This is not a functional path!")

input_image_folder()

label_keys = {
    ord('f'): 'forest',
    ord('g'): 'grasslands',
    ord('w'): 'wheat',
    ord('s'): 'swamp',
    ord('m'): 'mine',
    ord('l'): 'lake',
    ord('u'): 'unknown'
}

for board_idx, img in enumerate(fullBoards):
    ROWS, COLS = 5, 5
    cell_height = img.shape[0] // ROWS
    cell_width  = img.shape[1] // COLS

    board_folder = f'dataset/board_{board_idx}'
    os.makedirs(board_folder, exist_ok=True)

    for y in range(ROWS):
        for x in range(COLS):
            tile = img[y*cell_height:(y+1)*cell_height, x*cell_width:(x+1)*cell_width]
            cv2.imshow("Label tile", tile)

            # 1. Tile-type
            key = cv2.waitKey(0)
            if key in label_keys:
                label = label_keys[key]

                # 2. Crown-input via terminal
                while True:
                    crown_input = input(f"Board {board_idx}, Tile ({y},{x}), Type {label}, antal kroner (0-3): ")
                    if crown_input in ['0','1','2','3']:
                        crowns = int(crown_input)
                        break
                    print("Forkert input. Indtast 0,1,2 eller 3")

                # 3. Gem fil med info i navnet
                filename = f"tile_{y}_{x}_{label}_{crowns}.jpg"
                cv2.imwrite(os.path.join(board_folder, filename), tile)

            elif key == 27:  # ESC for at stoppe
                break

cv2.destroyAllWindows()