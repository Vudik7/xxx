from PIL import Image
import numpy as np
import os

def save_rgb_components(image_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    img = Image.open(image_path).convert("RGB")
    img_array = np.array(img)
    red = img_array.copy()
    red[:, :, 1] = 0  
    red[:, :, 2] = 0 

    green = img_array.copy()
    green[:, :, 0] = 0  
    green[:, :, 2] = 0 

    blue = img_array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0

    Image.fromarray(red).save(os.path.join(output_folder, "red_component.png"))
    Image.fromarray(green).save(os.path.join(output_folder, "green_component.png"))
    Image.fromarray(blue).save(os.path.join(output_folder, "blue_component.png"))

save_rgb_components("comand7.png", "output_folder")
