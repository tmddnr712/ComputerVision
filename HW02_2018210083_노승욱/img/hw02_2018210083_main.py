import os
import cv2
from hw02_2018210083_template_matching import Result_find

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def Main():
    img = cv2.imread('test_background.png', cv2.IMREAD_GRAYSCALE)
    template = cv2.imread('fish.png', cv2.IMREAD_GRAYSCALE)
    Result_find(template, img)

Main()