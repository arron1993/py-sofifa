import pytesseract
import numpy as np
import cv2 as cv
import json

from attribute import Attribute


class Collector:
    def __init__(self, image_bytes):
        image = cv.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
        self.original_image = image
        # image = self.resize(image)

        image = self.grayscale(image)
        image = self.gaussian_blur(image)
        image = self.threshold(image)
        image = self.invert(image)
        self.image = image
        self.save(image)

    def collect(self):
        attributes = [
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

        attribute_map = {}
        text = self.to_text()
        for attribute in attributes:
            attr = Attribute(attribute, f"{attribute} ?([0-9]+)")
            attribute_map[attr.key] = attr.apply(text)
        return json.dumps(attribute_map)

    def to_text(self):
        return pytesseract.image_to_string(self.image, lang="eng", config="--psm 6")

    def threshold(self, img):
        return cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

    def resize(self, img):
        return cv.resize(img, (0, 0), fx=2, fy=2)

    def load_image(self):
        return cv.imread("./image.jpg")

    def grayscale(self, img):
        return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    def gaussian_blur(self, img):
        return cv.GaussianBlur(img, (5, 5), 0)

    def save(self, img):
        cv.imwrite("./out.jpg", img)

    def invert(self, img):
        return cv.bitwise_not(img)


if __name__ == "__main__":
    main()
