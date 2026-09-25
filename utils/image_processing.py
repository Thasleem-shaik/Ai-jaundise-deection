import cv2
import numpy as np


def resize_image(image, width=224, height=224):

    return cv2.resize(
        image,
        (width, height)
    )


def normalize_image(image):

    image = image.astype(
        np.float32
    )

    image = image / 255.0

    return image


def improve_image(image):

    lab = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2LAB
    )

    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    l = clahe.apply(l)

    enhanced = cv2.merge(
        (l, a, b)
    )

    enhanced = cv2.cvtColor(
        enhanced,
        cv2.COLOR_LAB2BGR
    )

    return enhanced