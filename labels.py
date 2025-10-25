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

'''import os
import cv2

# Liste til at gemme alle boards
fullBoards = []

# Funktion til at loade alle boards fra en mappe
def input_image_folder():
    imageDir = ("ImageFiles/TestBilleder")

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
    board_folder = f'GroundTruth/board_{board_idx}'
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
print("\nAlle tiles er gemt med labels og kroner!\n")'''

import os
import cv2

# Liste til at gemme alle boards
fullBoards = []

# Funktion til at loade alle boards fra en mappe
def input_image_folder():
    imageDir = "ImageFiles/TestBilleder"

    if not os.path.isdir(imageDir):
        raise FileNotFoundError(f"The folder does not exist: {imageDir}")

    for file in os.listdir(imageDir):
        full_path = os.path.join(imageDir, file)
        img = cv2.imread(full_path)
        if img is None:
            print(f"Could not load image: {full_path}")
        else:
            print(f"✅ Image loaded: {full_path}")
            fullBoards.append(img)

# Tile-type keys
label_keys = {
    ord('f'): 'forest',
    ord('g'): 'grasslands',
    ord('w'): 'wheat',
    ord('s'): 'swamp',
    ord('m'): 'mine',
    ord('l'): 'lake',
    ord('u'): 'unknown'
}

# Crown keys
crown_keys = {
    ord('0'): 0,
    ord('1'): 1,
    ord('2'): 2,
    ord('3'): 3
}

# Load boards
input_image_folder()
print(f"Total boards loaded: {len(fullBoards)}")

ROWS, COLS = 5, 5
selected_tile = None
current_label = None

def mouse_click(event, x, y, flags, param):
    global selected_tile
    if event == cv2.EVENT_LBUTTONDOWN:
        img, board_idx, cell_h, cell_w = param
        j = x // cell_w
        i = y // cell_h
        selected_tile = (i, j)
        print(f"\n🟨 Klik på Tile ({i},{j}) i board {board_idx}")

for board_idx, img in enumerate(fullBoards):
    print(f"\n========== BOARD {board_idx} ==========")

    board_folder = f'GroundTruth/board_{board_idx}'
    os.makedirs(board_folder, exist_ok=True)

    cell_height = img.shape[0] // ROWS
    cell_width = img.shape[1] // COLS

    display_img = img.copy()
    for i in range(ROWS):
        for j in range(COLS):
            y1, y2 = i * cell_height, (i + 1) * cell_height
            x1, x2 = j * cell_width, (j + 1) * cell_width
            cv2.rectangle(display_img, (x1, y1), (x2, y2), (255, 255, 255), 1)

    cv2.namedWindow("Label board")
    cv2.setMouseCallback("Label board", mouse_click, param=(img, board_idx, cell_height, cell_width))

    while True:
        temp_display = display_img.copy()
        cv2.imshow("Label board", temp_display)
        key = cv2.waitKey(50) & 0xFF

        # Luk board med ESC
        if key == 27:
            print(f"✅ Færdig med board {board_idx}")
            break

        # Hvis der er valgt et tile, vent på label- og crown-keys
        if selected_tile:
            i, j = selected_tile
            tile = img[i*cell_height:(i+1)*cell_height, j*cell_width:(j+1)*cell_width]

            if key in label_keys:
                current_label = label_keys[key]
                print(f"Tile-type: {current_label} — vælg antal kroner (0–3)")
            elif current_label and key in crown_keys:
                crowns = crown_keys[key]

                filename = f"tile_{i}_{j}_{current_label}_{crowns}.jpg"
                save_path = os.path.join(board_folder, filename)
                cv2.imwrite(save_path, tile)
                print(f"💾 Gemte: {save_path}")

                # Grøn ramme rundt om færdigt tile
                y1, y2 = i * cell_height, (i + 1) * cell_height
                x1, x2 = j * cell_width, (j + 1) * cell_width
                cv2.rectangle(display_img, (x1, y1), (x2, y2), (0, 255, 0), 2)

                selected_tile = None
                current_label = None

cv2.destroyAllWindows()
print("\n✅ Alle boards label’et og gemt!\n")