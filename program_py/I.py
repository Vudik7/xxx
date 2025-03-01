import cv2
import numpy as np
import os

def rgb_to_hsi(image):
    # Нормализуем изображение (диапазон 0-1)
    img = image.astype(np.float32) / 255.0
    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]

    # Вычисляем яркость (I)
    I = (R + G + B) / 3

    return I

def invert_intensity(image_path, output_path):
    # Загружаем изображение
    image = cv2.imread(image_path)
    
    # Преобразуем в HSI и извлекаем I (яркость)
    I = rgb_to_hsi(image)
    
    # Инвертируем яркость
    I_inv = 1 - I  # Инверсия: яркие -> тёмные, тёмные -> яркие

    # Масштабируем обратно в 0-255
    I_inv = (I_inv * 255).astype(np.uint8)

    # Сохраняем изображение
    cv2.imwrite(output_path, I_inv)

# Использование:
image_path = "comand7.png"  # Укажите путь к изображению
output_path = "comand7_inverted.png"
invert_intensity(image_path, output_path)

