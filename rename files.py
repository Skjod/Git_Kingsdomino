import os
os.getcwd()
collection = "dataset/wheat/"
for i, filename in enumerate(os.listdir(collection)):
    os.rename("dataset/wheat/" + filename, "dataset/wheat/" + str(i) + ".jpg")