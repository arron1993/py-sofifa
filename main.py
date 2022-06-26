import pytesseract
import numpy as np
import cv2 as cv
import re

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
            "Wide Back Acceleration",
            "Att. Position",
            "Crossing",
            "Balance",
            "Heading Acc.",
            "Stamina",
            "Shot Power",
            "FK Acc.",
            "Reactions",
            "Def.Aware",
            "Strength",
            "LongShots",
            "Long Pass ",
            "Composure",
            "Stand Tackle",
            "Aggression",
            "Penalties",
            "ShortPass",
            "Ball Control",
            "Slide Tackle",
            "Volleys",
            "Curve",
            "Dribbling",
        ]

    ]


    for att in attribute_map:
        att.apply(image_text)
        print(att)





if __name__ == '__main__':
    main()
