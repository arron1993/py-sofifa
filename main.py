import pytesseract
import numpy as np
import cv2 as cv
import re


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

    sprint_speed = re.findall('Sprint Speed ([0-9]+)', image_text)[0]
    acceleration = re.findall('Acceleration ([0-9]+)', image_text)[0]
    finishing = re.findall('Finishing ?([0-9]+)', image_text)[0]

    print(sprint_speed, acceleration, finishing)




if __name__ == '__main__':
    main()
