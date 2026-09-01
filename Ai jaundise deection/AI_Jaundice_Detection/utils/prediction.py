import os
import numpy as np
from PIL import Image

MODEL_PATH = "model/jaundice_model.h5"

IMG_SIZE = 224


def preprocess_image(image):

    image = image.convert("RGB")

    image = image.resize((IMG_SIZE, IMG_SIZE))

    image_array = np.array(image)

    image_array = image_array / 255.0

    image_array = np.expand_dims(image_array, axis=0)

    return image_array


def predict_jaundice(image):

    """
    Temporary prediction function.

    Replace this with the trained TensorFlow model
    after jaundice_model.h5 is created.
    """

    # ------------------------------------------------
    # Temporary demonstration
    # ------------------------------------------------

    probability = 0.0

    result = "normal"

    return result, probability