import cv2
import numpy as np
import os

def rgb_to_hsi(image):
    img = image.astype(np.float32) / 255.0
    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    I = (R + G + B) / 3

    return I

def invert_intensity(image_path, output_path):
    image = cv2.imread(image_path)
    I = rgb_to_hsi(image)
    I_inv = 1 - I 
    I_inv = (I_inv * 255).astype(np.uint8)
    cv2.imwrite(output_path, I_inv)

image_path = "comand7.png" 
output_path = "comand7_inverted.png"
invert_intensity(image_path, output_path)

