# AI Jaundice Detection

This repository contains a prototype computer-vision application for screening jaundice from eye images. The project is implemented as a Streamlit app and includes image preprocessing, eye/sclera detection utilities, and a training pipeline for a TensorFlow model.

## Overview

The application is designed to:

- Capture a live eye image from the device camera
- Preprocess and enhance the image for analysis
- Detect the eye region and sclera region
- Run a model-based screening step to classify whether jaundice is likely

The project currently includes a working UI and supporting image processing code, while the actual model inference is still a placeholder in the demo flow.

## Project structure

```text
.
├── README.md
└── Ai jaundise deection/
    └── AI_Jaundice_Detection/
        ├── app.py
        ├── requirements.txt
        ├── assets/
        │   ├── background.png
        │   └── logo.png
        ├── detection/
        │   ├── eye_detection.py
        │   └── sclera_detection.py
        ├── model/
        │   ├── class_names.txt
        │   └── jaundice_model.h5
        ├── training/
        │   ├── evaluate_model.py
        │   ├── preprocessing.py
        │   └── train_model.py
        └── utils/
            ├── image_processing.py
            └── prediction.py
```

## Core code modules

### 1. Streamlit application (`app.py`)

`app.py` is the main entry point. It:

- sets the page configuration for a wide-screen UI
- displays a title, instructions, and a camera capture widget
- allows the user to take a picture of the eye
- renders the captured image and a placeholder analysis result

The current logic simulates a detection result with a temporary value:

```python
result = "normal"
```

This means the app is a working prototype interface, but model integration is not yet finished in the live UI.

### 2. Image preprocessing (`utils/image_processing.py`)

This module provides utility functions for resizing and normalizing images:

- `resize_image(image, width=224, height=224)`
- `normalize_image(image)`
- `improve_image(image)`

The image enhancement uses Lab color-space processing with CLAHE (Contrast Limited Adaptive Histogram Equalization), which helps improve contrast before model prediction.

### 3. Eye and sclera detection (`detection/`)

#### Eye detection

`detection/eye_detection.py` uses OpenCV Haar cascade classifiers to detect faces/eyes in an image:

- converts the image to grayscale
- loads `haarcascade_eye.xml`
- uses `detectMultiScale()` with parameters such as `scaleFactor=1.1` and `minNeighbors=5`
- returns detected eye bounding boxes

#### Sclera detection

`detection/sclera_detection.py` extracts the sclera region using an HSV mask:

- converts the image to HSV
- defines lower and upper color bounds
- creates a mask and applies it to the original image
- returns the masked sclera image and mask

### 4. Prediction pipeline (`utils/prediction.py`)

The prediction utility defines:

- `preprocess_image(image)`
- `predict_jaundice(image)`

The file contains a placeholder implementation that currently returns:

- `result = "normal"`
- `probability = 0.0`

This indicates the model connection is planned but not yet implemented.

### 5. Training pipeline (`training/`)

#### `training/preprocessing.py`

This module handles dataset loading and image preparation for training. It is designed to convert dataset examples into a format suitable for a TensorFlow image model.

#### `training/train_model.py`

This script builds and trains a binary image classification model using MobileNetV2:

- uses `tf.keras.applications.MobileNetV2`
- disables the top layer and freezes the base model
- adds a global average pooling layer
- adds a dropout layer
- uses a sigmoid output layer for binary classification
- compiles with binary cross-entropy and accuracy, precision, and recall metrics
- trains for 10 epochs
- saves the trained model to `model/jaundice_model.h5`

### 6. Model artifact (`model/`)

The repository includes:

- `model/jaundice_model.h5` - trained model file
- `model/class_names.txt` - label list for model classes

## Setup and run

### Install dependencies

From the project directory:

```bash
cd "Ai jaundise deection/AI_Jaundice_Detection"
pip install -r requirements.txt
```

### Run the app

```bash
streamlit run app.py
```

This starts the camera-based screening application in the browser.

## Dependencies

The project relies on:

- Python 3.x
- OpenCV (`opencv-python`)
- TensorFlow / Keras
- NumPy
- Pillow (PIL)
- Streamlit

These are declared in `AI_Jaundice_Detection/requirements.txt`.

## Current status

This is an educational prototype and not a clinical diagnostic tool. The codebase demonstrates the end-to-end architecture for an AI jaundice screening application, but the final production workflow still requires:

- a labeled dataset of jaundice and non-jaundice eye images
- trained model validation and calibration
- real prediction integration in the Streamlit UI
- robust image quality checks and medical safety constraints

## Notes

The repository structure suggests that the team intends to build a classification workflow around image preprocessing, eye detection, CNN modeling, and screening output generation. The current implementation is a strong foundation for future development, but several inference and data pipeline steps remain placeholders.
