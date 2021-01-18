import numpy as np
import cv2
import random

# Global variables
mouse_is_pressed = False
mouse_start_x = -1
mouse_start_y = -1
color = (255, 255, 255)
mode = 0
items = []

# Mouse event callback
def mouse_callback(event, x, y, flags, param):
    global mouse_is_pressed, mouse_start_x, mouse_start_y, color, mode, img_color
    # Left button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_is_pressed = True
        mouse_start_x = x
        mouse_start_y = y
        color = (random.randrange(256), random.randrange(256), random.randrange(256))
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_is_pressed:
            img_color = np.zeros((rows, cols, 3), np.uint8)
            for i in items:
                if i[-1] == 0:
                    cv2.rectangle(img_color, i[0], i[1], i[2], -1)
                elif i[-1] == 1:
                    cv2.ellipse(img_color, i[0], i[1], 0, 0, 360, i[2], -1)
                elif i[-1] == 2:
                    cv2.circle(img_color, i[0], 5, i[1], -1)
            if mode == 0:
                cv2.rectangle(img_color, (mouse_start_x, mouse_start_y), (x, y), color, -1)
            elif mode == 1:
                a = int((x-mouse_start_x)/2)
                b = int((y-mouse_start_y)/2)
                center = (int(mouse_start_x+a), int(mouse_start_y+b))
                axes = (abs(a), abs(b))
                cv2.ellipse(img_color, center, axes, 0, 0, 360, color, -1)
            elif mode == 2:
                items.append(((x, y), color, mode))
                cv2.circle(img_color, (x, y), 5, color, -1)

    # Left button released
    elif event == cv2.EVENT_LBUTTONUP:
        # Flag off
        mouse_is_pressed = False
        if mode == 0:
            items.append(((mouse_start_x, mouse_start_y), (x, y), color, mode))
            cv2.rectangle(img_color, (mouse_start_x, mouse_start_y), (x, y), color, -1)
        elif mode == 1:
            a = int((x-mouse_start_x)/2)
            b = int((y-mouse_start_y)/2)
            center = (int(mouse_start_x+a), int(mouse_start_y+b))
            axes = (abs(a), abs(b))
            items.append((center, axes, color, mode))
            cv2.ellipse(img_color, center, axes, 0, 0, 360, color, -1)
        elif mode == 2:
            items.append(((x, y), color, mode))
            cv2.circle(img_color, (x, y), 5, color, -1)

# Create a black image
rows = 480
cols = 640
img_color = np.zeros((rows, cols, 3), np.uint8)

# Create a window
winname = 'Mouse Events'
cv2.namedWindow(winname)

# Register the mouse callback function
cv2.setMouseCallback(winname, mouse_callback)

# Infinite loop
while True:
    cv2.imshow(winname, img_color)
    key = cv2.waitKey(1)
    if key == 27: break
    elif key == ord('m'):
        if mode == 2:
            mode = 0
        else:
            mode += 1

cv2.destroyAllWindows()