import cv2
import numpy as np
import os

def rgb_to_hsi(image):
    # Нормализуем изображение (диапазон 0-1)
    img = image.astype(np.float32) / 255.0
    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]

    # Вычисляем яркость (I)
    I = (R + G + B) / 3

    # Создаем 3-канальное HSI-изображение, но будем использовать только I
    HSI = np.zeros_like(img)
    HSI[:, :, 2] = I  # I (яркость)

    return HSI

def save_intensity_component(image_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)  # Создаем папку, если её нет

    # Загружаем изображение
    img = cv2.imread(image_path)  # Читаем изображение в BGR
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Конвертируем в RGB

    # Преобразуем в HSI
    hsi_image = rgb_to_hsi(img)

    # Извлекаем компоненту яркости (I)
    intensity = (hsi_image[:, :, 2] * 255).astype(np.uint8)

    # Сохраняем результат
    intensity_path = os.path.join(output_folder, "comand7.png")
    cv2.imwrite(intensity_path, intensity)

    print(f"Яркостная компонента сохранена: {intensity_path}")

# Пример использования
save_intensity_component("comand7.png", "comand7_HSI")
