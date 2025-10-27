from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imutils import paths
from skimage.feature import hog
import cv2
import numpy as np
import pickle
import os


DATASET_PATH = r"C:\Users\laura\Documents\GitHub\Git_Kingsdomino\dataset"
K_NEIGHBORS = 3
JOBS = -1

# find billeder
print("[INFO] loading images...")
imagePaths = list(paths.list_images(DATASET_PATH))

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

    # farvefeatures
    color_features = cv2.resize(image, (16, 16)).flatten() / 255.0

    # kombinér HOG + farve
    return np.hstack([hog_features, color_features])

# loop over alle billeder
for (i, path) in enumerate(imagePaths):
    image = cv2.imread(path)
    features = extract_features(image)
    label = os.path.basename(os.path.dirname(path))

    data.append(features)
    labels.append(label)

    if i % 200 == 0:
        print(f"[INFO] processed {i}/{len(imagePaths)}")

data = np.array(data)
labels = np.array(labels)

print(f"[INFO] feature matrix size: {data.shape}")


le = LabelEncoder()
labels = le.fit_transform(labels)

# split data
(trainX, testX, trainY, testY) = train_test_split(
    data, labels, test_size=0.25, random_state=42, stratify=labels)

# KNN model
print("[INFO] training k-NN classifier...")
model = KNeighborsClassifier(n_neighbors=K_NEIGHBORS, n_jobs=JOBS)
model.fit(trainX, trainY)

# evaluering af model
print("[INFO] evaluating classifier...")
preds = model.predict(testX)

print(classification_report(
    testY,
    preds,
    labels=le.transform(le.classes_),
    target_names=le.classes_,
    zero_division=0
))

# gem model og labelencoder
pickle.dump((model, le), open("knn_model_new.pkl", "wb"))
print("[INFO] model saved to knn_model_new.pkl")