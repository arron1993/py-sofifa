import pytesseract
import numpy as np
import cv2 as cv
import json

from attribute import Attribute


class Collector():
    def __init__(self, image_bytes):
        image = cv.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
        self.original_image = image
        img = self.invert(image)
        img = self.grayscale(img)
        img = self.gaussian_blur(img)
        self.img = img
        self.save(img)


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
            attr = Attribute(attribute, f'{attribute} ?([0-9]+)')
            attribute_map[attr.key] = attr.apply(text)
        return json.dumps(attribute_map)

    def to_text(self):
        return pytesseract.image_to_string(self.img, lang="eng")


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


if __name__ == '__main__':
    main()
