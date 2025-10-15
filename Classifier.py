'''import cv2 as cv
import numpy as np
import pickle
from Preprocessor import SimplePreprocessor

(model, le) = pickle.load(open("knn_model.pkl", "rb"))

#importer billede
img = cv.imread("ImageFiles/CroppedBoards/73.jpg")

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

sp = SimplePreprocessor(64, 64)

board_labels = []

for y in range(ROWS):
    row_labels = []
    for x in range(COLS):
        cell = board[y][x]

        # preprocess cellen
        cell_proc = sp.preprocess(cell).reshape(1, 64*64*3)

        # lav prediktion
        pred = model.predict(cell_proc)[0]

        # konverter tal til tekstlabel
        label_text = le.inverse_transform([pred])[0]
        row_labels.append(label_text)

    board_labels.append(row_labels)

# print hele boardet med tekstlabels
for row in board_labels:
    print(row)'''

from skimage.feature import hog
import cv2
import numpy as np
import pickle

# load model
(model, le) = pickle.load(open("knn_model.pkl", "rb"))

# importer billede
img = cv2.imread("ImageFiles/CroppedBoards/62.jpg")

ROWS, COLS = 5, 5
cell_height = img.shape[0] // ROWS
cell_width  = img.shape[1] // COLS

board_labels = []

# samme extract_features som i træningen!
def extract_features(image):
    image = cv2.resize(image, (64, 64))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hog_features = hog(
        gray,
        orientations=9,
        pixels_per_cell=(8, 8),
        cells_per_block=(2, 2),
        block_norm='L2-Hys',
        transform_sqrt=True,
        feature_vector=True
    )
    color_features = cv2.resize(image, (16, 16)).flatten() / 255.0

    combined = np.hstack([hog_features * 1.5, color_features])
    return combined

for y in range(ROWS):
    row_labels = []
    for x in range(COLS):
        cell = img[y*cell_height:(y+1)*cell_height, x*cell_width:(x+1)*cell_width]
        features = extract_features(cell).reshape(1, -1)
        pred = model.predict(features)[0]
        label = le.inverse_transform([pred])[0]
        row_labels.append(label)
    board_labels.append(row_labels)

# print hele boardet med labels
for row in board_labels:
    print(row)

