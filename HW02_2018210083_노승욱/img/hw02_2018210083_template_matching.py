import os
import cv2
import numpy as np


os.chdir(os.path.dirname(os.path.abspath(__file__)))

def Result_find(template, imga):
    img = cv2.imread('test_background.png', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('test_background.png')

    w, h = template.shape[::-1]

    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    x, y = maxLoc
    w, h = template.shape[::-1]

    img2 = cv2.rectangle(img2, (x, y), (x +  w, y + h) , (0, 0, 255), 2)
    
    cv2.imshow("Result_img", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()