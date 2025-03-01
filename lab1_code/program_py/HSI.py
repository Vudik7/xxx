import cv2
import numpy as np
import os

def rgb_to_hsi(image):
    
    img = image.astype(np.float32) / 255.0
    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]

    I = (R + G + B) / 3
    HSI = np.zeros_like(img)
    HSI[:, :, 2] = I 

    return HSI

def save_intensity_component(image_path, output_folder):
    os.makedirs(output_folder, exist_ok=True) 

    img = cv2.imread(image_path) 
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

    hsi_image = rgb_to_hsi(img)

    intensity = (hsi_image[:, :, 2] * 255).astype(np.uint8)

    intensity_path = os.path.join(output_folder, "comand7.png")
    cv2.imwrite(intensity_path, intensity)

    print(f"Яркостная компонента сохранена: {intensity_path}")

save_intensity_component("comand7.png", "comand7_HSI")
