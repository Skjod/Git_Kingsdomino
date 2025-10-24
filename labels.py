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

# Liste til at gemme alle boards
fullBoards = []

# Funktion til at loade alle boards fra en mappe
def input_image_folder():
    imageDir = "ImageFiles/ConfusionBilleder"

    if not os.path.isdir(imageDir):
        raise FileNotFoundError(f"The folder does not exist: {imageDir}")

    for file in os.listdir(imageDir):
        full_path = os.path.join(imageDir, file)
        img = cv2.imread(full_path)
        if img is None:
            print(f"Could not load image: {full_path}")
        else:
            print(f"Image loaded successfully: {full_path}")
            fullBoards.append(img)

# Tile-type tastatur keys
label_keys = {
    ord('f'): 'forest',
    ord('g'): 'grasslands',
    ord('w'): 'wheat',
    ord('s'): 'swamp',
    ord('m'): 'mine',
    ord('l'): 'lake',
    ord('u'): 'unknown'
}

# Crown-keys
crown_keys = {
    ord('0'): 0,
    ord('1'): 1,
    ord('2'): 2,
    ord('3'): 3
}

# Load boards
input_image_folder()
print(f"Total boards loaded: {len(fullBoards)}")

# Looper igennem alle boards
for board_idx, img in enumerate(fullBoards):
    ROWS, COLS = 5, 5
    cell_height = img.shape[0] // ROWS
    cell_width  = img.shape[1] // COLS

    # Mappen til dette board
    board_folder = f'Confusion matrix data/board_{board_idx}'
    os.makedirs(board_folder, exist_ok=True)

    for y in range(ROWS):
        for x in range(COLS):
            tile = img[y*cell_height:(y+1)*cell_height, x*cell_width:(x+1)*cell_width]
            cv2.imshow("Label tile", tile)
            print(f"\nBoard {board_idx} - Tile ({y},{x})")

            # 1️⃣ Vælg tile-type
            print("Tryk: [f]=forest, [g]=grasslands, [w]=wheat, [s]=swamp, [m]=mine, [l]=lake, [u]=unknown, [ESC]=skip tile")
            key = cv2.waitKey(0)

            if key == 27:  # ESC → spring over
                print("⏭️  Skipped tile")
                continue
            if key not in label_keys:
                print("Ugyldig tast, springer over...")
                continue

            label = label_keys[key]
            print(f"Tile-type valgt: {label}")

            # 2️⃣ Vælg kroner
            print("Tryk 0–3 for antal kroner:")
            crown_key = cv2.waitKey(0)
            if crown_key not in crown_keys:
                print("Ugyldigt antal kroner – sætter til 0.")
                crowns = 0
            else:
                crowns = crown_keys[crown_key]

            # 3️⃣ Gem tile
            filename = f"tile_{y}_{x}_{label}_{crowns}.jpg"
            save_path = os.path.join(board_folder, filename)
            cv2.imwrite(save_path, tile)
            print(f"💾  Gemte: {save_path}")

    print(f"✅ Færdig med board {board_idx}")

cv2.destroyAllWindows()
print("\nAlle tiles er gemt med labels og kroner!\n")