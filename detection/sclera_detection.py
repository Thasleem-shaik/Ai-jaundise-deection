import cv2
import numpy as np


def detect_sclera(image):

    hsv = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2HSV
    )

    lower = np.array([0, 0, 80])

    upper = np.array([180, 100, 255])

    mask = cv2.inRange(
        hsv,
        lower,
        upper
    )

    sclera = cv2.bitwise_and(
        image,
        image,
        mask=mask
    )

    return sclera, mask