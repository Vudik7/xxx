import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def rgb_to_grayscale(image):
    image = np.array(image)
    gray_image = np.dot(image[...,:3], [0.299, 0.587, 0.114])
    return gray_image

def sauvola_threshold(image, window_size=5, k=0.2, r=128):
    img = image.astype(np.float32)
    pad_size = window_size // 2
    padded_image = np.pad(img, pad_size, mode='reflect')
    rows, cols = img.shape
    binary_image = np.zeros_like(img)

    for i in range(rows):
        for j in range(cols):
            window = padded_image[i:i+window_size, j:j+window_size]
            mean = np.mean(window)
            std_dev = np.std(window)
            threshold = mean * (1 + k * ((std_dev / r) - 1))
            binary_image[i, j] = 255 if img[i, j] > threshold else 0

    return binary_image


image_paths = ["path_to_image1.png", "path_to_image2.png"] 
images = [Image.open(img) for img in image_paths]

plt.figure(figsize=(12, 6))

for i, img in enumerate(images):
    gray_image = rgb_to_grayscale(img)
    binary_img = sauvola_threshold(gray_image, window_size=5)
    plt.subplot(len(images), 2, 2*i + 1)
    plt.imshow(gray_image, cmap='gray')
    plt.title(f"Оригинал {i+1}")
    plt.axis("off")

    plt.subplot(len(images), 2, 2*i + 2)
    plt.imshow(binary_img, cmap='gray')
    plt.title(f"Бинаризация Сауволы {i+1}")
    plt.axis("off")

plt.tight_layout()
plt.show()
