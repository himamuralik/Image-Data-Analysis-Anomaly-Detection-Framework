import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras import layers, models

class SteganalysisModel:
    def __init__(self, input_shape=(128, 128, 3)):
        self.input_shape = input_shape
        self.model = self._build_cnn()

    def _build_cnn(self):
        """
        Builds a Convolutional Neural Network (CNN) to detect 
        high-frequency noise patterns typical in steganography.
        """
        model = models.Sequential([
            # Preprocessing / Feature Extraction Layer
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=self.input_shape),
            layers.MaxPooling2D((2, 2)),
            layers.BatchNormalization(),

            # Deep Feature Learning
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Dropout(0.25),

            layers.Conv2D(128, (3, 3), activation='relu'),
            layers.Flatten(),

            # Classification Head
            layers.Dense(64, activation='relu'),
            layers.Dense(1, activation='sigmoid') # Binary Output: 0=Clean, 1=Stego
        ])
        
        model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
        return model

    def preprocess_image(self, image_path):
        """
        Loads and normalizes an image for the model.
        """
        try:
            img = cv2.imread(image_path)
            img = cv2.resize(img, (self.input_shape[0], self.input_shape[1]))
            img = img / 255.0  # Normalize pixel values
            return np.expand_dims(img, axis=0) # Add batch dimension
        except Exception as e:
            print(f"Error processing image: {e}")
            return None

    def predict(self, image_path):
        """
        Predicts if an image contains hidden data.
        """
        processed_img = self.preprocess_image(image_path)
        if processed_img is not None:
            prediction = self.model.predict(processed_img)
            return "Stego (Hidden Data Detected)" if prediction[0][0] > 0.5 else "Clean Image"
        return "Error"

if __name__ == "__main__":
    # Example usage flow
    print("Initializing Steganalysis Framework...")
    detector = SteganalysisModel()
    print("Model Architecture Built Successfully.")
    detector.model.summary()
