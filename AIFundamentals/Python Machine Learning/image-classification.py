import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Function to load images from a directory
def load_images_from_folder(folder):
    images = []
    labels = []
    print(f"Loading images from: {folder}")  # Print the path being used
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        print(f"Loading image: {img_path}")  # Print each image path
        img = cv2.imread(img_path)
        if img is not None:
            img = cv2.resize(img, (64, 64))  # Resize images
            images.append(img)
            # Assuming the folder name is the label
            labels.append(os.path.basename(folder))
        else:
            print(f"Warning: Unable to load image {img_path}")
    return np.array(images), np.array(labels)

# Load flower and table images
flower_images, flower_labels = load_images_from_folder('/Users/kamal/Documents/Python Machine Learning/Dataset/FLOWERS')
table_images, table_labels = load_images_from_folder('/Users/kamal/Documents/Python Machine Learning/Dataset/CARS')

# Combine images and labels
images = np.concatenate((flower_images, table_images), axis=0)
labels = np.concatenate((flower_labels, table_labels), axis=0)

# Flatten the images for training
n_samples, h, w, c = images.shape
X = images.reshape(n_samples, h * w * c)  # Flatten images
y = labels

# Encode labels to integers
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train an SVM classifier
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)

# Test the model on the test set
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Print accuracy
print(f'Accuracy: {accuracy:.2f}')

# Function to predict the class of a new image
def predict_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (64, 64))
    img_flattened = img.reshape(1, -1)  # Flatten the image
    prediction = clf.predict(img_flattened)
    return label_encoder.inverse_transform(prediction)

# Example usage to predict a new image
new_image_path = '/Users/kamal/Documents/Python Machine Learning/car image.jpeg'  # Change to your test image path
predicted_label = predict_image(new_image_path)
print(f'Predicted label for the uploaded image: {predicted_label[0]}')