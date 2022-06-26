import pytesseract
import numpy as np
import cv2 as cv
import json

from attribute import Attribute

def load_image():
    return cv.imread("./image.jpg")


def grayscale(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


def gaussian_blur(img):
    return cv.GaussianBlur(img, (5, 5), 0)


def save(img):
    cv.imwrite("./out.jpg", img)


def invert(img):
    return cv.bitwise_not(img)


def main():
    original_image = load_image()
    img = invert(original_image)
    img = grayscale(img)
    img = gaussian_blur(img)
    image_text = pytesseract.image_to_string(img, lang="eng")
    attribute_map = [
        Attribute(label, f'{label} ?([0-9]+)') for label in [
            "Sprint Speed",
            "Finishing",
            "Vision",
            "Agility",
            "Interceptions",
            "Jumping",
            "Acceleration",
            "Att. Position",
            "Crossing",
            "Balance",
            "Heading Acc.",
            "Stamina",
            "Shot Power",
            "FK Acc.",
            "Reactions",
            "Def. Aware",
            "Strength",
            "Long Shots",
            "Long Pass",
            "Composure",
            "Stand Tackle",
            "Aggression",
            "Penalties",
            "Short Pass",
            "Ball Control",
            "Slide Tackle",
            "Volleys",
            "Curve",
            "Dribbling",
        ]
    ]


    atts = {att.key: att.apply(image_text) for att in attribute_map}
    print(json.dumps(atts))








if __name__ == '__main__':
    main()
