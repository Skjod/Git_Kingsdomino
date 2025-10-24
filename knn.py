from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imutils import paths
from skimage.feature import hog
import cv2
import numpy as np
import argparse
import pickle
import os

# argumenter
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to input dataset")
ap.add_argument("-k", "--neighbors", type=int, default=3, help="# of nearest neighbors")
ap.add_argument("-j", "--jobs", type=int, default=-1, help="# of jobs for KNN")
args = vars(ap.parse_args())

# find billeder
print("[INFO] loading images...")
imagePaths = list(paths.list_images(args["dataset"]))

data = []
labels = []

# funktion til feature extraction
def extract_features(image):
    image = cv2.resize(image, (64, 64))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # HOG features
    hog_features = hog(
        gray,
        orientations=9,
        pixels_per_cell=(8, 8),
        cells_per_block=(2, 2),
        block_norm='L2-Hys',
        transform_sqrt=True,
        feature_vector=True
    )

    # farvefeatures (nedskaleret for at holde vektoren lille)
    color_features = cv2.resize(image, (16, 16)).flatten() / 255.0

    # kombinér HOG + farve
    return np.hstack([hog_features, color_features])

# loop over alle billeder
for (i, path) in enumerate(imagePaths):
    image = cv2.imread(path)
    features = extract_features(image)
    label = os.path.basename(os.path.dirname(path))  # mappenavn som label

    data.append(features)
    labels.append(label)

    if i % 200 == 0:
        print(f"[INFO] processed {i}/{len(imagePaths)}")

data = np.array(data)
labels = np.array(labels)

print(f"[INFO] feature matrix size: {data.shape}")

# encode labels
le = LabelEncoder()
labels = le.fit_transform(labels)

# split data
(trainX, testX, trainY, testY) = train_test_split(
    data, labels, test_size=0.25, random_state=42, stratify=labels)

# KNN model
print("[INFO] training k-NN classifier...")
model = KNeighborsClassifier(n_neighbors=args["neighbors"], n_jobs=args["jobs"])
model.fit(trainX, trainY)

# evaluering
print("[INFO] evaluating classifier...")
preds = model.predict(testX)

print(classification_report(
    testY,
    preds,
    labels=le.transform(le.classes_),  # alle labels som integers
    target_names=le.classes_,          # tilsvarende navne
    zero_division=0                    # undgår advarsler hvis nogle klasser ikke er i test
))

# gem model og labelencoder
pickle.dump((model, le), open("knn_model.pkl", "wb"))
print("[INFO] model saved to knn_model.pkl")