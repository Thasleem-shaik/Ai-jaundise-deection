import cv2
import numpy as np


IMG_SIZE = 224


def preprocess_image(image):
    """
    Preprocess an eye image before sending it to the AI model.
    """

    # Resize image
    image = cv2.resize(
        image,
        (IMG_SIZE, IMG_SIZE)
    )

    # Convert BGR to RGB
    image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    # Normalize pixel values
    image = image.astype(
        np.float32
    ) / 255.0

    return image


def enhance_image(image):
    """
    Improve image contrast.
    """

    # Convert RGB to LAB
    lab = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2LAB
    )

    l_channel, a_channel, b_channel = cv2.split(lab)

    # CLAHE for contrast enhancement
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    l_channel = clahe.apply(l_channel)

    # Merge channels
    enhanced = cv2.merge(
        (l_channel, a_channel, b_channel)
    )

    # Convert back to RGB
    enhanced = cv2.cvtColor(
        enhanced,
        cv2.COLOR_LAB2RGB
    )

    return enhanced


def prepare_image(image):
    """
    Complete preprocessing pipeline.
    """

    image = enhance_image(image)

    image = preprocess_image(image)

    # Add batch dimension
    image = np.expand_dims(
        image,
        axis=0
    )

    return image